%global source0_hash f557911bf6171621e1f72ff35f5b1825bb35b52ed45325dcdee931e5d3c0787a
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: libidn2
Version: 2.3.8
Release: 1%{?dist}
Summary: Internationalized domain name library
License: GPL-3.0-or-later AND LGPL-3.0-or-later
URL: https://www.gnu.org/software/libidn/
Source0: https://ftp.gnu.org/gnu/libidn/libidn2-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: patchelf
BuildRequires: libunistring-devel
%endif

%description
Internationalized domain name library

%package devel
Summary: Internationalized domain name library
Requires: libidn2%{?_isa} = %{version}-%{release}

%description devel
Internationalized domain name library

%prep
%oreon_sha256
%autosetup -n libidn2-2.3.8 -p1

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
