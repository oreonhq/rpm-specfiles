%global source0_hash d77f68f48879510e79a2f65977ccc68981781ea0923e5bdffac2a193ea3d660e
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: libgcrypt
Version: 1.12.4
Release: 1%{?dist}
Summary: General purpose cryptographic library
License: LGPL-2.1-or-later
URL: https://gnupg.org/software/libgcrypt/
Source0: https://gnupg.org/ftp/gcrypt/libgcrypt/libgcrypt-%{version}.tar.bz2
Source1: libgcrypt-%{version}.tar.bz2.sig
Source2: gnupg-signing-keys.asc

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gnupg2
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: libgpg-error-devel
BuildRequires: patchelf
%endif

%description
Libgcrypt is a general purpose cryptographic library based on the code
from GnuPG.

%package devel
Summary: Development files for libgcrypt
Requires: libgcrypt%{?_isa} = %{version}-%{release}

%description devel
Headers, libraries and pkg-config files for building against libgcrypt.

%prep
%oreon_sha256
%if %{without bootstrap} && !0%{?bootstrap}
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%endif
%autosetup -n libgcrypt-%{version} -p1

%build
%oreon_configure --disable-static --enable-noexecstack --disable-doc
%oreon_make

%install
%oreon_make_install
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_infodir}/dir
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
