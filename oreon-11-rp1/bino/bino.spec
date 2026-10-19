%global source2_hash 4e3a0863dd448b928c5acba130974a16c1aff9a396a1b9e9cca067a198265f5e
%global source0_hash 464c2ca8746d9339ed99f5499f10013efe5c45503cb8338f3371e8f3a633416f
Name:           bino
Version:        2.8
Release:        1%{?dist}
Summary:        3D video player
License:        GPL-3.0-or-later
URL:            https://bino3d.org
Source0:        https://%{name}3d.org/releases/%{name}-%{version}.tar.gz
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
BuildRequires:  libxkbcommon-devel
BuildRequires:  pandoc
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtmultimedia-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  qvr-devel
# /oreon:deps
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
%oreon_autofiles main

%check

desktop-file-validate \
  %{buildroot}%{_datadir}/applications/org.bino3d.bino.desktop
appstream-util validate-relax --nonet \
  %{buildroot}%{_metainfodir}/org.bino3d.bino.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
