%global source0_hash b5db2479360d5efa00c1856466e98481571d22064ed63272706ff0d5098f0e5e
Name:           algobox
Version:        1.1.1
Release:        1%{?dist}
Summary:        Algorithmic software
Summary(fr):    Logiciel d'algorithmique
License:        GPL-2.0-or-later
URL:            https://www.xm1math.net/algobox
Source0:        https://www.xm1math.net/%{name}/%{name}-%{version}.tar.bz2
ExclusiveArch:  %{qt5_qtwebengine_arches}
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtwebengine-devel
# /oreon:deps
%description
Algobox is an initiation to algorithmic software at high school level.

%description -l fr
Algobox est un logiciel d'initiation à l'algorithmique au niveau lycée.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
chmod -x license.txt

%build

%{qmake_qt5}
%make_build
%install
%make_install INSTALL_ROOT=%{buildroot}
%oreon_autofiles main

%check

desktop-file-validate \
  %{buildroot}%{_datadir}/applications/algobox.desktop
appstream-util validate-relax --nonet \
  %{buildroot}%{_metainfodir}/*.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
