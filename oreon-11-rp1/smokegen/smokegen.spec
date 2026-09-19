%global source0_hash 430bfad52596bb1f775be3de7424225351df788988bbfa2cfaee5c16491ec4c5

%global __cmake_in_source_build 1

Name: smokegen
Version: 4.14.3
Release: 28%{?dist}
Summary: Smoke Generator

# Automatically converted from old format: LGPLv2 and GPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2 AND GPL-2.0-or-later
URL: https://projects.kde.org/projects/kde/kdebindings/smoke 
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: make
BuildRequires: cmake >= 2.8.8
BuildRequires: pkgconfig(QtCore) pkgconfig(QtXml) 

Conflicts: kdebindings < 4.7.0

%{?_qt4:Requires: qt4%{?_isa} >= %{_qt4_version}}

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

%files
%doc COPYING COPYING.LIB
%doc README
%{_libdir}/libsmokebase.so.3*

%files devel
%{_bindir}/smokeapi
%{_bindir}/smokegen
%{_libdir}/libcppparser.so
%{_libdir}/libsmokebase.so
%{_libdir}/smokegen/
%{_includedir}/smoke.h
%{_includedir}/smokegen/
%{_datadir}/smoke/
%{_datadir}/smokegen/

%changelog
%autochangelog
