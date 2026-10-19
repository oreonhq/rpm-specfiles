%global source0_hash f7575326a4d01366cf9aa53f0d453a7ec94d68e12b88f7586b7fa34e805594ff
%global plugin check_openmanage
%global debug_package %{nil}
Name:          nagios-plugins-openmanage
Version:       3.7.12
Release:        1%{?dist}
Summary:        Nagios plugin to monitor hardware health on Dell servers
License:       GPL-3.0-or-later
URL:           http://folk.uio.no/trondham/software/%{plugin}.html
Source0:        http://folk.uio.no/trondham/software/files/%{plugin}-%{version}.tar.gz
Requires:      perl(Config::Tiny)
Requires:      perl(Net::SNMP)
Requires: nagios-common
Provides:      nagios-plugins-check-openmanage = %{version}-%{release}
Obsoletes:     nagios-plugins-check-openmanage < 3.7.2-3
# oreon:deps
BuildRequires:  docbook-style-xsl
BuildRequires:  libxml2
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  perl-generators
# /oreon:deps
%description
check_openmanage is a plugin for Nagios which checks the hardware
health of Dell servers running OpenManage Server Administrator
(OMSA). The plugin can be used remotely with SNMP or locally with
NRPE, check_by_ssh or similar, whichever suits your needs and
particular taste. The plugin checks the health of the storage
subsystem, power supplies, memory modules, temperature probes etc.,
and gives an alert if any of the components are faulty or operate
outside normal parameters.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{plugin}-%{version}
rm -f %{plugin}.exe

%build

pushd man
make clean && make
popd
%install
install -Dp -m 0755 %{plugin} %{buildroot}%{_libdir}/nagios/plugins/%{plugin}
install -Dp -m 0644 man/%{plugin}.8 %{buildroot}%{_mandir}/man8/%{plugin}.8
install -Dp -m 0644 man/%{plugin}.conf.5 %{buildroot}%{_mandir}/man5/%{plugin}.conf.5
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
