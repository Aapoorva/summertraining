
# importing kairos face recognition face API
import kairos_face as kf

# setting up API keys
kf.settings.app_id = 'a123a233'
kf.settings.app_key = '03a5065270150ba0e23a0584ae716b0d'

def detect_face_fn(img_path) :

	detected_face = kf.detect.detect_face(file=img_path, gallery_name='members')

	print(detected_face)

def add_face_fn(img_path) :
	
	# reading new member id to be used as subject id
	user_id = input("enter your member id : ")
	
	# Enrolling from a file
	kf.enroll.enroll_face(file=img_path, subject_id=user_id, gallery_name='members')

def recog_face_fn(img_path) :

	# Recognizing from a file
	recognized_faces = kf.recognize_face(file=img_path, gallery_name='members')

	print(recognized_faces) 


def  mark_attendence() :

	options = '''
		1. detect
		2. add
		3. recognize
	'''

	print(options)

	ch = input('your choice : ')

	img_path = input('give img path : ')

	if ch == '1' :

		detect_face(img_path)

	elif ch == '2' :

		add_face_fn(img_path)

	elif ch == '3' :

		recog_face_fn(img_path)

	else :
		print('invalid choice')


mark_attendence()