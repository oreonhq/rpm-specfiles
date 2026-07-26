%global source0_hash none

%if 0%{?fedora}
# With _package_note_file enabled, godot.x11.opt.tools fails to link with:
# g++: fatal error: environment variable 'RPM_ARCH' not defined
%undefine _package_note_file
%endif

# Headless is editor binary to run without X11, e.g. for exporting games from CLI
%bcond_without  headless
# Server is template (optimized, no tools) binary to run multiplayer servers
%bcond_without  server

%define status  stable
%define uversion %{version}-%{status}

%define uname   godot
%define urdnsname org.godotengine.Godot
%define rdnsname %{urdnsname}3

Name:           godot3
Version:        3.6.1
Release:        3%{?dist}
Summary:        Multi-platform 2D and 3D game engine with a feature-rich editor (version 3)
%if 0%{?mageia}
Group:          Development/Tools
%endif
# Godot itself is MIT-licensed, the rest is from vendored thirdparty libraries
License:        MIT and CC-BY and ASL 2.0 and BSD and zlib and OFL and Bitstream Vera and ISC and MPLv2.0
URL:            https://godotengine.org
Source0:        https://github.com/godotengine/godot-builds/releases/download/%{uversion}/%{uname}-%{uversion}.tar.xz
Source1:        https://github.com/godotengine/godot-builds/releases/download/%{uversion}/%{uname}-%{uversion}.tar.xz.sha256

Patch0:         godot3-dist-files-rebranding.patch
# https://github.com/godotengine/godot/pull/100389
Patch1:         godot3-miniupnp228.patch
# Partial port of https://github.com/godotengine/godot/pull/90482
Patch3:         godot3-mbedtls3-90482.patch

# Upstream does not support those arches (for now)
ExcludeArch:    ppc64 ppc64le s390x

BuildRequires:  gcc-c++
BuildRequires:  mbedtls-devel
BuildRequires:  miniupnpc-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(bullet) >= 2.89
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libpcre2-32)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libwslay)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(opusfile)
BuildRequires:  pkgconfig(theora)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vorbisfile)
BuildRequires:  pkgconfig(vpx)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(zlib)
%if 0%{?mageia}
BuildRequires:  scons
%else
BuildRequires:  python3-scons
%endif

%ifarch aarch64 x86_64
BuildRequires:  embree3-devel
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

# Bundled libraries: many of the libraries code in `thirdparty` can be
# unbundled when the libraries are provided by the system. Keep in mind
# though that the `thirdparty` folder also contains code which is typically
# not packaged in distros, and is probably best left bundled.

# Has some modifications for IPv6 support, upstream enet is unresponsive.
# Should not be unbundled.
# Cf: https://github.com/godotengine/godot/issues/6992
Provides:       bundled(enet) = 1.3.18
# Upstream commit from 2016 (32d5ac49414a8914ec1e1f285f3f927c6e8ec29d),
# newer than 1.0.0.27 which is the last tag.
# Could be unbundled if packaged.
Provides:       bundled(libwebm)
# Has custom changes to support seeking in zip archives
# Should not be unbundled.
Provides:       bundled(minizip) = 1.3.1
# Upstream commit 93ce879dc4c04a3ef1758428ec80083c38610b1f, no releases.
# Could be unbundled if packaged.
Provides:       bundled(nanosvg)
%ifarch x86_64
# Could be unbundled but requires some upstream work, and it's not clear if
# upstream code would be compatible with more recent OIDN releases.
Provides:       bundled(oidn) = 1.1.0
%endif
# Could be unbundled if packaged.
Provides:       bundled(squish) = 1.15
# Could be unbundled if packaged.
Provides:       bundled(tinyexr) = 1.0.8

%description
Godot 3 is an advanced, feature-packed, multi-platform 2D and 3D game engine.
It provides a huge set of common tools, so you can just focus on making
your game without reinventing the wheel.

Godot is completely free and open source under the very permissive MIT
license. No strings attached, no royalties, nothing. Your game is yours,
down to the last line of engine code.

%files
%doc CHANGELOG.md DONORS.md README.md
%license AUTHORS.md COPYRIGHT.txt LICENSE.txt LOGO_LICENSE.md
%{_bindir}/%{name}
%{_datadir}/applications/%{rdnsname}.desktop
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/fish/vendor_completions.d/%{name}.fish
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/metainfo/%{rdnsname}.appdata.xml
%{_datadir}/mime/application/%{rdnsname}.xml
%{_datadir}/zsh/site-functions/_%{name}
%{_mandir}/man6/%{name}.6*

#----------------------------------------------------------------------

%if %{with headless}
%package        headless
Summary:        Godot 3 headless editor binary for CLI usage
%if 0%{?mageia}
Group:          Development/Tools
%endif

