%global source0_hash 2489745f3ec6b1bf0484b500c1fbc1d10caa80179bf81378fb0d00ee52382fdb

# Set %%bcond_without bootstrap to build without depending on plugins for localhost monitoring
%bcond_with bootstrap

%global with_selinux 1
%global selinuxtype targeted

Name:           nagios
Version:        4.5.11
Release:        1%{?dist}

Summary: Host/service/network monitoring program

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            https://www.nagios.org/projects/nagios-core/
Source0:        https://github.com/NagiosEnterprises/nagioscore/archive/nagios-%{version}.tar.gz#/nagioscore-nagios-%{version}.tar.gz
Source1: nagios.logrotate
Source2: nagios.htaccess
Source3: nagios.internet.cfg
Source4: nagios.htpasswd
Source5: nagios.upgrade_to_v4.ReadMe
Source6: nagios.upgrade_to_v4.sh
Source8: nagios.tmpfiles.conf
# PNG files from the old nagios-0010-Added-several-images-to-the-sample-config.patch
Source10: printer.png
Source11: router.png
Source12: switch.png
Source13: nagios.README.SELinux.rst
Source14: nagios.te
Source15: nagios.fc
Source16: nagios.if

Patch1: nagios-0001-default-init.patch
# Sent upstream
Patch2: nagios-0002-Fix-installation-of-httpd-conf.d-config-file.patch
Patch3: nagios-0003-Install-config-files-too.patch
Patch4: nagios-0004-Fix-path-to-CGI-executables.patch
Patch5: nagios-0005-Fixed-path-to-passwd-file-in-Apache-s-config-file.patch
Patch6: nagios-0006-Added-several-images-to-the-sample-config-revb.patch
Patch9: nagios-0009-fix-localstatedir-for-linux.patch
## This has been requested for security groups not wanting to leak
## their nagios location.
Patch10: nagios-0010-remove-information-leak.patch
## Make it so it knows about all the arches fedora cares about
Patch11: nagios-0011-remove-rpmbuild.patch
Patch12: nagios-0012-fix-spool.patch
Patch13: nagios-0013-fix-plugin.patch
Patch14: nagios-0014-fix-uidgid.patch

BuildRequires:  make
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gd-devel > 1.8
BuildRequires:  gperf
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  zlib-devel
BuildRequires:  perl-generators
BuildRequires:  perl(CPAN)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::Embed)
BuildRequires:  perl(Test::Harness)
%if 0%{?el6}%{?fedora}
BuildRequires:  perl(Test::HTML::Lint)
%endif
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Simple)
BuildRequires:  openssl-devel

# For up-to-date config.sub and config.guess
BuildRequires:  libtool

# For selinux tools
BuildRequires: checkpolicy, selinux-policy-devel

Requires:       httpd
Requires:       php
Requires:       %{_bindir}/mail
Requires:       nagios-common
Requires:       user(nagios)
Requires:       group(nagios)

# This plugins are required for localhost monitoring
%if %{without bootstrap}
Requires:       nagios-plugins-ping
Requires:       nagios-plugins-load
Requires:       nagios-plugins-users
Requires:       nagios-plugins-http
Requires:       nagios-plugins-disk
Requires:       nagios-plugins-ssh
Requires:       nagios-plugins-swap
Requires:       nagios-plugins-procs
%endif

%if 0%{?with_selinux}
# This ensures that the *-selinux package and all it’s dependencies are not pulled
# into containers and other systems that do not use SELinux
Requires:       (%{name}-selinux if selinux-policy-%{selinuxtype})
%endif

Requires(pre):    group(nagios)
Requires(pre):    user(nagios)
%if 0%{?rhel} > 6 || 0%{?fedora} > 20
# For necessary macros
BuildRequires:  systemd
%else
Requires(preun):  initscripts, chkconfig
Requires(post):   initscripts, chkconfig
Requires(postun): initscripts
%endif

%description
Nagios is a program that will monitor hosts and services on your
network.  It has the ability to send email or page alerts when a
problem arises and when a problem is resolved.  Nagios is written
in C and is designed to run under Linux (and some other *NIX
variants) as a background process, intermittently running checks
on various services that you specify.

The actual service checks are performed by separate "plugin" programs
which return the status of the checks to Nagios. The plugins are
available at https://github.com/nagios-plugins/nagios-plugins

This package provides the core program, web interface, and documentation
files for Nagios. Development files are built as a separate package.

%package common
Summary:        Provides common directories, uid and gid among nagios-related packages
Requires(post): shadow-utils
Provides:       user(nagios)
Provides:       group(nagios)

%description common
Provides common directories, uid and gid among nagios-related packages.

%package devel
Summary:        Provides include files that Nagios-related applications may compile against
Requires:       %{name} = %{version}-%{release}

