%global source0_hash 69aa0cd365dba5ea7799b850a7da659ad303e6074bbd67f4ab84e4d6f5f6c3a4

Name:         liblo
Version:      0.34
Release:      3%{?dist}
Summary:      Open Sound Control library
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:      LicenseRef-Callaway-LGPLv2+
URL:          https://liblo.sourceforge.net
Source0:      https://download.sf.net/sourceforge/liblo/liblo-%{version}.tar.gz
Patch0:       %{name}-Werror.patch

BuildRequires: gcc
BuildRequires: doxygen
BuildRequires: make

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

%autosetup -p 1

%build
%configure --disable-static
# We don't want rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

%install
%make_install

# install man pages by hand
mkdir -p %{buildroot}%{_mandir}/man3/
install -m 0664 doc/man/man3/*.3 %{buildroot}%{_mandir}/man3/

# remove libtool archives
find %{buildroot} -type f -name "*.la" -delete

%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS NEWS
%{_libdir}/liblo.so.*
%{_bindir}/oscdump
%{_bindir}/oscsend
%{_bindir}/oscsendfile

%files devel
%doc doc/html examples/*.c*
%{_libdir}/liblo.so
%{_includedir}/lo
%{_libdir}/pkgconfig/liblo.pc
%{_mandir}/man3/*

%changelog
%autochangelog
