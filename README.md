# some android app template

[some](https://github.com/renehorstmann/some) is a small C game engine, that can be compiled to Desktop, Android, Web, ...

This is a template to generate an Android App Project for [AndroidStudio](https://developer.android.com/studio).

## Getting started

- Open the python script [template.py](template.py) in a text editor
- change the template strings to match your App	
	- `DOMAIN_NAMESPACE`
	- `DOMAIN`
	- `APP`
- run the script
- open the project in `out/<APP>` [AndroidStudio](https://developer.android.com/studio)
- test the some hello world demo
- replace the code in: `out/<APP>/app/jni/src/include` & `out/<APP>/app/jni/src/src`
- add resources to some: `out/<APP>/app/src/main/assets/res`
- have a look at the Android makefile: `out/<APP>/app/jni/src/Android.mk`
- change the icons in: `out/<APP>/app/src/main/res`
- have fun


## Author

René Horstmann

## License

The somme project is licensed under the MIT License - see the someLICENSE file for details

- Used third party libraries:
    - [SDL2](https://www.libsdl.org/) (zlib License)
    - [Emscripten](emscripten.org) (MIT License)
    - [nuklear](https://github.com/Immediate-Mode-UI/Nuklear) for debug gui windows (MIT License)
    - [curl](https://curl.se/docs/copyright.html) (MIT like License)
