%global source0_hash 8ec730cce33daed24b3b09296f77c91f29cd34b49905daeff0bd86556549c6aa
Name:           onesixtyone
Version:        0.3.4
Release:        1%{?dist}
Summary:        Fast SNMP scanner
%global         gituser trailofbits
%global         gitname onesixtyone 
License:        GPL-2.0-or-later
URL:            https://github.com/trailofbits/onesixtyone/
VCS:            https://github.com/trailofbits/onesixtyone/
Source0:        https://github.com/%{gituser}/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         https://github.com/trailofbits/onesixtyone/pull/28.patch#/onesixtyone-makeinstall.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
onesixtyone takes a different approach to SNMP scanning. It takes advantage of
the fact that SNMP is a connection-less protocol and sends all SNMP requests
as fast as it can. Then the scanner waits for responses to come back and logs
them, in a fashion similar to Nmap ping sweeps.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%set_build_flags
%make_build
%install
%set_build_flags
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
