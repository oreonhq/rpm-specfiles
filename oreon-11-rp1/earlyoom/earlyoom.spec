%global source0_hash b2fe5e1e071a5a000b22fb9602c068fd69d09c057f0ba972dfc5d85daf464b2a

%global makeflags VERSION=%{version} PREFIX=%{_prefix} SYSCONFDIR=%{_sysconfdir} SYSTEMDUNITDIR=%{_unitdir}

Name: earlyoom
Version: 1.9.0
Release: %autorelease

License: MIT
URL: https://github.com/rfjakob/%{name}
Summary: Early OOM Daemon for Linux
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1: %{name}.conf

%{?systemd_requires}
BuildRequires: systemd
BuildRequires: pandoc
BuildRequires: gcc
BuildRequires: make

%description
User-space OOM killer daemon that can avoid the system going into the
unresponsive state. It checks the amount of available memory and
free swap up to 10 times a second (less often if there is a lot of free
memory) and kills the largest processes with the highest oom_score.

Percentages are configured through the configuration file.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
cp -f %{SOURCE1} %{name}.default
sed -e '/systemctl/d' -i Makefile

%build
%set_build_flags
%make_build %{makeflags}

%install
%make_install %{makeflags}

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%{_mandir}/man1/%{name}.*
%config(noreplace) %{_sysconfdir}/default/%{name}

%changelog
%autochangelog
