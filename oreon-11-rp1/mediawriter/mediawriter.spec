%global source0_hash 8a8054893044dd559a696bfbed61da9d979898b55f85904f275f37f57901f415
Name:           mediawriter
Version:        5.3.2
Release:        1%{?dist}
Summary:        Fedora Media Writer
License:        LGPL-2.0-or-later AND GPL-2.0-or-later
URL:            https://github.com/FedoraQt/MediaWriter
Source0:        https://github.com/FedoraQt/MediaWriter/archive/%{version}.tar.gz#/MediaWriter-%{version}.tar.gz
Provides:       liveusb-creator = %{version}-%{release}
Obsoletes:      liveusb-creator <= 3.95.4-2
Requires:       qt6-qtdeclarative
Requires:       qt6-qtsvg
%if !0%{?flatpak}
Requires:       polkit
%endif
Requires:       xz-libs
%if !0%{?flatpak}
Requires: udisks
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  xz-devel
# /oreon:deps
%description
A tool to write images of Fedora media to portable drives
like flash drives or memory cards.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir MediaWriter-%{version}
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/org.fedoraproject.MediaWriter.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
