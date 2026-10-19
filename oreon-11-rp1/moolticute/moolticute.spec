%global source0_hash 90e3cc00a6c10f3de882f467d0815668e1631b4617664e220a9c03e36e881e33
%bcond_without  tests
%global qtver 5
%global qmake %{expand:%{qmake_qt%{qtver}}}
%global forgeurl    https://github.com/mooltipass/%{name}
Version:        1.04.0
%forgemeta
Name:           moolticute
Release:        1%{?dist}
Summary:        Companion GUI application for Mooltipass password manager devices
License:        GPL-3.0-or-later AND (GPL-3.0-only WITH Qt-GPL-exception-1.0) AND BSD-2-Clause AND BSD-3-Clause AND MIT AND OFL-1.1 AND CC-BY-3.0
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1:         moolticute-unbundle-QZXing.patch
Patch2:         moolticute-remove-updater.patch
Requires:       systemd
Requires:       hicolor-icon-theme
Requires:       mooltipass-udev
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  pkgconfig(QZXing)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5WebSockets)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  qt5-linguist
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Moolticute is an easy to use companion app to your Mooltipass device and extends
the power of the device to more platform/tools. It allows you to manage your
Mooltipass with a cross-platform app and daemon service that handles all USB
communication with the device.

Moolticute comes with a daemon that runs in the background, and a user interface
app to control your Mooltipass. Other clients can also connect and talk to the
daemon (it uses a WebSocket connection and simple JSON messages).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

# Remove bundled QZXing
rm -rf src/QZXing
# Remove bundled QSimpleUpdater
rm -rf src/QSimpleUpdater

# Change the version from git to the specific release version.
# Also set the APP_TYPE to deb to disable the update checker. This isn't
# used anywhere else, so doesn't really matter.
cat <<EOF > ./src/version.h
#ifndef VERSION__H
#define VERSION__H
#define APP_VERSION "v%{version}"
#define APP_TYPE "deb"
#endif
EOF

%build

%qmake  Moolticute.pro -o build/ \
    PREFIX=%{_prefix} \
    CONFIG+=use_system_qzxing
%make_build -C build
%install
%make_install INSTALL_ROOT=%{buildroot} -C build
mkdir LICENSES
install -pm 0644 LICENSE LICENSES/LICENSE.GPL3
install -pm 0644 src/AnsiEscapeCodeHandler/LICENSE.GPL3-EXCEPT LICENSES/LICENSE.AnsiEscapeCodeHandler
install -pm 0644 src/QtAwesome/LICENSE.md LICENSES/LICENSE.QtAwesome
install -pm 0644 src/http-parser/LICENSE-MIT LICENSES/LICENSE.http-parser
install -pm 0644 src/qtcsv/LICENSE LICENSES/LICENSE.qtcsv
install -pm 0644 src/qtcsv6/LICENSE LICENSES/LICENSE.qtcsv6
install -pm 0644 src/CyoEncode/LICENSE.TXT LICENSES/LICENSE.CyoEncode
install -pm 0644 src/SimpleCrypt/LICENSE LICENSES/LICENSE.SimpleCrypt
install -pm 0644 src/zxcvbn-c/LICENSE LICENSES/LICENSE.zxcvbn-c
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}/%{_datadir}/applications/moolticute.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
%if %{with tests}
%make_build -C build check
%endif
%post

%systemd_post moolticuted.service
%preun

%systemd_preun moolticuted.service
%postun

%systemd_postun_with_restart moolticuted.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
