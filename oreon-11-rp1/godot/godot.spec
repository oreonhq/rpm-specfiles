%global source1_hash d256cb4868bbf6ec147e782cda861d8bab72cd80487bb3eeb76ac234bf55a650
%global source0_hash a18ce0ccec3ecc40b0dd6c4f5132ca934e9fb7c2979717940ff32aee1eb35481
%define status  stable
%define uversion %{version}-%{status}
%define rdnsname org.godotengine.Godot
Name:           godot
Version:        4.7.2
Release:        1%{?dist}
Summary:        Multi-platform 2D and 3D game engine with a feature-rich editor
%if 0%{?mageia}
Group:          Development/Tools
%endif
License:        MIT AND AML-glslang AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND BSL-1.0 AND CC0-1.0 AND CC-BY-4.0 AND MPL-2.0 AND OFL-1.1 AND Unlicense AND X11 AND Zlib
URL:            https://godotengine.org
Source0:        https://github.com/%{name}engine/%{name}-builds/releases/download/%{uversion}/%{name}-%{uversion}.tar.xz
Source1:        https://github.com/godotengine/godot-builds/releases/download/%{uversion}/%{name}-%{uversion}.tar.xz.sha256
Patch0:         preconfigure-blender-oidn-paths.patch
ExcludeArch:    s390x
%ifarch aarch64 x86_64
%endif
%if 0%{?mageia}
%else
%endif
%define system_glslang 0
%define system_recastnavigation 0%{?mageia}
%if %{system_glslang}
%endif
%if %{system_recastnavigation}
%endif
%if 0%{?mageia}
%else
%endif
Requires:       hicolor-icon-theme
Recommends:     blender
Recommends:     oidn
Provides:       bundled(enet) = 1.3.18
%if ! %{system_glslang}
Provides:       bundled(glslang) = 14.2.0
%endif
Provides:       bundled(minizip) = 1.3.1.2
%if ! %{system_recastnavigation}
Provides:       bundled(recastnavigation) = 1.6.0
%endif
Obsoletes:      godot-headless < 4.0-1
Provides:       godot-headless == %{version}-%{release}
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  libsquish-devel
BuildRequires:  mbedtls-devel
BuildRequires:  miniupnpc-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(graphite2)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(harfbuzz-icu)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libbrotlicommon)
BuildRequires:  pkgconfig(libbrotlidec)
BuildRequires:  pkgconfig(libdecor-0)
BuildRequires:  pkgconfig(libpcre2-32)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libturbojpeg)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libwslay)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(openxr)
BuildRequires:  pkgconfig(sdl3)
BuildRequires:  pkgconfig(speech-dispatcher)
BuildRequires:  pkgconfig(theora)
BuildRequires:  pkgconfig(theoradec)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vorbisfile)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3-scons
# /oreon:deps
%description
Godot is an advanced, feature-packed, multi-platform 2D and 3D game engine.
It provides a huge set of common tools, so you can just focus on making
your game without reinventing the wheel.

Godot is completely free and open source under the very permissive MIT
license. No strings attached, no royalties, nothing. Your game is yours,
down to the last line of engine code.

To use the editor on the command line in a non-graphical environment (e.g. to
export games from the source code), use the --headless flag.

%package        runner
Summary:        Shared binary to play games and run servers developed with the Godot engine
%if 0%{?mageia}
Group:          Games/Other
%endif
Obsoletes:      godot-server < 4.0-1
Provides:       godot-server == %{version}-%{release}
%description    runner
This package contains a godot-runner binary for the Linux X11 platform,
which can be used to run any game developed with the Godot engine simply
by pointing to the location of the game's data package.

To run the game as a dedicated server, use the --headless flag.

%prep

%autosetup -p1 -n %{name}-%{uversion}

%build

to_unbundle="brotli embree freetype graphite harfbuzz icu4c libjpeg_turbo libogg libpng libtheora libvorbis libwebp mbedtls miniupnpc openxr pcre2 sdl wslay zlib zstd"
%if %{system_glslang}
to_unbundle+=" glslang"
%endif
%if %{system_recastnavigation}
to_unbundle+=" recastnavigation"
%endif
system_libs="use_sowrap=no "
rm -rf thirdparty/linuxbsd_headers
for lib in $to_unbundle; do
    system_libs+="builtin_"$lib"=no "
    rm -rf thirdparty/$lib
done
%define _scons scons %{?_smp_mflags} "CCFLAGS=%{?build_cflags}" "LINKFLAGS=%{?build_ldflags}" arch=%{godot_arch} $system_libs lto=full use_static_cpp=no debug_symbols=yes progress=no
%if 0%{?mageia}
export BUILD_NAME="mageia"
%endif
%_scons p=linuxbsd target=editor
%_scons p=linuxbsd target=template_release
%install
install -d %{buildroot}%{_bindir}
install -m755 bin/%{name}.linuxbsd.editor.%{godot_arch} %{buildroot}%{_bindir}/%{name}
install -m755 bin/%{name}.linuxbsd.template_release.%{godot_arch} %{buildroot}%{_bindir}/%{name}-runner
install -D -m644 icon.svg \
    %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
install -D -m644 misc/dist/linux/%{rdnsname}.desktop \
    %{buildroot}%{_datadir}/applications/%{rdnsname}.desktop
install -D -m644 misc/dist/linux/%{rdnsname}.appdata.xml \
    %{buildroot}%{_datadir}/metainfo/%{rdnsname}.appdata.xml
install -D -m644 misc/dist/linux/%{rdnsname}.xml \
    %{buildroot}%{_datadir}/mime/packages/%{rdnsname}.xml
install -D -m644 misc/dist/linux/%{name}.6 \
    %{buildroot}%{_mandir}/man6/%{name}.6
install -D -m644 misc/dist/shell/%{name}.bash-completion \
    %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -D -m644 misc/dist/shell/%{name}.fish \
    %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish
install -D -m644 misc/dist/shell/_%{name}.zsh-completion \
    %{buildroot}%{_datadir}/zsh/site-functions/_%{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{rdnsname}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{rdnsname}.appdata.xml
%files -f %{oreon_filedir}/main.list
%files -n godot-runner -f %{oreon_filedir}/godot-runner.list

%changelog

%autochangelog
