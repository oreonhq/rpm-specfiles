%global source0_hash 7eb2c34b407056b8719e665114043a3a4be199a5fc1628b1cb853ef8cae81384

Name:           gencolormap
Version:        2.3
Release:        %autorelease
Summary:        Tools to generate color maps for visualization

License:        MIT
URL:            https://marlam.de/gencolormap
Source0:        %{url}/releases/%{name}-%{version}.tar.gz
Source1:        %{url}/releases/%{name}-%{version}.tar.gz.sig
Source2:        https://marlam.de/key.txt

Requires:       hicolor-icon-theme

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  libappstream-glib

BuildRequires:  libGL-devel
BuildRequires:  qt6-qtbase-devel

%description
gencolormap provides tools generate color maps for visualization. A variety of
methods for sequential, diverging, and qualitative maps is available.

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
  %{buildroot}%{_datadir}/applications/de.marlam.gencolormap.desktop
appstream-util validate-relax --nonet \
  %{buildroot}%{_metainfodir}/de.marlam.gencolormap.metainfo.xml

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-gui
%{_datadir}/applications/de.marlam.gencolormap.desktop
%{_datadir}/icons/hicolor/*/apps/de.marlam.gencolormap.*
%{_metainfodir}/de.marlam.gencolormap.metainfo.xml

%changelog
%autochangelog
