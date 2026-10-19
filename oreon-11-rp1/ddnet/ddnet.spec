%global source0_hash c4f6cca7b04e9d370fc2f187b873347b546d6e0c749c01fa7e5cd7d278c88851
%bcond_without ninja_build
Name:           ddnet
Version:        20.0
Release:        1%{?dist}
Summary:        DDraceNetwork, a cooperative racing mod of Teeworlds
License:        Zlib AND LicenseRef-Callaway-CC-BY-SA AND Apache-2.0 AND LicenseRef-Callaway-MIT AND LicenseRef-Callaway-Public-Domain
URL:            https://ddnet.org/
Source0:        https://github.com/ddnet/ddnet/archive/%{version}/%{name}-%{version}.tar.gz
Patch1:         0001-Disabled-network-lookup-test.patch
Patch2:         0002-Unbundle-md5_and_json-parser.patch
%if %{with ninja_build}
%endif
Requires:       %{name}-data = %{version}-%{release}
Provides:       bundled(dejavu-sans-cjkname-fonts)
Provides:       bundled(adobe-source-han-sans-sc-fonts)
# oreon:deps
BuildRequires:  (crate(cxx/default) >= 1.0.0 with crate(cxx/default) < 2.0.0~)
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  glslang
BuildRequires:  gmock-devel
BuildRequires:  libappstream-glib
BuildRequires:  ninja-build
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
BuildRequires:  python3
# /oreon:deps
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

sed '/Cargo.lock/d' -i CMakeLists.txt
touch CMakeLists.txt

# Remove bundled stuff...
rm -rf src/engine/external

%build

export RUSTFLAGS="%build_rustflags"
%cmake \
    %{?with_ninja_build: -GNinja} \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DPREFER_BUNDLED_LIBS=OFF \
    -DVIDEORECORDER=OFF \
    -DAUTOUPDATE=OFF -Wno-dev
%cmake_build
%install
%cmake_install
install -Dp -m 0644 man/DDNet.6 %{buildroot}%{_mandir}/man6/DDNet.6
install -Dp -m 0644 man/DDNet-Server.6 %{buildroot}%{_mandir}/man6/DDNet-Server.6
%oreon_autofiles ddnet-data usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ddnet-server usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export GTEST_FILTER='-Net.Ipv4AndIpv6Work'
%cmake_build --target run_tests
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%files -f %{oreon_filedir}/main.list
%files -n ddnet-data -f %{oreon_filedir}/ddnet-data.list
%files -n ddnet-server -f %{oreon_filedir}/ddnet-server.list

%changelog

%autochangelog
