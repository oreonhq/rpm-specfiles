%global source0_hash 4e002a2a619d592f7c9b9d284381ffc004d8a71c38945aa95d5d53f2e4c0c8cf
Name: schedtool       
Version:  1.3.0   
Release:        1%{?dist}
Summary:        Tool to query or alter process scheduling policy
License:  GPL-2.0-only      
URL: http://freequaos.host.sk/schedtool/           
Source0:        http://freequaos.host.sk/schedtool/%{name}-%{version}.tar.bz2
Patch0: schedtool-c99.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
Schedtool interfaces with the Linux CPU scheduler. It allows the user to set 
and query the CPU-affinity and nice-levels of processes, as well as all 
scheduling policies, like batch or real-time (RR/FIFO) classes and 
their priorities

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

make CFLAGS="%{optflags}" %{?_smp_mflags} 
%install
rm -rf $RPM_BUILD_ROOT
make install RELEASE="%{name}" DESTPREFIX=%{_prefix} DESTDIR=$RPM_BUILD_ROOT
chmod -x $RPM_BUILD_ROOT%{_mandir}/man8/schedtool.8.gz
cp -p CHANGES TODO TUNING $RPM_BUILD_ROOT%{_docdir}/%{name}/
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/INSTALL
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
