%global source0_hash d986ff68de94b80e505f8b6bd68bd1ba146bf234b40d1f519695fe15592e995b

%{!?_httpd_mmn: %{expand: %%global _httpd_mmn %%(cat %{_includedir}/httpd/.mmn || echo 0-0)}}
Name:      mod_gnutls
Version:   0.12.0
Release:   14%{?dist}
Summary:   GnuTLS module for the Apache HTTP server
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:   Apache-2.0
URL:       http://mod.gnutls.org/
Source0:   https://mod.gnutls.org/downloads/%{name}-%{version}.tar.bz2
Source1:   mod_gnutls.conf
ExcludeArch: %{ix86}  %{arm}
BuildRequires: make
BuildRequires: gnutls-devel, gnutls-utils, httpd-devel, apr-util-devel >= 1.3, libtool, autoconf, automake, softhsm-devel, python3, python3-pyyaml
Requires:  apr-util >= 1.3, gnutls-utils, httpd-mmn = %{_httpd_mmn}

%description
mod_gnutls uses the GnuTLS library to provide SSL 3.0, TLS 1.0 and TLS 1.1
encryption for Apache HTTPD.  It is similar to mod_ssl in purpose, but does
not use OpenSSL.  A primary benefit of using this module is the ability to
configure multiple SSL certificates for a single IP-address/port combination
(useful for securing virtual hosts).
    
Features
    * Support for SSL 3.0, TLS 1.0 and TLS 1.1.
    * Support for client certificates.
    * Support for RFC 5081 OpenPGP certificate authentication.
    * Support for Server Name Indication.
    * Distributed SSL Session Cache via Memcached
    * Local SSL Session Cache using DBM
    * Sets enviromental vars for scripts (compatible with mod_ssl vars)
    * Small and focused code base:
         Lines of code in mod_gnutls: 3,593
         Lines of code in mod_ssl: 15,324

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
cp %{SOURCE1} .

%build
rm -f configure
export APR_MEMCACHE_LIBS="`apu-1-config --link-ld`"
export APR_MEMCACHE_CFLAGS="`apu-1-config --includes`"
autoreconf -f -i

rm -rf autom4te.cache

%configure %{?_httpd_apxs:--with-apxs=%{_httpd_apxs}}
%{__make} %{?_smp_mflags}

%check
# missing dependencies for running test
# %{__make} check

%install
rm -rf %{buildroot}
%{__install} -m 755 -D src/.libs/mod_gnutls.so %{buildroot}%{_libdir}/httpd/modules/mod_gnutls.so
%{__install} -m 644 -D %{SOURCE1} %{buildroot}%{_sysconfdir}/httpd/conf.d/mod_gnutls.conf

%pre
rm -fr %{_localstatedir}/cache/mod_gnutls

%files
%doc README NOTICE LICENSE 
%{_libdir}/httpd/modules/*.so
%config(noreplace) %{_sysconfdir}/httpd/conf.d/mod_gnutls.conf

%changelog
%autochangelog
