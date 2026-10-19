%global source1_hash 88c6c4af84f08dcb8e025f50d41d08eca741fa72d104e81228e109820a3d43f8
%global source0_hash ef05eb7521c841e7571b57cdd67bb729fb60ea76725a8fe27e74d805bbab9580
%bcond_with debug
%global baseversion 286
%undefine _auto_set_build_flags
Name:           mame
Version:        0.%{baseversion}
Release:        1%{?dist}
Summary:        Multiple Arcade Machine Emulator
License:        GPL-2.0-or-later
URL:            http://mamedev.org/
Source0:        https://github.com/%{name}dev/%{name}/archive/%{name}0%{baseversion}/%{name}-%{name}0%{baseversion}.tar.gz
Source1:        https://mamedev.org/releases/whatsnew_0%{baseversion}.txt
Patch0:         %{name}-fortify.patch
Patch1:         0001-Hack-allowing-bgfx-to-initialise-in-absence-of-dx9-s.patch
ExcludeArch:    %{arm} %{ix86}
Requires:       %{name}-data = %{version}-%{release}
Provides:       bundled(asmjit) = 1.20
Provides:       bundled(bgfx)
Provides:       bundled(bimg)
Provides:       bundled(bx)
Provides:       bundled(linenoise)
Provides:       bundled(lsqlite3)
Provides:       bundled(lua) = 5.4.7
Provides:       bundled(luafilesystem)
Provides:       bundled(lua-linenoise)
Provides:       bundled(lua-zlib)
Provides:       bundled(lzma-sdk) = 23.01
Provides:       bundled(minimp3)
Provides:       bundled(softfloat)
# oreon:deps
BuildRequires:  SDL3_ttf-devel
BuildRequires:  asio-static
BuildRequires:  expat-devel
BuildRequires:  flac-devel
BuildRequires:  gcc-c++
BuildRequires:  glm-devel
BuildRequires:  jack-audio-connection-kit
BuildRequires:  libXi-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libzstd-devel
BuildRequires:  lua-devel
BuildRequires:  make
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  portaudio-devel
BuildRequires:  portmidi-devel
BuildRequires:  pugixml-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-sphinxcontrib-rsvgconverter
BuildRequires:  qt6-qtbase-devel
BuildRequires:  rapidjson-devel
BuildRequires:  sqlite-devel
BuildRequires:  utf8proc-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
MAME stands for Multiple Arcade Machine Emulator.  When used in conjunction
with an arcade game's data files (ROMs), MAME will more or less faithfully
reproduce that game on a PC.

The ROM images that MAME utilizes are "dumped" from arcade games' original
circuit-board ROM chips.  MAME becomes the "hardware" for the games, taking
the place of their original CPUs and support chips.  Therefore, these games
are NOT simulations, but the actual, original games that appeared in arcades.

MAME's purpose is to preserve these decades of video-game history.  As gaming
technology continues to rush forward, MAME prevents these important "vintage"
games from being lost and forgotten.  This is achieved by documenting the
hardware and how it functions, thanks to the talent of programmers from the
MAME team and from other contributors.  Being able to play the games is just
a nice side-effect, which doesn't happen all the time.  MAME strives for
emulating the games faithfully.

%package tools
Summary:        Additional tools for MAME
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description tools
%{summary}.

%package data
Summary:        Data files used by MAME
BuildArch:      noarch
%description data
%{summary}.

%package data-software-lists
Summary:        Software lists used by MAME
Requires:       %{name}-data = %{version}-%{release}
BuildArch:      noarch
%description data-software-lists
%{summary}. These are split from the main -data
subpackage due to relatively large size.

%package doc
Summary:        Documentation for MAME
BuildArch:      noarch
%description doc
HTML documentation for MAME.

%prep

%autosetup -n %{name}-%{name}0%{baseversion} -p1

#remove system libs or document themes to ensure system ones are used
#remove 3rdparty code not needed on Linux
rm -rf \
    3rdparty/asio \
    3rdparty/compat \
    3rdparty/dxsdk \
    3rdparty/expat \
    3rdparty/glm \
    3rdparty/flac \
    3rdparty/libjpeg \
    3rdparty/portaudio \
    3rdparty/portmidi \
    3rdparty/pugixml \
    3rdparty/rapidjson \
    3rdparty/sqlite3 \
    3rdparty/tap-windows6 \
    3rdparty/utf8proc \
    3rdparty/zlib \
    3rdparty/zstd \
    docs/themes

