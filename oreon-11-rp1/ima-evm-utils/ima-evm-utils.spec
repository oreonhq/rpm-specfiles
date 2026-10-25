%global source0_hash 9346a5ccd5ca77caf6a9d2ac0d83873c04d0372414a632126df4e7a88bedff4a
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: ima-evm-utils
Version: 1.6.2
Release: 1%{?dist}
Summary: IMA and EVM utilities
License: GPL-2.0-or-later
URL: https://github.com/linux-integrity/ima-evm-utils
Source0: https://github.com/linux-integrity/ima-evm-utils/releases/download/v%{version}/ima-evm-utils-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: patchelf
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: openssl-devel
BuildRequires: keyutils-devel
%endif

%description
IMA and EVM utilities

%package devel
Summary: IMA and EVM utilities
Requires: ima-evm-utils%{?_isa} = %{version}-%{release}

%description devel
IMA and EVM utilities

%prep
%oreon_sha256
%autosetup -n ima-evm-utils-1.6.2 -p1
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
%license COPYING

%files devel -f %{_builddir}/%{name}-devel.files
