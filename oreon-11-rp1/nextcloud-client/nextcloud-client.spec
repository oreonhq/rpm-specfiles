%global source0_hash c21388d3925293d4cd0d3cc43c3050789d4d109c79ff11d7214c1a1a4274c171
%if 0%{?el8}
%undefine __cmake_in_source_build
%undefine _cmake_skip_rpath
%endif
Name:           nextcloud-client
Version:        4.0.7
Release:        1%{?dist}
Summary:        The Nextcloud Client
License:        LGPL-2.1-or-later and GPL-2.0-only
Url:            https://nextcloud.com/install/#install-clients
Source0:        https://github.com/nextcloud/desktop/archive/v%{version}/desktop-%{version}.tar.gz
Source1:        com.nextcloud.desktopclient.nextcloud.metainfo.xml
ExclusiveArch:  %{qt6_qtwebengine_arches}
%if 0%{?fedora} >= 24 || 0%{?rhel} > 7 || 0%{?oreon} >= 11
%endif
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Provides: mirall = %{version}-%{release}
Obsoletes: mirall < 1.8.0
# oreon:deps
BuildRequires:  check
BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  extra-cmake-modules
BuildRequires:  inkscape
BuildRequires:  inotify-tools-devel
BuildRequires:  kf6-karchive-devel
BuildRequires:  kf6-kbookmarks-devel
BuildRequires:  kf6-kcoreaddons-devel
BuildRequires:  kf6-kguiaddons-devel
BuildRequires:  kf6-kio-devel
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  libcloudproviders-devel
BuildRequires:  libp11-devel
BuildRequires:  neon-devel
BuildRequires:  openssl-devel
BuildRequires:  openssl-devel-engine
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  python3-sphinx
BuildRequires:  qt6-qt5compat-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-gui
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qtquickcontrols2-devel
BuildRequires:  qt6-qtscxml-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  qt6-qttools
BuildRequires:  qt6-qttools-devel
BuildRequires:  qt6-qtwebengine-devel
BuildRequires:  qt6-qtwebsockets-devel
BuildRequires:  qtkeychain-qt6-devel
BuildRequires:  qtlockedfile-qt6-devel
BuildRequires:  qtsingleapplication-qt6-devel
BuildRequires:  sqlite-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Nextcloud-client enables you to connect to your private Nextcloud Server.
With it you can create folders in your home directory, and keep the contents
of those folders synced with your Nextcloud server. Simply copy a file into
the directory and the Nextcloud Client does the rest.

%package libs
Summary: Common files for nextcloud-client
License: LGPL-2.1-or-later
Provides: mirall-common = %{version}-%{release}
Obsoletes: mirall-common < 1.8.0
Requires: %{name}%{?_isa} = %{version}-%{release}
%description libs
Provides common files for nextcloud-client such as the
configuration file that determines the excluded files in a sync.

%package devel
Summary: Development files for nextcloud-client
License: LGPL-2.1-or-later
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: %{name}-static = %{version}-%{release}
Provides: mirall-devel = %{version}-%{release}
Obsoletes: mirall-devel < 1.8.0
%description devel
Development headers for use of the nextcloud-client library

%package nautilus
Summary: nextcloud client nautilus extension
Supplements: (nextcloud-client and nautilus)
Requires: nautilus
Requires: nautilus-python
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: mirall-nautilus = %{version}-%{release}
Obsoletes: mirall-nautilus < 1.8.0
%description nautilus
The nextcloud desktop client nautilus extension.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -n desktop-%{version}

# change compiler flag
sed -i 's/-fPIE/-fPIC/g' src/gui/CMakeLists.txt
sed -i 's/-fPIE/-fPIC/g' src/cmd/CMakeLists.txt

#patch -P0 -p1 -b .drop-qt6guiprivate-dependency

%build

%cmake_kf6 \
  -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed" \
  -DNO_SHIBBOLETH=1 \
  -DBUILD_UPDATER=False
%cmake_build
%install
%cmake_install
%find_lang client --with-qt
mkdir -p %{buildroot}%{_datadir}/metainfo/
install -pm 644 %{SOURCE1} %{buildroot}%{_datadir}/metainfo/com.nextcloud.desktopclient.nextcloud.metainfo.xml
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%postun

%check

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/com.nextcloud.desktopclient.nextcloud.metainfo.xml
%ldconfig_scriptlets libs
%if 0%{?fedora} >= 24 || 0%{?rhel} > 7 || 0%{?oreon} >= 11
%ldconfig_scriptlets dolphin
%endif
%files -f %{oreon_filedir}/main.list
%files -n nextcloud-client-libs -f %{oreon_filedir}/nextcloud-client-libs.list
%files -n nextcloud-client-devel -f %{oreon_filedir}/nextcloud-client-devel.list
%files -n nextcloud-client-nautilus -f %{oreon_filedir}/nextcloud-client-nautilus.list

%changelog

%autochangelog
