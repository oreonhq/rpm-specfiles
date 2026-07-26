%global source0_hash none

%if 0%{?fedora}
# With _package_note_file enabled, godot.x11.opt.tools fails to link with:
# g++: fatal error: environment variable 'RPM_ARCH' not defined
%undefine _package_note_file
%ifarch %{arm32}
%global _lto_cflags %nil
%endif
%endif

%define status  stable
%define uversion %{version}-%{status}

%define rdnsname org.godotengine.Godot

Name:           godot
Version:        4.6.1
Release:        1%{?dist}
Summary:        Multi-platform 2D and 3D game engine with a feature-rich editor
%if 0%{?mageia}
Group:          Development/Tools
%endif
# Godot itself is MIT-licensed, the rest is from vendored thirdparty libraries
License:        MIT AND AML-glslang AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND BSL-1.0 AND CC0-1.0 AND CC-BY-4.0 AND MPL-2.0 AND OFL-1.1 AND Unlicense AND X11 AND Zlib
URL:            https://godotengine.org
Source0:        https://github.com/godotengine/godot-builds/releases/download/%{uversion}/%{name}-%{uversion}.tar.xz
Source1:        https://github.com/godotengine/godot-builds/releases/download/%{uversion}/%{name}-%{uversion}.tar.xz.sha256

# Preconfigure Blender and oidnDenoise paths to use system-installed versions.
Patch0:         preconfigure-blender-oidn-paths.patch

# Upstream does not support this arch (for now)
ExcludeArch:    s390x

BuildRequires:  gcc-c++
BuildRequires:  libsquish-devel
BuildRequires:  mbedtls-devel
BuildRequires:  miniupnpc-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(harfbuzz-icu)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(graphite2)
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

%ifarch aarch64 x86_64
BuildRequires:  embree-devel >= 4
%endif

%if 0%{?mageia}
BuildRequires:  scons
%else
BuildRequires:  python3-scons
%endif

# See bundled section for explanations.
%define system_glslang 0
%define system_recastnavigation 0%{?mageia}

%if %{system_glslang}
BuildRequires:  glslang-devel
%endif

%if %{system_recastnavigation}
BuildRequires:  recastnavigation-devel
%endif

# For desktop and appdata files validation
BuildRequires:  desktop-file-utils
%if 0%{?mageia}
BuildRequires:  appstream-util
%else
BuildRequires:  libappstream-glib
%endif

# Ensure the hicolor icon theme dirs exist
Requires:       hicolor-icon-theme

# To support importing .blend files
Recommends:     blender
# For better denoising of lightmaps, using oidnDenoise
Recommends:     oidn

# Bundled libraries: many of the libraries code in `thirdparty` can be
# unbundled when the libraries are provided by the system. Keep in mind
# though that the `thirdparty` folder also contains code which is typically
# not packaged in distros, and is probably best left bundled.

# Has some modifications for IPv6 support, upstream enet is unresponsive.
# Should not be unbundled.
# Cf: https://github.com/godotengine/godot/issues/6992
Provides:       bundled(enet) = 1.3.18
%if ! %{system_glslang}
# Fedora package only provides static libs, needs more work to be usable.
Provides:       bundled(glslang) = 14.2.0
%endif
# Has custom changes to support seeking in zip archives.
# Should not be unbundled.
Provides:       bundled(minizip) = 1.3.1.2
%if ! %{system_recastnavigation}
# Could be unbundled if packaged.
Provides:       bundled(recastnavigation) = 1.6.0
%endif

Obsoletes:      godot-headless < 4.0-1
Provides:       godot-headless == %{version}-%{release}

%description
Godot is an advanced, feature-packed, multi-platform 2D and 3D game engine.
It provides a huge set of common tools, so you can just focus on making
your game without reinventing the wheel.

Godot is completely free and open source under the very permissive MIT
license. No strings attached, no royalties, nothing. Your game is yours,
down to the last line of engine code.

To use the editor on the command line in a non-graphical environment (e.g. to
export games from the source code), use the --headless flag.

%files
%doc CHANGELOG.md DONORS.md README.md
%license AUTHORS.md COPYRIGHT.txt LICENSE.txt LOGO_LICENSE.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{rdnsname}.desktop
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/fish/vendor_completions.d/%{name}.fish
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/metainfo/%{rdnsname}.appdata.xml
%{_datadir}/mime/packages/%{rdnsname}.xml
%{_datadir}/zsh/site-functions/_%{name}
%{_mandir}/man6/%{name}.6*

#----------------------------------------------------------------------

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

%files          runner
%license AUTHORS.md COPYRIGHT.txt LICENSE.txt
%{_bindir}/%{name}-runner

#----------------------------------------------------------------------

%{lua: function get_godot_arch()
  arch = rpm.expand("%{_target_cpu}")
  if string.match(rpm.expand("%{arm32}"), arch) then
    arch = "arm32"
  elseif string.match(rpm.expand("%{arm64}"), arch) then
    arch = "arm64"
  elseif string.match(rpm.expand("%{ix86}"), arch) then
    arch = "x86_32"
  elseif string.match(rpm.expand("%{power64}"), arch) then
    arch = "ppc64"
  elseif string.match(rpm.expand("%{riscv64}"), arch) then
    arch = "rv64"
  end
  return arch
end}

%define godot_arch %{lua: print(get_godot_arch())}

%prep
%autosetup -p1 -n %{name}-%{uversion}

%build
# Needs to be in %%build so that system_libs stays in scope
# We don't unbundle enet and minizip as they have necessary custom changes
to_unbundle="brotli embree freetype graphite harfbuzz icu4c libjpeg_turbo libogg libpng libtheora libvorbis libwebp mbedtls miniupnpc openxr pcre2 sdl wslay zlib zstd"

%if %{system_glslang}
to_unbundle+=" glslang"
%endif
%if %{system_recastnavigation}
to_unbundle+=" recastnavigation"
%endif

# Disable dlopen wrappers for Linux deps, we link them dynamically.
system_libs="use_sowrap=no "
rm -rf thirdparty/linuxbsd_headers

for lib in $to_unbundle; do
    system_libs+="builtin_"$lib"=no "
    rm -rf thirdparty/$lib
done

%define _scons scons %{?_smp_mflags} "CCFLAGS=%{?build_cflags}" "LINKFLAGS=%{?build_ldflags}" arch=%{godot_arch} $system_libs lto=full use_static_cpp=no debug_symbols=yes progress=no

%if 0%{?fedora}
export BUILD_NAME="fedora"
%endif
%if 0%{?mageia}
export BUILD_NAME="mageia"
%endif

# Build graphical editor.
%_scons p=linuxbsd target=editor

# Build game runner.
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

%check
# Validate desktop and appdata files
desktop-file-validate %{buildroot}%{_datadir}/applications/%{rdnsname}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{rdnsname}.appdata.xml

%changelog
%autochangelog
