%global source0_hash 821ab0695c842eab51752a81980c92b0410c7eadd04103f791d5d2a526784966
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: gpgme
Version: 2.0.1
Release: 1%{?dist}
Summary: GnuPG library
License: LGPL-2.1-or-later
URL: https://gnupg.org/software/gpgme/
Source0: https://www.gnupg.org/ftp/gcrypt/gpgme/gpgme-%{version}.tar.bz2

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: patchelf
BuildRequires: libassuan-devel
BuildRequires: libgpg-error-devel
%endif

%description
GnuPG library

%package devel
Summary: GnuPG library
Requires: gpgme%{?_isa} = %{version}-%{release}

%description devel
GnuPG library

%prep
%oreon_sha256
%autosetup -n gpgme-2.0.1 -p1

%build
%oreon_configure --disable-static --disable-gpg-test --disable-gpgsm-test --disable-g13-test
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
%license COPYING.LESSER

%files devel -f %{_builddir}/%{name}-devel.files
