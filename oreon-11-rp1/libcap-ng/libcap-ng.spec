%global source0_hash e4be07fdd234f10b866433f224d183626003c65634ed0552b02e654a380244c2
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: libcap-ng
Version: 0.8.5
Release: 1%{?dist}
Summary: POSIX capabilities library
License: LGPL-2.1-or-later
URL: https://github.com/stevegrubb/libcap-ng
Source0: https://github.com/stevegrubb/libcap-ng/archive/refs/tags/v%{version}.tar.gz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: patchelf
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
%endif

%description
POSIX capabilities library

%package devel
Summary: POSIX capabilities library
Requires: libcap-ng%{?_isa} = %{version}-%{release}

%description devel
POSIX capabilities library

%prep
%oreon_sha256
%autosetup -n libcap-ng-0.8.5 -p1
./autogen.sh

%build
%oreon_configure --disable-static
%oreon_make

%install
%oreon_make_install
rm -f %{buildroot}%{_libdir}/*.la
find %{buildroot} -type f | while read -r f; do
  file -b "$f" | grep -q '^ELF' || continue
  r=$(patchelf --print-rpath "$f")
  if [ -n "$r" ]; then
    chmod u+w "$f"
    patchelf --remove-rpath "$f"
  fi
done
%oreon_filelist_devel

%files -f %{_builddir}/%{name}.files
%license COPYING.LIB

%files devel -f %{_builddir}/%{name}-devel.files
