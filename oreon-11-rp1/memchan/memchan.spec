%global source0_hash adaa5952fe532a917372dcdbc873c082656c49b613d92b09e7938d8f276f2749
%{!?tcl_version: %global tcl_version %(echo 'puts $tcl_version' | tclsh8)}
%{!?tcl_sitearch: %global tcl_sitearch %{_libdir}/tcl%{tcl_version}}
Name:           memchan
Version:        2.3
Release:        35%{?dist}
Summary:        In-memory channels for Tcl
License:        LicenseRef-Callaway-MIT AND LicenseRef-Callaway-Public-Domain
URL:            http://memchan.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/Memchan%{version}.tar.gz
Patch0:         memchan-2.3-c23.patch
Requires:       tcl(abi) = 8.6
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  tcl8-devel
BuildRequires:  tcl8-tcllib
# /oreon:deps
%description
Memchan is an extension library to the script language Tcl, as created by John
Ousterhout. It provides several new channel types for in-memory channels and
the appropriate commands for their creation.

%package devel
Summary: Development files for compiling against the Tcl memchan extension
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Development files for compiling against the Tcl memchan extension

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Memchan%{version}
%patch -P0 -p1 -b .c23

%build

%configure --enable-threads --libdir=%{tcl_sitearch}
make %{?_smp_mflags}
%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_mandir}/mann/random.n
chmod -x %{buildroot}%{tcl_sitearch}/Memchan%{version}/*.a
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n memchan-devel -f %{oreon_filedir}/memchan-devel.list

%changelog

%autochangelog
