%global source0_hash 83b6085232d1588c379dc9b9cae47bb37407cf262e6e74993c61ba72d2a784dc
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: libseccomp
Version: 2.6.0
Release: 1%{?dist}
Summary: seccomp syscall filter library
License: LGPL-2.1-or-later
URL: https://github.com/seccomp/libseccomp
Source0: https://github.com/seccomp/libseccomp/releases/download/v%{version}/libseccomp-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: patchelf
BuildRequires: gperf
%endif

%description
seccomp syscall filter library

%package devel
Summary: seccomp syscall filter library
Requires: libseccomp%{?_isa} = %{version}-%{release}

%description devel
seccomp syscall filter library

%prep
%oreon_sha256
%autosetup -n libseccomp-2.6.0 -p1

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
%license LICENSE

%files devel -f %{_builddir}/%{name}-devel.files
