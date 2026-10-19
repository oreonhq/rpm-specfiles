%global source7_hash 20e50fe7aae3e56378ebf0417d9de904f55a0e61e4df315333e632a4d3555d95
%global source6_hash 33a3bb43b08497a0bdb2f49f140a2829e582d5c16c0ad52be1595c803f706912
%global source0_hash 52e7dd315ae0e5c3868a23231e691578cd694bcca5af627fc57c03f32bdc846f
%global irr_version 1.9.0mt13
%global minetest_game_version 5.8.0
Name:     minetest
Version:  5.17.0
Release:        1%{?dist}
Summary:        Multiplayer infinite-world block sandbox with survival mode
License:  LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-CC-BY-SA
URL:      https://luanti.org
Source0:        https://github.com/luanti-org/luanti/archive/%{version}/%{name}-%{version}.tar.gz
Source2:  %{name}@.service
Source3:  %{name}.rsyslog
Source4:  %{name}.logrotate
Source5:  %{name}.README
Source6:  https://github.com/luanti-org/minetest_game/archive/%{minetest_game_version}/%{name}_game-%{minetest_game_version}.tar.gz
Source7:  http://www.gnu.org/licenses/lgpl-2.1.txt
Source8:  default.conf
Patch0:   metainfo.patch
ExclusiveArch:  %{arm} %{ix86} x86_64 %{mips} aarch64
Requires:       %{name}-server = %{version}-%{release}
Provides:       %{name}-data-game = %{version}-%{release}
Obsoletes:      %{name}-data-game < 5.8.0-1
Requires:       hicolor-icon-theme
Provides:  bundled(irrlicht) = %{irr_version}
# oreon:deps
BuildRequires:  bzip2-devel
BuildRequires:  cmake
BuildRequires:  cmake(SDL2)
BuildRequires:  desktop-file-utils
BuildRequires:  freetype-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  gmp-devel
BuildRequires:  hiredis-devel
BuildRequires:  jsoncpp-devel
BuildRequires:  leveldb-devel
BuildRequires:  libXi-devel
BuildRequires:  libXxf86vm-devel
BuildRequires:  libappstream-glib
BuildRequires:  libcurl-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libogg-devel
BuildRequires:  libpng-devel
BuildRequires:  libpq-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libzstd-devel
BuildRequires:  luajit-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  openal-soft-devel
BuildRequires:  openssl-devel
BuildRequires:  spatialindex-devel
BuildRequires:  sqlite-devel
BuildRequires:  systemd
BuildRequires:  zlib-devel
# /oreon:deps
%description
Game of mining, crafting and building in the infinite world of cubic blocks with
optional hostile creatures, features both single and the network multiplayer
mode, mods. Public multiplayer servers are available.

%package server
Summary:  Minetest multiplayer server
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd
Requires:         %{name}-data-common = %{version}-%{release}
%description server
Minetest multiplayer server. This package does not require X Window System.

%package data-common
Summary:  Minetest common data between client and server
%description data-common
Minetest common data. This package is shared between minetest server and client.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n luanti-%{version}

#pushd lib
#tar xf %%{SOURCE9}
#mv irrlicht-%%{irr_version} irrlichtmt
#popd

cp %{SOURCE7} doc/

# purge bundled jsoncpp and lua, and gmp :P
rm -vrf lib/jsoncpp lib/lua lib/gmp

find . -name .gitignore -print -delete
find . -name .travis.yml -print -delete
find . -name .luacheckrc -print -delete

# Create a sysusers.d config file
cat >minetest.sysusers.conf <<EOF
u minetest - 'Minetest multiplayer server' %{_sharedstatedir}/%{name} /bin/bash
EOF

%build

%ifarch aarch64
%define _lto_cflags %{nil}
%endif
LDFLAGS="$LDFLAGS $(pkg-config --libs openssl)"
export LDFLAGS
%cmake -DENABLE_CURL=TRUE           \
       -DENABLE_LEVELDB=TRUE        \
       -DENABLE_LUAJIT=TRUE         \
       -DENABLE_GETTEXT=TRUE        \
       -DENABLE_SOUND=TRUE          \
       -DENABLE_SYSTEM_JSONCPP=TRUE \
       -DENABLE_SYSTEM_GMP=TRUE     \
       -DENABLE_FREETYPE=TRUE       \
       -DENABLE_REDIS=TRUE          \
       -DENABLE_POSTGRESQL=TRUE     \
       -DPostgreSQL_TYPE_INCLUDE_DIR=%{_includedir}/pgsql \
       -DBUILD_SERVER=TRUE          \
       -DJSON_INCLUDE_DIR=/usr/include/json \
%{nil}
%cmake_build
%install
%cmake_install
desktop-file-validate %{buildroot}%{_datadir}/applications/org.luanti.luanti.desktop
mkdir -p %{buildroot}%{_unitdir}/
install -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_sysconfdir}/rsyslog.d/
install -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/rsyslog.d/%{name}.conf
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d/
install -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}-server
install -d -m 0775 %{buildroot}%{_sharedstatedir}/%{name}/
install -d -m 0775 %{buildroot}%{_sharedstatedir}/%{name}/default/
install -d -m 0775 %{buildroot}%{_sharedstatedir}/%{name}/.minetest/
install -d -m 0775 %{buildroot}%{_sharedstatedir}/%{name}/.minetest/games/
pushd %{buildroot}%{_sharedstatedir}/%{name}/.minetest/games/
tar xf %{SOURCE6}
mv %{name}_game-%{minetest_game_version} %{name}_game
popd
install -d -m 0775 %{buildroot}%{_sysconfdir}/%{name}/
install    -m 0664 minetest.conf.example %{buildroot}%{_sysconfdir}/%{name}/default.conf
install -d -m 0775 %{buildroot}%{_sysconfdir}/sysconfig/%{name}/
install    -m 0664 %{SOURCE8} %{buildroot}%{_sysconfdir}/sysconfig/%{name}
cp -p %{SOURCE5} README.fedora
mkdir __doc
mv  %{buildroot}%{_datadir}/doc/luanti/* __doc
rm -rf %{buildroot}%{_datadir}/doc/luanti
%find_lang luanti
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.luanti.luanti.metainfo.xml
install -m0644 -D minetest.sysusers.conf %{buildroot}%{_sysusersdir}/minetest.conf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post server

%systemd_post %{name}@default.service
%preun server

%systemd_preun %{name}@default.service
%postun server

%systemd_postun_with_restart %{name}@default.service
%files -f %{oreon_filedir}/main.list
%files -n minetest-server -f %{oreon_filedir}/minetest-server.list
%files -n minetest-data-common -f %{oreon_filedir}/minetest-data-common.list

%changelog

%autochangelog
