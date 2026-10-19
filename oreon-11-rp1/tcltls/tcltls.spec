%global source0_hash e84e2b7a275ec82c4aaa9d1b1f9786dbe4358c815e917539ffe7f667ff4bc3b4
%{!?tcl_version: %global tcl_version %((echo '8.5'; echo 'puts $tcl_version' | tclsh 2>/dev/null) | tail -1)}
%{!?tcl_sitearch: %global tcl_sitearch %{_libdir}/tcl%{tcl_version}}
Name:           tcltls
Version:        2.0b2
Release:        1%{?dist}
Summary:        OpenSSL extension for Tcl
License:        LicenseRef-Callaway-BSD
URL:            https://core.tcl.tk/tcltls/home
Source0:        https://core.tcl.tk/tcltls/uv/%{name}-%{version}.tar.gz
Patch0:         tcltls-1.7.21-cipher-tests.patch
Patch1:         tcltls-1.7.21-hostname-tests.patch
Patch2:         tcltls-1.7.22-cert-tests.patch
Patch3:         tcltls-1.7.22-fall-through.patch
Patch4:         tcltls-1.7.22-openssl3.patch
Patch5:         tcltls-1.7.22-tcl-9_0.patch
Patch6:         tcltls-1.7.22-tcl-9_0_second.patch
Patch7:         tcltls-1.7.22-tcl-9_0_third.patch
Requires:       tcl(abi) = %{tcl_version}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openssl11-devel
BuildRequires:  tcl-devel
# /oreon:deps
%description
A TLS OpenSSL extension for Tcl

%package devel
Summary:        Header files for the OpenSSL extension for Tcl
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
The TLS OpenSSL extension to Tcl

This package contains the development files for tls.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Disable strip via objcopy(1) to achieve -debuginfo
sed -e 's/-@\(WEAKEN\|REMOVE\)SYMS@/:/' -i Makefile.in

# Build against OpenSSL 1.1 on RHEL 7 (for TLSv1.3 support)

%build

%configure --disable-rpath --with-ssl-dir=%{_prefix}
%make_build
%check

make test
%install
%make_install libdir=%{tcl_sitearch}
%{__install} -D -p -m 0644 tls.h %{buildroot}%{_includedir}/tls.h
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n tcltls-devel -f %{oreon_filedir}/tcltls-devel.list

%changelog

%autochangelog
