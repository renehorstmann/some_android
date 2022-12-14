LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)

LOCAL_MODULE := main

#
# compile definitions
#
LOCAL_CFLAGS := -DPLATFORM_ANDROID -DOPTION_GLES -DOPTION_SDL
LOCAL_CFLAGS += -DM_NO_PRINT_COLOR -DS_LOG_DO_NOT_USE_COLOR
LOCAL_CFLAGS += -DSOME_ANDROID_PACKAGE=@@@package_underscored@@@

# LOCAL_CFLAGS += -DOPTION_TTF

# for option fetch, uncomment AndroidManifest.xml : android.permission.INTERNET
#@@@USE_FETCH@@@LOCAL_CFLAGS += -DOPTION_FETCH


#
# includes
#

# ext includes like SDL
LOCAL_C_INCLUDES := $(LOCAL_PATH)/../include

# some includes
LOCAL_C_INCLUDES += $(LOCAL_PATH)/include


#
# source files
#

# Add your application source directories here...
SOME_SRC_FILES := $(wildcard $(LOCAL_PATH)/src/*.c)
SOME_SRC_FILES += $(wildcard $(LOCAL_PATH)/src/e/*.c)
SOME_SRC_FILES += $(wildcard $(LOCAL_PATH)/src/p/*.c)
SOME_SRC_FILES += $(wildcard $(LOCAL_PATH)/src/r/*.c)
SOME_SRC_FILES += $(wildcard $(LOCAL_PATH)/src/u/*.c)

LOCAL_SRC_FILES := $(SOME_SRC_FILES:$(LOCAL_PATH)/%=%)

#
# libraries used
#

# Also have a look at SDLActivity.java : getLibraries in which the modules are loaded (uncomment there, too)
LOCAL_SHARED_LIBRARIES := SDL2
LOCAL_SHARED_LIBRARIES += SDL2_image
#@@@USE_MIXER@@@LOCAL_SHARED_LIBRARIES += SDL2_mixer
# LOCAL_SHARED_LIBRARIES += SDL2_net
# LOCAL_SHARED_LIBRARIES += SDL2_ttf


# link libraries
LOCAL_LDLIBS := -lEGL -lGLESv3 -lOpenSLES -llog -landroid

include $(BUILD_SHARED_LIBRARY)
