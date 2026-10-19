%global source0_hash 69aa0cd365dba5ea7799b850a7da659ad303e6074bbd67f4ab84e4d6f5f6c3a4
Name:         liblo
Version:      0.34
Release:        1%{?dist}
Summary:        Open Sound Control library
License:      LicenseRef-Callaway-LGPLv2+
URL:          https://liblo.sourceforge.net
Source0:        https://download.sf.net/sourceforge/liblo/liblo-%{version}.tar.gz
Patch0:       %{name}-Werror.patch
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
liblo is an implementation of the Open Sound Control protocol for
POSIX systems developed by Steve Harris.

%package devel
Summary:  Libraries, includes, etc to develop liblo applications
Requires: liblo%{?_isa} = %{version}-%{release}
%description devel
Libraries, include files, etc you can use to develop liblo 
based Open Sound Control applications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build
%install
%make_install
mkdir -p %{buildroot}%{_mandir}/man3/
install -m 0664 doc/man/man3/*.3 %{buildroot}%{_mandir}/man3/
find %{buildroot} -type f -name "*.la" -delete
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n liblo-devel -f %{oreon_filedir}/liblo-devel.list

%changelog

%autochangelog
