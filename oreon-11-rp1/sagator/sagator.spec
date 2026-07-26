%global source0_hash 45d590acbb32c201db511766037ef68e90eb685edad204051e7983431be50325

%global CHROOTDIR %{_var}/spool/vscan
%global BASE_LIBS glibc,libgcc,expat,libstdc++,zlib,bzip2-libs,cracklib,cracklib-dicts
%global ARCHIVERS tar,arc,unace,unrar,rar,zoo,unarj,arj,unzip,zip,gzip,bzip2
%global ANTIVIRS clamav,clamav-libs,avglinux,nod32ls,nod32lfs,kav4mailservers-linux
%global ANTISPAMS bogofilter,qsf
%global CLAMAV_VERSION 0.100

# SElinux temporarily disabled for all systems
%global install_sepolicy 0
%global sepolicy %{_datadir}/%{name}/selinux/%{name}.pp

%if 0%{?fedora} >= 28 || 0%{?rhel} >= 8
%global python_version python3
%else
%global python_version python2
%endif

Summary:   Antivirus/anti-spam gateway for smtp server
Name:      sagator
Version:   2.0.3
Release:   0.beta3%{?dist}.8
Source:    http://www.salstar.sk/pub/antivir/snapshots/unstable/sagator-%{version}-0.beta3.tar.bz2
URL:       http://www.salstar.sk/sagator/
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:   GPL-2.0-or-later
BuildArch: noarch
BuildRequires: %{python_version}-devel, ed, gettext
BuildRequires: %{python_version}-passlib
BuildRequires: make
Requires:  %{name}-core = %{version}-%{release}
Requires:  sed
Requires:  spamassassin
%if 0%{?suse_version}
Requires:  clamav >= %{CLAMAV_VERSION}
%else
Requires:  clamav-lib >= %{CLAMAV_VERSION}, clamav-update
%endif

%description
This program is an email antivirus/anti-spam gateway. It is an interface to
the postfix, sendmail, or any other smtpd, which runs antivirus and/or
spam checker. Its modular architecture can use any combination of
antivirus/spam checker according to configuration.

It has some internal checkers (string_scanner and regexp_scanner). Sagator
can parse MIME mails and decompress archives, if it is configured so.

Features:
    * simple chroot support
    * modular antivirus/spam checker support
          o attach an intrascanner to another intrascanner or realscanner
          o combine intrascanners
          o combine realscanners
          o virus/spam level based scanners
    * database support
          o SQL logging
          o dynamic scanner (antivirus/anti-spam) configuration
    * daily reports for users
    * web quarantine accessible for all users
    * you don't need any perl modules or any other modules, only python
    * you can return any quarantined mail to mailq/user mailbox
    * mailbox/maildir scanning and cleaning
    * smtp policy service (greylist)
    * nice statistics via WWW or MRTG
    * easy installation and configuration

%package core
Summary:        Antivirus/anti-spam gateway for smtp server, core files
Requires:       sed
%if 0%{?suse_version}
BuildRequires: aaa_base, python-xml, clamav >= %{CLAMAV_VERSION}
Requires:       aaa_base, smtp_daemon
%else
Requires:       server(smtp)
BuildRequires:  clamav-devel >= %{CLAMAV_VERSION}
Requires:       clamav-lib >= %{CLAMAV_VERSION}
%endif
BuildRequires:  systemd
%{?systemd_requires}
Requires:       spamassassin
BuildRequires:  logwatch
Obsoletes:      sagator-libclamav <= 1.2.3
Obsoletes:      sagator-pydspam <= 0.9.1

%description core
SAGATOR's core files. You can use this package separatelly, if you do
not to depend on other software, required by sagator.

%package webq
Summary:        SAGATOR's web quarantine access
Requires:       sagator-core = %{version}-%{release}
%if 0%{?fedora} || 0%{?rhel} > 7
Requires:       %{python_version}-jinja2
%else
Requires:       python-jinja2
%endif

%description webq
SAGATOR's web quarantine access can be used to allow users (or admin)
to access their emails in sagator's quarantine.

%if 0%{?install_sepolicy}>0
%package        selinux
Summary:        SELinux support for SAGATOR
Requires:       %{name}-core = %{version}-%{release}
Requires(postun): policycoreutils, selinux-policy
BuildRequires: selinux-policy-devel

%description selinux
This package helps moving to the upstream SELinux module.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

