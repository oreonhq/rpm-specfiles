%global source0_hash 945ba620a57349fe9a5c62f3173d605b6489cbeb4c3a766870972436d3afd5c9

%global nagios_plugins_dir %{_libdir}/nagios/plugins

Name:           nagios-plugins-snmp-disk-proc
Version:        1.3.1
Release:        27%{?dist}
Summary:        Nagios SNMP plugins to monitor remote disk and processes
# Version intent from README
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            https://github.com/glensc/nagios-snmp-plugins/
Source0:        https://github.com/glensc/nagios-snmp-plugins/releases/download/%{version}/nagios-snmp-plugins-%{version}.tar.gz
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  autoconf, automake
BuildRequires:  net-snmp-devel
BuildRequires:  openssl-devel
# BuildRequires:  tcp_wrappers-devel
Requires:       nagios-plugins
Provides:	nagios-snmp-plugins = %{version}-%{release}

%description
These plugins allow you to monitor disk space and running processes on
a remote machine via SNMP.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n nagios-snmp-plugins-%{version}

%build
touch ChangeLog
aclocal
autoheader
automake --add-missing
autoconf
%configure
make %{?_smp_mflags}

%install
install -d -m 755 $RPM_BUILD_ROOT/%{nagios_plugins_dir}
install -p -m 755 check_snmp_disk $RPM_BUILD_ROOT/%{nagios_plugins_dir}
install -p -m 755 check_snmp_proc $RPM_BUILD_ROOT/%{nagios_plugins_dir}

%files
%doc README COPYING AUTHORS NEWS
%{nagios_plugins_dir}/check_snmp_disk
%{nagios_plugins_dir}/check_snmp_proc

%changelog
%autochangelog
