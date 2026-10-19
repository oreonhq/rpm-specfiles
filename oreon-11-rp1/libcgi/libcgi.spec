%global source0_hash 861df39cc0195d43419c4c3de8dff4f42478db66c9ba0b0c1e994c99400e130c
%global static  0
%{?_with_static:%global static 1}
%global libcgi_somajor 1
%global libcgi_sominor 0
Name:           libcgi
Version:        1.0
Release:        1%{?dist}
Summary:        CGI easy as C
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://libcgi.sourceforge.net/
Source0:        http://prdownloads.sourceforge.net/libcgi/libcgi-%{version}.tar.gz
Patch0:         libcgi-1.0-Makefile.in.patch
Patch1:         libcgi-1.0-cgi.c-hextable.patch
Patch2:         libcgi-1.0-string.c-make_string.patch
Patch3:         libcgi-configure-c99.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
LibCGI is a library written from scratch to easily make CGI applications in C.

%package devel
Summary:        Header files and libraries for LibCGI development
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
The libcgi-devel package contains the header files and libraries needed
to develop programs that use the LibCGI library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
find examples/ -name "Makefile.am" -delete

%build

%configure
make SOMAJOR=%{libcgi_somajor} \
     SOMINOR=%{libcgi_sominor} \
     %{?_smp_mflags}
%install
make SOMAJOR=%{libcgi_somajor} \
     SOMINOR=%{libcgi_sominor} \
     DESTDIR=$RPM_BUILD_ROOT \
     LIBDIR=%{_libdir} \
     INCDIR=%{_includedir}/%{name} \
     install
make DESTDIR=$RPM_BUILD_ROOT install_man
%if ! %{static}
rm -f $RPM_BUILD_ROOT%{_libdir}/libcgi.a
%endif
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libcgi-devel -f %{oreon_filedir}/libcgi-devel.list

%changelog

%autochangelog
