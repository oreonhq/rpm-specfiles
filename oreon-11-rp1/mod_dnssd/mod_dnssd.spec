%global source0_hash 2cd171d76eba398f03c1d5bcc468a1756f4801cd8ed5bd065086e4374997c5aa

%{!?_httpd_apxs:       %{expand: %%global _httpd_apxs       %%{_sbindir}/apxs}}
%{!?_httpd_mmn:        %{expand: %%global _httpd_mmn        %%(cat %{_includedir}/httpd/.mmn || echo 0-0)}}
%{!?_httpd_confdir:    %{expand: %%global _httpd_confdir    %%{_sysconfdir}/httpd/conf.d}}
# /etc/httpd/conf.d with httpd < 2.4 and defined as /etc/httpd/conf.modules.d with httpd >= 2.4
%{!?_httpd_modconfdir: %{expand: %%global _httpd_modconfdir %%{_sysconfdir}/httpd/conf.d}}

Name:           mod_dnssd
Version:        0.6
Release:        36%{?dist}
Summary:        An Apache HTTPD module which adds Zeroconf support

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            http://0pointer.de/lennart/projects/mod_dnssd/
Source0:        http://0pointer.de/lennart/projects/mod_dnssd/%{name}-%{version}.tar.gz
Source1:        mod_dnssd.conf-httpd
Patch0:         mod_dnssd-0.6-httpd24.patch
Requires:       httpd-mmn = %{_httpd_mmn}
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  httpd-devel avahi-devel e2fsprogs-devel

%description
mod_dnssd is an Apache HTTPD module which adds Zeroconf support via DNS-SD
using Avahi.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .httpd24

%build
export APXS=%{_httpd_apxs}
%configure --disable-lynx
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
install -Dp src/.libs/mod_dnssd.so $RPM_BUILD_ROOT%{_libdir}/httpd/modules/mod_dnssd.so
%if "%{_httpd_confdir}" == "%{_httpd_modconfdir}"
install -Dp -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_httpd_confdir}/mod_dnssd.conf
%else
sed -n /^LoadModule/p %{SOURCE1} > 10-mod_dnssd.conf
sed /^LoadModule/d %{SOURCE1} > mod_dnssd.conf
touch -r %{SOURCE1} 10-mod_dnssd.conf mod_dnssd.conf
install -Dp -m 0644 mod_dnssd.conf $RPM_BUILD_ROOT%{_httpd_confdir}/mod_dnssd.conf
install -Dp -m 0644 10-mod_dnssd.conf $RPM_BUILD_ROOT%{_httpd_modconfdir}/10-mod_dnssd.conf
%endif

%files
%doc LICENSE doc/README doc/README.html
%config(noreplace) %{_sysconfdir}/httpd/conf.*/*.conf
%{_libdir}/httpd/modules/mod_dnssd.so

%changelog
%autochangelog
