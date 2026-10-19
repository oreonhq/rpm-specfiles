%global source0_hash 67d663740c0c84b7069c805048e7c5a0c50f818d173dba514a8e68c5bbc6b4a1
%global plugin check_linux_bonding
%global debug_package %{nil}
Name:          nagios-plugins-bonding
Version:       1.4
Release:        1%{?dist}
Summary:        Nagios plugin to monitor Linux bonding interfaces
License:       GPL-3.0-or-later
URL:           http://folk.uio.no/trondham/software/%{plugin}.html
Source0:        http://folk.uio.no/trondham/software/files/%{plugin}-%{version}.tar.gz
Requires: nagios-plugins
Provides:      check_linux_bonding = %{version}-%{release}
Obsoletes:     check_linux_bonding < 1.3.2
# oreon:deps
BuildRequires:  docbook-style-xsl
BuildRequires:  libxml2
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  perl-generators
# /oreon:deps
%description
This package contains check_linux_bonding, which is a plugin for
Nagios that checks bonding network interfaces on Linux. The plugin
will report any interfaces that are down (both masters and slaves), as
well as other aspects which may point to a problem with bonded
interfaces.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{plugin}-%{version}

%build

: # use pre-built man-pages on old systems
%install
rm -rf %{buildroot}
install -Dp -m 0755 %{plugin} %{buildroot}%{_libdir}/nagios/plugins/%{plugin}
install -Dp -m 0644 man/%{plugin}.8 %{buildroot}%{_mandir}/man8/%{plugin}.8
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
