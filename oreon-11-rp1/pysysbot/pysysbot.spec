%global source0_hash ee503c51b66c223176aca9c3ac6936c74cc7e707b705ad5f5fa59a718b8ffccc

name:           pysysbot
Version:        0.3.0
Release:        29%{?dist}
Summary:        A simple python jabber bot for getting system information

License:        LicenseRef-Callaway-BSD
URL:            http://affolter-engineering.ch/pysysbot
Source0:        https://github.com/fabaff/pysysbot/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  systemd

Requires:         python3-slixmpp
Requires:         python3-psutil
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

%description
This python jabber (XMPP) bot is based on the jabberbot framework. The bot
is capable to display details about the system it is running on. If you don't
want or can stay connected through SSH all the time this is an easy way to
get information about the remote system.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
install -Dp -m 0644 data/%{name}.service %{buildroot}%{_unitdir}/%{name}.service
install -Dp -m 0644 data/%{name}.conf %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf
install -Dp -m 0644 man/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
rm -rf %{buildroot}%{_defaultdocdir}

%pyproject_save_files -l pysysbot

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files -n %files -n pysysbot -f %{pyproject_files}
%doc AUTHORS ChangeLog README.rst
%license COPYING
%{_mandir}/man*/%{name}*.*
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/
%{_unitdir}/%{name}.service

%changelog
%autochangelog
