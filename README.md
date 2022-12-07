# some android app template

[some](https://github.com/renehorstmann/some) is a small C game engine, that can be compiled to Desktop, Android, Web, ...

This is a template to generate an Android App Project for [AndroidStudio](https://developer.android.com/studio).

## Getting started

- Clone the project and cd to that dir
- run the template script: `python template.py <DOMAIN_NAMESPACE> <DOMAIN> <APP>
- open the project `out/<APP>` in [AndroidStudio](https://developer.android.com/studio)
- test the some *hello world* demo
- replace the code in: `out/<APP>/app/jni/src/include` & `out/<APP>/app/jni/src/src`
- add resources: `out/<APP>/app/src/main/assets/res`
- have a look at the Android makefile: `out/<APP>/app/jni/src/Android.mk`
- change the icons in: `out/<APP>/app/src/main/res`
- have fun


## Google AdMob and Play Store Billing
By default, the app will be created with dependencies on Google AdMob and Play Store Billing.
With these dependencies, an App can show reward ads or allow for IN-APP purchases.

If you DO NOT WANT to use them, remove the dependencies in the build.gradle module file.
Remove the lines in the application section of the AndoridManifest.xml
And comment out all stuff in SDLActivity with ump_*, admob_* and billing_* (and the imports and usages of course)

## Author

René Horstmann

## License

The some project is licensed under the MIT License - see the someLICENSE file for details

- Used third party libraries:
    - [SDL2](https://www.libsdl.org/) (zlib License)
    - [Emscripten](emscripten.org) (MIT License)
    - [nuklear](https://github.com/Immediate-Mode-UI/Nuklear) for debug gui windows (MIT License)
    - [curl](https://curl.se/docs/copyright.html) (MIT like License)
    - [sfd](https://github.com/rxi/sfd) for simple file dialogs (MIT License)