%description devel
Nagios is a program that will monitor hosts and services on your
network. It has the ability to email or page you when a problem arises
and when a problem is resolved. Nagios is written in C and is
designed to run under Linux (and some other *NIX variants) as a
background process, intermittently running checks on various services
that you specify.

This package provides include files that Nagios-related applications
may compile against.

%if 0%{?with_selinux}
# SELinux subpackage
%package selinux
Summary:          SELinux context for %{name}
BuildArch:        noarch
Requires:         selinux-policy-%{selinuxtype}
Requires(post):   selinux-policy-%{selinuxtype}
BuildRequires:    checkpolicy, selinux-policy-devel
%{?selinux_requires}

%description selinux
SElinux security policy for %{name}.
%endif

%package contrib
Summary:          Eventhandlers contributed to nagios
Requires:         %name = %version-%release

%description contrib
Various contributed items used by plugins and other tools.

%if 0%{?with_selinux}
# SELinux contexts are saved so that only affected files can be
# relabeled after the policy module installation
%pre selinux
%selinux_relabel_pre -s %{selinuxtype}
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n nagioscore-nagios-%{version}

install -p -m 0644 %{SOURCE10} %{SOURCE11} %{SOURCE12} html/images/logos/

# Create a sysusers.d config file
cat >nagios.sysusers.conf <<EOF
u nagios - - %{_localstatedir}/spool/%{name} -
EOF

%build
%configure \
    --prefix=%{_datadir}/%{name} \
    --exec-prefix=%{_localstatedir}/lib/%{name} \
    --libdir=%{_libdir}/%{name} \
    --bindir=%{_sbindir} \
    --datadir=%{_datadir}/%{name}/html \
    --libexecdir=%{_libdir}/%{name}/plugins \
    --localstatedir=%{_localstatedir} \
    --with-checkresult-dir=%{_localstatedir}/spool/%{name}/checkresults \
    --with-cgibindir=%{_libdir}/nagios/cgi \
    --sysconfdir=%{_sysconfdir}/%{name} \
    --with-cgiurl=/%{name}/cgi-bin \
    --with-command-user=apache \
    --with-command-group=apache \
    --with-gd-lib=%{_libdir} \
    --with-gd-inc=%{_includedir} \
    --with-htmlurl=/%{name} \
    --with-lockfile=%{_localstatedir}/run/%{name}/%{name}.pid \
%if 0%{?rhel} == 6
    --with-mail=/bin/mail \
    --with-initdir=%{_initrddir} \
    --with-init-type=sysv \
%else
    --with-mail=/usr/bin/mail \
    --with-initdir=%{_unitdir} \
    --with-init-type=systemd \
%endif
    --with-nagios-user=nagios \
    --with-nagios-grp=nagios \
    --with-template-objects \
    --with-template-extinfo \
    --enable-event-broker \
    --disable-static \
    STRIP=/bin/true

%make_build all

### Build our documentation
%make_build dox

### Apparently contrib does not obey configure !
%make_build -C contrib

sed -e "s|/usr/lib/|%{_libdir}/|" %{SOURCE2} > %{name}.htaccess
cp -f %{SOURCE3} internet.cfg
cp -f %{SOURCE5} UpgradeToVersion4.ReadMe
cp -f %{SOURCE6} UpgradeToVersion4.sh
echo >> html/stylesheets/common.css

%if 0%{?with_selinux}
mkdir selinux
# Shipping the whole nagios policy (originally from selinux-policy-contrib)
# this policy module will override the production module
cp -p %{SOURCE14} selinux/
cp -p %{SOURCE15} selinux/
cp -p %{SOURCE16} selinux/

%make_build -f %{_datadir}/selinux/devel/Makefile %{name}.pp
bzip2 -9 %{name}.pp
%endif

%install
%make_install INIT_OPTS="" INSTALL_OPTS="" COMMAND_OPTS="" CGIDIR="%{_libdir}/%{name}/cgi-bin" CFGDIR="%{_sysconfdir}/%{name}" fullinstall

# relocated to sbin (Fedora-specific)
install -d -m 0755 %{buildroot}%{_bindir}
%if 0%{?fedora} < 42 && 0%{?rhel} < 11
mv %{buildroot}%{_sbindir}/nagiostats %{buildroot}%{_bindir}/nagiostats
%endif

install -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}/private
mv %{buildroot}%{_sysconfdir}/%{name}/resource.cfg %{buildroot}%{_sysconfdir}/%{name}/private/resource.cfg

install -D -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/%{name}/passwd

# Install header-file
install -D -m 0644 include/locations.h %{buildroot}%{_includedir}/%{name}/locations.h

# Install logrotate rule
install -D -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

