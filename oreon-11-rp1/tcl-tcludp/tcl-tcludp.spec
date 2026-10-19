%global source0_hash a8a29d55a718eb90aada643841b3e0715216d27cea2e2df243e184edb780aa9d
%{!?tcl_version: %global tcl_version %(echo 'puts $tcl_version' | tclsh)}
%{!?tcl_sitearch: %global tcl_sitearch %{_libdir}/tcl%{tcl_version}}
%global realname tcludp
Name:		tcl-%{realname}
Version:	1.0.11
Release:        1%{?dist}
Summary:        Tcl extension for UDP support
License:	MIT
URL:		http://sourceforge.net/projects/tcludp
Source0:        http://downloads.sourceforge.net/%{realname}/%{realname}-%{version}.tar.gz
Provides:	tcl-udp = %{version}-%{release}
Provides:	%{realname} = %{version}-%{release}
Requires:	tcl(abi) = 8.6
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  tcl-devel
BuildRequires:  tk-devel
# /oreon:deps
%description
The Tcl UDP extension provides a simple library to support UDP socket in Tcl.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{realname}

%build

%configure
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
install -d %{buildroot}%{tcl_sitearch}
mv %{buildroot}%{_libdir}/udp%{version} %{buildroot}%{tcl_sitearch}/udp%{version}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
