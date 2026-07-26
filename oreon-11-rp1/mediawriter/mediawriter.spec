%global source0_hash aa5ab3c74f227475ae1ea93adac4e62f41673411d7d08eb86f23088aa8925131

Name:           mediawriter
Version:        5.2.9
Release:        2%{?dist}
Summary:        Fedora Media Writer

License:        LGPL-2.0-or-later AND GPL-2.0-or-later
URL:            https://github.com/FedoraQt/MediaWriter
Source0:        https://github.com/FedoraQt/MediaWriter/archive/%{version}.tar.gz#/MediaWriter-%{version}.tar.gz

Provides:       liveusb-creator = %{version}-%{release}
Obsoletes:      liveusb-creator <= 3.95.4-2

BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  libappstream-glib
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  xz-devel

Requires:       qt6-qtdeclarative
Requires:       qt6-qtsvg

%if !0%{?flatpak}
Requires:       polkit
%endif
Requires:       xz-libs

%if !0%{?flatpak}
%if 0%{?fedora} && 0%{?fedora} != 25
Requires: storaged
%else
Requires: udisks
%endif
%endif

%description
A tool to write images of Fedora media to portable drives
like flash drives or memory cards.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n MediaWriter-%{version}

%build
%cmake

%cmake_build

%install
%cmake_install

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/org.fedoraproject.MediaWriter.appdata.xml

%files
%license LICENSE.GPL-2 LICENSE.LGPL-2
%{_bindir}/%{name}
%{_libexecdir}/%{name}/
%{_datadir}/metainfo/org.fedoraproject.MediaWriter.appdata.xml
%{_datadir}/applications/org.fedoraproject.MediaWriter.desktop
%{_datadir}/icons/hicolor/16x16/apps/org.fedoraproject.MediaWriter.png
%{_datadir}/icons/hicolor/22x22/apps/org.fedoraproject.MediaWriter.png
%{_datadir}/icons/hicolor/24x24/apps/org.fedoraproject.MediaWriter.png
%{_datadir}/icons/hicolor/32x32/apps/org.fedoraproject.MediaWriter.png
%{_datadir}/icons/hicolor/48x48/apps/org.fedoraproject.MediaWriter.png
%{_datadir}/icons/hicolor/64x64/apps/org.fedoraproject.MediaWriter.png
%{_datadir}/icons/hicolor/128x128/apps/org.fedoraproject.MediaWriter.png
%{_datadir}/icons/hicolor/256x256/apps/org.fedoraproject.MediaWriter.png
%{_datadir}/icons/hicolor/512x512/apps/org.fedoraproject.MediaWriter.png

%changelog
%autochangelog
