%global source0_hash 33a3bb43b08497a0bdb2f49f140a2829e582d5c16c0ad52be1595c803f706912

%global irr_version 1.9.0mt13
%global minetest_game_version 5.8.0
Name:     minetest
Version:  5.15.1
Release:  1%{?dist}
Summary:  Multiplayer infinite-world block sandbox with survival mode

# Automatically converted from old format: LGPLv2+ and CC-BY-SA - review is highly recommended.
License:  LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-CC-BY-SA
URL:      https://luanti.org

Source0:  https://github.com/luanti-org/luanti/archive/%{version}/%{name}-%{version}.tar.gz
Source2:  %{name}@.service
Source3:  %{name}.rsyslog
Source4:  %{name}.logrotate
Source5:  %{name}.README
Source6:  https://github.com/luanti-org/minetest_game/archive/%{minetest_game_version}/%{name}_game-%{minetest_game_version}.tar.gz
Source7:  http://www.gnu.org/licenses/lgpl-2.1.txt
Source8:  default.conf
#Source9:  https://github.com/minetest/irrlicht/archive/%%{irr_version}/%%{name}-%%{irr_version}.tar.gz
Patch0:   metainfo.patch

%if 0%{?rhel}
ExclusiveArch:  %{ix86} x86_64
%else
# LuaJIT arches
ExclusiveArch:  %{arm} %{ix86} x86_64 %{mips} aarch64
%endif

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake >= 2.6.0
BuildRequires:  bzip2-devel gettext-devel sqlite-devel zlib-devel
BuildRequires:  libpng-devel libjpeg-turbo-devel libXxf86vm-devel mesa-libGL-devel
BuildRequires:  desktop-file-utils
BuildRequires:  systemd
BuildRequires:  openal-soft-devel
BuildRequires:  libvorbis-devel
BuildRequires:  jsoncpp-devel
BuildRequires:  libcurl-devel
BuildRequires:  luajit-devel
BuildRequires:  leveldb-devel
BuildRequires:  gmp-devel
BuildRequires:  libappstream-glib
BuildRequires:  freetype-devel
BuildRequires:  spatialindex-devel
BuildRequires:  openssl-devel
BuildRequires:  libogg-devel
BuildRequires:  libpq-devel
BuildRequires:  hiredis-devel
BuildRequires:  libzstd-devel
BuildRequires:  libXi-devel
BuildRequires:  cmake(SDL2)

Requires:       %{name}-server = %{version}-%{release}

#Drop after f42
Provides:       %{name}-data-game = %{version}-%{release}
Obsoletes:      %{name}-data-game < 5.8.0-1

Requires:       hicolor-icon-theme

Provides:  bundled(irrlicht) = %{irr_version}

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
# -DENABLE_FREETYPE=ON needed for Unicode in text chat
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

# Add desktop file
desktop-file-validate %{buildroot}%{_datadir}/applications/org.luanti.luanti.desktop

# Systemd unit file
mkdir -p %{buildroot}%{_unitdir}/
install -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}

# /etc/rsyslog.d/minetest.conf
mkdir -p %{buildroot}%{_sysconfdir}/rsyslog.d/
install -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/rsyslog.d/%{name}.conf

# /etc/logrotate.d/minetest
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d/
install -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}-server

# /var/lib/minetest directory for server data files
install -d -m 0775 %{buildroot}%{_sharedstatedir}/%{name}/
install -d -m 0775 %{buildroot}%{_sharedstatedir}/%{name}/default/
install -d -m 0775 %{buildroot}%{_sharedstatedir}/%{name}/.minetest/
install -d -m 0775 %{buildroot}%{_sharedstatedir}/%{name}/.minetest/games/

pushd %{buildroot}%{_sharedstatedir}/%{name}/.minetest/games/
tar xf %{SOURCE6}
mv %{name}_game-%{minetest_game_version} %{name}_game
popd

# /etc/minetest/default.conf
install -d -m 0775 %{buildroot}%{_sysconfdir}/%{name}/
install    -m 0664 minetest.conf.example %{buildroot}%{_sysconfdir}/%{name}/default.conf

# /etc/sysconfig/default.conf
install -d -m 0775 %{buildroot}%{_sysconfdir}/sysconfig/%{name}/
install    -m 0664 %{SOURCE8} %{buildroot}%{_sysconfdir}/sysconfig/%{name}

cp -p %{SOURCE5} README.fedora

# Move doc directory back to the sources
mkdir __doc
mv  %{buildroot}%{_datadir}/doc/luanti/* __doc
rm -rf %{buildroot}%{_datadir}/doc/luanti

%find_lang luanti

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.luanti.luanti.metainfo.xml

install -m0644 -D minetest.sysusers.conf %{buildroot}%{_sysusersdir}/minetest.conf

%post server
%systemd_post %{name}@default.service

%preun server
%systemd_preun %{name}@default.service

%postun server
%systemd_postun_with_restart %{name}@default.service

%files -f luanti.lang
%license doc/lgpl-2.1.txt
%doc README.fedora
%{_bindir}/%{name}
%{_bindir}/luanti
%{_datadir}/luanti/client
%{_datadir}/luanti/fonts
%{_datadir}/luanti/textures
%{_datadir}/applications/org.luanti.luanti.desktop
%{_datadir}/icons/hicolor/*/apps/luanti.png
%{_datadir}/icons/hicolor/scalable/apps/luanti.svg
%{_mandir}/man6/luanti.*
%{_datadir}/metainfo/org.luanti.luanti.metainfo.xml

%files server
%license doc/lgpl-2.1.txt
%doc README.md doc/protocol.txt README.fedora
%{_bindir}/minetestserver
%{_bindir}/luantiserver
%{_unitdir}/%{name}@.service
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}-server
%config(noreplace) %{_sysconfdir}/rsyslog.d/%{name}.conf
%attr(-,minetest,minetest)%{_sharedstatedir}/%{name}/
%config(noreplace) %attr(-,minetest,minetest)%{_sysconfdir}/%{name}/
%attr(-,minetest,minetest)%{_sysconfdir}/sysconfig/%{name}/
%{_mandir}/man6/luantiserver.*
%{_sysusersdir}/minetest.conf

%files data-common
%license doc/lgpl-2.1.txt
%{_datadir}/luanti/builtin

%changelog
%autochangelog
