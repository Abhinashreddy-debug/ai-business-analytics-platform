from .analytics import kpis,by_category,by_region
def generate_insights(d):
    k=kpis(d); c=by_category(d); r=by_region(d)
    low=c.assign(margin=c.profit/c.revenue.replace(0,1)).sort_values("margin").iloc[0]
    lines=[f"**Revenue leader:** {c.iloc[0].category} leads with ₹{c.iloc[0].revenue:,.0f} revenue. Review stock and repeat-purchase opportunities.",
    f"**Regional focus:** {r.iloc[0].region} leads revenue with ₹{r.iloc[0].revenue:,.0f}. Compare its campaign and product mix with other regions.",
    f"**Margin watch:** {low.category} has the lowest category margin in this selection. Review costs and discounting.",
    f"**Overall:** Profit margin is {k['Profit margin']:.1f}%. Monitor profitability alongside revenue growth."]
    try:
        import os
        if os.getenv("OPENAI_API_KEY"):
            from openai import OpenAI
            client=OpenAI()
            msg="Create 3-4 concise evidence-based recommendations from these figures. Do not invent numbers.\n"+"\n".join(lines)
            out=client.chat.completions.create(model=os.getenv("OPENAI_MODEL","gpt-4o-mini"),messages=[{"role":"user","content":msg}],temperature=.2)
            return out.choices[0].message.content,"Live LLM"
    except Exception:
        pass
    return "\n\n".join(lines),"Built-in analytics insight engine"
