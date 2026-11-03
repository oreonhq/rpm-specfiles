%global source0_hash ce7ebdc9789ae51f3e7d26b5408de7395ddea0950d5d73568ed9565f5fae4d4c
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}
%global py3_sitearch %{_libdir}/python%(python3 -c 'import sys;print("%d.%d"%sys.version_info[:2])' 2>/dev/null)/site-packages

Name: librepo
Version: 1.22.0
Release: 2%{?dist}
Summary: Repodata download library
License: LGPL-2.1-or-later
URL: https://github.com/rpm-software-management/librepo
Source0: https://github.com/rpm-software-management/librepo/archive/refs/tags/%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: pkgconf
BuildRequires: glib2-devel
BuildRequires: openssl-devel
BuildRequires: libxml2-devel
BuildRequires: libcurl-devel
BuildRequires: gpgme-devel
BuildRequires: libselinux-devel
BuildRequires: zchunk-devel
BuildRequires: python3-devel
BuildRequires: patchelf

%description
librepo downloads repodata and packages.

%package devel
Summary: Repodata download library
Requires: librepo%{?_isa} = %{version}-%{release}

%description devel
librepo downloads repodata and packages.

%package -n python3-librepo
Summary: Python 3 bindings for librepo
Requires: librepo%{?_isa} = %{version}-%{release}

%description -n python3-librepo
Python 3 bindings for the librepo library.

%prep
%oreon_sha256
%autosetup -p1

%build
%oreon_cmake \
  -DCMAKE_SKIP_RPATH=ON \
  -DENABLE_TESTS=OFF \
  -DENABLE_DOCS=OFF \
  -DENABLE_EXAMPLES=OFF \
  -DWITH_ZCHUNK=ON \
  -DUSE_GPGME=ON \
  -DENABLE_SELINUX=ON \
  -DENABLE_PYTHON=ON
%oreon_cmake_build

%install
%oreon_cmake_install
rm -f %{buildroot}%{_libdir}/*.a
find %{buildroot} -type f | while read -r f; do
  file -b "$f" | grep -q '^ELF' || continue
  r=$(patchelf --print-rpath "$f")
  if [ -n "$r" ]; then
    chmod u+w "$f"
    patchelf --remove-rpath "$f"
  fi
done

%ldconfig_scriptlets

%files
%license COPYING
%{_libdir}/librepo.so.0

%files devel
%{_includedir}/librepo/
%{_libdir}/librepo.so
%{_libdir}/pkgconfig/librepo.pc

%files -n python3-librepo
%{py3_sitearch}/librepo/
