%global source0_hash 2b7210a0c8950c13e648d8abc36b7bca8ce58035999526301a715aacd40d15d4

Name:           tetrinetx
Version:        1.13.16
Release:        43%{?dist}
Summary:        The GNU TetriNET server

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://tetrinetx.sourceforge.net/
Source0:        http://switch.dl.sourceforge.net/sourceforge/tetrinetx/%{name}-%{version}+qirc-1.40c.tar.gz
Source1:        tetrinetx.init
Source2:        tetrinetx.logrotate
Source3:        tetrinetx.service
Source4:        %{name}-tmpfiles.conf

%{?systemd_requires}
BuildRequires:  gcc
BuildRequires:  systemd-rpm-macros
BuildRequires:  adns-devel
Requires:       logrotate

%description
Tetrinetx is the GNU TetriNET server written in C. It includes IRC and
Spectator supports. As many other tetrinet servers, it uses IP independent
decryption which allows the server to run behind a router.

TetriNET is a network-based, multiplayer falling bricks game. This package
contains a server for hosting TetriNET games over a public or private network.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}+qirc-1.40c
# Modify the compile script to use correct directories and use "tetrinetx" as
# the program name
sed -i "s:/usr/local:%{_prefix}:g; s/tetrix\\.linux/tetrinetx/g" -i src/compile.linux

# Modify the default config file to use the correct pid file location
sed -i "s:game\\.pid:%{_localstatedir}/run/tetrinetx/game.pid:" bin/game.conf

# Modify config.h to use correct directories for config files, etc
sed -i "s:game\\.log:%{_localstatedir}/log/tetrinetx/game\\.log:;
        s:game\\.pid:%{_localstatedir}/run/tetrinetx/game\\.pid:;
        s:game\\.winlist:%{_localstatedir}/games/tetrinetx/game\\.winlist:g;
        s:\"game:\"%{_sysconfdir}/tetrinetx/game:g" src/config.h

# Create a sysusers.d config file
cat >tetrinetx.sysusers.conf <<EOF
u tetrinetx - 'Tetrinetx service account' %{_localstatedir}/games/tetrinetx -
EOF

%build
%undefine _fortify_level
cd src
./compile.linux "%{optflags} -std=gnu17"
cd ..

%install
# Install executable
mkdir -p %{buildroot}%{_bindir}
install -m 755 bin/tetrinetx %{buildroot}%{_bindir}/
# Install configuration files
mkdir -p %{buildroot}%{_sysconfdir}/tetrinetx
install -p -m 644 bin/game.conf %{buildroot}%{_sysconfdir}/tetrinetx
install -p -m 644 bin/game.motd %{buildroot}%{_sysconfdir}/tetrinetx
install -p -m 644 bin/game.pmotd %{buildroot}%{_sysconfdir}/tetrinetx
install -p -m 600 bin/game.secure %{buildroot}%{_sysconfdir}/tetrinetx
# Install system init script
mkdir -p %{buildroot}%{_unitdir}
install -p -m 644 %{SOURCE3} %{buildroot}%{_unitdir}/tetrinetx.service
# Install logrotate.d entry
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
install -p -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/tetrinetx
# Log files are placed under /var/log/tetrinetx
mkdir -p %{buildroot}%{_localstatedir}/log/tetrinetx
# State data (winlists, etc) for the game will be placed in /var/games/tetrinetx
mkdir -p %{buildroot}%{_localstatedir}/games/tetrinetx
# Tetrinetx pid file goes here
mkdir -p %{buildroot}%{_tmpfilesdir}/
install -p -m 644 %{SOURCE4} %{buildroot}%{_tmpfilesdir}/%{name}.conf
mkdir -p %{buildroot}%{_localstatedir}/run/tetrinetx

install -m0644 -D tetrinetx.sysusers.conf %{buildroot}%{_sysusersdir}/tetrinetx.conf

%post
%systemd_post tetrinetx.service

%preun
%systemd_preun tetrinetx.service

%postun
%systemd_postun_with_restart tetrinetx.service

%files
%doc AUTHORS ChangeLog README README.qirc.spectators bin/game.allow.example bin/game.ban.compromise.example bin/game.ban.example
%license COPYING
%{_bindir}/tetrinetx
%{_unitdir}/tetrinetx.service
%dir %{_sysconfdir}/tetrinetx
%config(noreplace) %{_sysconfdir}/logrotate.d/tetrinetx
%dir %attr(-,tetrinetx,tetrinetx) %{_localstatedir}/log/tetrinetx/
%dir %attr(-,tetrinetx,tetrinetx) %{_localstatedir}/games/tetrinetx/
%dir %attr(-,tetrinetx,tetrinetx) %{_localstatedir}/run/tetrinetx/
%{_tmpfilesdir}/%{name}.conf
%config(noreplace) %{_sysconfdir}/tetrinetx/*
%{_sysusersdir}/tetrinetx.conf

%changelog
%autochangelog
