"""Deterministic low-poly props, in metres, Y up; pivot at ground centre.
Run with ../venv3d/bin/python gen_props.py. No external assets required.
"""
from pathlib import Path
import json
import numpy as np
import trimesh as tm

OUT = Path(__file__).resolve().parent
WOOD = [139, 86, 43, 255]
BLACK = [25, 27, 31, 255]
RED = [210, 43, 27, 255]
WHITE = [239, 235, 218, 255]


def paint(mesh, color):
    mesh.visual.vertex_colors = np.tile(color, (len(mesh.vertices), 1))
    return mesh


def box(size, pos, color):
    m = tm.creation.box(extents=size)
    m.apply_translation(pos)
    return paint(m, color)


def cyl(radius, height, pos, color, sections=12):
    m = tm.creation.cylinder(radius=radius, height=height, sections=sections)
    m.apply_transform(tm.transformations.rotation_matrix(-np.pi / 2, [1, 0, 0]))
    m.apply_translation(pos)
    return paint(m, color)


def ball(size, pos, color):
    m = tm.creation.icosphere(subdivisions=1, radius=1)
    m.vertices *= np.array(size)
    m.apply_translation(pos)
    return paint(m, color)


def rod(a, b, radius, color, sections=8):
    a, b = np.array(a), np.array(b)
    m = tm.creation.cylinder(radius=radius, height=np.linalg.norm(b-a), sections=sections)
    m.apply_transform(tm.geometry.align_vectors([0, 0, 1], b-a))
    m.apply_translation((a+b)/2)
    return paint(m, color)


def taper(r0, r1, height, y, color, sections=16):
    # Revolved profile forms closed frustums, including cone bands.
    profile = [[0, 0], [r0, 0], [r1, height], [0, height]]
    m = tm.creation.revolve(profile, sections=sections)
    m.apply_transform(tm.transformations.rotation_matrix(-np.pi/2, [1, 0, 0]))
    m.apply_translation([0, y, 0])
    return paint(m, color)


def wooden_crate():
    p = []
    for i in range(5):
        col = [133 + i*6, 80+i*4, 40+i*2, 255]
        x = (i-2)*.117
        p.append(box([.112,.026,.58], [x,.013,0], col))
        for z in [-.287,.287]:
            p.append(box([.112,.55,.026], [x,.29,z], col))
        for side in [-1,1]:
            p.append(box([.026,.55,.112], [side*.287,.29,x], col))
        p.append(box([.112,.026,.58], [x,.577,0], col))
    for x in [-.275,.275]:
        for z in [-.307,.307]:
            p.append(box([.048,.59,.025], [x,.295,z], WOOD))
    return p


def bottle():
    green = [21,74,44,255]
    return [cyl(.043,.18,[0,.09,0],green), taper(.043,.018,.045,.18,green),
            cyl(.018,.085,[0,.2675,0],green), cyl(.022,.018,[0,.319,0],[40,47,30,255]),
            cyl(.0435,.065,[0,.105,0],[204,190,142,255])]


def chochin_lantern():
    p = [ball([.19,.25,.19],[0,.29,0],[225,42,37,255]),
         cyl(.092,.04,[0,.04,0],BLACK), cyl(.092,.04,[0,.54,0],BLACK)]
    # Thin dark hoops emphasize the ribbed paper silhouette.
    for y in [.14,.22,.30,.38,.46]:
        r = .19*np.sqrt(max(0,1-((y-.29)/.25)**2))
        m = tm.creation.torus(major_radius=r, minor_radius=.0025, major_sections=16, minor_sections=4)
        m.apply_transform(tm.transformations.rotation_matrix(-np.pi/2,[1,0,0]))
        m.apply_translation([0,y,0])
        p.append(paint(m,[148,30,25,255]))
    p.append(rod([0,.56,0],[0,.63,0],.009,BLACK))
    return p


def mini_torii():
    p = [cyl(.035,.60,[x,.30,0],RED) for x in [-.23,.23]]
    p += [box([.69,.055,.09],[0,.61,0],RED),box([.57,.035,.055],[0,.48,0],RED),
          box([.76,.028,.11],[0,.651,0],[53,35,30,255]),box([.027,.13,.03],[0,.545,0],RED)]
    return p


def mic_stand():
    p = [cyl(.012,1.30,[0,.68,0],BLACK),cyl(.022,.055,[0,.50,0],[64,65,69,255])]
    for angle in np.arange(3)*2*np.pi/3:
        end = [.30*np.cos(angle),.015,.30*np.sin(angle)]
        p += [rod([0,.17,0],end,.012,BLACK),ball([.022,.015,.022],end,BLACK)]
    p += [rod([0,1.32,0],[.28,1.48,0],.013,BLACK),
          rod([.25,1.46,0],[.38,1.53,0],.025,[48,49,53,255]),
          ball([.038,.038,.038],[.39,1.535,0],[103,105,109,255])]
    return p


