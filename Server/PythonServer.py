import json
import web
import NavigationKP as nav
import ar_markers_livetest as camera
import time

urls = ('/(.*)','index')

app = web.application(urls,globals())

web.config.debug = True

class index:
        def __init__(self):
                self.process_location = True
                self.id = None
                self.coord = None
                print("new person, same old mistakes")
        def GET(self, name=None):
                start = time.time()
                user_data = web.input()
                process_me = user_data.sending
                op = None
                print("proc: " + str(self.process_location))
                if process_me == 'True':
                        print("first_part")
                        #give the coordinates of the marker
                        frame_start = time.time()
                        id, ord = camera.get_from_frame()
                        print("get id time: " + str(time.time() - frame_start))
                        op = {'id': id, 'xpos': ord[0], 'zpos': ord[2]}
                        print(op)
                        self.coord = (ord[0], ord[2])
                        self.id = id
                else:
                        #return the route based on the destination the client sends
                        #the if and else statements alternate
                        print("second-part")
                        user = nav.Person()
                        user.set_position(user_data.x1, user_data.z1)
                        print("user position x1 z1",user_data.x1,user_data.z1)
                        xs, ys = user.get_points(2007)
                        web.header('Content-Type', 'application/json')
                        op = {'x': xs, 'z': ys}

                print("time taken: " + str(time.time() - start))
                return json.dumps(op)
if __name__=="__main__":app.run()
