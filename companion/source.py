"""Convert each local wall-clock hour to a destination time zone on a chosen date."""
from datetime import date,datetime,time,timezone
from zoneinfo import ZoneInfo
from serve import page
INTERVAL=30
def snapshot(o,m):
    a=ZoneInfo(o["from_zone"]);b=ZoneInfo(o["to_zone"])
    d=date.fromisoformat(o["date"]) if o.get("date") else datetime.now(a).date()
    first=int(o.get("start_hour",9))
    if not 0<=first<=23:raise ValueError("Start hour must be 0–23")
    pages=[]
    for j in range(24):
        hour=(first+j)%24;naive=datetime.combine(d,time(hour));seen=set();found=False
        for fold in (0,1):
            src=naive.replace(tzinfo=a,fold=fold);utc=src.astimezone(timezone.utc)
            if utc in seen or utc.astimezone(a).replace(tzinfo=None)!=naive:continue
            seen.add(utc);found=True;dst=utc.astimezone(b);daydiff=(dst.date()-d).days
            pages.append(page(src.strftime("%H:%M %Z"),dst.strftime("%H:%M"),dst.strftime("%Y-%m-%d %Z"),o["to_zone"],"Same day" if not daydiff else f"Day {daydiff:+d}"))
        if not found:pages.append(page(f"{hour:02}:00","Skipped","Local hour does not exist","DST spring transition"))
    return dict(state=d.isoformat()+" / local date",key=str(d),pages=pages)