# Make room for event-handlers
install -d -m 0755 %{buildroot}%{_libdir}/%{name}/plugins/eventhandlers
install -d -m 0755 %{buildroot}%{_libdir}/%{name}/plugins/eventhandlers/distributed-monitoring/
install -d -m 0755 %{buildroot}%{_libdir}/%{name}/plugins/eventhandlers/redundancy-scenario1/

install -d -m 0755 %{buildroot}%{_localstatedir}/spool/%{name}/cmd
install -d -m 0755 %{buildroot}%{_localstatedir}/run/%{name}

# Make a run directory
install -d -m 0755 %{buildroot}%{_localstatedir}/run/%{name}

# Make logdirs
install -d -m 0755 %{buildroot}/%{_localstatedir}/log/
install -d -m 0755 %{buildroot}/%{_localstatedir}/log/%{name}/
install -d -m 0755 %{buildroot}/%{_localstatedir}/log/%{name}/archives

# Use systemd unit on rhel7 or any supported Fedora
%if 0%{?rhel} > 6 || 0%{?fedora} > 20
# Install systemd entry
install -D -m 0644 -p %{SOURCE8} %{buildroot}%{_tmpfilesdir}/%{name}.conf

# Remove SystemV init-script
rm -f %{buildroot}%{_initrddir}/nagios

# Fix systemd unit file permissions #1676334
chmod -x %{buildroot}%{_unitdir}/%{name}.service
%endif

# Fix permissions - FIXME remove this when unneeded
chmod 755 %{buildroot}%{_sbindir}/nagios %{buildroot}%{_bindir}/nagiostats

