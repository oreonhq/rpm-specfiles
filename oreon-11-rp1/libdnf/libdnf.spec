%global source0_hash 95477cc412a5980ebaa3152d5561e35826f550d91cf303d3eb7ad3dad10cb46d
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}
%global py3_sitearch %{_libdir}/python%(python3 -c 'import sys;print("%d.%d"%sys.version_info[:2])' 2>/dev/null)/site-packages

Name: libdnf
Version: 0.76.0
Release: 2%{?dist}
Summary: DNF library
License: LGPL-2.1-or-later
URL: https://github.com/rpm-software-management/libdnf
Source0: https://github.com/rpm-software-management/libdnf/archive/refs/tags/%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: glibc-devel
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: pkgconf
BuildRequires: glib2-devel
BuildRequires: json-c-devel
BuildRequires: libmodulemd-devel
BuildRequires: librepo-devel
BuildRequires: libsolv-devel
BuildRequires: rpm-devel
BuildRequires: sqlite-devel
BuildRequires: libsmartcols-devel
BuildRequires: zchunk-devel
BuildRequires: swig
BuildRequires: gettext
BuildRequires: python3-devel
BuildRequires: patchelf

%description
libdnf is the library behind dnf 4.

%package devel
Summary: DNF library
Requires: libdnf%{?_isa} = %{version}-%{release}

%description devel
libdnf is the library behind dnf 4.

%package -n python3-libdnf
Summary: Python 3 bindings for libdnf
Requires: libdnf%{?_isa} = %{version}-%{release}

%description -n python3-libdnf
Python 3 bindings for the libdnf library.

%package -n python3-hawkey
Summary: Python 3 hawkey bindings for libdnf
Requires: libdnf%{?_isa} = %{version}-%{release}
Requires: python3-libdnf%{?_isa} = %{version}-%{release}

%description -n python3-hawkey
Python 3 hawkey bindings for the libdnf library.

%prep
%oreon_sha256
%autosetup -p1

%build
%oreon_cmake \
  -DCMAKE_SKIP_RPATH=ON \
  -DWITH_ZCHUNK=ON \
  -DWITH_GTKDOC=OFF \
  -DWITH_HTML=OFF \
  -DWITH_MAN=OFF \
  -DWITH_TESTS=OFF \
  -DWITH_BINDINGS=ON \
  -DENABLE_DNF5_CONF_DROP_IN=OFF \
  -DENABLE_DNF5_CONF_REPOS_OVERRIDE=OFF
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
%find_lang libdnf

%ldconfig_scriptlets

%files -f libdnf.lang
%license COPYING
%{_libdir}/libdnf.so.2
%dir %{_libdir}/libdnf
%dir %{_libdir}/libdnf/plugins
%{_libdir}/libdnf/plugins/README

%files devel
%{_includedir}/libdnf/
%{_libdir}/libdnf.so
%{_libdir}/pkgconfig/libdnf.pc

%files -n python3-libdnf
%{py3_sitearch}/libdnf/
%{py3_sitearch}/libdnf-%{version}.dist-info/

%files -n python3-hawkey
%{py3_sitearch}/hawkey/
