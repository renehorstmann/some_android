import os
import re


#
# This file sets a package name for the some android app
#


def apply_replace(src_file, dst_file, template: dict):
    """reads in the src file, applies the replace list and saves the generated file under dst (and creates all dirs)"""
    file = open(src_file, 'r')
    text = file.read()
    file.close()

    for item in template:
        text = re.sub(item, template[item], text)

    os.makedirs(os.path.dirname(dst_file), exist_ok=True)
    file = open(dst_file, 'w')
    file.write(text)
    file.close()


def apply_replace_on_file(file, template: dict):
    apply_replace(file, file, template)


#
# Template
#

# the templates needs a website like structure like de.horsimann.some for horsimann.de/some


DOMAIN_NAMESPACE = 'de'
DOMAIN = 'horsimann'
APP = 'some'


if __name__ == '__main__':

    print('applying template')
    import shutil

    if os.path.exists('out'):
        shutil.rmtree('out')

    print('copying project...')
    shutil.copytree('in', 'out/APP')

    print('replacing package names...')
    TEMPLATE = {
        '@@@package_underscored@@@': DOMAIN_NAMESPACE + '_' + DOMAIN + '_' + APP,
        '@@@package_dotted@@@': DOMAIN_NAMESPACE + '.' + DOMAIN + '.' + APP,
        '@@@package_slashed@@@':  DOMAIN_NAMESPACE + '/' + DOMAIN + '/' + APP,
        '@@@app_name@@@': APP
    }

    apply_replace_on_file('out/APP/app/jni/src/Android.mk', TEMPLATE)

    apply_replace_on_file('out/APP/app/jni/SDL/src/core/android/SDL_android.c', TEMPLATE)
    apply_replace_on_file('out/APP/app/jni/SDL/src/hidapi/android/hid.cpp', TEMPLATE)

    apply_replace_on_file('out/APP/app/src/main/java/de/horsimann/some/HIDDevice.java', TEMPLATE)
    apply_replace_on_file('out/APP/app/src/main/java/de/horsimann/some/HIDDeviceBLESteamController.java', TEMPLATE)
    apply_replace_on_file('out/APP/app/src/main/java/de/horsimann/some/HIDDeviceManager.java', TEMPLATE)
    apply_replace_on_file('out/APP/app/src/main/java/de/horsimann/some/HIDDeviceUSB.java', TEMPLATE)
    apply_replace_on_file('out/APP/app/src/main/java/de/horsimann/some/SDL.java', TEMPLATE)
    apply_replace_on_file('out/APP/app/src/main/java/de/horsimann/some/SDLActivity.java', TEMPLATE)
    apply_replace_on_file('out/APP/app/src/main/java/de/horsimann/some/SDLAudioManager.java', TEMPLATE)
    apply_replace_on_file('out/APP/app/src/main/java/de/horsimann/some/SDLControllerManager.java', TEMPLATE)
    apply_replace_on_file('out/APP/app/src/main/AndroidManifest.xml', TEMPLATE)
    apply_replace_on_file('out/APP/app/build.gradle', TEMPLATE)

    apply_replace_on_file('out/APP/app/src/main/res/values/strings.xml', TEMPLATE)

    print('renaming package dirs...')
    shutil.move('out/APP/app/src/main/java/de/horsimann/some', 'out/APP/app/src/main/java/de/horsimann/' + APP)
    shutil.move('out/APP/app/src/main/java/de/horsimann/', 'out/APP/app/src/main/java/de/' + DOMAIN)
    shutil.move('out/APP/app/src/main/java/de/', 'out/APP/app/src/main/java/' + DOMAIN_NAMESPACE)
    shutil.move('out/APP', 'out/'+APP)

    print('finish')

    print('')
    print('Start the some Hello World App with Android Studio and test it')
    print('')
    print('Now you can replace your apps code and assets:')
    print('  src and include  ->  out/'+APP+'/app/jni/src')
    print('  res               ->  out/'+APP+'/app/src/main/assets')
    print('Replace the App icons in out/'+APP+'/app/src/main/res')
    print('')
    print('You should now be ready to compile your own App in AndroidStudio')
