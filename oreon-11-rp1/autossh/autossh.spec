%global source0_hash 5fc3cee3361ca1615af862364c480593171d0c54ec156de79fc421e31ae21277
Summary:        Utility to autorestart SSH tunnels
Name: autossh
Version: 1.4g
Release:        1%{?dist}
License: LicenseRef-Callaway-BSD
URL: https://www.harding.motd.ca/autossh/
Source0:        https://www.harding.motd.ca/autossh/autossh-1.4g.tgz
Source1: autossh@.service
Source2: README.service
Patch0: autossh-configure-c99.patch
%{?systemd_requires}
Requires: /usr/bin/ssh
# oreon:deps
BuildRequires:  /usr/bin/ssh
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  systemd
# /oreon:deps
%description
autossh is a utility to start and monitor an ssh tunnel. If the tunnel
dies or stops passing traffic, autossh will automatically restart it.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
cp -p %{SOURCE2} .

# Create a sysusers.d config file
cat >autossh.sysusers.conf <<EOF
u autossh - 'autossh service account' %{_sysconfdir}/autossh -
EOF

%build

%configure
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/autossh
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
mkdir -p examples
cp -p autossh.host rscreen examples
chmod 0644 examples/*
install -m 0755 -p autossh $RPM_BUILD_ROOT%{_bindir}
cp -p autossh.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -m 0644 -p %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}
install -m0644 -D autossh.sysusers.conf %{buildroot}%{_sysusersdir}/autossh.conf
%oreon_autofiles main

%post

%systemd_post autossh@.service
%preun

if [ $1 -eq 0 ] && [ -x /usr/bin/systemctl ]; then
    if [ -d /run/systemd/system ]; then
        /usr/bin/systemctl --no-reload disable --now autossh@.service || :
	systemctl stop "autossh@*.service" || :
    else
        /usr/bin/systemctl --no-reload disable autossh@.service || :
    fi
fi
%postun

%systemd_postun_with_restart "autossh@*.service"
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
