%global source0_hash 624863d764fac75432dcc44e9cc8e0887eecdc9ef600529e3ae83998c82801e9
%global tftpboot_dir %{_sharedstatedir}/tftpboot/
%global commit 700eb5bdfb28baba4de5e4083bec9e132a763bcb
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global selinuxtype targeted
%bcond check 0
Name:           cobbler
Version:        3.3.10
Release:        1%{?dist}
Summary:        Boot server configurator
URL:            https://cobbler.github.io/
License:        GPL-2.0-or-later
Source0:        https://github.com/cobbler/cobbler/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        migrate-settings.sh
Source2:        %{name}.te
Source3:        %{name}.if
Source4:        %{name}.fc
Patch0:         cobbler-nocov.patch
Patch2:         cobbler-reposync.patch
BuildArch:      noarch
%if 0%{?fedora} >= 42 || 0%{?rhel} >= 10 || 0%{?oreon} >= 11
%else
%endif
%if %{with check}
%endif
Requires: (%{name}-selinux if selinux-policy-%{selinuxtype})
Requires: httpd
Requires: tftp-server
Requires: dosfstools
Requires: createrepo_c
Requires: rsync
Requires: xorriso
Requires: genisoimage
Recommends: bash-completion
Requires: dnf-plugins-core
Requires: (syslinux if (filesystem(x86-64) or filesystem(x86-32)))
Recommends: grub2-efi-ia32
Recommends: grub2-efi-x64
Recommends: logrotate
Recommends: %{py3_dist librepo}
Obsoletes: cobbler-web < 3.3
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
# oreon:deps
BuildRequires:  make
BuildRequires:  pkgconfig(systemd)
BuildRequires:  python3-devel
BuildRequires:  python3dist(crypt-r)
BuildRequires:  python3dist(ct3)
BuildRequires:  python3dist(distro)
BuildRequires:  python3dist(dnspython)
BuildRequires:  python3dist(file-magic)
BuildRequires:  python3dist(netaddr)
BuildRequires:  python3dist(pytest-benchmark)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(schema)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)
BuildRequires:  selinux-policy
BuildRequires:  selinux-policy-devel
BuildRequires:  systemd
# /oreon:deps
%description
Cobbler is a network install server. Cobbler supports PXE, ISO
virtualized installs, and re-installing existing Linux machines. The
last two modes use a helper tool, 'koan', that integrates with cobbler.
Cobbler's advanced features include importing distributions from DVDs
and rsync mirrors, kickstart templating, integrated yum mirroring, and
built-in DHCP/DNS Management. Cobbler has a XML-RPC API for integration
with other applications.

%package selinux
Summary:        SELinux policies for %{name}
Requires:       selinux-policy-%{selinuxtype}
Requires(post): selinux-policy-%{selinuxtype}
BuildRequires:  selinux-policy-devel
BuildArch:      noarch
%{?selinux_requires}
%description selinux
SELinux policies for %{name}.

%package tests
Summary:        Unit tests for cobbler
Requires:       cobbler = %{version}-%{release}
%description tests
Unit test files from the Cobbler project.

%package tests-containers
Summary:        Dockerfiles and scripts to setup testing containers
Requires:       cobbler = %{version}-%{release}
%description tests-containers
Dockerfiles and scripts to setup testing containers.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
mkdir -p selinux
cp -p %{SOURCE2} %{SOURCE3} %{SOURCE4} selinux/

# Cheetah switched names from Cheetah3 to CT3 in its metadata in version 3.3.0.
# https://github.com/CheetahTemplate3/cheetah3/commit/673259b2d139b4ea970b1c2da12607b7ac39cbec
%if 0%{?fedora} >= 42 || 0%{?rhel} >= 10 || 0%{?oreon} >= 11
sed -e 's/Cheetah3/CT3/' -i setup.py
%endif

%build