def speaker_box():
    p = [box([.36,.62,.28],[0,.31,0],BLACK)]
    for y,r in [(.20,.12),(.46,.08)]:
        p += [rod([0,y,.140],[0,y,.155],r,[70,72,76,255],16),
              rod([0,y,.155],[0,y,.161],r*.77,[34,35,39,255],16),
              ball([r*.30,r*.30,.016],[0,y,.166],[91,93,97,255])]
    return p


def chair():
    p = [box([.44,.045,.44],[0,.45,0],WOOD)]
    for x in [-.17,.17]:
        for z in [-.17,.17]:
            p.append(box([.045,.43,.045],[x,.215,z],[111,65,32,255]))
        p.append(box([.04,.42,.04],[x,.66,-.18],WOOD))
    for y in [.64,.76,.86]:
        p.append(box([.42,.065,.03],[0,y,-.18],[160,104,58,255]))
    return p


def table():
    p = [cyl(.43,.045,[0,.7375,0],[154,96,49,255],24),cyl(.045,.69,[0,.3675,0],WOOD)]
    for a in np.arange(3)*2*np.pi/3:
        p.append(rod([0,.14,0],[.31*np.cos(a),.022,.31*np.sin(a)],.022,WOOD))
    return p


def book_stack():
    p=[]
    for i,col in enumerate([[57,93,148,255],[163,49,49,255],[60,125,88,255]]):
        y=i*.055
        parts=[box([.24,.038,.17],[0,y+.027,0],WHITE),
               box([.255,.008,.185],[0,y+.004,0],col),
               box([.255,.008,.185],[0,y+.050,0],col),
               box([.012,.046,.185],[-.122,y+.027,0],col)]
        for m in parts:
            m.apply_transform(tm.transformations.rotation_matrix((i-1)*.10,[0,1,0]))
        p.extend(parts)
    return p


def plant_pot():
    return [taper(.09,.135,.23,0,[170,85,53,255]),cyl(.145,.04,[0,.23,0],[191,104,65,255]),
            cyl(.124,.008,[0,.253,0],[64,43,27,255]),rod([0,.25,0],[0,.43,0],.016,[63,94,43,255]),
            ball([.20,.20,.19],[0,.52,0],[49,122,53,255]),
            ball([.12,.14,.12],[-.13,.43,.02],[64,143,61,255]),
            ball([.12,.15,.12],[.12,.47,-.04],[38,102,46,255])]


def traffic_cone():
    orange=[244,104,24,255]
    p=[box([.36,.035,.36],[0,.0175,0],orange)]
    h=.47
    for lo,hi,c in [(0,.18,orange),(.18,.28,WHITE),(.28,.37,orange),(.37,.42,WHITE),(.42,.47,orange)]:
        radius=lambda y: .145 + (.012-.145)*y/h
        p.append(taper(radius(lo),radius(hi),hi-lo,.035+lo,c))
    return p


def gift_box():
    p=[box([.32,.28,.32],[0,.14,0],[61,113,180,255]),
       box([.34,.035,.34],[0,.2975,0],[75,135,207,255])]
    gold=[245,193,59,255]
    p += [box([.045,.318,.344],[0,.159,0],gold),box([.344,.318,.045],[0,.159,0],gold)]
    for x in [-.045,.045]:
        p.append(ball([.055,.025,.031],[x,.34,0],gold))
    return p


BUILDERS = [wooden_crate,bottle,chochin_lantern,mini_torii,mic_stand,speaker_box,chair,table,book_stack,plant_pot,traffic_cone,gift_box]


def main():
    manifest=[]
    for build in BUILDERS:
        mesh=tm.util.concatenate(build())
        bounds=mesh.bounds
        mesh.apply_translation([-bounds[:,0].mean(),-bounds[0,1],-bounds[:,2].mean()])
        assert np.isfinite(mesh.vertices).all() and mesh.is_watertight
        path=OUT / (build.__name__+'.glb')
        scene=tm.Scene(mesh)
        scene.metadata.update({'units':'meters','up_axis':'Y','pivot':'ground_center'})
        path.write_bytes(scene.export(file_type='glb'))
        loaded=tm.load(path,force='scene')
        geometries=list(loaded.geometry.values())
        faces=sum(len(g.faces) for g in geometries)
        vertices=sum(len(g.vertices) for g in geometries)
        assert faces==len(mesh.faces) and vertices==len(mesh.vertices)
        assert np.allclose(loaded.bounds[0,1],0,atol=1e-6)
        assert np.allclose(loaded.bounds[:,[0,2]].mean(axis=0),0,atol=1e-6)
        assert all(g.visual.kind=='vertex' for g in geometries)
        manifest.append(dict(name=build.__name__,file=path.name,faces=faces,vertices=vertices))
        print(f'{path.name}: {faces} faces, {vertices} vertices, size {mesh.extents.round(3)} m')
    (OUT/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
    assert len(manifest)==12 and all((OUT/item['file']).is_file() for item in manifest)
    print('Verified all 12 GLBs and manifest.json')


if __name__=='__main__':
    main()
