%global source0_hash c2f84393011827219ae117131dba8e7684c2bed0961eed11b0642c2acba440b5
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: libksba
Version: 1.8.1
Release: 1%{?dist}
Summary: X.509 and CMS library
License: (LGPL-3.0-or-later OR GPL-2.0-or-later) AND GPL-3.0-or-later
URL: https://gnupg.org/software/libksba/
Source0: https://gnupg.org/ftp/gcrypt/libksba/libksba-%{version}.tar.bz2
Source1: libksba-%{version}.tar.bz2.sig
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
Libksba handles X.509 certificates and the CMS data used by S/MIME.

%package devel
Summary: Development files for libksba
Requires: libksba%{?_isa} = %{version}-%{release}

%description devel
Headers, libraries and pkg-config files for building against libksba.

%prep
%oreon_sha256
%if %{without bootstrap} && !0%{?bootstrap}
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%endif
%autosetup -n libksba-%{version} -p1

%build
%oreon_configure --disable-static
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
%license COPYING

%files devel -f %{_builddir}/%{name}-devel.files
