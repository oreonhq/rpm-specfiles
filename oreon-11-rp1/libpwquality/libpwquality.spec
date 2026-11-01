%global source0_hash 6fcf18b75d305d99d04d2e42982ed5b787a081af2842220ed63287a2d6a10988
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: libpwquality
Version: 1.4.5
Release: 1%{?dist}
Summary: Password quality checking library
License: BSD-3-Clause OR GPL-2.0-or-later
URL: https://github.com/libpwquality/libpwquality
Source0: https://github.com/libpwquality/libpwquality/releases/download/libpwquality-%{version}/libpwquality-%{version}.tar.bz2
Requires: cracklib

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: patchelf
BuildRequires: cracklib-devel
BuildRequires: pam-devel
BuildRequires: gettext

%description
libpwquality checks password strength and generates random passwords. It
ships a PAM module (pam_pwquality).

%package devel
Summary: Development files for libpwquality
Requires: libpwquality%{?_isa} = %{version}-%{release}
Provides: pkgconfig(pwquality)

%description devel
Headers and libraries for developing against libpwquality.

%prep
%oreon_sha256
%autosetup -n libpwquality-%{version} -p1

%build
%oreon_configure --disable-static --disable-python-bindings --with-securedir=%{_libdir}/security
%oreon_make

%install
%oreon_make_install
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_infodir}/dir
find %{buildroot} -type f | while read -r f; do
  file -b "$f" | grep -q '^ELF' || continue
  r=$(patchelf --print-rpath "$f" 2>/dev/null || true)
  if [ -n "$r" ]; then
    chmod u+w "$f"
    patchelf --remove-rpath "$f"
  fi
done
%oreon_filelist_devel

%files -f %{_builddir}/%{name}.files
%license COPYING

%files devel -f %{_builddir}/%{name}-devel.files
