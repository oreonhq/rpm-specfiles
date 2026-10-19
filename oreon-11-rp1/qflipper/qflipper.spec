%global source1_hash 4b877587c1e468521a59de9a2b4fc02a3f21bfa878f2ae74da45051fb12b89e5
%global source0_hash 4b877587c1e468521a59de9a2b4fc02a3f21bfa878f2ae74da45051fb12b89e5
%global commit bfce851d4da5a01f24189ba79eac9385b7ce8533
%global timestamp 1699609231
%global nanopb_commit 13666952914f3cf43a70c6b9738a7dc0dd06a6dc
%global srcname qFlipper
%global forgeurl https://github.com/flipperdevices/%{srcname}
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:           qflipper
Version:        1.3.3
Release:        1%{?dist}
Summary:        Desktop application for updating Flipper Zero firmware via PC
License:        GPL-3.0-or-later AND Zlib
URL:            https://update.flipperzero.one
Source0:        %{forgeurl}/archive/%{version}/%{srcname}-%{version}.tar.gz
Source1:        https://github.com/nanopb/nanopb/archive/%{nanopb_commit}/nanopb-%{nanopb_commit}.tar.gz
Source2:        one.flipperzero.qflipper.metainfo.xml
ExcludeArch:    %{ix86}
Requires:       systemd-udev
Provides:       bundled(nanopb) = 0.4.5
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  libusb1-devel
BuildRequires:  make
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtquickcontrols2-devel
BuildRequires:  qt5-qtserialport-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  sed
BuildRequires:  systemd-rpm-macros
BuildRequires:  zlib-devel
# /oreon:deps
%description
Graphical desktop application for updating Flipper Zero firmware via PC.

Features:
* Update Flipper's firmware and supplemental data with a press of one button
* Repair a broken fimware installation
* Stream Flipper's display and control it remotely
* Install firmware from a .dfu file
* Backup and restore settings, progress and pairing data
* Automatic self-update feature
* Command line interface

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -b 1

# Use the correct nanopb snapshot
rmdir 3rdparty/nanopb
ln -s ../../nanopb-%{nanopb_commit} 3rdparty/nanopb

# Set the version
sed -i qflipper_common.pri \
    -e 's/$$GIT_VERSION/%{version}/' \
    -e 's/$$GIT_COMMIT/%{shortcommit}/' \
    -e 's/$$GIT_TIMESTAMP/%{timestamp}/'

# Fix the plugins library path
sed -e 's:/lib/:/%{_lib}/:' \
    -i backend/applicationbackend.cpp plugins/flipperproto0/flipperproto0.pro

%build

%qmake_qt5 \
  PREFIX=%{buildroot}%{_prefix} \
  CONFIG+=qtquickcompiler \
  DEFINES+=DISABLE_APPLICATION_UPDATES
%make_build
%install
%make_install
install -Dpm0644 -t %{buildroot}%{_metainfodir} %SOURCE2
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{srcname}.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
