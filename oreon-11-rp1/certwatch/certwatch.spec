%global source0_hash 8dde863f352ece4d61deeee4d850753316d84261b7f2c5aef8307af477f8b2bf

Name:           certwatch
Version:        1.2
Release:        21%{?dist}
Summary:        SSL/TLS certificate expiry warning generator
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/notroj/certwatch
Source0:        https://github.com/notroj/certwatch/archive/v%{version}.tar.gz#/certwatch-%{version}.tar.gz
Source1:        notyetvalid.pem
BuildRequires:  gcc, openssl-devel, xmlto, autoconf, automake
BuildRequires:  perl(Test), perl(Test::Harness), perl(Test::Output), /usr/bin/openssl
BuildRequires: make
Obsoletes:      crypto-utils < 2.5-7

%description
This package provides a utility for generating warnings when SSL/TLS
certificates are soon to expire. 

%package mod_ssl
Summary: SSL/TLS certificate expiry warnings for mod_ssl
Requires: crontabs, mod_ssl, certwatch = %{version}-%{release}, /usr/sbin/sendmail

%description mod_ssl
The certwatch-mod_ssl package contains a cron script which runs a
daily check for any expired or soon-to-expire certificates listed in
the mod_ssl configuration.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
autoreconf -i
cp %{SOURCE1} t/notvalid.pem

%build
%configure
%make_build

%install
%make_install
install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/cron.daily
install -m 755 -p certwatch.cron $RPM_BUILD_ROOT%{_sysconfdir}/cron.daily/certwatch

%check
export TZ=UTC
make check || true

%files
%{_bindir}/certwatch
%license LICENSE
%{_mandir}/man1/*

%files -n certwatch-mod_ssl
%ghost %{_sysconfdir}/sysconfig/certwatch
%config(noreplace) %{_sysconfdir}/cron.daily/certwatch
%{_mandir}/man5/*

%changelog
%autochangelog