%description    headless
This package contains the headless binary for the Godot 3 game engine,
particularly suited for CLI usage, e.g. to export projects from a server
or build system.

To run game servers, see the godot-server package which contains an
optimized template build.

%files          headless
%license AUTHORS.md COPYRIGHT.txt LICENSE.txt
%{_bindir}/%{name}-headless
%endif

#----------------------------------------------------------------------

%if %{with server}
%package        server
Summary:        Godot 3 headless runtime binary for hosting game servers
%if 0%{?mageia}
Group:          Games/Other
%endif

%description    server
This package contains the headless binary for the Godot 3 game engine's
runtime, useful to host standalone game servers.

To use editor tools from the command line, see the godot-headless
package.

%files          server
%license AUTHORS.md COPYRIGHT.txt LICENSE.txt
%{_bindir}/%{name}-server
%endif

#----------------------------------------------------------------------

%package        runner
Summary:        Shared binary to play games developed with the Godot 3 game engine
%if 0%{?mageia}
Group:          Games/Other
%endif

%description    runner
This package contains a godot-runner binary for the Linux X11 platform,
which can be used to run any game developed with the Godot 3 game engine
simply by pointing to the location of the game's data package.

%files          runner
%license AUTHORS.md COPYRIGHT.txt LICENSE.txt
%{_bindir}/%{name}-runner

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n %{uname}-%{uversion}

%build
# Needs to be in %%build so that system_libs stays in scope
# We don't unbundle enet and minizip as they have necessary custom changes
to_unbundle="bullet embree freetype libogg libpng libtheora libvorbis libvpx libwebp mbedtls miniupnpc opus pcre2 wslay zlib zstd"

system_libs=""
for lib in $to_unbundle; do
    system_libs+="builtin_"$lib"=no "
    rm -rf thirdparty/$lib
done

# The denoise module depends on OIDN which is x86_64 only (in the vendored version).
# Godot's own logic to disable it on other arches is a bit brittle when it comes to cross-compiling currently.
%ifnarch x86_64
%define disable_modules module_denoise_enabled=no
%endif

%define _scons scons %{?_smp_mflags} "CCFLAGS=%{?build_cflags}" "LINKFLAGS=%{?build_ldflags}" $system_libs lto=full use_static_cpp=no progress=no %{?disable_modules}

%if 0%{?fedora}
export BUILD_NAME="fedora"
%endif
%if 0%{?mageia}
export BUILD_NAME="mageia"
%endif

# Build graphical editor (tools)
%_scons p=x11 tools=yes target=release_debug

# Build game runner (without tools)
%_scons p=x11 tools=no target=release

%if %{with headless}
# Build headless version of the editor
%_scons p=server tools=yes target=release_debug
%endif

%if %{with server}
# Build headless version of the runtime for servers
%_scons p=server tools=no target=release
%endif

%install
%ifarch riscv64
suffix=rv64
%else
suffix=%{__isa_bits}
%endif
install -d %{buildroot}%{_bindir}
install -m755 bin/%{uname}.x11.opt.tools.$suffix %{buildroot}%{_bindir}/%{name}
install -m755 bin/%{uname}.x11.opt.$suffix %{buildroot}%{_bindir}/%{name}-runner
%if %{with headless}
install -m755 bin/%{uname}_server.x11.opt.tools.$suffix %{buildroot}%{_bindir}/%{name}-headless
%endif
%if %{with server}
install -m755 bin/%{uname}_server.x11.opt.$suffix %{buildroot}%{_bindir}/%{name}-server
%endif

install -D -m644 icon.svg \
    %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
install -D -m644 misc/dist/linux/%{urdnsname}.desktop \
    %{buildroot}%{_datadir}/applications/%{rdnsname}.desktop
install -D -m644 misc/dist/linux/%{urdnsname}.appdata.xml \
    %{buildroot}%{_datadir}/metainfo/%{rdnsname}.appdata.xml
install -D -m644 misc/dist/linux/%{urdnsname}.xml \
    %{buildroot}%{_datadir}/mime/application/%{rdnsname}.xml
install -D -m644 misc/dist/linux/%{uname}.6 \
    %{buildroot}%{_mandir}/man6/%{name}.6
install -D -m644 misc/dist/shell/%{uname}.bash-completion \
    %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -D -m644 misc/dist/shell/%{uname}.fish \
    %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish
install -D -m644 misc/dist/shell/_%{uname}.zsh-completion \
    %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

%check
# Validate desktop and appdata files
desktop-file-validate %{buildroot}%{_datadir}/applications/%{rdnsname}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{rdnsname}.appdata.xml

%changelog
%autochangelog
