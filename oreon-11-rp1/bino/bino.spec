%global source0_hash 843cac2c951dd933e55987717223a45462d3fb0f332fc6311e173d8dabe66e5c

Name:           bino
Version:        2.6
Release:        %autorelease
Summary:        3D video player

License:        GPL-3.0-or-later
URL:            https://bino3d.org
Source0:        %{url}/releases/%{name}-%{version}.tar.gz
Source1:        %{url}/releases/%{name}-%{version}.tar.gz.sig
Source2:        https://marlam.de/key.txt

Requires:       hicolor-icon-theme

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  libappstream-glib
BuildRequires:  pandoc

BuildRequires:  libGL-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtmultimedia-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  qvr-devel

%description
Bino is a 3D video player. It supports stereoscopic 3D video with a wide
variety of input and output formats. It also supports multi-display video
and it can be used for powerwalls, virtual reality installations and other
multi-projector setups.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%check
desktop-file-validate \
  %{buildroot}%{_datadir}/applications/org.bino3d.bino.desktop
appstream-util validate-relax --nonet \
  %{buildroot}%{_metainfodir}/org.bino3d.bino.metainfo.xml

%files
%license LICENSE.md
%doc README.md NEWS.md
%doc %{_pkgdocdir}/%{name}-manual.*
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/applications/org.bino3d.bino.desktop
%{_datadir}/icons/hicolor/*/apps/org.bino3d.bino.*
%{_metainfodir}/org.bino3d.bino.metainfo.xml

%changelog
%autochangelog
