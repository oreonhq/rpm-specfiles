%global source0_hash 35db93f681317942f31dfa0bddea01a464b1d83ada22db7707a1919ba780f091

%{!?tcl_version: %global tcl_version %(echo 'puts $tcl_version' | tclsh)}
%{!?tcl_sitearch: %global tcl_sitearch %{_libdir}/tcl%{tcl_version}}

Name:           tcl-thread
Version:        2.8.8
Release:        9%{?dist}
Summary:        Tcl Thread extension
License:        TCL
URL:            http://tcl.sourceforge.net
Source0:        http://prdownloads.sourceforge.net/tcl/thread%{version}.tar.gz
Patch0:         tcl-thread-x86_64-build.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  tcl-devel < 1:9
BuildRequires:  tk-devel < 1:9
BuildRequires:  gdbm-devel
Requires:       tcl(abi) = 8.6

%description
Thread extension for the Tcl toolkit.  You can use this extension to gain
script level access to Tcl threading capabilities.

%package        devel
Summary:        Include files and mandatory libraries for development
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Include files and mandatory libraries for development.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0 -n thread%{version}

%build
%configure --with-gdbm --enable-64bit
%make_build

%install
%make_install
mkdir -p %{buildroot}%{tcl_sitearch}
mv %{buildroot}%{_libdir}/thread%{version} %{buildroot}%{tcl_sitearch}/
chmod 755 %{buildroot}%{tcl_sitearch}/thread%{version}/libthread%{version}.so

%files
%doc README ChangeLog
%license license.terms
%{tcl_sitearch}/thread%{version}
%{_mandir}/mann/*

%files devel
%{_includedir}/tclThread.h

%changelog
%autochangelog
