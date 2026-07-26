%global source0_hash 90e3cc00a6c10f3de882f467d0815668e1631b4617664e220a9c03e36e881e33

%bcond_without  tests

%if 0%{?fedora} >= 40
%global qtver 6
%else
%global qtver 5
%endif

%global qmake %{expand:%{qmake_qt%{qtver}}}

%global forgeurl    https://github.com/mooltipass/%{name}

Version:        1.04.0

%forgemeta

Name:           moolticute
Release:        %autorelease
Summary:        Companion GUI application for Mooltipass password manager devices

# The entire source code is GPL-3.0-or-later except:
# src/AnsiEscapeCodeHandler.[cpp|h] which is GPL-3.0-only WITH Qt-GPL-exception-1.0,
# src/CyoEncode/ which is BSD-2-Clause,
# src/QtAwesome/ which is MIT AND OFL-1.1 AND CC-BY-3.0 (see src/QtAwesome/README.md for details),
# src/SimpleCrypt/ which is BSD-3-Clause,
# src/http-parser/ which is MIT,
# src/qtcsv/ which is MIT,
# src/qtcsv6/ which is MIT,
# src/zxcvbn-c which is BSD-3-Clause.
#
# Note: src/qwinoverlappedionotifier.[cpp|h] is not compiled, and thus ignored.
# Note: Missing license files are being added: https://github.com/mooltipass/moolticute/pull/1098
License:        GPL-3.0-or-later AND (GPL-3.0-only WITH Qt-GPL-exception-1.0) AND BSD-2-Clause AND BSD-3-Clause AND MIT AND OFL-1.1 AND CC-BY-3.0
URL:            %{forgeurl}
Source0:        %{forgesource}

# https://github.com/mooltipass/moolticute/pull/1231
Patch1:         moolticute-unbundle-QZXing.patch
# QSimpleUpdater is licensed under DBAD, which isn't approved. The updater isn't used anyway, so this patch removes it.
Patch2:         moolticute-remove-updater.patch

Requires:       systemd
Requires:       hicolor-icon-theme
Requires:       mooltipass-udev

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(Qt%{qtver}Core)
BuildRequires:  pkgconfig(Qt%{qtver}DBus)
BuildRequires:  pkgconfig(Qt%{qtver}Gui)
BuildRequires:  pkgconfig(Qt%{qtver}Network)
BuildRequires:  pkgconfig(Qt%{qtver}WebSockets)
BuildRequires:  pkgconfig(Qt%{qtver}Widgets)
BuildRequires:  pkgconfig(QZXing)
BuildRequires:  qt%{qtver}-linguist
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

%if %{with tests}
BuildRequires:  pkgconfig(Qt%{qtver}Test)
%endif

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

# Collect licenses
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

%files
%license LICENSES/*
%doc README.md
%{_bindir}/moolticute
%{_bindir}/moolticuted
%{_metainfodir}/*.metainfo.xml
%{_datadir}/applications/moolticute.desktop
%{_datadir}/icons/hicolor/scalable/apps/moolticute.svg
%{_datadir}/icons/hicolor/32x32/apps/moolticute.png
%{_datadir}/icons/hicolor/128x128/apps/moolticute.png
%{_unitdir}/moolticuted.service

%changelog
%autochangelog
