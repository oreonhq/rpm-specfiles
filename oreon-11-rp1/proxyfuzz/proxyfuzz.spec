%global source0_hash none
Name:		proxyfuzz	
Version:	20190404
Release:        30%{?dist}
Summary:        Man-in-the-middle non-deterministic network fuzzer
License:	GPL-3.0-or-later
URL:		https://github.com/SECFORCE
Source0:        proxyfuzz.py
Source1:	README-Fedora
BuildArch:	noarch
Requires:	python3-twisted
%if 0%{?with_python3}
%endif # if with_python3
# oreon:deps
BuildRequires:  python3-devel
# /oreon:deps
%description
ProxyFuzz is a man-in-the-middle non-deterministic network fuzzier written in
Python. ProxyFuzz randomly changes (fuzzes) contents on the network traffic.
It supports TCP and UDP protocols and can also be configured to fuzz only one
side of the communication. ProxyFuzz is protocol agnostic so it can randomly
fuzz any network communication.

%prep

cp -p %{SOURCE0} .
cp -p %{SOURCE1} .
#%patch0 -p1 -b .make-executable

%build

%install
rm -rf $RPM_BUILD_ROOT
install -m 755 -p -d ${RPM_BUILD_ROOT}/%{_sbindir}
install -m 755 -p proxyfuzz.py ${RPM_BUILD_ROOT}/%{_sbindir}/proxyfuzz
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
