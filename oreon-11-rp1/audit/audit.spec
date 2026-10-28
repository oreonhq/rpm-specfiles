%global source0_hash 42876d195ee2ded19e5f72d7664096eee314928aa36ad346719ba5b25818fc84
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: audit
Version: 4.2.1
Release: 1%{?dist}
Provides: audit-libs = %{version}-%{release}
Provides: audit-libs%{_isa} = %{version}-%{release}
Obsoletes: audit-libs < 4.3
Summary: Linux audit library
License: GPL-2.0-or-later
URL: https://github.com/linux-audit/audit-userspace
Source0: https://github.com/linux-audit/audit-userspace/archive/refs/tags/v%{version}.tar.gz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: patchelf
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: libcap-ng-devel
BuildRequires: openldap-devel
%endif

%description
Linux audit library

%package devel
Summary: Linux audit library
Requires: audit%{?_isa} = %{version}-%{release}

%description devel
Linux audit library

%prep
%oreon_sha256
%autosetup -n audit-userspace-%{version} -p1
autoreconf -fi

%build
%oreon_configure --disable-static --without-python3 --with-libcap-ng
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