# Install documentation
install -d -m 0755 %{buildroot}%{_datadir}/nagios/html/docs
%{__cp} -r Documentation/html/* %{buildroot}%{_datadir}/nagios/html/docs

%if 0%{?with_selinux}
install -pm 0644 %{SOURCE13} README.SELinux.rst
install -D -m 0644 %{name}.pp.bz2 %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}/%{name}.pp.bz2
install -D -p -m 0644 selinux/%{name}.if %{buildroot}%{_datadir}/selinux/devel/include/distributed/%{name}.if

%endif

### CONTRIB ITEMS TAKEN FROM UPSTREAM NAGIOS SPEC
%make_install -C contrib INSTALL_OPTS=""
install -p -m 644 contrib/eventhandlers/disable_active_service_checks %{buildroot}%{_libdir}/nagios/plugins/eventhandlers/
install -p -m 644 contrib/eventhandlers/disable_notifications %{buildroot}%{_libdir}/nagios/plugins/eventhandlers/
install -p -m 644 contrib/eventhandlers/enable_active_service_checks %{buildroot}%{_libdir}/nagios/plugins/eventhandlers/
install -p -m 644 contrib/eventhandlers/enable_notifications %{buildroot}%{_libdir}/nagios/plugins/eventhandlers/
install -p -m 644 contrib/eventhandlers/submit_check_result %{buildroot}%{_libdir}/nagios/plugins/eventhandlers/

install -p -m 644 contrib/eventhandlers/distributed-monitoring/obsessive_svc_handler %{buildroot}%{_libdir}/nagios/plugins/eventhandlers/distributed-monitoring/
install -p -m 644 contrib/eventhandlers/distributed-monitoring/submit_check_result_via_nsca %{buildroot}%{_libdir}/nagios/plugins/eventhandlers/distributed-monitoring/
install -p -m 644 contrib/eventhandlers/redundancy-scenario1/handle-master-host-event %{buildroot}%{_libdir}/nagios/plugins/eventhandlers/redundancy-scenario1/
install -p -m 644 contrib/eventhandlers/redundancy-scenario1/handle-master-proc-event %{buildroot}%{_libdir}/nagios/plugins/eventhandlers/redundancy-scenario1/

%{__mv} contrib/README contrib/README.contrib

# Fix permissions #2275532
chmod -R g-w %{buildroot}%{_datadir}/%{name} %{buildroot}%{_libdir}/%{name} %{buildroot}%{_sysconfdir} %{buildroot}%{_sbindir}

install -m0644 -D nagios.sysusers.conf %{buildroot}%{_sysusersdir}/nagios.conf

%post
%{_sbindir}/usermod -a -G %{name} apache || :

%if 0%{?rhel} > 6 || 0%{?fedora} > 20
%systemd_post %{name}.service  > /dev/null 2>&1 || :
%else
if [ $1 -eq 1 ]; then
        # Initial installation
        /sbin/chkconfig --add %{name} || :
fi
%endif

%if 0%{?el5}%{?el6}
/sbin/service httpd condrestart > /dev/null 2>&1 || :
if [ $1 -gt 1 ]; then
  /sbin/service nagios reload > /dev/null 2>&1 || :
fi
%else
/usr/bin/systemctl condrestart httpd > /dev/null 2>&1 || :

if [ $1 -gt 1 ]; then
  /usr/bin/systemctl reload nagios  > /dev/null 2>&1 || :
fi
%endif

%preun
%if 0%{?rhel} > 6 || 0%{?fedora} > 20
%systemd_preun %{name}.service
%else
if [ $1 -eq 0 ]; then
        # Package removal, not upgrade
        /sbin/service %{name} stop >/dev/null 2>&1 || :
        /sbin/chkconfig --del %{name} || :
fi
%endif

%postun
%if 0%{?el5}%{?el6}
/sbin/service httpd condrestart > /dev/null 2>&1 || :
%else
/usr/bin/systemctl condrestart httpd  > /dev/null 2>&1 || :
%endif

%if 0%{?fedora} > 20
%triggerun -- %{name} < 3.5.1-2
# Save the current service runlevel info
# User must manually run systemd-sysv-convert --apply opensips
# to migrate them to systemd targets
/usr/bin/systemd-sysv-convert --save %{name} >/dev/null 2>&1 ||:

# Run these because the SysV package being removed won't do them
/sbin/chkconfig --del %{name} >/dev/null 2>&1 || :
/bin/systemctl try-restart %{name}.service >/dev/null 2>&1 || :
%endif

%if 0%{?with_selinux}
%post selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{name}.pp.bz2
%selinux_relabel_post -s %{selinuxtype}

if [ "$1" -le "1" ]; then # First install
   %systemd_postun_with_restart %{name}.service
fi

%postun selinux
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{name}
    %selinux_relabel_post -s %{selinuxtype}
    %systemd_postun_with_restart %{name}.service
fi
%endif

%files
%dir %{_libdir}/%{name}/cgi-bin
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/html
%doc %{_datadir}/%{name}/html/docs
%doc Changelog INSTALLING README.md UPGRADING UpgradeToVersion4.ReadMe UpgradeToVersion4.sh
%doc internet.cfg
%license LICENSE
%{_datadir}/%{name}/html/[^cd]*
%{_datadir}/%{name}/html/contexthelp/

%if 0%{?fedora} < 42 && 0%{?rhel} < 11
%{_sbindir}/*
%endif

%{_bindir}/*
%{_libdir}/%{name}/cgi-bin/*cgi
%if 0%{?rhel} > 6 || 0%{?fedora} > 20
%{_unitdir}/%{name}.service
%{_tmpfilesdir}/%{name}.conf
%else
%{_initrddir}/nagios
%endif
%config(noreplace) %{_sysconfdir}/httpd/conf.d/nagios.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/*cfg
%config(noreplace) %{_sysconfdir}/%{name}/objects/*cfg
%attr(0750,root,nagios) %dir %{_sysconfdir}/%{name}/private
%attr(0750,root,nagios) %dir %{_sysconfdir}/%{name}/objects

%attr(0640,root,nagios) %config(noreplace) %{_sysconfdir}/%{name}/private/resource.cfg
%attr(0640,root,apache) %config(noreplace) %{_sysconfdir}/%{name}/passwd
%attr(0640,root,apache) %config(noreplace) %{_datadir}/%{name}/html/config.inc.php
%attr(2755,nagios,nagios) %dir %{_localstatedir}/spool/%{name}/cmd
%attr(0750,nagios,nagios) %dir %{_localstatedir}/run/%{name}
%attr(0750,nagios,nagios) %dir %{_localstatedir}/log/%{name}
%attr(0750,nagios,nagios) %dir %{_localstatedir}/log/%{name}/archives
%attr(0750,nagios,nagios) %dir %{_localstatedir}/spool/%{name}/checkresults

%files common
%dir %{_sysconfdir}/%{name}
%dir %{_libdir}/%{name}
%attr(0755,root,root) %dir %{_libdir}/%{name}/plugins
%attr(0755,root,root) %dir %{_libdir}/%{name}/plugins/eventhandlers/
%attr(0755,nagios,nagios) %dir %{_localstatedir}/spool/%{name}
%{_sysusersdir}/nagios.conf

%files devel
%{_includedir}/%{name}
%attr(0644,root,root) %{_libdir}/%{name}/libnagios.a

%if 0%{?with_selinux}
%files selinux
%doc README.SELinux.rst
%{_datadir}/selinux/packages/%{selinuxtype}/%{name}.pp.*
%{_datadir}/selinux/devel/include/distributed/%{name}.if
%ghost %verify(not md5 size mode mtime) %{_sharedstatedir}/selinux/%{selinuxtype}/active/modules/200/%{name}
%endif

%files contrib 
%doc contrib/README.contrib
%attr(0750,root,root) %{_libdir}/%{name}/plugins/eventhandlers/*
%{_libdir}/%{name}/cgi/

%changelog
%autochangelog
