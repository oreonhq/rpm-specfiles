%global source0_hash aba4679a5b1f2bf62482eba6e8814a94de7ffc86de5f8587ba199fcc61b4a04f

Name:           allegro
Version:        5.2.11.3
Release:        1%{?dist}

Summary:        A game programming library
Summary(es):    Una libreria de programacion de juegos
Summary(fr):    Une librairie de programmation de jeux
Summary(it):    Una libreria per la programmazione di videogiochi
Summary(cs):    Knihovna pro programování her

License:        Giftware
URL:            http://liballeg.org/
Source0:        https://github.com/liballeg/allegro5/releases/download/%{version}/allegro-%{version}.tar.gz
Patch1:         allegro-4.0.3-cfg.patch
Patch2:         allegro-4.0.3-libdir.patch
Patch5:         allegro-4.4.2-buildsys-fix.patch
Patch6:         allegro-4.4.2-doc-noversion.patch
# Replace racy recursive mutex implementation with proper recursive mutexes
Patch8:         allegro-4.4.2-mutex-fix.patch
# Calling Xsync from the bg thread causes deadlock issues
Patch9:         allegro-4.4.2-no-xsync-from-thread.patch
# gnome-shell starts apps while gnome-shell has the keyb grabbed...
Patch10:        allegro-4.4.2-keybgrab-fix.patch
# 4.4.3 has dropped the fadd/fsub etc aliases, but some apps need them
Patch11:        allegro-4.4.2-compat-fix-aliases.patch
# 4.4.3 accidentally broke the tools, fix them (rhbz1682921)
Patch12:        allegro-4.4.3-datafile-double-free.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1767827
# starting texinfo-6.7 the default encoding is UTF-8 and because allegro's
# source .texi file is encoded in ISO-8859-1, additional command is needed
Patch13:        allegro-4.4.3-texinfo-non-utf8-input-fix.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=2225996
# Fix a buffer overflow in dat2c tool causing FTBFS of allegro using packages
Patch14:        allegro-4.4.3-dat2c-buffer-overflow.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  texinfo cmake
BuildRequires:  xorg-x11-proto-devel libX11-devel libXpm-devel libXcursor-devel
BuildRequires:  libXxf86vm-devel libXxf86dga-devel libGL-devel libGLU-devel
BuildRequires:  alsa-lib-devel jack-audio-connection-kit-devel
BuildRequires:  libjpeg-devel libpng-devel libvorbis-devel
Requires:       timidity++-patches

%description
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

%description -l es
Allegro es una librería multi-plataforma creada para ser usada en la
programación de juegos u otro tipo de programación multimedia.

%description -l fr
Allegro est une librairie multi-plateforme destinée à être utilisée
dans les jeux vidéo ou d'autres types de programmation multimédia.

%description -l it
Allegro è una libreria multipiattaforma dedicata all'uso nei
videogiochi ed in altri tipi di programmazione multimediale.

%description -l cs
Allegro je multiplatformní knihovna pro počítačové hry a jiné
typy multimediálního programování.


%package devel
Summary:        A game programming library
Summary(es):    Una libreria de programacion de juegos
Summary(fr):    Une librairie de programmation de jeux
Summary(it):    Una libreria per la programmazione di videogiochi
Summary(cs):    Knihovna pro programování her
Requires:       %{name}%{?_isa} = %{version}-%{release}, xorg-x11-proto-devel
Requires:       libX11-devel, libXcursor-devel

%description devel
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming. This package is needed to
build programs written with Allegro.

%description devel -l es
Allegro es una librería multi-plataforma creada para ser usada en la
programación de juegos u otro tipo de programación multimedia. Este
paquete es necesario para compilar los programas que usen Allegro.

%description devel -l fr
Allegro est une librairie multi-plateforme destinée à être utilisée
dans les jeux vidéo ou d'autres types de programmation multimédia. Ce
package est nécessaire pour compiler les programmes utilisant Allegro.

%description devel -l it
Allegro è una libreria multipiattaforma dedicata all'uso nei
videogiochi ed in altri tipi di programmazione multimediale. Questo
pacchetto è necessario per compilare programmi scritti con Allegro.

%description devel -l cs
Allegro je multiplatformní knihovna pro počítačové hry a jiné
typy multimediálního programování. Tento balíček je je potřebný
k sestavení programů napsaných v Allegru.


%package tools
Summary:        Extra tools for the Allegro programming library
Summary(es):    Herramientas adicionales para la librería de programación Allegro
Summary(fr):    Outils supplémentaires pour la librairie de programmation Allegro
Summary(it):    Programmi di utilità aggiuntivi per la libreria Allegro
Summary(cs):    Přídavné nástroje pro programovou knihovnu Allegro
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description tools
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming. This package contains extra
tools which are useful for developing Allegro programs.

%description tools -l es
Allegro es una librería multi-plataforma creada para ser usada en la
programación de juegos u otro tipo de programación multimedia. Este
paquete contiene herramientas adicionales que son útiles para
desarrollar programas que usen Allegro.

%description tools -l fr
Allegro est une librairie multi-plateforme destinée à être utilisée
dans les jeux vidéo ou d'autres types de programmation multimédia. Ce
package contient des outils supplémentaires qui sont utiles pour le
développement de programmes avec Allegro.

%description tools -l it
Allegro è una libreria multipiattaforma dedicata all'uso nei
videogiochi ed in altri tipi di programmazione multimediale. Questo
pacchetto contiene programmi di utilità aggiuntivi utili allo sviluppo
di programmi con Allegro.

%description tools -l cs
Allegro je multiplatformní knihovna pro počítačové hry a jiné
typy multimediálního programování. Tento balíček obsahuje přídavné nástroje,
které jsou užitečné pro vývoj Allegro programů.

%package jack-plugin
Summary:        Allegro JACK (Jack Audio Connection Kit) plugin
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description jack-plugin
This package contains a plugin for Allegro which enables Allegro to playback
sound through JACK (Jack Audio Connection Kit).


%package -n alleggl
Summary:        OpenGL support library for Allegro
License:        Zlib OR GPL-1.0-or-later
URL:            http://allegrogl.sourceforge.net/
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n alleggl
AllegroGL is an Allegro add-on that allows you to use OpenGL alongside Allegro.
You use OpenGL for your rendering to the screen, and Allegro for miscellaneous
tasks like gathering input, doing timers, getting cross-platform portability,
loading data, and drawing your textures. So this library fills the same hole
that things like glut do.

%package -n alleggl-devel
Summary:        Development files for alleggl
License:        Zlib OR GPL-1.0-or-later
Requires:       alleggl%{?_isa} = %{version}-%{release}

%description -n alleggl-devel
The alleggl-devel package contains libraries and header files for
developing applications that use alleggl.


%package -n jpgalleg
Summary:        JPEG library for the Allegro game library
License:        Zlib
URL:            http://www.ecplusplus.com/index.php?page=projects&pid=1
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n jpgalleg
jpgalleg is a JPEG library for use with the Allegro game library. It allows
using JPEG's as Allegro bitmaps.

%package -n jpgalleg-devel
Summary:        Development files for jpgalleg
License:        Zlib
Requires:       jpgalleg%{?_isa} = %{version}-%{release}

%description -n jpgalleg-devel
The jpgalleg-devel package contains libraries and header files for
developing applications that use jpgalleg.


%package loadpng
Summary:        OGG/Vorbis library for the Allegro game library
License:        LicenseRef-Fedora-Public-Domain
URL:            http://wiki.allegro.cc/index.php?title=LoadPNG
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description loadpng
loadpng is some glue that makes it easy to use libpng to load and
save bitmaps from Allegro programs.

%package loadpng-devel
Summary:        Development files for loadpng
License:        LicenseRef-Fedora-Public-Domain
Requires:       %{name}-loadpng%{?_isa} = %{version}-%{release}

%description loadpng-devel
The loadpng-devel package contains libraries and header files for
developing applications that use loadpng.


%package logg
Summary:        OGG/Vorbis library for the Allegro game library
License:        MIT
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description logg
LOGG is an Allegro add-on library for playing OGG/Vorbis audio files.

%package logg-devel
Summary:        Development files for logg
License:        MIT
Requires:       %{name}-logg%{?_isa} = %{version}-%{release}

%description logg-devel
The logg-devel package contains libraries and header files for
developing applications that use logg.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

%build
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake \
%if "%{?_lib}" == "lib64"
 %{?_cmake_lib_suffix64} \
%endif
 -DOpenGL_GL_PREFERENCE:STRING=LEGACY -DCMAKE_SKIP_RPATH:BOOL=YES -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES \
 -DDOCDIR:STRING=%{_pkgdocdir} -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE
%cmake_build

