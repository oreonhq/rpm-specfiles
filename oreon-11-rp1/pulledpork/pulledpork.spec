%global source0_hash f0149eb6f723b622024295e0ee00e1acade93fae464b9fdc323fdf15e99c388c

# Warning:
# Anyone editing this spec file please make sure the same spec file
# works on other fedora and epel releases, which are supported by this software.
# No quick Rawhide-only fixes will be allowed.

%global etcfiles disablesid.conf dropsid.conf enablesid.conf modifysid.conf pulledpork.conf

Summary:	Pulled Pork for Snort and Suricata rule management
Name:		pulledpork
Version:	0.7.4
Release:	15%{?dist}
# contrib/oink-conv.pl is GPLv2+
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		https://github.com/shirkdog/pulledpork
Source0:	https://github.com/shirkdog/pulledpork/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Prepare pulledpork.conf for Fedora/EPEL
# sed -i 's#/usr/local/etc#/etc#g' pulledpork.conf
# sed -i 's#/usr/local/lib#/usr/lib64#g' pulledpork.conf
# sed -i 's#snort_path=/usr/local/bin#snort_path=/sbin#' pulledpork.conf
# sed -i 's#snort_control=/usr/local/bin#snort_control=/bin#' pulledpork.conf
# sed -i '/rule_url.*<oinkcode>/s/^/#/' pulledpork.conf
# sed -i '/sid=/s/^# //' pulledpork.conf
# sed -i 's#sid=/etc/snort#sid=/etc/pulledpork#' pulledpork.conf
# sed -i 's#distro=.*#distro=Centos-8#' pulledpork.conf
Source1:	%{name}.conf
BuildArch:	noarch

BuildRequires:	perl-generators
%if 0%{?fedora}
BuildRequires:	perl-interpreter
%else
BuildRequires:	perl
%endif

# Used by pulledpork to download rules, without it one gets errors like
# Error 501 when fetching https://snort.org/downloads/community/community-rules.tar.gz.md5
# https://github.com/shirkdog/pulledpork/issues/221
BuildRequires:	perl(LWP::Protocol::https)
Requires:	perl(LWP::Protocol::https)
# Other dependencies
BuildRequires:	perl(LWP::UserAgent)
Requires:	perl(LWP::UserAgent)
BuildRequires:	perl(Sys::Syslog)
Requires:	perl(Sys::Syslog)
BuildRequires:	perl(Archive::Tar)
Requires:	perl(Archive::Tar)
BuildRequires:	perl(File::Copy)
Requires:	perl(File::Copy)

# handle license on el{6,7}: global must be defined after the License field above
%{!?_licensedir: %global license %doc}

%description
Pulled Pork for Snort and Suricata rule management (from Google code).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}

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

%check
./pulledpork.pl -V

%files
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/contrib
%{_datadir}/%{name}/contrib/oink-conv.pl
%{_datadir}/%{name}/contrib/README.CONTRIB
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/disablesid.conf
%config(noreplace) %{_sysconfdir}/%{name}/dropsid.conf
%config(noreplace) %{_sysconfdir}/%{name}/enablesid.conf
%config(noreplace) %{_sysconfdir}/%{name}/modifysid.conf
%config(noreplace) %{_sysconfdir}/%{name}/pulledpork.conf
%doc README.md doc/README.CATEGORIES doc/README.CHANGES doc/README.RULESET doc/README.SHAREDOBJECTS
%license LICENSE

%changelog
%autochangelog
