%global source0_hash 92e0e3bd4c02d4aeee76036b2ddd83f0c732ba4cda5cb71d583272b23587a76c
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: libtasn1
Version: 4.20.0
Release: 1%{?dist}
Summary: ASN.1 library
License: LGPL-2.1-or-later
URL: https://www.gnu.org/software/libtasn1/
Source0: https://ftp.gnu.org/gnu/libtasn1/libtasn1-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: patchelf
%endif

%description
ASN.1 library

%package devel
Summary: ASN.1 library
Requires: libtasn1%{?_isa} = %{version}-%{release}

%description devel
ASN.1 library

%prep
%oreon_sha256
%autosetup -n libtasn1-4.20.0 -p1

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
%license COPYING.LESSERv2

%files devel -f %{_builddir}/%{name}-devel.files
