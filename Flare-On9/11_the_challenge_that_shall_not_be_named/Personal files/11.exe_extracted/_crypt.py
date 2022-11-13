import inspect
import dis

for frameinfo in inspect.stack():
    print(frameinfo.frame)

frame = inspect.stack()[12]
frame = frame.frame

c = frame.f_code
print(c.co_names)
