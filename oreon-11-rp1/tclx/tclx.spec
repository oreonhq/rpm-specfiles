%global source0_hash 257591f9dffc21cf3ed541a9ef81a3ff5dd739dff5cebb70c4cec7010e2def66
%bcond_without wcheck
%{!?tcl_version: %global tcl_version %(echo 'puts $tcl_version' | tclsh8)}
%{!?tcl_sitearch: %global tcl_sitearch %{_libdir}/tcl%{tcl_version}}
%define major_ver 8.4
%define upversion 8.5
Summary:        Extensions for Tcl and Tk
Name: tclx
Version: %{major_ver}.0
Release:        1%{?dist}
License: LicenseRef-Callaway-BSD
URL: http://tclx.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}%{major_ver}.tar.bz2
Requires: tcl8%{?_isa}
Requires: tk8%{?_isa}
Patch: tclx-%{major_ver}-varinit.patch
Patch: tclx-%{major_ver}-relid.patch
Patch: tclx-%{major_ver}-man.patch
Patch: tclx-%{major_ver}-tcl86.patch
Patch: tclx-configure-c99.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  tcl-devel
BuildRequires:  tk-devel
# /oreon:deps
%description
Extended Tcl (TclX) is a set of extensions to the Tcl programming language.
Extended Tcl is oriented towards system programming tasks and large
application development. TclX provides additional interfaces to the
operating system, and adds many new programming constructs, text manipulation
and debugging tools.

%package devel
Summary: Extended Tcl development files
Requires: tclx = %{version}-%{release}
%description devel
This package contains the tclx development files needed for building
applications embedding tclx.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n tclx%{major_ver}

# patch2 touches tcl.m4

%build

export CFLAGS="%{build_cflags} -std=gnu17"
%configure \
   --enable-tk=YES \
   --with-tclconfig=%{_libdir} \
   --with-tkconfig=%{_libdir} \
   --with-tclinclude=%{_includedir} \
   --with-tkinclude=%{_includedir} \
   --enable-gcc \
   --disable-threads \
   --enable-64bit \
   --libdir=%{tcl_sitearch}
%make_build
%check

%if %{without wcheck}
   make test
%endif
%install
%make_install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/ld.so.conf.d/
echo '%{_libdir}/tcl%{tcl_version}/%{name}%{major_ver}' > $RPM_BUILD_ROOT%{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n tclx-devel -f %{oreon_filedir}/tclx-devel.list

%changelog

%autochangelog
