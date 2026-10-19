%global source2_hash 4e3a0863dd448b928c5acba130974a16c1aff9a396a1b9e9cca067a198265f5e
%global source0_hash 42e49831e415412d42bdae86c3054cab5d2b1e75488e21341b303ae31e60f453
Name:           gencolormap
Version:        2.6
Release:        1%{?dist}
Summary:        Tools to generate color maps for visualization
License:        MIT
URL:            https://marlam.de/gencolormap
Source0:        https://marlam.de/%{name}/releases/%{name}-%{version}.tar.gz
Source1:        %{url}/releases/%{name}-%{version}.tar.gz.sig
Source2:        https://marlam.de/key.txt
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  libGL-devel
BuildRequires:  libappstream-glib
BuildRequires:  qt6-qtbase-devel
# /oreon:deps
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
%oreon_autofiles main

%check

desktop-file-validate \
  %{buildroot}%{_datadir}/applications/de.marlam.gencolormap.desktop
appstream-util validate-relax --nonet \
  %{buildroot}%{_metainfodir}/de.marlam.gencolormap.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
