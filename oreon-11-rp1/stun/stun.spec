%global source0_hash 83e1bf9c21399244c5e8ad19789121a3537399d6523a887a5abc6187adcdb1d7
%define	download_name	stund
Name:		stun
Version:	0.97    
Release:        1%{?dist}
Summary:        Implements a simple Stun Client
License:	VSL-1.0
URL:		http://sourceforge.net/projects/%{name}
Source0:        http://downloads.sourceforge.net/%{name}/%{download_name}-%{version}.tgz
Patch0:		patch0.diff
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
%description
Implements a simple STUN client on Windows, Linux, and Solaris. 
The STUN protocol (Simple Traversal of UDP through NATs) is described in the 
IETF RFC 3489, available at http://www.ietf.org/rfc/rfc3489.txt

%package server
Summary:	Implements the Stun Server
%description server
Implements a simple STUN client on Windows, Linux, and Solaris.           
The STUN protocol (Simple Traversal of UDP through NATs) is described in the
IETF RFC 3489, available at http://www.ietf.org/rfc/rfc3489.txt

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q  -n %{download_name}
%patch -P0 -p0

%build

make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_sbindir}
install   client $RPM_BUILD_ROOT%{_bindir}/stun-client
install   server $RPM_BUILD_ROOT%{_sbindir}/stun-server
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n stun-server -f %{oreon_filedir}/stun-server.list

%changelog

%autochangelog
