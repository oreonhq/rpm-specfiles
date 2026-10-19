%global source4_hash d6270219a2492e5cd6a0510104514f52aa7dc342da3037fb97c3cf9405525830
%global source3_hash 8dbbb09ee4036e34f567fa7a4fd043c1700819e297c802dc16cef6340346ab91
%global source0_hash e2fa88b63812db6ad6101c287a887eb77c6bd9f2d38abc20fb8843ad32152f8d
%global pypi_name postfix_mta_sts_resolver
Name:           postfix-mta-sts-resolver
Version:        1.5.1
Release:        1%{?dist}
Summary:        Daemon providing MTA-STS map to Postfix
License:        MIT
URL:            https://github.com/Snawoot/%{name}
Source0:        https://github.com/Snawoot/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        mta-sts-daemon.yml
Source2:        postfix-mta-sts-resolver.service
Source3:        https://github.com/Snawoot/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz.asc
Source4:        https://github.com/Snawoot.gpg
BuildArch:      noarch
Obsoletes:      postfix-mta-sts-resolver+uvloop < 1.5.1-2
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 42.0.0
Requires:       python3-postfix-mta-sts-resolver = %{version}-%{release}
# /oreon:deps
%description
postfix-mta-sts-resolver provides a lookup daemon and command line
query utility for MTA-STS policies (RFC 8461).  The daemon provides TLS
client policy to Postfix via socketmap.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE4}' --signature='%{SOURCE3}' --data='%{SOURCE0}'
%autosetup -n %{name}-%{version} -p1

%build

%pyproject_wheel
make doc
%install
%pyproject_install
install -p -D -m 0640 %{SOURCE1} %{buildroot}%{_sysconfdir}/mta-sts-daemon.yml
install -p -D -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.service
mkdir -p %{buildroot}%{_sharedstatedir}/mta-sts
mkdir -p %{buildroot}%{_mandir}/man1
install -p -D -m 0644 man/*.1 %{buildroot}%{_mandir}/man1/
mkdir -p %{buildroot}%{_mandir}/man5
install -p -D -m 0644 man/*.5 %{buildroot}%{_mandir}/man5/
install -m0644 -D postfix-mta-sts-resolver.sysusers.conf %{buildroot}%{_sysusersdir}/postfix-mta-sts-resolver.conf
%oreon_autofiles main

%check

%pyproject_check_import -e 'postfix_mta_sts_resolver.postgres_cache' -e 'postfix_mta_sts_resolver.redis_cache' -e 'postfix_mta_sts_resolver.sqlite_cache'
%post

%systemd_post %{name}.service
%preun

%systemd_preun %{name}.service
%postun

%systemd_postun_with_restart %{name}.service
%files

%changelog

%autochangelog
