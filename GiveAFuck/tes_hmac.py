# import os
import hmac
import time
import hashlib
import random, string , sched
digest_maker = hmac.new(b'secret_key',b'14', hashlib.sha1)

print("HEXDIGEST:", digest_maker.hexdigest())
# print("HEXDIGEST:", digest_maker.hexdigest())
digest_maker.update(b'another {}') #update digest
print("Block SIZE",digest_maker.block_size)
print("DIGEST SIZE:",digest_maker.digest_size)
print("DIGEST CANONICAL NAME:",digest_maker.name)
print("DIGEST end = :",end=' ')
print (digest_maker.digest())
digest_clone = digest_maker.copy()
print('Clone :', digest_clone.hexdigest())
# os.rename(r'/media/ifu/1E36996536993F29/Projects/PythonProjects/nz_free_pr/one/GiveAFuck/media/files-2021/ISEEYOU.exe',r'/media/ifu/1E36996536993F29/Projects/PythonProjects/nz_free_pr/one/GiveAFuck/media/files-2021/2021-04-04-23-42-57-ChromeSetup.exe')
# print('YESSS IT IS WORKING')


# starttime = time.time()
# while True:
#     print ("tick")
#     time.sleep(60.0 - ((time.time() - starttime) % 60.0))


# s = sched.scheduler(time.time, time.sleep)
# def do_something(sc): 
#     print("Doing stuff...")
#     # do your stuff
#     s.enter(10, 1, do_something, (sc,))

# s.enter(10, 1, do_something, (s,))
# s.run()