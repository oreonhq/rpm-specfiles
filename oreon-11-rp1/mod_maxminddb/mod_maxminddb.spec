%global source0_hash 877d3a36fa4bbcf807468c00b8cfedd7e16fa4039c5d465b5490bbdb243ad5cd
%{!?_httpd_mmn: %global _httpd_mmn %(cat %{_includedir}/httpd/.mmn 2> /dev/null || echo 0-0)}
Summary:        Module for the Apache web server to query MaxMind DB files
Name:           mod_maxminddb
Version:        1.3.0
Release:        3%{?dist}
License:        Apache-2.0
URL:            https://maxmind.github.io/mod_maxminddb/
Source0:        https://github.com/maxmind/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        10-maxminddb.conf
Source2:        maxminddb.conf
Requires:       httpd-mmn = %{_httpd_mmn}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  httpd-devel
BuildRequires:  libmaxminddb-devel
# /oreon:deps
%description
The mod_maxminddb allows to query MaxMind DB files from the Apache web
server using the libmaxminddb library. The MaxMind DB files are provided
as free GeoLite2 databases as well as commercial GeoIP2 databases.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%{_httpd_apxs} -lmaxminddb -c src/%{name}.c  # Avoid faulty upstream Makefile
%install
install -D -p -m 0755 src/.libs/%{name}.so $RPM_BUILD_ROOT%{_httpd_moddir}/%{name}.so
install -D -p -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_httpd_modconfdir}/10-maxminddb.conf
install -D -p -m 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_httpd_confdir}/maxminddb.conf
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
