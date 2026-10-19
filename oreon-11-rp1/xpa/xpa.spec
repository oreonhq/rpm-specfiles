%global source0_hash 854af367c0f4ffe7a65cb4da854a624e20af3c529f88187b50b22b68f024786a
%{!?tcl_version: %global tcl_version %(echo 'puts $tcl_version' | tclsh)}
%{!?tcl_sitearch: %global tcl_sitearch %{_libdir}/tcl%{tcl_version}}
Name: xpa
Version: 2.1.20
Release:        1%{?dist}
Summary:        The X Public Access messaging system
License: MIT
URL: http://hea-www.harvard.edu/RD/xpa/
Source0:        https://github.com/ericmandel/xpa/archive/%{version}/%{name}-%{version}.tar.gz
Patch0: xpa-makefile.patch
Patch1: xpa-configure-c99.patch
Requires: tcl(abi) = 8.6
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libXt-devel
BuildRequires:  make
BuildRequires:  tcl8-devel
# /oreon:deps
%description
The XPA messaging system provides seamless communication between many kinds 
of Unix programs, including X programs and Tcl/Tk programs. 
It also provides an easy way for users to communicate with these 
XPA-enabled programs by executing XPA client commands in the shell or by 
utilizing such commands in scripts.
This package contains command-line utilities for managing XPA.

%package devel
Summary: Headers for developing programs that will use %{name}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: %{name}-tcl%{?_isa} = %{version}-%{release}
%description devel
These are the header files and libraries needed to develop a %{name} 
application.

%package libs
Summary: The XPA messaging system runtime libraries
%description libs
The XPA messaging system provides seamless communication between many kinds 
of Unix programs, including X programs and Tcl/Tk programs. 
This package contains the %{name} run-time library

%package tcl
Summary: The XPA messaging system TCL interface
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Provides: tcl-xpa = %{version}-%{release}
%description tcl
The XPA messaging system provides seamless communication between many kinds 
of Unix programs, including X programs and Tcl/Tk programs. 
This package contains the %{name} TCL interface

%package doc
Summary: Documentation for %{name}
BuildArch: noarch
%description doc
This package contains the documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}
# Remove ps files in html docs
rm -rf %{_builddir}/%{name}-%{version}/doc/*.ps

%build

%configure --includedir=%{_includedir}/xpa --datadir=%{_datadir}/xpa \
	--enable-shared --with-tcl=%{_libdir} \
	--with-x --enable-threaded-xpans
make 
make tclxpa
%install
make INSTALL_ROOT=%{buildroot} install
mkdir -p %{buildroot}%{tcl_sitearch}/tclxpa
cp -a pkgIndex.tcl %{buildroot}%{tcl_sitearch}/tclxpa
mv %{buildroot}%{_libdir}/libtcl* %{buildroot}%{tcl_sitearch}/tclxpa
%ldconfig_scriptlets libs
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n xpa-devel -f %{oreon_filedir}/xpa-devel.list
%files -n xpa-libs -f %{oreon_filedir}/xpa-libs.list
%files -n xpa-tcl -f %{oreon_filedir}/xpa-tcl.list
%files -n xpa-doc -f %{oreon_filedir}/xpa-doc.list

%changelog

%autochangelog
