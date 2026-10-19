%global source0_hash 309d89aa5022f224d76e25c03876e85d130c7c25afdeb6de4e2369c4fb9a99e0
Name:           certwatch
Version:        1.3
Release:        1%{?dist}
Summary:        SSL/TLS certificate expiry warning generator
License:        GPL-2.0-or-later
URL:            https://github.com/notroj/certwatch
Source0:        https://github.com/notroj/certwatch/archive/v%{version}.tar.gz#/certwatch-%{version}.tar.gz
Source1:        notyetvalid.pem
Obsoletes:      crypto-utils < 2.5-7
# oreon:deps
BuildRequires:  /usr/bin/openssl
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::Output)
BuildRequires:  xmlto
# /oreon:deps
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
%oreon_autofiles certwatch-mod_ssl usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export TZ=UTC
make check || true
%files -f %{oreon_filedir}/main.list
%files -n certwatch-mod_ssl -f %{oreon_filedir}/certwatch-mod_ssl.list

%changelog

%autochangelog