. ./distro_build_configs.sh
%py3_build
make man
make -f %{_datadir}/selinux/devel/Makefile %{name}.pp
bzip2 -9 %{name}.pp
%install
. ./distro_build_configs.sh
%py3_install ||:
rm %{buildroot}%{_sysconfdir}/cobbler/cobbler.conf
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
mv %{buildroot}%{_sysconfdir}/cobbler/cobblerd_rotate %{buildroot}%{_sysconfdir}/logrotate.d/cobblerd
mkdir -p %{buildroot}%{tftpboot_dir}/{boot,etc,grub/system{,_link},images{,2},ppc,pxelinux.cfg,s390x}
mkdir -p %{buildroot}%{_unitdir}
mv %{buildroot}%{_sysconfdir}/cobbler/cobblerd.service %{buildroot}%{_unitdir}
touch %{buildroot}%{_sharedstatedir}/cobbler/web.ss
install -p -m0755 %SOURCE1 %{buildroot}%{_datadir}/cobbler/bin/migrate-settings.sh
install -D -m 0644 %{name}.pp.bz2 %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}/%{name}.pp.bz2
install -D -p -m 0644 selinux/%{name}.if %{buildroot}%{_datadir}/selinux/devel/include/distributed/%{name}.if
%oreon_autofiles cobbler-selinux usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cobbler-tests usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cobbler-tests-containers usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%pytest -v
%endif
%pre

if [ $1 -ge 2 ]; then
    DATE=$(date "+%%Y%%m%%d-%%H%%M%%S")
    if [ ! -d "%{_sharedstatedir}/cobbler/backup/upgrade-${DATE}" ]; then
        mkdir -p "%{_sharedstatedir}/cobbler/backup/upgrade-${DATE}"
    fi
    for i in "config" "snippets" "templates" "triggers" "scripts"; do
        if [ -d "%{_sharedstatedir}/cobbler/${i}" ]; then
            cp -r "%{_sharedstatedir}/cobbler/${i}" "%{_sharedstatedir}/cobbler/backup/upgrade-${DATE}"
        fi
    done
    if [ -d %{_sysconfdir}/cobbler ]; then
        cp -r %{_sysconfdir}/cobbler "%{_sharedstatedir}/cobbler/backup/upgrade-${DATE}"
    fi
fi
%post

%systemd_post cobblerd.service
chmod 640 %{_sysconfdir}/cobbler/settings.yaml
chmod 600 %{_sysconfdir}/cobbler/mongodb.conf
chmod 600 %{_sysconfdir}/cobbler/modules.conf
chmod 640 %{_sysconfdir}/cobbler/users.conf
chmod 640 %{_sysconfdir}/cobbler/users.digest
chmod 750 %{_sysconfdir}/cobbler/settings.d
chmod 640 %{_sysconfdir}/cobbler/settings.d/*
chgrp apache %{_sysconfdir}/cobbler/settings.yaml
chgrp apache %{_sysconfdir}/cobbler/users.conf
chgrp apache %{_sysconfdir}/cobbler/users.digest
chgrp apache %{_sysconfdir}/cobbler/settings.d
chgrp apache %{_sysconfdir}/cobbler/settings.d/*
if [ -f %{_sharedstatedir}/cobbler/web.ss ]; then
    chown root %{_sharedstatedir}/cobbler/web.ss
fi
%posttrans

if [ -f %{_sysconfdir}/cobbler/settings.rpmsave ]; then
    echo warning: migrating old settings to settings.yaml
    mv %{_sysconfdir}/cobbler/settings.yaml{,.rpmnew}
    cp -a %{_sysconfdir}/cobbler/settings.{rpmsave,rpmorig}
    mv %{_sysconfdir}/cobbler/settings.{rpmsave,yaml}
    %{_datadir}/cobbler/bin/migrate-settings.sh
fi
grep -q '^reposync_rsync_flags:' %{_sysconfdir}/cobbler/settings.yaml || echo -e '#ADDED:\nreposync_rsync_flags: "-rltDv --copy-unsafe-links"' >> %{_sysconfdir}/cobbler/settings.yaml
%preun

%systemd_preun cobblerd.service
%postun

%systemd_postun_with_restart cobblerd.service
%pre selinux

%selinux_relabel_pre -s %{selinuxtype}
%post selinux

%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{name}.pp.bz2
%selinux_relabel_post -s %{selinuxtype}
if [ "$1" -le "1" ]; then # First install
   %systemd_postun_with_restart cobblerd.service
fi
%postun selinux

if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{name}
    %selinux_relabel_post -s %{selinuxtype}
fi
%files -f %{oreon_filedir}/main.list
%files -n cobbler-selinux -f %{oreon_filedir}/cobbler-selinux.list
%files -n cobbler-tests -f %{oreon_filedir}/cobbler-tests.list
%files -n cobbler-tests-containers -f %{oreon_filedir}/cobbler-tests-containers.list

%changelog

%autochangelog
