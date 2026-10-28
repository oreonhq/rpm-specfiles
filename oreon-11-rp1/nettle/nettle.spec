%global source0_hash b0fcdd7fc0cdea6e80dcf1dd85ba794af0d5b4a57e26397eee3bc193272d9132
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: nettle
Version: 3.10.1
Release: 1%{?dist}
Summary: Low-level cryptographic library
License: LGPL-3.0-or-later
URL: https://www.lysator.liu.se/~nisse/nettle/
Source0: https://ftp.gnu.org/gnu/nettle/nettle-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: m4
BuildRequires: patchelf
BuildRequires: gmp-devel
%endif

%description
Low-level cryptographic library

%package devel
Summary: Low-level cryptographic library
Requires: nettle%{?_isa} = %{version}-%{release}

%description devel
Low-level cryptographic library

%prep
%oreon_sha256
%autosetup -n nettle-3.10.1 -p1

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
%license COPYING.LESSERv3

%files devel -f %{_builddir}/%{name}-devel.files
