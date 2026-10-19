%global source0_hash 430bfad52596bb1f775be3de7424225351df788988bbfa2cfaee5c16491ec4c5
%global __cmake_in_source_build 1
Name: smokegen
Version: 4.14.3
Release:        28%{?dist}
Summary:        Smoke Generator
License: LicenseRef-Callaway-LGPLv2 AND GPL-2.0-or-later
URL: https://projects.kde.org/projects/kde/kdebindings/smoke 
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/stable/%{version}/src/%{name}-%{version}.tar.xz
Conflicts: kdebindings < 4.7.0
%{?_qt4:Requires: qt4%{?_isa} >= %{_qt4_version}}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  pkgconfig(QtCore)
BuildRequires:  pkgconfig(QtXml)
# /oreon:deps
%description
This package includes Smoke Generator.

%package devel
Summary: Development files for Smoke Generator
Conflicts: kdebindings-devel < 4.7.0
Requires: qt4-devel
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake} ..
popd
make %{?_smp_mflags} -C %{_target_platform}
%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n smokegen-devel -f %{oreon_filedir}/smokegen-devel.list

%changelog

%autochangelog
