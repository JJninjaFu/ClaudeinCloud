import math
def qmul(a,b):
    ax,ay,az,aw=a;bx,by,bz,bw=b
    return (aw*bx+ax*bw+ay*bz-az*by, aw*by-ax*bz+ay*bw+az*bx, aw*bz+ax*by-ay*bx+az*bw, aw*bw-ax*bx-ay*by-az*bz)
def qconj(a): return (-a[0],-a[1],-a[2],a[3])
def qrot(q,v):
    r=qmul(qmul(q,(v[0],v[1],v[2],0)),qconj(q)); return r[:3]
def qy(deg): a=math.radians(deg)/2; return (0,math.sin(a),0,math.cos(a))
def qaxis(ax,deg):
    a=math.radians(deg)/2; n=math.sqrt(sum(c*c for c in ax)); return tuple(c/n*math.sin(a) for c in ax)+(math.cos(a),)
