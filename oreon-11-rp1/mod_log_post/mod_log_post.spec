%global source0_hash a6b7edfa898d5364bd1d0ce0bc166851b501fd101f81478b3a834c45bba6c7d4

# /usr/sbin/apxs with httpd < 2.4 and defined as /usr/bin/apxs with httpd >= 2.4
%{!?_httpd_apxs:       %{expand: %%global _httpd_apxs       %%{_sbindir}/apxs}}
%{!?_httpd_mmn:        %{expand: %%global _httpd_mmn        %%(cat %{_includedir}/httpd/.mmn || echo 0-0)}}
%{!?_httpd_confdir:    %{expand: %%global _httpd_confdir    %%{_sysconfdir}/httpd/conf.d}}
# /etc/httpd/conf.d with httpd < 2.4 and defined as /etc/httpd/conf.modules.d with httpd >= 2.4
%{!?_httpd_modconfdir: %{expand: %%global _httpd_modconfdir %%{_sysconfdir}/httpd/conf.d}}

Summary:        Module for the Apache web server to log all HTTP POST messages
Summary(de):    Modul für den Apache Webserver zur Protokollierung von HTTP POST
Name:           mod_log_post
Version:        0.1.0
Release:        35%{?dist}
# Automatically converted from old format: GPLv2 with exceptions - review is highly recommended.
License:        LicenseRef-Callaway-GPLv2-with-exceptions
URL:            https://ftp.robert-scheck.de/linux/%{name}/
Source0:        https://ftp.robert-scheck.de/linux/%{name}/%{name}-%{version}.tar.gz
Patch0:         mod_log_post-0.1.0-httpd24.patch
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  httpd-devel >= 2.0.39
Requires:       httpd-mmn = %{_httpd_mmn}

%description
mod_log_post can be used for logging all HTTP POST messages. The module
is based on mod_security but in difference it never returns any error
messages to the visitors of your websites. Logging of POST data can be
very useful for debugging purposes or analyses. As the module is loaded
and run after the SSL decryption, it even can log POST data transmitted
before via SSL to the Apache web server.

%description -l de
mod_log_post kann verwendet werden, um POST von HTTP zu protokollieren.
Das Modul basiert auf mod_security, im Unterschied dazu jedoch liefert
es niemals eine Fehlermeldung an den Besucher einer Webseite aus. Das
Protokollieren von POST-Daten kann bei der Fehlersuche bzw. Analyse sehr
hilfreich sein. Nachdem das Modul nach der SSL-Entschlüsselung geladen
und ausgeführt wird, kann es auch POST-Daten mitschreiben, die mittels
SSL an den Apache Webserver übermittelt worden sind.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .httpd24

%build
%configure --with-apxs=%{_httpd_apxs}
%make_build

%install
%make_install

mkdir -p $RPM_BUILD_ROOT%{_httpd_modconfdir}
sed -n /^LoadModule/p $RPM_BUILD_ROOT%{_httpd_confdir}/log_post.conf \
    >> $RPM_BUILD_ROOT%{_httpd_modconfdir}/10-log_post.conf
sed -i /^LoadModule/d $RPM_BUILD_ROOT%{_httpd_confdir}/log_post.conf
touch -c -r log_post.conf $RPM_BUILD_ROOT%{_httpd_confdir}/log_post.conf \
    $RPM_BUILD_ROOT%{_httpd_modconfdir}/10-log_post.conf

%files
%license COPYING LICENSING_EXCEPTION
%doc ChangeLog README
%{_libdir}/httpd/modules/%{name}.so
%config(noreplace) %{_httpd_modconfdir}/10-log_post.conf
%config(noreplace) %{_httpd_confdir}/log_post.conf

%changelog
%autochangelog
