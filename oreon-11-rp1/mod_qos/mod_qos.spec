%global source0_hash f317bf01e4f459e1e2d4949e2578ad0d5cd97744ae79fd65522ce7df83b543fc

%{!?_httpd_apxs: %{expand: %%global _httpd_apxs %%{_sbindir}/apxs}}
%{!?_httpd_mmn: %{expand: %%global _httpd_mmn %%(cat %{_includedir}/httpd/.mmn 2>/dev/null || echo 0-0)}}
# /etc/httpd/conf.d with httpd < 2.4 and defined as /etc/httpd/conf.modules.d with httpd >= 2.4
%{!?_httpd_modconfdir: %{expand: %%global _httpd_modconfdir %%{_sysconfdir}/httpd/conf.d}}

Name:           mod_qos
Version:        11.76
Release:        2%{?dist}
Summary:        Quality of service module for Apache

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://opensource.adnovum.ch/mod_qos/
Source0:        http://downloads.sourceforge.net/project/mod-qos/%{name}-%{version}.tar.gz
Source1:        10-mod_qos.conf

BuildRequires: automake
BuildRequires: gcc
BuildRequires: httpd-devel
BuildRequires: libpng-devel
BuildRequires: make
BuildRequires: openssl-devel
BuildRequires: pcre2-devel

Requires: httpd-mmn = %{_httpd_mmn}

%description
The mod_qos module may be used to determine which requests should be served and 
which shouldn't in order to avoid resource over-subscription. The module 
collects different attributes such as the request URL, HTTP request and response
headers, the IP source address, the HTTP response code, history data (based on 
user session and source IP address), the number of concurrent requests to the 
server (total or requests having similar attributes), the number of concurrent 
TCP connections (total or from a single source IP), and so forth.

Counteractive measures to enforce the defined rules are: request blocking, 
dynamic timeout adjustment, request delay, response throttling, and dropping of 
TCP connections. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup 

%build
%{_httpd_apxs} -Wc,"%{optflags}" -c apache2/mod_qos.c -lcrypto

# Tools building
# Need to fix the binaries

pushd .
cd tools/
aclocal
automake --add-missing
%configure
make %{?_smp_mflags}
popd

%install
install -Dpm 755 apache2/.libs/mod_qos.so \
    $RPM_BUILD_ROOT%{_libdir}/httpd/modules/mod_qos.so

install -Dpm 644 %{SOURCE1} %{buildroot}%{_httpd_modconfdir}/10-mod_qos.conf

cd tools/
%make_install
install -d %{buildroot}%{_mandir}/man1/
install -Dpm 644 man1/*  %{buildroot}%{_mandir}/man1/

%files
%{_bindir}/*
%{_mandir}/man1/*
%doc doc README.TXT
%{_libdir}/httpd/modules/mod_qos.so
%config(noreplace)  %{_httpd_modconfdir}/10-mod_qos.conf

%changelog
%autochangelog
