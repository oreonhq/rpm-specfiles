%global source0_hash 34a2a2068fe11753ef1e4bdd7b7077cad8f4d4e3e797de85a6737e876347b843

Summary:        Sendmail milter for amavisd-new using the AM.PDP protocol
Name:           amavisd-milter
Version:        1.7.2
Release:        12%{?dist}
# ISC (compat/strlcpy.c) and BSD-3-Clause (the rest)
License:        BSD-3-Clause AND ISC
URL:            https://github.com/prehor/amavisd-milter
Source0:        https://github.com/prehor/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        amavisd-milter.service
Source2:        amavisd-milter.sysconfig
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  sendmail-milter-devel >= 8.12.0
BuildRequires:  systemd-rpm-macros
Requires:       amavis
%{?systemd_requires}

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
%if 0%{?fedora} > 41 || 0%{?rhel} > 10
export CFLAGS="$CFLAGS -std=gnu17"  # RHBZ#2336394, comment #4
%endif

%configure \
  --localstatedir=/run/amavisd \
  --with-working-dir=%{_localstatedir}/spool/amavisd/tmp
%make_build

%install
%make_install

# Install systemd unit file
install -D -p -m 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/%{name}
install -D -p -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/%{name}.service

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license LICENSE
%doc CHANGES
%{_sbindir}/%{name}
%{_unitdir}/%{name}.service
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_mandir}/man8/%{name}.8*

%changelog
%autochangelog
