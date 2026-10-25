%global source0_hash 95b178148863f07d45df0cea67e880a79b9ef71f5d230baddc0071128516ef78
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: libgpg-error
Version: 1.55
Release: 1%{?dist}
Summary: Common error values for GnuPG components
License: LGPL-2.1-or-later
URL: https://gnupg.org/software/libgpg-error/
Source0: https://www.gnupg.org/ftp/gcrypt/libgpg-error/libgpg-error-%{version}.tar.bz2

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: patchelf%endif

%description
Common error values for GnuPG components

%package devel
Summary: Common error values for GnuPG components
Requires: libgpg-error%{?_isa} = %{version}-%{release}

%description devel
Common error values for GnuPG components

%prep
%oreon_sha256
%autosetup -n libgpg-error-1.55 -p1

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
