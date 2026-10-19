%global source0_hash 7b7b8caa4d399f6418a6f9d66af979e583c5f9cb0765073663f8531bee0091f0
Summary:        Sendmail milter for amavisd-new using the AM.PDP protocol
Name:           amavisd-milter
Version:        1.7.2
Release:        1%{?dist}
License:        BSD-3-Clause AND ISC
URL:            https://github.com/prehor/amavisd-milter
Source0:        https://github.com/prehor/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        amavisd-milter.service
Source2:        amavisd-milter.sysconfig
Requires:       amavis
%{?systemd_requires}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  sendmail-milter-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
The amavisd-milter is a sendmail milter (mail filter) for amavisd-new or
amavis 2.4.3 (and above) and sendmail 8.13 (and above) which use the new
AM.PDP protocol.

Run 'usermod -a -G amavis postfix' when using Postfix and amavisd-milter
via the unix socket.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure \
  --localstatedir=/run/amavisd \
  --with-working-dir=%{_localstatedir}/spool/amavisd/tmp
%make_build
%install
%make_install
install -D -p -m 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/%{name}
install -D -p -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/%{name}.service
%oreon_autofiles main

%post

%systemd_post %{name}.service
%preun

%systemd_preun %{name}.service
%postun

%systemd_postun_with_restart %{name}.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
