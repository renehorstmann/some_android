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

USE_MIXER = False
USE_FETCH = False
USE_ADMOB = False
USE_BILLING = False


def run_template():
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
    
    if USE_MIXER:
        TEMPLATE['#@@@USE_MIXER@@@'] = ''
        TEMPLATE['//@@@USE_MIXER@@@'] = ''
    
    if USE_FETCH:
        TEMPLATE['#@@@USE_FETCH@@@'] = ''
        TEMPLATE['<!--@@@USE_FETCH@@@'] = ''
        TEMPLATE['@@@USE_FETCH@@@-->'] = ''
    
    if USE_ADMOB:
        TEMPLATE['//@@@USE_ADMOB@@@'] = ''
        TEMPLATE['<!--@@@USE_ADMOB@@@'] = ''
        TEMPLATE['@@@USE_ADMOB@@@-->'] = ''
        
    if USE_BILLING:
        TEMPLATE['//@@@USE_BILLING@@@'] = ''
        TEMPLATE['<!--@@@USE_BILLING@@@'] = ''
        TEMPLATE['@@@USE_BILLING@@@-->'] = ''

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
    print('~ '*32)
    print('')
    print('Start the some Hello World App with Android Studio and test it')
    print('')
    print('Now you can replace your apps code and assets:')
    print('  src and include  ->  out/'+APP+'/app/jni/src')
    print('  res               ->  out/'+APP+'/app/src/main/assets')
    print('Replace the App icons in out/'+APP+'/app/src/main/res')
    print('')
    
    if USE_ADMOB:
        print('AdMob: Replace your ad app id in -> out/'+APP+'/app/src/main/AndroidManifest.xml')
        print('AdMob: Replace your ad reward id in -> out/'+APP+'/app/src/main/java/'+DOMAIN_NAMESPACE+'/'+DOMAIN+'/'+APP+'/SDLActivity.java')
        print('')
    if USE_BILLING:
        print('Billing: Replace your billing product ids in -> out/'+APP+'/app/src/main/java/'+DOMAIN_NAMESPACE+'/'+DOMAIN+'/'+APP+'/SDLActivity.java')
        print('')
    
    print('You should now be ready to compile your own App in AndroidStudio')
    
    input('')


if __name__ == '__main__':
    import sys
    
    def print_help():
        print('Usage: python', sys.argv[0], '<DOMAIN_NAMESPACE> <DOMAIN> <APP> [use_mixer] [use_fetch] [use_admob] [use_billing]')
        print(' e.g.: python', sys.argv[0], 'de horsimann some')
        exit(1)
    

    if len(sys.argv) < 4 or len(sys.argv) > 8:
        print_help()

    DOMAIN_NAMESPACE = sys.argv[1]
    DOMAIN = sys.argv[2]
    APP = sys.argv[3]
    
    if 'use_mixer' in sys.argv[4:]:
        USE_MIXER = True
    
    if 'use_fetch' in sys.argv[4:]:
        USE_FETCH = True
    
    if 'use_admob' in sys.argv[4:]:
        USE_ADMOB = True
        
    if 'use_billing' in sys.argv[4:]:
        USE_BILLING = True

    print('DOMAIN_NAMESPACE =', DOMAIN_NAMESPACE)
    print('DOMAIN =', DOMAIN)
    print('APP =', APP)
    print('use_mixer =', USE_MIXER)
    print('use_fetch =', USE_FETCH)
    print('use_admob =', USE_ADMOB)
    print('use_billing =', USE_BILLING)

    run_template()