pushd %{_vpath_builddir}
# Converting text documentation to UTF-8 encoding.
for file in docs/AUTHORS docs/CHANGES docs/THANKS \
        docs/info/*.info docs/txt/*.txt docs/man/get_camera_matrix.3 \
        ../addons/allegrogl/changelog; do
  iconv -f ISO-8859-1 -t UTF-8 -o $file.new $file && \
  touch -r $file $file.new && \
  mv $file.new $file
done
popd

%install
%cmake_install

pushd %{_vpath_builddir}
# installation of these is broken, because they use a cmake GLOB, but
# that gets "resolved" when runnning cmake, and at that time the files
# to install aren't generated yet ...
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man3
mkdir -p $RPM_BUILD_ROOT%{_pkgdocdir}/html
install -p -m 644 docs/man/*.3 $RPM_BUILD_ROOT%{_mandir}/man3
install -p -m 644 docs/html/*.{html,css} \
    $RPM_BUILD_ROOT%{_pkgdocdir}/html/
install -m 755 docs/makedoc $RPM_BUILD_ROOT%{_bindir}/allegro-makedoc
popd

# Install some extra files
install -Dpm 644 allegro.cfg $RPM_BUILD_ROOT%{_sysconfdir}/allegrorc
install -pm 755 tools/x11/xfixicon.sh $RPM_BUILD_ROOT%{_bindir}
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/allegro
install -pm 644 keyboard.dat language.dat $RPM_BUILD_ROOT%{_datadir}/allegro
install -Dpm 644 misc/allegro.m4 $RPM_BUILD_ROOT%{_datadir}/aclocal/allegro.m4

mkdir -p $RPM_BUILD_ROOT%{_pkgdocdir}/allegrogl
install -pm 644 addons/allegrogl/changelog addons/allegrogl/faq.txt \
 addons/allegrogl/readme.txt addons/allegrogl/bugs.txt \
 addons/allegrogl/extensions.txt addons/allegrogl/howto.txt addons/allegrogl/quickstart.txt \
 addons/allegrogl/todo.txt $RPM_BUILD_ROOT%{_pkgdocdir}/allegrogl/

mkdir -p $RPM_BUILD_ROOT%{_pkgdocdir}/loadpng
install -pm 644 addons/loadpng/CHANGES.txt addons/loadpng/README.txt addons/loadpng/THANKS.txt \
 $RPM_BUILD_ROOT%{_pkgdocdir}/loadpng/

mkdir -p $RPM_BUILD_ROOT%{_pkgdocdir}/jpgalleg
install -pm 644 addons/jpgalleg/readme.txt \
 $RPM_BUILD_ROOT%{_pkgdocdir}/jpgalleg/


%ldconfig_scriptlets 
%ldconfig_scriptlets -n alleggl 

%ldconfig_scriptlets -n jpgalleg

%ldconfig_scriptlets loadpng

%ldconfig_scriptlets logg


%files
%{_pkgdocdir}/
%exclude %{_pkgdocdir}/dat*.txt
%exclude %{_pkgdocdir}/grabber.txt
%exclude %{_pkgdocdir}/allegrogl
%exclude %{_pkgdocdir}/jpgalleg
%exclude %{_pkgdocdir}/loadpng
%exclude %{_pkgdocdir}/loadpng
%license %{_pkgdocdir}/license.txt
%config(noreplace) %{_sysconfdir}/allegrorc
%{_libdir}/liballeg.so.4*
%{_datadir}/allegro
# We cannot use exclude for alleg-jack.so because then the build-id for it
# still ends up in the main allegro package, e.g. rpmlint says:
# allegro.x86_64: W: dangling-relative-symlink /usr/lib/.build-id/48/024a0ddad02d9c6f4b956fb18f20d4a0bfde41 ../../../../usr/lib64/allegro/4.4.3/alleg-jack.so
%dir %{_libdir}/allegro
%dir %{_libdir}/allegro/4.4.3
%{_libdir}/allegro/4.4.3/alleg-alsa*.so
%{_libdir}/allegro/4.4.3/alleg-dga2.so
%{_libdir}/allegro/4.4.3/modules.lst

%files devel
%{_bindir}/allegro-config
%{_bindir}/allegro-makedoc
%{_libdir}/liballeg.so
%{_libdir}/pkgconfig/allegro.pc
%{_includedir}/allegro
%{_includedir}/allegro.h
%{_includedir}/xalleg.h
%{_datadir}/aclocal/allegro.m4
%{_infodir}/allegro.info*
%{_mandir}/man3/*

%{_pkgconfigdir}/allegro_acodec.pc
%{_pkgconfigdir}/allegro_audio.pc
%{_pkgconfigdir}/allegro_color.pc
%{_pkgconfigdir}/allegro_dialog.pc
%{_pkgconfigdir}/allegro_font.pc
%{_pkgconfigdir}/allegro_image.pc
%{_pkgconfigdir}/allegro_main.pc
%{_pkgconfigdir}/allegro_memfile.pc
%{_pkgconfigdir}/allegro_monolith.pc
%{_pkgconfigdir}/allegro_physfs.pc
%{_pkgconfigdir}/allegro_primitives.pc
%{_pkgconfigdir}/allegro_ttf.pc
%{_pkgconfigdir}/allegro_video.pc
%{_mandir}/man3/ALLEGRO_AUDIO_DEPTH.3.*
%{_mandir}/man3/ALLEGRO_AUDIO_DEVICE.3.*
%{_mandir}/man3/ALLEGRO_AUDIO_EVENT_TYPE.3.*
%{_mandir}/man3/ALLEGRO_AUDIO_PAN_NONE.3.*
%{_mandir}/man3/ALLEGRO_AUDIO_RECORDER.3.*
%{_mandir}/man3/ALLEGRO_AUDIO_RECORDER_EVENT.3.*
%{_mandir}/man3/ALLEGRO_AUDIO_STREAM.3.*
%{_mandir}/man3/ALLEGRO_BITMAP.3.*
%{_mandir}/man3/ALLEGRO_BITMAP_WRAP.3.*
%{_mandir}/man3/ALLEGRO_BPM_TO_SECS.3.*
%{_mandir}/man3/ALLEGRO_BPS_TO_SECS.3.*
%{_mandir}/man3/ALLEGRO_CHANNEL_CONF.3.*
%{_mandir}/man3/ALLEGRO_COLOR.3.*
%{_mandir}/man3/ALLEGRO_COND.3.*
%{_mandir}/man3/ALLEGRO_CONFIG.3.*
%{_mandir}/man3/ALLEGRO_CONFIG_ENTRY.3.*
%{_mandir}/man3/ALLEGRO_CONFIG_SECTION.3.*
%{_mandir}/man3/ALLEGRO_DISPLAY.3.*
%{_mandir}/man3/ALLEGRO_DISPLAY_MODE.3.*
%{_mandir}/man3/ALLEGRO_EVENT.3.*
%{_mandir}/man3/ALLEGRO_EVENT_QUEUE.3.*
%{_mandir}/man3/ALLEGRO_EVENT_SOURCE.3.*
%{_mandir}/man3/ALLEGRO_EVENT_TYPE.3.*
%{_mandir}/man3/ALLEGRO_EVENT_TYPE_IS_USER.3.*
%{_mandir}/man3/ALLEGRO_FILE.3.*
%{_mandir}/man3/ALLEGRO_FILECHOOSER.3.*
%{_mandir}/man3/ALLEGRO_FILE_INTERFACE.3.*
%{_mandir}/man3/ALLEGRO_FILE_MODE.3.*
%{_mandir}/man3/ALLEGRO_FONT.3.*
%{_mandir}/man3/ALLEGRO_FOR_EACH_FS_ENTRY_RESULT.3.*
%{_mandir}/man3/ALLEGRO_FS_ENTRY.3.*
%{_mandir}/man3/ALLEGRO_FS_INTERFACE.3.*
%{_mandir}/man3/ALLEGRO_GAMEPAD_BUTTON.3.*
%{_mandir}/man3/ALLEGRO_GAMEPAD_STICK.3.*
%{_mandir}/man3/ALLEGRO_GET_EVENT_TYPE.3.*
%{_mandir}/man3/ALLEGRO_GLYPH.3.*
%{_mandir}/man3/ALLEGRO_HAPTIC.3.*
%{_mandir}/man3/ALLEGRO_HAPTIC_CONSTANTS.3.*
%{_mandir}/man3/ALLEGRO_HAPTIC_EFFECT.3.*
%{_mandir}/man3/ALLEGRO_HAPTIC_EFFECT_ID.3.*
%{_mandir}/man3/ALLEGRO_INDEX_BUFFER.3.*
%{_mandir}/man3/ALLEGRO_JOYFLAGS.3.*
%{_mandir}/man3/ALLEGRO_JOYSTICK.3.*
%{_mandir}/man3/ALLEGRO_JOYSTICK_GUID.3.*
%{_mandir}/man3/ALLEGRO_JOYSTICK_STATE.3.*
%{_mandir}/man3/ALLEGRO_JOYSTICK_TYPE.3.*
%{_mandir}/man3/ALLEGRO_KEYBOARD_STATE.3.*
%{_mandir}/man3/ALLEGRO_LINE_CAP.3.*
%{_mandir}/man3/ALLEGRO_LINE_JOIN.3.*
%{_mandir}/man3/ALLEGRO_LOCKED_REGION.3.*
%{_mandir}/man3/ALLEGRO_MEMORY_INTERFACE.3.*
%{_mandir}/man3/ALLEGRO_MENU.3.*
%{_mandir}/man3/ALLEGRO_MENU_INFO.3.*
%{_mandir}/man3/ALLEGRO_MIXER.3.*
%{_mandir}/man3/ALLEGRO_MIXER_QUALITY.3.*
%{_mandir}/man3/ALLEGRO_MONITOR_INFO.3.*
%{_mandir}/man3/ALLEGRO_MOUSE_EMULATION_MODE.3.*
%{_mandir}/man3/ALLEGRO_MOUSE_STATE.3.*
%{_mandir}/man3/ALLEGRO_MSECS_TO_SECS.3.*
%{_mandir}/man3/ALLEGRO_MUTEX.3.*
%{_mandir}/man3/ALLEGRO_NEW_WINDOW_TITLE_MAX_SIZE.3.*
%{_mandir}/man3/ALLEGRO_PI.3.*
%{_mandir}/man3/ALLEGRO_PIXEL_FORMAT.3.*
%{_mandir}/man3/ALLEGRO_PLAYMODE.3.*
%{_mandir}/man3/ALLEGRO_PRIM_ATTR.3.*
%{_mandir}/man3/ALLEGRO_PRIM_BUFFER_FLAGS.3.*
%{_mandir}/man3/ALLEGRO_PRIM_QUALITY.3.*
%{_mandir}/man3/ALLEGRO_PRIM_STORAGE.3.*
%{_mandir}/man3/ALLEGRO_PRIM_TYPE.3.*
%{_mandir}/man3/ALLEGRO_RENDER_FUNCTION.3.*
%{_mandir}/man3/ALLEGRO_RENDER_STATE.3.*
%{_mandir}/man3/ALLEGRO_SAMPLE.3.*
%{_mandir}/man3/ALLEGRO_SAMPLE_ID.3.*
%{_mandir}/man3/ALLEGRO_SAMPLE_INSTANCE.3.*
%{_mandir}/man3/ALLEGRO_SEEK.3.*
%{_mandir}/man3/ALLEGRO_SHADER.3.*
%{_mandir}/man3/ALLEGRO_SHADER_PLATFORM.3.*
%{_mandir}/man3/ALLEGRO_SHADER_TYPE.3.*
%{_mandir}/man3/ALLEGRO_STATE.3.*
%{_mandir}/man3/ALLEGRO_STATE_FLAGS.3.*
%{_mandir}/man3/ALLEGRO_SYSTEM_ID.3.*
%{_mandir}/man3/ALLEGRO_TEXTLOG.3.*
%{_mandir}/man3/ALLEGRO_THREAD.3.*
%{_mandir}/man3/ALLEGRO_TIMEOUT.3.*
%{_mandir}/man3/ALLEGRO_TIMER.3.*
%{_mandir}/man3/ALLEGRO_TOUCH_INPUT.3.*
%{_mandir}/man3/ALLEGRO_TOUCH_INPUT_MAX_TOUCH_COUNT.3.*
%{_mandir}/man3/ALLEGRO_TOUCH_INPUT_STATE.3.*
%{_mandir}/man3/ALLEGRO_TOUCH_STATE.3.*
%{_mandir}/man3/ALLEGRO_TRANSFORM.3.*
%{_mandir}/man3/ALLEGRO_USECS_TO_SECS.3.*
%{_mandir}/man3/ALLEGRO_USER_EVENT.3.*
%{_mandir}/man3/ALLEGRO_USTR.3.*
%{_mandir}/man3/ALLEGRO_USTR_INFO.3.*
%{_mandir}/man3/ALLEGRO_VERTEX.3.*
%{_mandir}/man3/ALLEGRO_VERTEX_BUFFER.3.*
%{_mandir}/man3/ALLEGRO_VERTEX_CACHE_SIZE.3.*
%{_mandir}/man3/ALLEGRO_VERTEX_DECL.3.*
%{_mandir}/man3/ALLEGRO_VERTEX_ELEMENT.3.*
%{_mandir}/man3/ALLEGRO_VIDEO_EVENT_TYPE.3.*
%{_mandir}/man3/ALLEGRO_VIDEO_POSITION_TYPE.3.*
%{_mandir}/man3/ALLEGRO_VOICE.3.*
%{_mandir}/man3/ALLEGRO_WRITE_MASK_FLAGS.3.*
%{_mandir}/man3/al_acknowledge_drawing_halt.3.*
%{_mandir}/man3/al_acknowledge_drawing_resume.3.*
%{_mandir}/man3/al_acknowledge_resize.3.*
%{_mandir}/man3/al_add_config_comment.3.*
%{_mandir}/man3/al_add_config_section.3.*
%{_mandir}/man3/al_add_new_bitmap_flag.3.*
%{_mandir}/man3/al_add_timer_count.3.*
%{_mandir}/man3/al_android_get_activity.3.*
%{_mandir}/man3/al_android_get_jni_env.3.*
%{_mandir}/man3/al_android_get_os_version.3.*
%{_mandir}/man3/al_android_open_fd.3.*
%{_mandir}/man3/al_android_set_apk_file_interface.3.*
%{_mandir}/man3/al_android_set_apk_fs_interface.3.*
%{_mandir}/man3/al_append_menu_item.3.*
%{_mandir}/man3/al_append_native_text_log.3.*
%{_mandir}/man3/al_append_path_component.3.*
%{_mandir}/man3/al_apply_window_constraints.3.*
%{_mandir}/man3/al_attach_audio_stream_to_mixer.3.*
%{_mandir}/man3/al_attach_audio_stream_to_voice.3.*
%{_mandir}/man3/al_attach_mixer_to_mixer.3.*
%{_mandir}/man3/al_attach_mixer_to_voice.3.*
%{_mandir}/man3/al_attach_sample_instance_to_mixer.3.*
%{_mandir}/man3/al_attach_sample_instance_to_voice.3.*
%{_mandir}/man3/al_attach_shader_source.3.*
%{_mandir}/man3/al_attach_shader_source_file.3.*
%{_mandir}/man3/al_backup_dirty_bitmap.3.*
%{_mandir}/man3/al_backup_dirty_bitmaps.3.*
%{_mandir}/man3/al_broadcast_cond.3.*
%{_mandir}/man3/al_build_camera_transform.3.*
%{_mandir}/man3/al_build_menu.3.*
%{_mandir}/man3/al_build_shader.3.*
%{_mandir}/man3/al_build_transform.3.*
%{_mandir}/man3/al_calculate_arc.3.*
%{_mandir}/man3/al_calculate_ribbon.3.*
%{_mandir}/man3/al_calculate_spline.3.*
%{_mandir}/man3/al_calloc.3.*
%{_mandir}/man3/al_calloc_with_context.3.*
%{_mandir}/man3/al_can_get_mouse_cursor_position.3.*
%{_mandir}/man3/al_can_set_keyboard_leds.3.*
%{_mandir}/man3/al_change_directory.3.*
%{_mandir}/man3/al_check_inverse.3.*
%{_mandir}/man3/al_clear_depth_buffer.3.*
%{_mandir}/man3/al_clear_keyboard_state.3.*
%{_mandir}/man3/al_clear_to_color.3.*
%{_mandir}/man3/al_clipboard_has_text.3.*
%{_mandir}/man3/al_clone_bitmap.3.*
%{_mandir}/man3/al_clone_menu.3.*
%{_mandir}/man3/al_clone_menu_for_popup.3.*
%{_mandir}/man3/al_clone_path.3.*
%{_mandir}/man3/al_close_directory.3.*
%{_mandir}/man3/al_close_native_text_log.3.*
%{_mandir}/man3/al_close_video.3.*
%{_mandir}/man3/al_color_cmyk.3.*
%{_mandir}/man3/al_color_cmyk_to_rgb.3.*
%{_mandir}/man3/al_color_distance_ciede2000.3.*
%{_mandir}/man3/al_color_hsl.3.*
%{_mandir}/man3/al_color_hsl_to_rgb.3.*
%{_mandir}/man3/al_color_hsv.3.*
%{_mandir}/man3/al_color_hsv_to_rgb.3.*
%{_mandir}/man3/al_color_html.3.*
%{_mandir}/man3/al_color_html_to_rgb.3.*
%{_mandir}/man3/al_color_lab.3.*
%{_mandir}/man3/al_color_lab_to_rgb.3.*
%{_mandir}/man3/al_color_lch.3.*
%{_mandir}/man3/al_color_lch_to_rgb.3.*
%{_mandir}/man3/al_color_linear.3.*
%{_mandir}/man3/al_color_linear_to_rgb.3.*
%{_mandir}/man3/al_color_name.3.*
%{_mandir}/man3/al_color_name_to_rgb.3.*
%{_mandir}/man3/al_color_oklab.3.*
%{_mandir}/man3/al_color_oklab_to_rgb.3.*
%{_mandir}/man3/al_color_rgb_to_cmyk.3.*
%{_mandir}/man3/al_color_rgb_to_hsl.3.*
%{_mandir}/man3/al_color_rgb_to_hsv.3.*
%{_mandir}/man3/al_color_rgb_to_html.3.*
%{_mandir}/man3/al_color_rgb_to_lab.3.*
%{_mandir}/man3/al_color_rgb_to_lch.3.*
%{_mandir}/man3/al_color_rgb_to_linear.3.*
%{_mandir}/man3/al_color_rgb_to_name.3.*
%{_mandir}/man3/al_color_rgb_to_oklab.3.*
%{_mandir}/man3/al_color_rgb_to_xyy.3.*
%{_mandir}/man3/al_color_rgb_to_xyz.3.*
%{_mandir}/man3/al_color_rgb_to_yuv.3.*
%{_mandir}/man3/al_color_xyy.3.*
%{_mandir}/man3/al_color_xyy_to_rgb.3.*
%{_mandir}/man3/al_color_xyz.3.*
%{_mandir}/man3/al_color_xyz_to_rgb.3.*
%{_mandir}/man3/al_color_yuv.3.*
%{_mandir}/man3/al_color_yuv_to_rgb.3.*
%{_mandir}/man3/al_compose_transform.3.*
%{_mandir}/man3/al_convert_bitmap.3.*
%{_mandir}/man3/al_convert_mask_to_alpha.3.*
%{_mandir}/man3/al_convert_memory_bitmaps.3.*
%{_mandir}/man3/al_copy_transform.3.*
%{_mandir}/man3/al_create_audio_recorder.3.*
%{_mandir}/man3/al_create_audio_stream.3.*
%{_mandir}/man3/al_create_bitmap.3.*
%{_mandir}/man3/al_create_builtin_font.3.*
%{_mandir}/man3/al_create_cond.3.*
%{_mandir}/man3/al_create_config.3.*
%{_mandir}/man3/al_create_display.3.*
%{_mandir}/man3/al_create_event_queue.3.*
%{_mandir}/man3/al_create_file_handle.3.*
%{_mandir}/man3/al_create_fs_entry.3.*
%{_mandir}/man3/al_create_index_buffer.3.*
%{_mandir}/man3/al_create_menu.3.*
%{_mandir}/man3/al_create_mixer.3.*
%{_mandir}/man3/al_create_mouse_cursor.3.*
%{_mandir}/man3/al_create_mutex.3.*
%{_mandir}/man3/al_create_mutex_recursive.3.*
%{_mandir}/man3/al_create_native_file_dialog.3.*
%{_mandir}/man3/al_create_path.3.*
%{_mandir}/man3/al_create_path_for_directory.3.*
%{_mandir}/man3/al_create_popup_menu.3.*
%{_mandir}/man3/al_create_sample.3.*
%{_mandir}/man3/al_create_sample_instance.3.*
%{_mandir}/man3/al_create_shader.3.*
%{_mandir}/man3/al_create_sub_bitmap.3.*
%{_mandir}/man3/al_create_thread.3.*
%{_mandir}/man3/al_create_thread_with_stacksize.3.*
%{_mandir}/man3/al_create_timer.3.*
%{_mandir}/man3/al_create_vertex_buffer.3.*
%{_mandir}/man3/al_create_vertex_decl.3.*
%{_mandir}/man3/al_create_voice.3.*
%{_mandir}/man3/al_cstr.3.*
%{_mandir}/man3/al_cstr_dup.3.*
%{_mandir}/man3/al_destroy_audio_recorder.3.*
%{_mandir}/man3/al_destroy_audio_stream.3.*
%{_mandir}/man3/al_destroy_bitmap.3.*
%{_mandir}/man3/al_destroy_cond.3.*
%{_mandir}/man3/al_destroy_config.3.*
%{_mandir}/man3/al_destroy_display.3.*
%{_mandir}/man3/al_destroy_event_queue.3.*
%{_mandir}/man3/al_destroy_font.3.*
%{_mandir}/man3/al_destroy_fs_entry.3.*
%{_mandir}/man3/al_destroy_index_buffer.3.*
%{_mandir}/man3/al_destroy_menu.3.*
%{_mandir}/man3/al_destroy_mixer.3.*
%{_mandir}/man3/al_destroy_mouse_cursor.3.*
%{_mandir}/man3/al_destroy_mutex.3.*
%{_mandir}/man3/al_destroy_native_file_dialog.3.*
%{_mandir}/man3/al_destroy_path.3.*
%{_mandir}/man3/al_destroy_sample.3.*
%{_mandir}/man3/al_destroy_sample_instance.3.*
%{_mandir}/man3/al_destroy_shader.3.*
%{_mandir}/man3/al_destroy_thread.3.*
%{_mandir}/man3/al_destroy_timer.3.*
%{_mandir}/man3/al_destroy_user_event_source.3.*
%{_mandir}/man3/al_destroy_vertex_buffer.3.*
%{_mandir}/man3/al_destroy_vertex_decl.3.*
%{_mandir}/man3/al_destroy_voice.3.*
%{_mandir}/man3/al_detach_audio_stream.3.*
%{_mandir}/man3/al_detach_mixer.3.*
%{_mandir}/man3/al_detach_sample_instance.3.*
%{_mandir}/man3/al_detach_voice.3.*
%{_mandir}/man3/al_disable_menu_event_source.3.*
%{_mandir}/man3/al_do_multiline_text.3.*
%{_mandir}/man3/al_do_multiline_ustr.3.*
%{_mandir}/man3/al_drain_audio_stream.3.*
%{_mandir}/man3/al_draw_arc.3.*
%{_mandir}/man3/al_draw_bitmap.3.*
%{_mandir}/man3/al_draw_bitmap_region.3.*
%{_mandir}/man3/al_draw_circle.3.*
%{_mandir}/man3/al_draw_ellipse.3.*
%{_mandir}/man3/al_draw_elliptical_arc.3.*
%{_mandir}/man3/al_draw_filled_circle.3.*
%{_mandir}/man3/al_draw_filled_ellipse.3.*
%{_mandir}/man3/al_draw_filled_pieslice.3.*
%{_mandir}/man3/al_draw_filled_polygon.3.*
%{_mandir}/man3/al_draw_filled_polygon_with_holes.3.*
%{_mandir}/man3/al_draw_filled_rectangle.3.*
%{_mandir}/man3/al_draw_filled_rounded_rectangle.3.*
%{_mandir}/man3/al_draw_filled_triangle.3.*
%{_mandir}/man3/al_draw_glyph.3.*
%{_mandir}/man3/al_draw_indexed_buffer.3.*
%{_mandir}/man3/al_draw_indexed_prim.3.*
%{_mandir}/man3/al_draw_justified_text.3.*
%{_mandir}/man3/al_draw_justified_textf.3.*
%{_mandir}/man3/al_draw_justified_ustr.3.*
%{_mandir}/man3/al_draw_line.3.*
%{_mandir}/man3/al_draw_multiline_text.3.*
%{_mandir}/man3/al_draw_multiline_textf.3.*
%{_mandir}/man3/al_draw_multiline_ustr.3.*
%{_mandir}/man3/al_draw_pieslice.3.*
%{_mandir}/man3/al_draw_pixel.3.*
%{_mandir}/man3/al_draw_polygon.3.*
%{_mandir}/man3/al_draw_polyline.3.*
%{_mandir}/man3/al_draw_prim.3.*
%{_mandir}/man3/al_draw_rectangle.3.*
%{_mandir}/man3/al_draw_ribbon.3.*
%{_mandir}/man3/al_draw_rotated_bitmap.3.*
%{_mandir}/man3/al_draw_rounded_rectangle.3.*
%{_mandir}/man3/al_draw_scaled_bitmap.3.*
%{_mandir}/man3/al_draw_scaled_rotated_bitmap.3.*
%{_mandir}/man3/al_draw_soft_line.3.*
%{_mandir}/man3/al_draw_soft_triangle.3.*
%{_mandir}/man3/al_draw_spline.3.*
%{_mandir}/man3/al_draw_text.3.*
%{_mandir}/man3/al_draw_textf.3.*
%{_mandir}/man3/al_draw_tinted_bitmap.3.*
%{_mandir}/man3/al_draw_tinted_bitmap_region.3.*
%{_mandir}/man3/al_draw_tinted_rotated_bitmap.3.*
%{_mandir}/man3/al_draw_tinted_scaled_bitmap.3.*
%{_mandir}/man3/al_draw_tinted_scaled_rotated_bitmap.3.*
%{_mandir}/man3/al_draw_tinted_scaled_rotated_bitmap_region.3.*
%{_mandir}/man3/al_draw_triangle.3.*
%{_mandir}/man3/al_draw_ustr.3.*
%{_mandir}/man3/al_draw_vertex_buffer.3.*
%{_mandir}/man3/al_drop_next_event.3.*
%{_mandir}/man3/al_drop_path_tail.3.*
%{_mandir}/man3/al_emit_user_event.3.*
%{_mandir}/man3/al_enable_menu_event_source.3.*
%{_mandir}/man3/al_fclearerr.3.*
%{_mandir}/man3/al_fclose.3.*
%{_mandir}/man3/al_feof.3.*
%{_mandir}/man3/al_ferrmsg.3.*
%{_mandir}/man3/al_ferror.3.*
%{_mandir}/man3/al_fflush.3.*
%{_mandir}/man3/al_fget_ustr.3.*
%{_mandir}/man3/al_fgetc.3.*
%{_mandir}/man3/al_fgets.3.*
%{_mandir}/man3/al_filename_exists.3.*
%{_mandir}/man3/al_fill_silence.3.*
%{_mandir}/man3/al_find_menu.3.*
%{_mandir}/man3/al_find_menu_item.3.*
%{_mandir}/man3/al_fixacos.3.*
%{_mandir}/man3/al_fixadd.3.*
%{_mandir}/man3/al_fixasin.3.*
%{_mandir}/man3/al_fixatan.3.*
%{_mandir}/man3/al_fixatan2.3.*
%{_mandir}/man3/al_fixceil.3.*
%{_mandir}/man3/al_fixcos.3.*
%{_mandir}/man3/al_fixdiv.3.*
%{_mandir}/man3/al_fixed.3.*
%{_mandir}/man3/al_fixfloor.3.*
%{_mandir}/man3/al_fixhypot.3.*
%{_mandir}/man3/al_fixmul.3.*
%{_mandir}/man3/al_fixsin.3.*
%{_mandir}/man3/al_fixsqrt.3.*
%{_mandir}/man3/al_fixsub.3.*
%{_mandir}/man3/al_fixtan.3.*
%{_mandir}/man3/al_fixtof.3.*
%{_mandir}/man3/al_fixtoi.3.*
%{_mandir}/man3/al_fixtorad_r.3.*
%{_mandir}/man3/al_flip_display.3.*
%{_mandir}/man3/al_flush_event_queue.3.*
%{_mandir}/man3/al_fopen.3.*
%{_mandir}/man3/al_fopen_fd.3.*
%{_mandir}/man3/al_fopen_interface.3.*
%{_mandir}/man3/al_fopen_slice.3.*
%{_mandir}/man3/al_for_each_fs_entry.3.*
%{_mandir}/man3/al_fprintf.3.*
%{_mandir}/man3/al_fputc.3.*
%{_mandir}/man3/al_fputs.3.*
%{_mandir}/man3/al_fread.3.*
%{_mandir}/man3/al_fread16be.3.*
%{_mandir}/man3/al_fread16le.3.*
%{_mandir}/man3/al_fread32be.3.*
%{_mandir}/man3/al_fread32le.3.*
%{_mandir}/man3/al_free.3.*
%{_mandir}/man3/al_free_with_context.3.*
%{_mandir}/man3/al_fs_entry_exists.3.*
%{_mandir}/man3/al_fseek.3.*
%{_mandir}/man3/al_fsize.3.*
%{_mandir}/man3/al_ftell.3.*
%{_mandir}/man3/al_ftofix.3.*
%{_mandir}/man3/al_fungetc.3.*
%{_mandir}/man3/al_fwrite.3.*
%{_mandir}/man3/al_fwrite16be.3.*
%{_mandir}/man3/al_fwrite16le.3.*
%{_mandir}/man3/al_fwrite32be.3.*
%{_mandir}/man3/al_fwrite32le.3.*
%{_mandir}/man3/al_get_allegro_acodec_version.3.*
%{_mandir}/man3/al_get_allegro_audio_version.3.*
%{_mandir}/man3/al_get_allegro_color_version.3.*
%{_mandir}/man3/al_get_allegro_font_version.3.*
%{_mandir}/man3/al_get_allegro_image_version.3.*
%{_mandir}/man3/al_get_allegro_memfile_version.3.*
%{_mandir}/man3/al_get_allegro_native_dialog_version.3.*
%{_mandir}/man3/al_get_allegro_physfs_version.3.*
%{_mandir}/man3/al_get_allegro_primitives_version.3.*
%{_mandir}/man3/al_get_allegro_ttf_version.3.*
%{_mandir}/man3/al_get_allegro_version.3.*
%{_mandir}/man3/al_get_allegro_video_version.3.*
%{_mandir}/man3/al_get_app_name.3.*
%{_mandir}/man3/al_get_audio_depth_size.3.*
%{_mandir}/man3/al_get_audio_device_name.3.*
%{_mandir}/man3/al_get_audio_output_device.3.*
%{_mandir}/man3/al_get_audio_recorder_event.3.*
%{_mandir}/man3/al_get_audio_recorder_event_source.3.*
%{_mandir}/man3/al_get_audio_stream_attached.3.*
%{_mandir}/man3/al_get_audio_stream_channels.3.*
%{_mandir}/man3/al_get_audio_stream_depth.3.*
%{_mandir}/man3/al_get_audio_stream_event_source.3.*
%{_mandir}/man3/al_get_audio_stream_fragment.3.*
%{_mandir}/man3/al_get_audio_stream_fragments.3.*
%{_mandir}/man3/al_get_audio_stream_frequency.3.*
%{_mandir}/man3/al_get_audio_stream_gain.3.*
%{_mandir}/man3/al_get_audio_stream_length.3.*
%{_mandir}/man3/al_get_audio_stream_length_secs.3.*
%{_mandir}/man3/al_get_audio_stream_pan.3.*
%{_mandir}/man3/al_get_audio_stream_played_samples.3.*
%{_mandir}/man3/al_get_audio_stream_playing.3.*
%{_mandir}/man3/al_get_audio_stream_playmode.3.*
%{_mandir}/man3/al_get_audio_stream_position_secs.3.*
%{_mandir}/man3/al_get_audio_stream_speed.3.*
%{_mandir}/man3/al_get_available_audio_stream_fragments.3.*
%{_mandir}/man3/al_get_backbuffer.3.*
%{_mandir}/man3/al_get_bitmap_blend_color.3.*
%{_mandir}/man3/al_get_bitmap_blender.3.*
%{_mandir}/man3/al_get_bitmap_depth.3.*
%{_mandir}/man3/al_get_bitmap_flags.3.*
%{_mandir}/man3/al_get_bitmap_format.3.*
%{_mandir}/man3/al_get_bitmap_height.3.*
%{_mandir}/man3/al_get_bitmap_samples.3.*
%{_mandir}/man3/al_get_bitmap_width.3.*
%{_mandir}/man3/al_get_bitmap_x.3.*
%{_mandir}/man3/al_get_bitmap_y.3.*
%{_mandir}/man3/al_get_blend_color.3.*
%{_mandir}/man3/al_get_blender.3.*
%{_mandir}/man3/al_get_channel_count.3.*
%{_mandir}/man3/al_get_clipboard_text.3.*
%{_mandir}/man3/al_get_clipping_rectangle.3.*
%{_mandir}/man3/al_get_config_value.3.*
%{_mandir}/man3/al_get_cpu_count.3.*
%{_mandir}/man3/al_get_current_directory.3.*
%{_mandir}/man3/al_get_current_display.3.*
%{_mandir}/man3/al_get_current_inverse_transform.3.*
%{_mandir}/man3/al_get_current_projection_transform.3.*
%{_mandir}/man3/al_get_current_shader.3.*
%{_mandir}/man3/al_get_current_transform.3.*
%{_mandir}/man3/al_get_d3d_device.3.*
%{_mandir}/man3/al_get_d3d_system_texture.3.*
%{_mandir}/man3/al_get_d3d_texture_position.3.*
%{_mandir}/man3/al_get_d3d_texture_size.3.*
%{_mandir}/man3/al_get_d3d_video_texture.3.*
%{_mandir}/man3/al_get_default_menu_event_source.3.*
%{_mandir}/man3/al_get_default_mixer.3.*
%{_mandir}/man3/al_get_default_shader_source.3.*
%{_mandir}/man3/al_get_default_voice.3.*
%{_mandir}/man3/al_get_display_adapter.3.*
%{_mandir}/man3/al_get_display_event_source.3.*
%{_mandir}/man3/al_get_display_flags.3.*
%{_mandir}/man3/al_get_display_format.3.*
%{_mandir}/man3/al_get_display_height.3.*
%{_mandir}/man3/al_get_display_menu.3.*
%{_mandir}/man3/al_get_display_mode.3.*
%{_mandir}/man3/al_get_display_option.3.*
%{_mandir}/man3/al_get_display_orientation.3.*
%{_mandir}/man3/al_get_display_refresh_rate.3.*
%{_mandir}/man3/al_get_display_width.3.*
%{_mandir}/man3/al_get_errno.3.*
%{_mandir}/man3/al_get_event_source_data.3.*
%{_mandir}/man3/al_get_fallback_font.3.*
%{_mandir}/man3/al_get_file_userdata.3.*
%{_mandir}/man3/al_get_first_config_entry.3.*
%{_mandir}/man3/al_get_first_config_section.3.*
%{_mandir}/man3/al_get_font_ascent.3.*
%{_mandir}/man3/al_get_font_descent.3.*
%{_mandir}/man3/al_get_font_line_height.3.*
%{_mandir}/man3/al_get_font_ranges.3.*
%{_mandir}/man3/al_get_fs_entry_atime.3.*
%{_mandir}/man3/al_get_fs_entry_ctime.3.*
%{_mandir}/man3/al_get_fs_entry_mode.3.*
%{_mandir}/man3/al_get_fs_entry_mtime.3.*
%{_mandir}/man3/al_get_fs_entry_name.3.*
%{_mandir}/man3/al_get_fs_entry_size.3.*
%{_mandir}/man3/al_get_fs_interface.3.*
%{_mandir}/man3/al_get_glyph.3.*
%{_mandir}/man3/al_get_glyph_advance.3.*
%{_mandir}/man3/al_get_glyph_dimensions.3.*
%{_mandir}/man3/al_get_glyph_width.3.*
%{_mandir}/man3/al_get_haptic_autocenter.3.*
%{_mandir}/man3/al_get_haptic_capabilities.3.*
%{_mandir}/man3/al_get_haptic_effect_duration.3.*
%{_mandir}/man3/al_get_haptic_from_display.3.*
%{_mandir}/man3/al_get_haptic_from_joystick.3.*
%{_mandir}/man3/al_get_haptic_from_keyboard.3.*
%{_mandir}/man3/al_get_haptic_from_mouse.3.*
%{_mandir}/man3/al_get_haptic_from_touch_input.3.*
%{_mandir}/man3/al_get_haptic_gain.3.*
%{_mandir}/man3/al_get_index_buffer_size.3.*
%{_mandir}/man3/al_get_joystick.3.*
%{_mandir}/man3/al_get_joystick_active.3.*
%{_mandir}/man3/al_get_joystick_axis_name.3.*
%{_mandir}/man3/al_get_joystick_button_name.3.*
%{_mandir}/man3/al_get_joystick_event_source.3.*
%{_mandir}/man3/al_get_joystick_guid.3.*
%{_mandir}/man3/al_get_joystick_name.3.*
%{_mandir}/man3/al_get_joystick_num_axes.3.*
%{_mandir}/man3/al_get_joystick_num_buttons.3.*
%{_mandir}/man3/al_get_joystick_num_sticks.3.*
%{_mandir}/man3/al_get_joystick_state.3.*
%{_mandir}/man3/al_get_joystick_stick_flags.3.*
%{_mandir}/man3/al_get_joystick_stick_name.3.*
%{_mandir}/man3/al_get_joystick_type.3.*
%{_mandir}/man3/al_get_keyboard_event_source.3.*
%{_mandir}/man3/al_get_keyboard_state.3.*
%{_mandir}/man3/al_get_max_haptic_effects.3.*
%{_mandir}/man3/al_get_menu_item_caption.3.*
%{_mandir}/man3/al_get_menu_item_flags.3.*
%{_mandir}/man3/al_get_menu_item_icon.3.*
%{_mandir}/man3/al_get_mixer_attached.3.*
%{_mandir}/man3/al_get_mixer_channels.3.*
%{_mandir}/man3/al_get_mixer_depth.3.*
%{_mandir}/man3/al_get_mixer_frequency.3.*
%{_mandir}/man3/al_get_mixer_gain.3.*
%{_mandir}/man3/al_get_mixer_playing.3.*
%{_mandir}/man3/al_get_mixer_quality.3.*
%{_mandir}/man3/al_get_monitor_dpi.3.*
%{_mandir}/man3/al_get_monitor_info.3.*
%{_mandir}/man3/al_get_monitor_refresh_rate.3.*
%{_mandir}/man3/al_get_mouse_cursor_position.3.*
%{_mandir}/man3/al_get_mouse_emulation_mode.3.*
%{_mandir}/man3/al_get_mouse_event_source.3.*
%{_mandir}/man3/al_get_mouse_num_axes.3.*
%{_mandir}/man3/al_get_mouse_num_buttons.3.*
%{_mandir}/man3/al_get_mouse_state.3.*
%{_mandir}/man3/al_get_mouse_state_axis.3.*
%{_mandir}/man3/al_get_mouse_wheel_precision.3.*
%{_mandir}/man3/al_get_native_file_dialog_count.3.*
%{_mandir}/man3/al_get_native_file_dialog_path.3.*
%{_mandir}/man3/al_get_native_text_log_event_source.3.*
%{_mandir}/man3/al_get_new_bitmap_depth.3.*
%{_mandir}/man3/al_get_new_bitmap_flags.3.*
%{_mandir}/man3/al_get_new_bitmap_format.3.*
%{_mandir}/man3/al_get_new_bitmap_samples.3.*
%{_mandir}/man3/al_get_new_bitmap_wrap.3.*
%{_mandir}/man3/al_get_new_display_adapter.3.*
%{_mandir}/man3/al_get_new_display_flags.3.*
%{_mandir}/man3/al_get_new_display_option.3.*
%{_mandir}/man3/al_get_new_display_refresh_rate.3.*
%{_mandir}/man3/al_get_new_file_interface.3.*
%{_mandir}/man3/al_get_new_window_position.3.*
%{_mandir}/man3/al_get_new_window_title.3.*
%{_mandir}/man3/al_get_next_config_entry.3.*
%{_mandir}/man3/al_get_next_config_section.3.*
%{_mandir}/man3/al_get_next_event.3.*
%{_mandir}/man3/al_get_num_audio_output_devices.3.*
%{_mandir}/man3/al_get_num_display_modes.3.*
%{_mandir}/man3/al_get_num_joysticks.3.*
%{_mandir}/man3/al_get_num_video_adapters.3.*
%{_mandir}/man3/al_get_opengl_extension_list.3.*
%{_mandir}/man3/al_get_opengl_fbo.3.*
%{_mandir}/man3/al_get_opengl_proc_address.3.*
%{_mandir}/man3/al_get_opengl_program_object.3.*
%{_mandir}/man3/al_get_opengl_texture.3.*
%{_mandir}/man3/al_get_opengl_texture_position.3.*
%{_mandir}/man3/al_get_opengl_texture_size.3.*
%{_mandir}/man3/al_get_opengl_variant.3.*
%{_mandir}/man3/al_get_opengl_version.3.*
%{_mandir}/man3/al_get_org_name.3.*
%{_mandir}/man3/al_get_parent_bitmap.3.*
%{_mandir}/man3/al_get_path_basename.3.*
%{_mandir}/man3/al_get_path_component.3.*
%{_mandir}/man3/al_get_path_drive.3.*
%{_mandir}/man3/al_get_path_extension.3.*
%{_mandir}/man3/al_get_path_filename.3.*
%{_mandir}/man3/al_get_path_num_components.3.*
%{_mandir}/man3/al_get_path_tail.3.*
%{_mandir}/man3/al_get_pixel.3.*
%{_mandir}/man3/al_get_pixel_block_height.3.*
%{_mandir}/man3/al_get_pixel_block_size.3.*
%{_mandir}/man3/al_get_pixel_block_width.3.*
%{_mandir}/man3/al_get_pixel_format_bits.3.*
%{_mandir}/man3/al_get_pixel_size.3.*
%{_mandir}/man3/al_get_ram_size.3.*
%{_mandir}/man3/al_get_render_state.3.*
%{_mandir}/man3/al_get_sample.3.*
%{_mandir}/man3/al_get_sample_channels.3.*
%{_mandir}/man3/al_get_sample_data.3.*
%{_mandir}/man3/al_get_sample_depth.3.*
%{_mandir}/man3/al_get_sample_frequency.3.*
%{_mandir}/man3/al_get_sample_instance_attached.3.*
%{_mandir}/man3/al_get_sample_instance_channels.3.*
%{_mandir}/man3/al_get_sample_instance_depth.3.*
%{_mandir}/man3/al_get_sample_instance_frequency.3.*
%{_mandir}/man3/al_get_sample_instance_gain.3.*
%{_mandir}/man3/al_get_sample_instance_length.3.*
%{_mandir}/man3/al_get_sample_instance_pan.3.*
%{_mandir}/man3/al_get_sample_instance_playing.3.*
%{_mandir}/man3/al_get_sample_instance_playmode.3.*
%{_mandir}/man3/al_get_sample_instance_position.3.*
%{_mandir}/man3/al_get_sample_instance_speed.3.*
%{_mandir}/man3/al_get_sample_instance_time.3.*
%{_mandir}/man3/al_get_sample_length.3.*
%{_mandir}/man3/al_get_separate_bitmap_blender.3.*
%{_mandir}/man3/al_get_separate_blender.3.*
%{_mandir}/man3/al_get_shader_log.3.*
%{_mandir}/man3/al_get_shader_platform.3.*
%{_mandir}/man3/al_get_standard_path.3.*
%{_mandir}/man3/al_get_system_config.3.*
%{_mandir}/man3/al_get_system_id.3.*
%{_mandir}/man3/al_get_target_bitmap.3.*
%{_mandir}/man3/al_get_text_dimensions.3.*
%{_mandir}/man3/al_get_text_width.3.*
%{_mandir}/man3/al_get_thread_should_stop.3.*
%{_mandir}/man3/al_get_time.3.*
%{_mandir}/man3/al_get_timer_count.3.*
%{_mandir}/man3/al_get_timer_event_source.3.*
%{_mandir}/man3/al_get_timer_speed.3.*
%{_mandir}/man3/al_get_timer_started.3.*
%{_mandir}/man3/al_get_touch_input_event_source.3.*
%{_mandir}/man3/al_get_touch_input_mouse_emulation_event_source.3.*
%{_mandir}/man3/al_get_touch_input_state.3.*
%{_mandir}/man3/al_get_ustr_dimensions.3.*
%{_mandir}/man3/al_get_ustr_width.3.*
%{_mandir}/man3/al_get_vertex_buffer_size.3.*
%{_mandir}/man3/al_get_video_audio_rate.3.*
%{_mandir}/man3/al_get_video_event_source.3.*
%{_mandir}/man3/al_get_video_fps.3.*
%{_mandir}/man3/al_get_video_frame.3.*
%{_mandir}/man3/al_get_video_position.3.*
%{_mandir}/man3/al_get_video_scaled_height.3.*
%{_mandir}/man3/al_get_video_scaled_width.3.*
%{_mandir}/man3/al_get_voice_channels.3.*
%{_mandir}/man3/al_get_voice_depth.3.*
%{_mandir}/man3/al_get_voice_frequency.3.*
%{_mandir}/man3/al_get_voice_playing.3.*
%{_mandir}/man3/al_get_voice_position.3.*
%{_mandir}/man3/al_get_win_window_handle.3.*
%{_mandir}/man3/al_get_window_borders.3.*
%{_mandir}/man3/al_get_window_constraints.3.*
%{_mandir}/man3/al_get_window_position.3.*
%{_mandir}/man3/al_get_x_window_id.3.*
%{_mandir}/man3/al_grab_font_from_bitmap.3.*
%{_mandir}/man3/al_grab_mouse.3.*
%{_mandir}/man3/al_have_d3d_non_pow2_texture_support.3.*
%{_mandir}/man3/al_have_d3d_non_square_texture_support.3.*
%{_mandir}/man3/al_have_opengl_extension.3.*
%{_mandir}/man3/al_hide_mouse_cursor.3.*
%{_mandir}/man3/al_hold_bitmap_drawing.3.*
%{_mandir}/man3/al_horizontal_shear_transform.3.*
%{_mandir}/man3/al_identify_bitmap.3.*
%{_mandir}/man3/al_identify_bitmap_f.3.*
%{_mandir}/man3/al_identify_sample.3.*
%{_mandir}/man3/al_identify_sample_f.3.*
%{_mandir}/man3/al_identify_video.3.*
%{_mandir}/man3/al_identify_video_f.3.*
%{_mandir}/man3/al_identity_transform.3.*
%{_mandir}/man3/al_inhibit_screensaver.3.*
%{_mandir}/man3/al_init.3.*
%{_mandir}/man3/al_init_acodec_addon.3.*
%{_mandir}/man3/al_init_font_addon.3.*
%{_mandir}/man3/al_init_image_addon.3.*
%{_mandir}/man3/al_init_native_dialog_addon.3.*
%{_mandir}/man3/al_init_primitives_addon.3.*
%{_mandir}/man3/al_init_timeout.3.*
%{_mandir}/man3/al_init_ttf_addon.3.*
%{_mandir}/man3/al_init_user_event_source.3.*
%{_mandir}/man3/al_init_video_addon.3.*
%{_mandir}/man3/al_insert_menu_item.3.*
%{_mandir}/man3/al_insert_path_component.3.*
%{_mandir}/man3/al_install_audio.3.*
%{_mandir}/man3/al_install_haptic.3.*
%{_mandir}/man3/al_install_joystick.3.*
%{_mandir}/man3/al_install_keyboard.3.*
%{_mandir}/man3/al_install_mouse.3.*
%{_mandir}/man3/al_install_system.3.*
%{_mandir}/man3/al_install_touch_input.3.*
%{_mandir}/man3/al_invert_transform.3.*
%{_mandir}/man3/al_iphone_get_view.3.*
%{_mandir}/man3/al_iphone_get_window.3.*
%{_mandir}/man3/al_iphone_set_statusbar_orientation.3.*
%{_mandir}/man3/al_is_acodec_addon_initialized.3.*
%{_mandir}/man3/al_is_audio_installed.3.*
%{_mandir}/man3/al_is_audio_recorder_recording.3.*
%{_mandir}/man3/al_is_bitmap_drawing_held.3.*
%{_mandir}/man3/al_is_bitmap_locked.3.*
%{_mandir}/man3/al_is_color_valid.3.*
%{_mandir}/man3/al_is_compatible_bitmap.3.*
%{_mandir}/man3/al_is_d3d_device_lost.3.*
%{_mandir}/man3/al_is_display_haptic.3.*
%{_mandir}/man3/al_is_event_queue_empty.3.*
%{_mandir}/man3/al_is_event_queue_paused.3.*
%{_mandir}/man3/al_is_event_source_registered.3.*
%{_mandir}/man3/al_is_font_addon_initialized.3.*
%{_mandir}/man3/al_is_haptic_active.3.*
%{_mandir}/man3/al_is_haptic_capable.3.*
%{_mandir}/man3/al_is_haptic_effect_ok.3.*
%{_mandir}/man3/al_is_haptic_effect_playing.3.*
%{_mandir}/man3/al_is_haptic_installed.3.*
%{_mandir}/man3/al_is_image_addon_initialized.3.*
%{_mandir}/man3/al_is_joystick_haptic.3.*
%{_mandir}/man3/al_is_joystick_installed.3.*
%{_mandir}/man3/al_is_keyboard_haptic.3.*
%{_mandir}/man3/al_is_keyboard_installed.3.*
%{_mandir}/man3/al_is_mouse_haptic.3.*
%{_mandir}/man3/al_is_mouse_installed.3.*
%{_mandir}/man3/al_is_native_dialog_addon_initialized.3.*
%{_mandir}/man3/al_is_primitives_addon_initialized.3.*
%{_mandir}/man3/al_is_sub_bitmap.3.*
%{_mandir}/man3/al_is_system_installed.3.*
%{_mandir}/man3/al_is_touch_input_haptic.3.*
%{_mandir}/man3/al_is_touch_input_installed.3.*
%{_mandir}/man3/al_is_ttf_addon_initialized.3.*
%{_mandir}/man3/al_is_video_addon_initialized.3.*
%{_mandir}/man3/al_is_video_playing.3.*
%{_mandir}/man3/al_itofix.3.*
%{_mandir}/man3/al_join_paths.3.*
%{_mandir}/man3/al_join_thread.3.*
%{_mandir}/man3/al_key_down.3.*
%{_mandir}/man3/al_keycode_to_name.3.*
%{_mandir}/man3/al_load_audio_stream.3.*
%{_mandir}/man3/al_load_audio_stream_f.3.*
%{_mandir}/man3/al_load_bitmap.3.*
%{_mandir}/man3/al_load_bitmap_f.3.*
%{_mandir}/man3/al_load_bitmap_flags.3.*
%{_mandir}/man3/al_load_bitmap_flags_f.3.*
%{_mandir}/man3/al_load_bitmap_font.3.*
%{_mandir}/man3/al_load_bitmap_font_flags.3.*
%{_mandir}/man3/al_load_config_file.3.*
%{_mandir}/man3/al_load_config_file_f.3.*
%{_mandir}/man3/al_load_font.3.*
%{_mandir}/man3/al_load_sample.3.*
%{_mandir}/man3/al_load_sample_f.3.*
%{_mandir}/man3/al_load_ttf_font.3.*
%{_mandir}/man3/al_load_ttf_font_f.3.*
%{_mandir}/man3/al_load_ttf_font_stretch.3.*
%{_mandir}/man3/al_load_ttf_font_stretch_f.3.*
%{_mandir}/man3/al_lock_bitmap.3.*
%{_mandir}/man3/al_lock_bitmap_blocked.3.*
%{_mandir}/man3/al_lock_bitmap_region.3.*
%{_mandir}/man3/al_lock_bitmap_region_blocked.3.*
%{_mandir}/man3/al_lock_index_buffer.3.*
%{_mandir}/man3/al_lock_mutex.3.*
%{_mandir}/man3/al_lock_sample_id.3.*
%{_mandir}/man3/al_lock_vertex_buffer.3.*
%{_mandir}/man3/al_make_directory.3.*
%{_mandir}/man3/al_make_path_canonical.3.*
%{_mandir}/man3/al_make_temp_file.3.*
%{_mandir}/man3/al_malloc.3.*
%{_mandir}/man3/al_malloc_with_context.3.*
%{_mandir}/man3/al_map_rgb.3.*
%{_mandir}/man3/al_map_rgb_f.3.*
%{_mandir}/man3/al_map_rgba.3.*
%{_mandir}/man3/al_map_rgba_f.3.*
%{_mandir}/man3/al_merge_config.3.*
%{_mandir}/man3/al_merge_config_into.3.*
%{_mandir}/man3/al_mixer_has_attachments.3.*
%{_mandir}/man3/al_mouse_button_down.3.*
%{_mandir}/man3/al_open_directory.3.*
%{_mandir}/man3/al_open_fs_entry.3.*
%{_mandir}/man3/al_open_memfile.3.*
%{_mandir}/man3/al_open_native_text_log.3.*
%{_mandir}/man3/al_open_video.3.*
%{_mandir}/man3/al_open_video_f.3.*
%{_mandir}/man3/al_orthographic_transform.3.*
%{_mandir}/man3/al_osx_get_window.3.*
%{_mandir}/man3/al_path_cstr.3.*
%{_mandir}/man3/al_path_ustr.3.*
%{_mandir}/man3/al_pause_event_queue.3.*
%{_mandir}/man3/al_peek_next_event.3.*
%{_mandir}/man3/al_perspective_transform.3.*
%{_mandir}/man3/al_play_audio_stream.3.*
%{_mandir}/man3/al_play_audio_stream_f.3.*
%{_mandir}/man3/al_play_haptic_effect.3.*
%{_mandir}/man3/al_play_sample.3.*
%{_mandir}/man3/al_play_sample_instance.3.*
%{_mandir}/man3/al_popup_menu.3.*
%{_mandir}/man3/al_premul_rgba.3.*
%{_mandir}/man3/al_premul_rgba_f.3.*
%{_mandir}/man3/al_put_blended_pixel.3.*
%{_mandir}/man3/al_put_pixel.3.*
%{_mandir}/man3/al_radtofix_r.3.*
%{_mandir}/man3/al_read_directory.3.*
%{_mandir}/man3/al_realloc.3.*
%{_mandir}/man3/al_realloc_with_context.3.*
%{_mandir}/man3/al_rebase_path.3.*
%{_mandir}/man3/al_reconfigure_joysticks.3.*
%{_mandir}/man3/al_ref_buffer.3.*
%{_mandir}/man3/al_ref_cstr.3.*
%{_mandir}/man3/al_ref_info.3.*
%{_mandir}/man3/al_ref_ustr.3.*
%{_mandir}/man3/al_register_assert_handler.3.*
%{_mandir}/man3/al_register_audio_stream_loader.3.*
%{_mandir}/man3/al_register_audio_stream_loader_f.3.*
%{_mandir}/man3/al_register_bitmap_identifier.3.*
%{_mandir}/man3/al_register_bitmap_loader.3.*
%{_mandir}/man3/al_register_bitmap_loader_f.3.*
%{_mandir}/man3/al_register_bitmap_saver.3.*
%{_mandir}/man3/al_register_bitmap_saver_f.3.*
%{_mandir}/man3/al_register_event_source.3.*
%{_mandir}/man3/al_register_font_loader.3.*
%{_mandir}/man3/al_register_sample_identifier.3.*
%{_mandir}/man3/al_register_sample_loader.3.*
%{_mandir}/man3/al_register_sample_loader_f.3.*
%{_mandir}/man3/al_register_sample_saver.3.*
%{_mandir}/man3/al_register_sample_saver_f.3.*
%{_mandir}/man3/al_register_trace_handler.3.*
%{_mandir}/man3/al_release_haptic.3.*
%{_mandir}/man3/al_release_haptic_effect.3.*
%{_mandir}/man3/al_release_joystick.3.*
%{_mandir}/man3/al_remove_config_key.3.*
%{_mandir}/man3/al_remove_config_section.3.*
%{_mandir}/man3/al_remove_display_menu.3.*
%{_mandir}/man3/al_remove_filename.3.*
%{_mandir}/man3/al_remove_fs_entry.3.*
%{_mandir}/man3/al_remove_menu_item.3.*
%{_mandir}/man3/al_remove_opengl_fbo.3.*
%{_mandir}/man3/al_remove_path_component.3.*
%{_mandir}/man3/al_reparent_bitmap.3.*
%{_mandir}/man3/al_replace_path_component.3.*
%{_mandir}/man3/al_reserve_samples.3.*
%{_mandir}/man3/al_reset_bitmap_blender.3.*
%{_mandir}/man3/al_reset_clipping_rectangle.3.*
%{_mandir}/man3/al_reset_new_display_options.3.*
%{_mandir}/man3/al_resize_display.3.*
%{_mandir}/man3/al_rest.3.*
%{_mandir}/man3/al_restore_default_mixer.3.*
%{_mandir}/man3/al_restore_state.3.*
%{_mandir}/man3/al_resume_timer.3.*
%{_mandir}/man3/al_rewind_audio_stream.3.*
%{_mandir}/man3/al_rotate_transform.3.*
%{_mandir}/man3/al_rotate_transform_3d.3.*
%{_mandir}/man3/al_rumble_haptic.3.*
%{_mandir}/man3/al_run_detached_thread.3.*
%{_mandir}/man3/al_run_main.3.*
%{_mandir}/man3/al_save_bitmap.3.*
%{_mandir}/man3/al_save_bitmap_f.3.*
%{_mandir}/man3/al_save_config_file.3.*
%{_mandir}/man3/al_save_config_file_f.3.*
%{_mandir}/man3/al_save_sample.3.*
%{_mandir}/man3/al_save_sample_f.3.*
%{_mandir}/man3/al_scale_transform.3.*
%{_mandir}/man3/al_scale_transform_3d.3.*
%{_mandir}/man3/al_seek_audio_stream_secs.3.*
%{_mandir}/man3/al_seek_video.3.*
%{_mandir}/man3/al_set_app_name.3.*
%{_mandir}/man3/al_set_audio_stream_channel_matrix.3.*
%{_mandir}/man3/al_set_audio_stream_fragment.3.*
%{_mandir}/man3/al_set_audio_stream_gain.3.*
%{_mandir}/man3/al_set_audio_stream_loop_secs.3.*
%{_mandir}/man3/al_set_audio_stream_pan.3.*
%{_mandir}/man3/al_set_audio_stream_playing.3.*
%{_mandir}/man3/al_set_audio_stream_playmode.3.*
%{_mandir}/man3/al_set_audio_stream_speed.3.*
%{_mandir}/man3/al_set_bitmap_blend_color.3.*
%{_mandir}/man3/al_set_bitmap_blender.3.*
%{_mandir}/man3/al_set_blend_color.3.*
%{_mandir}/man3/al_set_blender.3.*
%{_mandir}/man3/al_set_clipboard_text.3.*
%{_mandir}/man3/al_set_clipping_rectangle.3.*
%{_mandir}/man3/al_set_config_value.3.*
%{_mandir}/man3/al_set_current_opengl_context.3.*
%{_mandir}/man3/al_set_d3d_device_release_callback.3.*
%{_mandir}/man3/al_set_d3d_device_restore_callback.3.*
%{_mandir}/man3/al_set_default_mixer.3.*
%{_mandir}/man3/al_set_default_voice.3.*
%{_mandir}/man3/al_set_display_flag.3.*
%{_mandir}/man3/al_set_display_icon.3.*
%{_mandir}/man3/al_set_display_icons.3.*
%{_mandir}/man3/al_set_display_menu.3.*
%{_mandir}/man3/al_set_display_option.3.*
%{_mandir}/man3/al_set_errno.3.*
%{_mandir}/man3/al_set_event_source_data.3.*
%{_mandir}/man3/al_set_exe_name.3.*
%{_mandir}/man3/al_set_fallback_font.3.*
%{_mandir}/man3/al_set_fs_interface.3.*
%{_mandir}/man3/al_set_haptic_autocenter.3.*
%{_mandir}/man3/al_set_haptic_gain.3.*
%{_mandir}/man3/al_set_joystick_mappings.3.*
%{_mandir}/man3/al_set_joystick_mappings_f.3.*
%{_mandir}/man3/al_set_keyboard_leds.3.*
%{_mandir}/man3/al_set_memory_interface.3.*
%{_mandir}/man3/al_set_menu_item_caption.3.*
%{_mandir}/man3/al_set_menu_item_flags.3.*
%{_mandir}/man3/al_set_menu_item_icon.3.*
%{_mandir}/man3/al_set_mixer_frequency.3.*
%{_mandir}/man3/al_set_mixer_gain.3.*
%{_mandir}/man3/al_set_mixer_playing.3.*
%{_mandir}/man3/al_set_mixer_postprocess_callback.3.*
%{_mandir}/man3/al_set_mixer_quality.3.*
%{_mandir}/man3/al_set_mouse_axis.3.*
%{_mandir}/man3/al_set_mouse_cursor.3.*
%{_mandir}/man3/al_set_mouse_emulation_mode.3.*
%{_mandir}/man3/al_set_mouse_w.3.*
%{_mandir}/man3/al_set_mouse_wheel_precision.3.*
%{_mandir}/man3/al_set_mouse_xy.3.*
%{_mandir}/man3/al_set_mouse_z.3.*
%{_mandir}/man3/al_set_new_bitmap_depth.3.*
%{_mandir}/man3/al_set_new_bitmap_flags.3.*
%{_mandir}/man3/al_set_new_bitmap_format.3.*
%{_mandir}/man3/al_set_new_bitmap_samples.3.*
%{_mandir}/man3/al_set_new_bitmap_wrap.3.*
%{_mandir}/man3/al_set_new_display_adapter.3.*
%{_mandir}/man3/al_set_new_display_flags.3.*
%{_mandir}/man3/al_set_new_display_option.3.*
%{_mandir}/man3/al_set_new_display_refresh_rate.3.*
%{_mandir}/man3/al_set_new_file_interface.3.*
%{_mandir}/man3/al_set_new_window_position.3.*
%{_mandir}/man3/al_set_new_window_title.3.*
%{_mandir}/man3/al_set_org_name.3.*
%{_mandir}/man3/al_set_path_drive.3.*
%{_mandir}/man3/al_set_path_extension.3.*
%{_mandir}/man3/al_set_path_filename.3.*
%{_mandir}/man3/al_set_physfs_file_interface.3.*
%{_mandir}/man3/al_set_render_state.3.*
%{_mandir}/man3/al_set_sample.3.*
%{_mandir}/man3/al_set_sample_instance_channel_matrix.3.*
%{_mandir}/man3/al_set_sample_instance_gain.3.*
%{_mandir}/man3/al_set_sample_instance_length.3.*
%{_mandir}/man3/al_set_sample_instance_pan.3.*
%{_mandir}/man3/al_set_sample_instance_playing.3.*
%{_mandir}/man3/al_set_sample_instance_playmode.3.*
%{_mandir}/man3/al_set_sample_instance_position.3.*
%{_mandir}/man3/al_set_sample_instance_speed.3.*
%{_mandir}/man3/al_set_separate_bitmap_blender.3.*
%{_mandir}/man3/al_set_separate_blender.3.*
%{_mandir}/man3/al_set_shader_bool.3.*
%{_mandir}/man3/al_set_shader_float.3.*
%{_mandir}/man3/al_set_shader_float_vector.3.*
%{_mandir}/man3/al_set_shader_int.3.*
%{_mandir}/man3/al_set_shader_int_vector.3.*
%{_mandir}/man3/al_set_shader_matrix.3.*
%{_mandir}/man3/al_set_shader_sampler.3.*
%{_mandir}/man3/al_set_standard_file_interface.3.*
%{_mandir}/man3/al_set_standard_fs_interface.3.*
%{_mandir}/man3/al_set_system_mouse_cursor.3.*
%{_mandir}/man3/al_set_target_backbuffer.3.*
%{_mandir}/man3/al_set_target_bitmap.3.*
%{_mandir}/man3/al_set_thread_should_stop.3.*
%{_mandir}/man3/al_set_timer_count.3.*
%{_mandir}/man3/al_set_timer_speed.3.*
%{_mandir}/man3/al_set_video_playing.3.*
%{_mandir}/man3/al_set_voice_playing.3.*
%{_mandir}/man3/al_set_voice_position.3.*
%{_mandir}/man3/al_set_window_constraints.3.*
%{_mandir}/man3/al_set_window_position.3.*
%{_mandir}/man3/al_set_window_title.3.*
%{_mandir}/man3/al_show_mouse_cursor.3.*
%{_mandir}/man3/al_show_native_file_dialog.3.*
%{_mandir}/man3/al_show_native_message_box.3.*
%{_mandir}/man3/al_shutdown_font_addon.3.*
%{_mandir}/man3/al_shutdown_image_addon.3.*
%{_mandir}/man3/al_shutdown_native_dialog_addon.3.*
%{_mandir}/man3/al_shutdown_primitives_addon.3.*
%{_mandir}/man3/al_shutdown_ttf_addon.3.*
%{_mandir}/man3/al_shutdown_video_addon.3.*
%{_mandir}/man3/al_signal_cond.3.*
%{_mandir}/man3/al_start_audio_recorder.3.*
%{_mandir}/man3/al_start_thread.3.*
%{_mandir}/man3/al_start_timer.3.*
%{_mandir}/man3/al_start_video.3.*
%{_mandir}/man3/al_start_video_with_voice.3.*
%{_mandir}/man3/al_stop_audio_recorder.3.*
%{_mandir}/man3/al_stop_haptic_effect.3.*
%{_mandir}/man3/al_stop_sample.3.*
%{_mandir}/man3/al_stop_sample_instance.3.*
%{_mandir}/man3/al_stop_samples.3.*
%{_mandir}/man3/al_stop_timer.3.*
%{_mandir}/man3/al_store_state.3.*
%{_mandir}/man3/al_toggle_menu_item_flags.3.*
%{_mandir}/man3/al_transform_coordinates.3.*
%{_mandir}/man3/al_transform_coordinates_3d.3.*
%{_mandir}/man3/al_transform_coordinates_3d_projective.3.*
%{_mandir}/man3/al_transform_coordinates_4d.3.*
%{_mandir}/man3/al_translate_transform.3.*
%{_mandir}/man3/al_translate_transform_3d.3.*
%{_mandir}/man3/al_transpose_transform.3.*
%{_mandir}/man3/al_triangulate_polygon.3.*
%{_mandir}/man3/al_ungrab_mouse.3.*
%{_mandir}/man3/al_uninstall_audio.3.*
%{_mandir}/man3/al_uninstall_haptic.3.*
%{_mandir}/man3/al_uninstall_joystick.3.*
%{_mandir}/man3/al_uninstall_keyboard.3.*
%{_mandir}/man3/al_uninstall_mouse.3.*
%{_mandir}/man3/al_uninstall_system.3.*
%{_mandir}/man3/al_uninstall_touch_input.3.*
%{_mandir}/man3/al_unlock_bitmap.3.*
%{_mandir}/man3/al_unlock_index_buffer.3.*
%{_mandir}/man3/al_unlock_mutex.3.*
%{_mandir}/man3/al_unlock_sample_id.3.*
%{_mandir}/man3/al_unlock_vertex_buffer.3.*
%{_mandir}/man3/al_unmap_rgb.3.*
%{_mandir}/man3/al_unmap_rgb_f.3.*
%{_mandir}/man3/al_unmap_rgba.3.*
%{_mandir}/man3/al_unmap_rgba_f.3.*
%{_mandir}/man3/al_unref_user_event.3.*
%{_mandir}/man3/al_unregister_event_source.3.*
%{_mandir}/man3/al_update_display_region.3.*
%{_mandir}/man3/al_update_fs_entry.3.*
%{_mandir}/man3/al_upload_and_play_haptic_effect.3.*
%{_mandir}/man3/al_upload_haptic_effect.3.*
%{_mandir}/man3/al_use_projection_transform.3.*
%{_mandir}/man3/al_use_shader.3.*
%{_mandir}/man3/al_use_transform.3.*
%{_mandir}/man3/al_ustr_append.3.*
%{_mandir}/man3/al_ustr_append_chr.3.*
%{_mandir}/man3/al_ustr_append_cstr.3.*
%{_mandir}/man3/al_ustr_appendf.3.*
%{_mandir}/man3/al_ustr_assign.3.*
%{_mandir}/man3/al_ustr_assign_cstr.3.*
%{_mandir}/man3/al_ustr_assign_substr.3.*
%{_mandir}/man3/al_ustr_compare.3.*
%{_mandir}/man3/al_ustr_dup.3.*
%{_mandir}/man3/al_ustr_dup_substr.3.*
%{_mandir}/man3/al_ustr_empty_string.3.*
%{_mandir}/man3/al_ustr_encode_utf16.3.*
%{_mandir}/man3/al_ustr_equal.3.*
%{_mandir}/man3/al_ustr_find_chr.3.*
%{_mandir}/man3/al_ustr_find_cset.3.*
%{_mandir}/man3/al_ustr_find_cset_cstr.3.*
%{_mandir}/man3/al_ustr_find_cstr.3.*
%{_mandir}/man3/al_ustr_find_replace.3.*
%{_mandir}/man3/al_ustr_find_replace_cstr.3.*
%{_mandir}/man3/al_ustr_find_set.3.*
%{_mandir}/man3/al_ustr_find_set_cstr.3.*
%{_mandir}/man3/al_ustr_find_str.3.*
%{_mandir}/man3/al_ustr_free.3.*
%{_mandir}/man3/al_ustr_get.3.*
%{_mandir}/man3/al_ustr_get_next.3.*
%{_mandir}/man3/al_ustr_has_prefix.3.*
%{_mandir}/man3/al_ustr_has_prefix_cstr.3.*
%{_mandir}/man3/al_ustr_has_suffix.3.*
%{_mandir}/man3/al_ustr_has_suffix_cstr.3.*
%{_mandir}/man3/al_ustr_insert.3.*
%{_mandir}/man3/al_ustr_insert_chr.3.*
%{_mandir}/man3/al_ustr_insert_cstr.3.*
%{_mandir}/man3/al_ustr_length.3.*
%{_mandir}/man3/al_ustr_ltrim_ws.3.*
%{_mandir}/man3/al_ustr_ncompare.3.*
%{_mandir}/man3/al_ustr_new.3.*
%{_mandir}/man3/al_ustr_new_from_buffer.3.*
%{_mandir}/man3/al_ustr_new_from_utf16.3.*
%{_mandir}/man3/al_ustr_newf.3.*
%{_mandir}/man3/al_ustr_next.3.*
%{_mandir}/man3/al_ustr_offset.3.*
%{_mandir}/man3/al_ustr_prev.3.*
%{_mandir}/man3/al_ustr_prev_get.3.*
%{_mandir}/man3/al_ustr_remove_chr.3.*
%{_mandir}/man3/al_ustr_remove_range.3.*
%{_mandir}/man3/al_ustr_replace_range.3.*
%{_mandir}/man3/al_ustr_rfind_chr.3.*
%{_mandir}/man3/al_ustr_rfind_cstr.3.*
%{_mandir}/man3/al_ustr_rfind_str.3.*
%{_mandir}/man3/al_ustr_rtrim_ws.3.*
%{_mandir}/man3/al_ustr_set_chr.3.*
%{_mandir}/man3/al_ustr_size.3.*
%{_mandir}/man3/al_ustr_size_utf16.3.*
%{_mandir}/man3/al_ustr_to_buffer.3.*
%{_mandir}/man3/al_ustr_trim_ws.3.*
%{_mandir}/man3/al_ustr_truncate.3.*
%{_mandir}/man3/al_ustr_vappendf.3.*
%{_mandir}/man3/al_utf16_encode.3.*
%{_mandir}/man3/al_utf16_width.3.*
%{_mandir}/man3/al_utf8_encode.3.*
%{_mandir}/man3/al_utf8_width.3.*
%{_mandir}/man3/al_vertical_shear_transform.3.*
%{_mandir}/man3/al_vfprintf.3.*
%{_mandir}/man3/al_voice_has_attachments.3.*
%{_mandir}/man3/al_wait_cond.3.*
%{_mandir}/man3/al_wait_cond_until.3.*
%{_mandir}/man3/al_wait_for_event.3.*
%{_mandir}/man3/al_wait_for_event_timed.3.*
%{_mandir}/man3/al_wait_for_event_until.3.*
%{_mandir}/man3/al_wait_for_vsync.3.*
%{_mandir}/man3/al_win_add_window_callback.3.*
%{_mandir}/man3/al_win_remove_window_callback.3.*
%{_mandir}/man3/al_x_set_initial_icon.3.*
%files tools
%{_pkgdocdir}/dat*.txt
%{_pkgdocdir}/grabber.txt
%{_bindir}/colormap
%{_bindir}/dat
%{_bindir}/dat2s
%{_bindir}/dat2c
%{_bindir}/exedat
%{_bindir}/grabber
%{_bindir}/pack
%{_bindir}/pat2dat
%{_bindir}/rgbmap
%{_bindir}/textconv
%{_bindir}/xfixicon.sh

%files jack-plugin
%{_libdir}/allegro/4.4.3/alleg-jack.so

%files -n alleggl
%license addons/allegrogl/gpl.txt
%license addons/allegrogl/zlib.txt
%{_libdir}/liballeggl.so.4*

%files -n alleggl-devel
%{_pkgdocdir}/allegrogl/
%{_libdir}/liballeggl.so
%{_includedir}/alleggl.h
%{_includedir}/allegrogl

%files -n jpgalleg
%license addons/jpgalleg/license.txt
%{_libdir}/libjpgalleg.so.4*

%files -n jpgalleg-devel
%{_pkgdocdir}/jpgalleg/
%{_libdir}/libjpgalleg.so
%{_includedir}/jpgalleg.h

%files loadpng
%license addons/loadpng/LICENSE.txt
%{_pkgdocdir}/loadpng/
%{_libdir}/libloadpng.so.4*

%files loadpng-devel
%{_libdir}/libloadpng.so
%{_includedir}/loadpng.h

%files logg
%license addons/logg/LICENSE.txt
%{_libdir}/liblogg.so.4*

%files logg-devel
%{_libdir}/liblogg.so
%{_includedir}/logg.h


%changelog
%autochangelog