%global source0_hash f0149eb6f723b622024295e0ee00e1acade93fae464b9fdc323fdf15e99c388c
%global etcfiles disablesid.conf dropsid.conf enablesid.conf modifysid.conf pulledpork.conf
Summary:        Pulled Pork for Snort and Suricata rule management
Name:		pulledpork
Version:	0.7.4
Release:        1%{?dist}
License:	GPL-2.0-or-later
URL:		https://github.com/shirkdog/pulledpork
Source0:        https://github.com/shirkdog/pulledpork/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:	%{name}.conf
BuildArch:	noarch
Requires:	perl(LWP::Protocol::https)
Requires:	perl(LWP::UserAgent)
Requires:	perl(Sys::Syslog)
Requires:	perl(Archive::Tar)
Requires:	perl(File::Copy)
%{!?_licensedir: %global license %doc}
# oreon:deps
BuildRequires:  perl
BuildRequires:  perl(Archive::Tar)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(LWP::Protocol::https)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Sys::Syslog)
BuildRequires:  perl-generators
# /oreon:deps
%description
Pulled Pork for Snort and Suricata rule management (from Google code).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%install
%{__install} -d -m 0755 $RPM_BUILD_ROOT/%{_bindir}
%{__install} -d -m 0755 $RPM_BUILD_ROOT/%{_datadir}/%{name}
%{__install} -d -m 0755 $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}
%{__install} -m 0755 %{name}.pl $RPM_BUILD_ROOT/%{_bindir}/%{name}
%{__sed} -i 's|#!/usr/bin/env perl|#!/usr/bin/perl -w|' $RPM_BUILD_ROOT/%{_bindir}/%{name}
%{__cp} -rp contrib $RPM_BUILD_ROOT/%{_datadir}/%{name}
%{__chmod} 0755 $RPM_BUILD_ROOT/%{_datadir}/%{name}/contrib/oink-conv.pl
cd etc
%{__rm} -f pulledpork.conf
%{__cp} %{SOURCE1} .
for file in disablesid.conf dropsid.conf enablesid.conf modifysid.conf pulledpork.conf; do
    %{__install} -m 0664 $file $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}
done
%oreon_autofiles main

%check

./pulledpork.pl -V
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