install -pm 644 %{SOURCE1} whatsnew_0%{baseversion}.txt

# Create ini files
cat > %{name}.ini << EOF
# Define multi-user paths
artpath            %{_datadir}/%{name}/artwork;%{_datadir}/%{name}/effects
bgfx_path          %{_datadir}/%{name}/bgfx
cheatpath          %{_datadir}/%{name}/cheat
crosshairpath      %{_datadir}/%{name}/crosshair
ctrlrpath          %{_datadir}/%{name}/ctrlr
fontpath           %{_datadir}/%{name}/fonts
hashpath           %{_datadir}/%{name}/hash
languagepath       %{_datadir}/%{name}/language
pluginspath        %{_datadir}/%{name}/plugins
rompath            %{_datadir}/%{name}/roms;%{_datadir}/%{name}/chds;\$HOME/.local/share/%{name}/roms;\$XDG_DATA_HOME/%{name}/roms
samplepath         %{_datadir}/%{name}/samples

# Allow user to override ini settings
inipath            \$XDG_CONFIG_HOME/%{name};\$HOME/.config/%{name};\$HOME/.%{name}/ini;%{_sysconfdir}/%{name}

# Set paths for local storage
cfg_directory      \$XDG_CONFIG_HOME/%{name}/cfg;\$HOME/.config/%{name}/cfg;\$HOME/.%{name}/cfg
comment_directory  \$XDG_CONFIG_HOME/%{name}/comments;\$HOME/.config/%{name}/comments;\$HOME/.%{name}/comments
diff_directory     \$XDG_CONFIG_HOME/%{name}/diff;\$HOME/.config/%{name}/diff;\$HOME/.%{name}/diff
input_directory    \$XDG_CONFIG_HOME/%{name}/inp;\$HOME/.config/%{name}/inp;\$HOME/.%{name}/inp
nvram_directory    \$XDG_STATE_HOME/%{name}/nvram;\$HOME/.local/state/%{name}/nvram;\$HOME/.%{name}/nvram
snapshot_directory \$XDG_STATE_HOME/%{name}/snap;\$HOME/.local/state/%{name}/snap;\$HOME/.%{name}/snap
state_directory    \$XDG_STATE_HOME/%{name}/sta;\$HOME/.local/state/%{name}/sta;\$HOME/.%{name}/sta

# Fedora custom defaults
autosave           1
EOF

#ensure genie uses $RPM_OPT_FLAGS and $RPM_LD_FLAGS
sed -i "s@-Wall -Wextra -Os \$(MPARAM)@$RPM_OPT_FLAGS@" 3rdparty/genie/build/gmake.linux/genie.make
sed -i "s@-s -rdynamic@$RPM_LD_FLAGS -rdynamic@" 3rdparty/genie/build/gmake.linux/genie.make

%build

RPM_OPT_FLAGS=$(echo $RPM_OPT_FLAGS | sed "s@-g@-g1@")
RPM_OPT_FLAGS=$(echo $RPM_OPT_FLAGS | sed "s@ -Wp,-D_GLIBCXX_ASSERTIONS@@")
%define _lto_cflags %{nil}
%make_build \
%if %{with debug}
    DEBUG=1 \
%endif
    NOWERROR=1 \
    OPTIMIZE=2 \
    OSD=sdl3 \
    PYTHON_EXECUTABLE=python3 \
    QT_HOME=%{_libdir}/qt6 \
    VERBOSE=1 \
    USE_SYSTEM_LIB_ASIO=1 \
    USE_SYSTEM_LIB_EXPAT=1 \
    USE_SYSTEM_LIB_FLAC=1 \
    USE_SYSTEM_LIB_GLM=1 \
    USE_SYSTEM_LIB_JPEG=1 \
    USE_SYSTEM_LIB_PORTAUDIO=1 \
    USE_SYSTEM_LIB_PORTMIDI=1 \
    USE_SYSTEM_LIB_PUGIXML=1 \
    USE_SYSTEM_LIB_RAPIDJSON=1 \
    USE_SYSTEM_LIB_SQLITE3=1 \
    USE_SYSTEM_LIB_UTF8PROC=1 \
    USE_SYSTEM_LIB_ZLIB=1 \
    USE_SYSTEM_LIB_ZSTD=1 \
    USE_WAYLAND=1 \
    SDL_INI_PATH="%{_sysconfdir}/%{name};" \
    TOOLS=1 \
    LDOPTS="$RPM_LD_FLAGS" \
    OPT_FLAGS="$RPM_OPT_FLAGS"