# Create a sysusers.d config file
cat >sagator.sysusers.conf <<EOF
u vscan - 'SAGATOR' %{CHROOTDIR} -
EOF

%build
sh configure --prefix=%{_prefix} --filelist --python=%{python_version}
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} PREFIX=%{_prefix} SBINDIR=%{buildroot}%{_sbindir} install
rm -f %{buildroot}%{_datadir}/sagator/etc/sgconf.py* \
  scripts/mkchroot.sh scripts/graphs/*.in
touch %{buildroot}%{_datadir}/%{name}/etc/sgconf.py_
ln -s ../../../..%{_sysconfdir}/sagator.conf \
  %{buildroot}%{_datadir}/%{name}/etc/sgconf.py
mkdir -p %{buildroot}%{CHROOTDIR}/tmp/quarantine
cp -arf scripts/db %{buildroot}%{_datadir}/%{name}/
%find_lang %{name}

install -m0644 -D sagator.sysusers.conf %{buildroot}%{_sysusersdir}/sagator.conf

%post core
touch %{_var}/lib/sagator-mkchroot
if [ $1 = 2 ]; then # upgrade
  [ -f %{_sysconfdir}/sysconfig/sagator ] && . %{_sysconfdir}/sysconfig/sagator || true
  # update configuration
  %{_datadir}/sagator/updatecfg.py || true
fi
%systemd_post %{name}.service

%preun core
%systemd_preun %{name}.service

%postun core
%systemd_postun_with_restart %{name}.service

%if 0%{?install_sepolicy}>0
%post selinux
if selinuxenabled; then
    # Replace the module by the upstream one
    #. /etc/selinux/config 2>/dev/null || :
    semodule -i %{sepolicy} 2>/dev/null || :
    # relabel files
    fixfiles -R %{name} restore || :
    # relabel chroot
    restorecon -R %{CHROOTDIR} || :
fi
%endif

%triggerin core -- sagator-webq,%{BASE_LIBS},%{ARCHIVERS},%{ANTIVIRS},%{ANTISPAMS}
touch %{_var}/lib/sagator-mkchroot

%triggerpostun core -- sagator-webq,%{BASE_LIBS},%{ARCHIVERS},%{ANTIVIRS},%{ANTISPAMS}
touch %{_var}/lib/sagator-mkchroot

%files
# no files, this package just requires others
# exclude sepolicy for builds without selinux module
%if 0%{?install_sepolicy}>0
%exclude %{sepolicy}
%endif

%files core -f filelist
%config(noreplace) %verify(not md5 size mtime) %attr(640,root,vscan) %{_sysconfdir}/%{name}.conf
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/sysconfig/%{name}
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/*/conf.d/%{name}.conf
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/mrtg/%{name}.cfg
%{_unitdir}/%{name}.service
%config(noreplace) %verify(not md5 size mtime) %attr(644,root,root) %{_sysconfdir}/cron.d/%{name}
%doc doc/README doc/FAQ doc/*.txt doc/*.html TODO COPYING ChangeLog test
%doc scripts/graphs scripts/*.sh scripts/log/analyzer.py
%{_bindir}/*
# Fedora 42 merged bin/sbin
%if "%{_bindir}" != "%{_sbindir}"
%{_sbindir}/*
%endif
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.py*
%dir %attr(750,root,vscan) %{_datadir}/%{name}/etc
%{_datadir}/%{name}/etc/*.py*
%exclude %{_datadir}/%{name}/etc/sgconf.py?
%{_datadir}/%{name}/avir
%{_datadir}/%{name}/aspam
%{_datadir}/%{name}/interscan
%{_datadir}/%{name}/srv
%exclude %{_datadir}/%{name}/srv/web
%exclude %{_datadir}/%{name}/srv/templates
%{_datadir}/%{name}/db
%{_mandir}/man*/*
%dir %{CHROOTDIR}
%attr(1777,vscan,vscan) %dir %{CHROOTDIR}/tmp
%attr(0770,vscan,vscan) %dir %{CHROOTDIR}/tmp/quarantine
%{_sysusersdir}/sagator.conf

%files webq -f sagator.lang
%{_datadir}/%{name}/srv/web
%{_datadir}/%{name}/srv/templates

%if 0%{?install_sepolicy}>0
%files selinux
%dir %{_datadir}/%{name}/selinux
%{sepolicy}
%endif

%changelog
%autochangelog
