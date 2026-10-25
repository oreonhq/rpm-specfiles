%global source0_hash df324fcd0834175dab07483133902d9774a605bfa298025f69883288fd20a8c7
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: libmicrohttpd
Version: 1.0.2
Release: 1%{?dist}
Summary: Embedded HTTP server library
License: LGPL-2.1-or-later
URL: https://www.gnu.org/software/libmicrohttpd/
Source0: https://ftp.gnu.org/gnu/libmicrohttpd/libmicrohttpd-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: patchelf
BuildRequires: gnutls-devel
%endif

%description
Embedded HTTP server library

%package devel
Summary: Embedded HTTP server library
Requires: libmicrohttpd%{?_isa} = %{version}-%{release}

%description devel
Embedded HTTP server library

%prep
%oreon_sha256
%autosetup -n libmicrohttpd-1.0.2 -p1

%build
%oreon_configure --disable-static --with-gnutls --disable-examples
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
%license COPYING

%files devel -f %{_builddir}/%{name}-devel.files