pushd docs
    %make_build html
popd
%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
for folder in cfg comments diff inp
do
    install -d $RPM_BUILD_ROOT%{_sysconfdir}/skel/.config/%{name}/$folder
done
for folder in memcard nvram snap sta
do
    install -d $RPM_BUILD_ROOT%{_sysconfdir}/skel/.local/state/%{name}/$folder
done
for folder in roms
do
    install -d $RPM_BUILD_ROOT%{_sysconfdir}/skel/.local/share/%{name}/$folder
done
install -d $RPM_BUILD_ROOT%{_bindir}
for folder in artwork bgfx chds cheats ctrlr effects fonts hash language \
    plugins keymaps roms samples shader
do
    install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/$folder
done
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install -d $RPM_BUILD_ROOT%{_mandir}/man6
install -pm 644 %{name}.ini $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
%if %{with debug}
install -pm 755 %{name}d $RPM_BUILD_ROOT%{_bindir}/%{name}d
%else
install -pm 755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
%endif
install -pm 755 castool chdman floptool imgtool jedutil ldresample ldverify \
    nltool nlwav pngcmp romcmp unidasm $RPM_BUILD_ROOT%{_bindir}
for tool in regrep split srcclean
do
    install -pm 755 $tool $RPM_BUILD_ROOT%{_bindir}/%{name}-$tool
done
pushd artwork
    find -type d -exec install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/artwork/{} \;
    find -type f -exec install -pm 644 {} $RPM_BUILD_ROOT%{_datadir}/%{name}/artwork/{} \;
popd
pushd bgfx
    find -type d -a ! -wholename \*dx\* -a ! -wholename \*metal\* -exec install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/bgfx/{} \;
    find -type f -a ! -wholename \*dx\* -a ! -wholename \*metal\* -exec install -pm 644 {} $RPM_BUILD_ROOT%{_datadir}/%{name}/bgfx/{} \;
popd
install -pm 644 hash/* $RPM_BUILD_ROOT%{_datadir}/%{name}/hash
install -pm 644 keymaps/* $RPM_BUILD_ROOT%{_datadir}/%{name}/keymaps
pushd language
    find -type d -exec install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/language/{} \;
    find -type f -name \*.mo -exec install -pm 644 {} $RPM_BUILD_ROOT%{_datadir}/%{name}/language/{} \;
    grep -r --include=*.po \"Language: | sed -r 's@(.*)/strings\.po:"Language: ([[:alpha:]]{2}(_[[:alpha:]]{2})?)\\n"@%lang(\2) %{_datadir}/%{name}/language/\1@' > ../%{name}.lang
popd
pushd plugins
    find -type d -exec install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins/{} \;
    find -type f -exec install -pm 644 {} $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins/{} \;
popd
pushd src/osd/modules/opengl
    install -pm 644 shader/*.?sh $RPM_BUILD_ROOT%{_datadir}/%{name}/shader
popd
pushd docs/man
install -pm 644 castool.1 chdman.1 imgtool.1 floptool.1 jedutil.1 ldresample.1 \
    ldverify.1 romcmp.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -pm 644 mame.6 $RPM_BUILD_ROOT%{_mandir}/man6
popd
rm -f docs/.buildinfo
rm -rf docs/build/html/_sources
find $RPM_BUILD_ROOT%{_datadir}/%{name} -name LICENSE -exec rm {} \;
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

./%{name} -validate
%files -f %{oreon_filedir}/main.list
%files -n mame-tools -f %{oreon_filedir}/mame-tools.list
%files -n mame-data -f %{oreon_filedir}/mame-data.list
%files -n mame-data-software-lists -f %{oreon_filedir}/mame-data-software-lists.list
%files -n mame-doc -f %{oreon_filedir}/mame-doc.list

%changelog

%autochangelog
