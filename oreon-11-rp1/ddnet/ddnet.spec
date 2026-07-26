%global source0_hash none

# Enable Ninja build
%bcond_without ninja_build

Name:           ddnet
Version:        19.5
Release:        1%{?dist}
Summary:        DDraceNetwork, a cooperative racing mod of Teeworlds

#
# CC-BY-SA
# --------------------------------------
# data/languages/
# data/fonts/DejaVuSans.ttf
# data/fonts/SourceHanSansSC-Regular.otf
#
# ASL 2.0
# --------------------------------------
# data/
#
# MIT
# --------------------------------------
# man/
#
# Public domain
# --------------------------------------
# src/base/hash_libtomcrypt.c
#

# Automatically converted from old format: zlib and CC-BY-SA and ASL 2.0 and MIT and Public Domain - review is highly recommended.
License:        Zlib AND LicenseRef-Callaway-CC-BY-SA AND Apache-2.0 AND LicenseRef-Callaway-MIT AND LicenseRef-Callaway-Public-Domain
URL:            https://ddnet.org/
Source0:        https://github.com/ddnet/ddnet/archive/%{version}/%{name}-%{version}.tar.gz

# Disable network lookup test because without internet access tests not pass
Patch1:         0001-Disabled-network-lookup-test.patch
# Unbundle md5 and json-parser
Patch2:         0002-Unbundle-md5_and_json-parser.patch

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

%if %{with ninja_build}
BuildRequires:  ninja-build
%endif

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  cargo
BuildRequires:  python3
BuildRequires:  cargo-rpm-macros >= 24

BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(json-parser)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(opusfile)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(wavpack)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  glslang
#BuildRequires:  pkgconfig(libavcodec)
#BuildRequires:  pkgconfig(libavformat)
#BuildRequires:  pkgconfig(libavutil)
#BuildRequires:  pkgconfig(libswscale)
#BuildRequires:  pkgconfig(libswresample)
#BuildRequires:  pkgconfig(x264)
BuildRequires:  (crate(cxx/default) >= 1.0.0 with crate(cxx/default) < 2.0.0~)
BuildRequires:  gmock-devel

Requires:       %{name}-data = %{version}-%{release}

# https://github.com/ddnet/ddnet/issues/2019
Provides:       bundled(dejavu-sans-cjkname-fonts)
Provides:       bundled(adobe-source-han-sans-sc-fonts)

%description
DDraceNetwork (DDNet) is an actively maintained version of DDRace,
a Teeworlds modification with a unique cooperative gameplay.
Help each other play through custom maps with up to 64 players,
compete against the best in international tournaments, design your
own maps, or run your own server.

%package        data
Summary:        Data files for %{name}

Requires:       %{name} = %{version}-%{release}
Requires:       hicolor-icon-theme

BuildArch:      noarch

%description    data
Data files for %{name}.

%package        server
Summary:        Standalone server for %{name}

Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    server
Standalone server for %{name}.

%prep
%autosetup -p1 -n %{name}-%{version}
find -type f -exec sed -i 's|engine/external/md5/md5.h|md5/md5.h|g' {} +
find -type f -exec sed -i 's|engine/external/json-parser/json.h|json-parser/json.h|g' {} +

%cargo_prep
sed '/Cargo.lock/d' -i CMakeLists.txt
touch CMakeLists.txt

# Remove bundled stuff...
rm -rf src/engine/external

%build
# ensure standard Rust compiler flags are set
export RUSTFLAGS="%build_rustflags"
# WebSockets disable because it freezes all GUI | https://github.com/ddnet/ddnet/issues/1900
# VIDEORECORDER needs ffpemg more x264
%cmake \
    %{?with_ninja_build: -GNinja} \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DPREFER_BUNDLED_LIBS=OFF \
    -DVIDEORECORDER=OFF \
    -DAUTOUPDATE=OFF -Wno-dev

%cmake_build

%install
%cmake_install

# Install man pages...
install -Dp -m 0644 man/DDNet.6 %{buildroot}%{_mandir}/man6/DDNet.6
install -Dp -m 0644 man/DDNet-Server.6 %{buildroot}%{_mandir}/man6/DDNet-Server.6

%check
# Disable connection test to avoid hanging the tests
export GTEST_FILTER='-Net.Ipv4AndIpv6Work'
%cmake_build --target run_tests
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%license license.txt
%doc README.md
%{_mandir}/man6/DDNet.6*

%{_bindir}/DDNet
%{_libdir}/%{name}/

%{_datadir}/applications/%{name}.desktop

%files data
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/*/apps/%{name}-server.png

%files server
%{_mandir}/man6/DDNet-Server.6*

%{_bindir}/DDNet-Server

%changelog
%autochangelog
