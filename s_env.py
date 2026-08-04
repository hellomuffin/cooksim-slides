import json
PID='1qwFEh0CVh5dkmF6t3eYVFeajgOR0PMNB-tkmGWwaLFc'
S='g3f64c654411_0_19'; E=914400
B='https://hellomuffin.github.io/cooksim-slides/talk/'
NAVY={'red':0.012,'green':0.176,'blue':0.376}
BLUE={'red':0.004,'green':0.463,'blue':0.827}
DIM ={'red':0.36,'green':0.42,'blue':0.49}
INK ={'red':0.09,'green':0.12,'blue':0.16}
def box(x,y,w,h): return {'pageObjectId':S,'size':{'width':{'magnitude':w*E,'unit':'EMU'},'height':{'magnitude':h*E,'unit':'EMU'}},
  'transform':{'scaleX':1,'scaleY':1,'translateX':x*E,'translateY':y*E,'unit':'EMU'}}
# the two bare labels sat at y=8.17 with nothing above them; rebuild as captioned panels
R=[{'deleteObject':{'objectId':o}} for o in ['g3f64c654411_0_22','g3f64c654411_0_44']]
def txt(oid,x,y,w,h,text,size,color=INK,bold=False,LS=125):
    R.append({'createShape':{'objectId':oid,'shapeType':'TEXT_BOX','elementProperties':box(x,y,w,h)}})
    R.append({'insertText':{'objectId':oid,'insertionIndex':0,'text':text}})
    R.append({'updateTextStyle':{'objectId':oid,'textRange':{'type':'ALL'},'style':{
        'fontFamily':'Open Sans','fontSize':{'magnitude':size,'unit':'PT'},'bold':bold,
        'foregroundColor':{'opaqueColor':{'rgbColor':color}}},'fields':'fontFamily,fontSize,bold,foregroundColor'}})
    R.append({'updateParagraphStyle':{'objectId':oid,'textRange':{'type':'ALL'},
        'style':{'alignment':'START','lineSpacing':LS},'fields':'alignment,lineSpacing'}})

txt('en_lede',0.94,1.80,17.6,0.5,'Two engines, one contract: an egocentric agent, a long-horizon task, and a world that keeps moving.',15,DIM)
R.append({'createImage':{'objectId':'en_vh','url':B+'env_virtualhome.gif','elementProperties':box(0.94,2.70,8.60,3.69)}})
R.append({'createImage':{'objectId':'en_oc','url':B+'env_overcook.gif','elementProperties':box(10.45,2.70,8.60,3.75)}})
txt('en_l1',0.94,6.65,8.60,0.5,'VIRTUALHOME — existing simulator',12,BLUE,True)
txt('en_d1',0.94,7.20,8.60,1.4,'Tidy up across rooms: turn off every device that is on, close anything\nleft open. Long horizon, many rooms, furniture to navigate.',13.5,INK,LS=140)
txt('en_l2',10.45,6.65,8.60,0.5,'EGOCENTRIC OVERCOOK — built by us',12,BLUE,True)
txt('en_d2',10.45,7.20,8.60,1.4,'Cheeseburger, plated in the required order. Short horizon, but the\nworld fights back: food burns, pans catch fire, orders expire.',13.5,INK,LS=140)
txt('en_note',0.94,8.62,17.6,0.4,'Both clips are ground-truth completions with no assistant. VirtualHome plays at real time; OverCook is compressed 6x.',10.5,DIM)
txt('en_kick',0.94,9.20,17.6,0.6,'We needed a second engine because cooking gives us something households do not: irreversible mistakes on a clock.',15,NAVY,True)
json.dump({'presentationId':PID,'requests':R},open('s_env.json','w'))
print('requests:',len(R))
