%global source0_hash 41eb05e22b8643c68d72fbbecbb38749c81264840dd38bac3594516e8dd2ee7e
%global sendmailcf %{_datadir}/sendmail-cf
Summary:        Additional m4 files used to generate sendmail.cf
Name:           open-sendmail
Version:        0
Release:        1%{?dist}
License:        Sendmail-8.23
URL:            http://open-sendmail.sourceforge.net/
Source0:        %{name}-%{version}.tar.bz2
Requires:       sendmail-cf
BuildArch:      noarch
# oreon:deps

# /oreon:deps
%description
Open-Sendmail is the open development of additional m4 files
used to generate and enhance sendmail.cf. The project contains
sendmail goodies previously provided at anfi.homeunix.net and
additional items.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%install
mkdir -p $RPM_BUILD_ROOT{%{sendmailcf}/{feature,mailer}/%{name},%{_datadir}/%{name}}
install -p -m 644 cf/feature/anfi/*.m4 $RPM_BUILD_ROOT%{sendmailcf}/feature/%{name}/
install -p -m 644 cf/mailer/anfi/*.m4 $RPM_BUILD_ROOT%{sendmailcf}/mailer/%{name}/
install -p -m 644 cf/m4/*.patch $RPM_BUILD_ROOT%{_datadir}/%{name}/
ln -sf %{name}/require_rdns.m4 $RPM_BUILD_ROOT%{sendmailcf}/feature/require_rdns2.m4
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
