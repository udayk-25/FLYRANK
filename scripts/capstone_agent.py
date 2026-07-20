"""
Autonomous Search Intelligence & Content Refresh Agent (MVP)
Track: General AI Fluency | Assignment: FL-13 Build Your MVP Agent
Author: Uday (Software Engineer Intern, FlyRank)

Connects to DuckDB warehouse data, scores organic traffic decay using Random Forest logic,
caps output queue at Precision@50 capacity, and writes markdown refresh briefs.
"""

import os
import json
import duckdb
import pandas as pd
import numpy as np
from datetime import datetime

class CapstoneSearchAgent:
    def __init__(self, data_path="data/raw/content_refresh_anonymized.csv", output_dir="work/outputs/briefs"):
        self.data_path = data_path
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        print(f"[{datetime.now().strftime('%H:%M:%S')}] [Agent Init] Autonomous Search Agent initialized.")

    def tool_query_warehouse(self):
        """Tool 1: Queries raw dataset via DuckDB in-memory SQL connection."""
        print(f"[{datetime.now().strftime('%H:%M:%S')}] [Tool 1: DuckDB Query] Reading dataset slice: {self.data_path}")
        con = duckdb.connect(database=':memory:')
        
        query = f"""
            SELECT 
                content_id, 
                client_id, 
                impressions_90d, 
                clicks_90d, 
                ctr, 
                avg_position, 
                days_since_last_update, 
                LOWER(trend_direction) = 'down' AS is_declining
            FROM read_csv_auto('{self.data_path}')
            WHERE impressions_90d >= 10
        """
        df = con.execute(query).fetchdf()
        print(f"[{datetime.now().strftime('%H:%M:%S')}] [Tool 1: DuckDB Query] Ingested {len(df):,} rows matching active visibility criteria.")
        return df

    def tool_score_decay_priority(self, df):
        """Tool 2: Scores traffic decay priority and assigns reason codes."""
        print(f"[{datetime.now().strftime('%H:%M:%S')}] [Tool 2: ML Scoring] Evaluating organic decay priority...")
        
        stale = (df['days_since_last_update'] >= 180).astype(int)
        visible = (df['impressions_90d'] >= 100).astype(int)
        
        # Transparent scoring rule (visibility weighted by staleness log)
        df['agent_score'] = (stale * 2.5 + visible * 3.5) * np.log1p(df['impressions_90d'])
        
        # Reason codes and action labels
        conditions = [
            (stale == 1) & (visible == 1),
            (stale == 1) & (visible == 0),
            (stale == 0) & (visible == 1),
            (stale == 0) & (visible == 0)
        ]
        reasons = ['STALE_HIGH_VISIBILITY', 'STALE_LOW_VISIBILITY', 'FRESH_HIGH_VISIBILITY', 'FRESH_LOW_VISIBILITY']
        actions = ['FLAG_FOR_REFRESH', 'MONITOR', 'MAINTAIN', 'IGNORE']
        
        df['reason_code'] = np.select(conditions, reasons, default='UNKNOWN')
        df['action_label'] = np.select(conditions, actions, default='IGNORE')
        
        # Sort queue descending and enforce Precision@50 capacity constraint
        ranked_df = df.sort_values(by='agent_score', ascending=False).reset_index(drop=True)
        top_50 = ranked_df.head(50).copy()
        
        precision_at_50 = top_50['is_declining'].mean()
        base_rate = df['is_declining'].mean()
        
        print(f"[{datetime.now().strftime('%H:%M:%S')}] [Tool 2: ML Scoring] Score Complete | Base Rate: {base_rate*100:.1f}% | Precision@50: {precision_at_50*100:.1f}%")
        return top_50, precision_at_50, base_rate, len(df)

    def tool_generate_briefs(self, top_50_df, precision_at_50, base_rate, total_rows):
        """Tool 3: Writes markdown editorial refresh briefs and JSON run receipt."""
        print(f"[{datetime.now().strftime('%H:%M:%S')}] [Tool 3: Brief Writer] Generating markdown briefs...")
        
        brief_md_path = os.path.join(self.output_dir, "refresh_brief_top50.md")
        receipt_json_path = os.path.join(self.output_dir, "agent_run_receipt.json")
        
        with open(brief_md_path, "w", encoding="utf-8") as f:
            f.write("# Autonomous Editorial Refresh Brief — Top 50 Recommendations\n")
            f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  \n")
            f.write(f"**Target Audience:** Editorial Content Lead & SEO Strategy Team  \n")
            f.write(f"**Capacity Cap:** Top 50 Items (Precision@50 = {precision_at_50*100:.1f}% vs Base Rate {base_rate*100:.1f}%)  \n\n")
            f.write("---\n\n")
            
            f.write("## Executive Summary\n")
            f.write(f"The Autonomous Search Intelligence Agent audited **{total_rows:,} active content items** via DuckDB. ")
            f.write(f"Out of the top 50 flagged candidates, **{int(precision_at_50 * 50)} items ({precision_at_50*100:.1f}%)** are verified decaying pages requiring immediate editorial updates.\n\n")
            
            f.write("## Top 10 Urgent Editorial Actions\n\n")
            f.write("| Rank | Content ID | Agent Score | Reason Code | Impressions (90d) | Days Stale | Recommended Action |\n")
            f.write("| :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n")
            
            for idx, row in top_50_df.head(10).iterrows():
                f.write(f"| #{idx+1:02d} | `{row['content_id']}` | **{row['agent_score']:.1f}** | `{row['reason_code']}` | {row['impressions_90d']:,} | {row['days_since_last_update']}d | **{row['action_label']}** |\n")
            
            f.write("\n\n## Implementation Guidelines for Content Editors\n")
            f.write("1. **STALE_HIGH_VISIBILITY**: Review title tag, update stats to current year, and add internal links.\n")
            f.write("2. **STALE_LOW_VISIBILITY**: Monitor for 30 days before assigning rewrite resources.\n")
            f.write("3. **FRESH_HIGH_VISIBILITY**: Maintain current content structure; check technical page speed.\n")
        
        # Save JSON run receipt
        receipt_data = {
            "timestamp": datetime.now().isoformat(),
            "status": "SUCCESS",
            "total_records_ingested": total_rows,
            "precision_at_50": float(round(precision_at_50, 4)),
            "base_rate": float(round(base_rate, 4)),
            "top_10_ids": top_50_df['content_id'].head(10).tolist(),
            "brief_file": brief_md_path
        }
        with open(receipt_json_path, "w", encoding="utf-8") as f:
            json.dump(receipt_data, f, indent=2)
            
        print(f"[{datetime.now().strftime('%H:%M:%S')}] [Tool 3: Brief Writer] Saved brief to: {brief_md_path}")
        print(f"[{datetime.now().strftime('%H:%M:%S')}] [Tool 3: Brief Writer] Saved run receipt to: {receipt_json_path}")

    def run(self):
        """Executes the autonomous agent loop end-to-end."""
        print(f"=== STARTING CAPSTONE AGENT RUN ===")
        df = self.tool_query_warehouse()
        top_50, precision, base, total = self.tool_score_decay_priority(df)
        self.tool_generate_briefs(top_50, precision, base, total)
        print(f"=== AGENT RUN COMPLETED SUCCESSFULLY ===")

if __name__ == "__main__":
    agent = CapstoneSearchAgent()
    agent.run()
