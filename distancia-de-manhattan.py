xm, ym, xr, yr = map(int,input().split())
d = 0
if xm > xr:
  if ym > yr:
    d = (xm - xr) + (ym - yr)
  elif yr > ym:
    d = (xm - xr) + (yr - ym)
  elif ym == yr:
    d = xm - xr
elif xr > xm:
  if yr > ym:
    d = (xr - xm) + (yr - ym)
  elif ym > yr:
    d = (xr - xm) + (ym - yr)
  elif ym == yr:
    d = xr - xm
elif xm == xr:
  if ym > yr:
    d = ym - yr
  elif yr > ym:
    d = yr - ym
print(d)