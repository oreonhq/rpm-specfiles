%global source0_hash 6d1863ba058d59acafb97f012eef2f882d41cbc497d215fecb07ad5595a3d04a
%bcond_with bootstrap
%global with_selinux 1
%global selinuxtype targeted
Name:           nagios
Version:        4.5.14
Release:        1%{?dist}
Summary:        Host/service/network monitoring program
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
Source10: printer.png
Source11: router.png
Source12: switch.png
Source13: nagios.README.SELinux.rst
Source14: nagios.te
Source15: nagios.fc
Source16: nagios.if
Patch1: nagios-0001-default-init.patch
Patch2: nagios-0002-Fix-installation-of-httpd-conf.d-config-file.patch
Patch3: nagios-0003-Install-config-files-too.patch
Patch4: nagios-0004-Fix-path-to-CGI-executables.patch
Patch5: nagios-0005-Fixed-path-to-passwd-file-in-Apache-s-config-file.patch
Patch6: nagios-0006-Added-several-images-to-the-sample-config-revb.patch
Patch9: nagios-0009-fix-localstatedir-for-linux.patch
Patch10: nagios-0010-remove-information-leak.patch
Patch11: nagios-0011-remove-rpmbuild.patch
Patch12: nagios-0012-fix-spool.patch
Patch13: nagios-0013-fix-plugin.patch
Patch14: nagios-0014-fix-uidgid.patch
Requires:       httpd
Requires:       php
Requires:       %{_bindir}/mail
Requires:       nagios-common
Requires:       user(nagios)
Requires:       group(nagios)
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
Requires:       (%{name}-selinux if selinux-policy-%{selinuxtype})
%endif
Requires(pre):    group(nagios)
Requires(pre):    user(nagios)
Requires(preun):  initscripts, chkconfig
Requires(post):   initscripts, chkconfig
Requires(postun): initscripts
# oreon:deps
BuildRequires:  checkpolicy
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gd-devel
BuildRequires:  gperf
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  perl(CPAN)
BuildRequires:  perl(ExtUtils::Embed)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Simple)
BuildRequires:  perl-generators
BuildRequires:  pkgconfig(systemd)
BuildRequires:  selinux-policy
BuildRequires:  selinux-policy-devel
BuildRequires:  zlib-devel
# /oreon:deps
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
    --with-mail=/usr/bin/mail \
    --with-initdir=%{_unitdir} \
    --with-init-type=systemd \
    --with-nagios-user=nagios \
    --with-nagios-grp=nagios \
    --with-template-objects \
    --with-template-extinfo \
    --enable-event-broker \
    --disable-static \
    STRIP=/bin/true
%make_build all
%make_build dox
%make_build -C contrib
sed -e "s|/usr/lib/|%{_libdir}/|" %{SOURCE2} > %{name}.htaccess
cp -f %{SOURCE3} internet.cfg
cp -f %{SOURCE5} UpgradeToVersion4.ReadMe
cp -f %{SOURCE6} UpgradeToVersion4.sh
echo >> html/stylesheets/common.css
%if 0%{?with_selinux}
mkdir selinux
cp -p %{SOURCE14} selinux/
cp -p %{SOURCE15} selinux/
cp -p %{SOURCE16} selinux/
%make_build -f %{_datadir}/selinux/devel/Makefile %{name}.pp
bzip2 -9 %{name}.pp
%endif
%install
%make_install INIT_OPTS="" INSTALL_OPTS="" COMMAND_OPTS="" CGIDIR="%{_libdir}/%{name}/cgi-bin" CFGDIR="%{_sysconfdir}/%{name}" fullinstall
install -d -m 0755 %{buildroot}%{_bindir}
%if 0%{?fedora} < 42 && 0%{?rhel} < 11 && 0%{?oreon} < 11
mv %{buildroot}%{_sbindir}/nagiostats %{buildroot}%{_bindir}/nagiostats
%endif
install -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}/private
mv %{buildroot}%{_sysconfdir}/%{name}/resource.cfg %{buildroot}%{_sysconfdir}/%{name}/private/resource.cfg
install -D -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/%{name}/passwd
install -D -m 0644 include/locations.h %{buildroot}%{_includedir}/%{name}/locations.h
install -D -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
install -d -m 0755 %{buildroot}%{_libdir}/%{name}/plugins/eventhandlers
install -d -m 0755 %{buildroot}%{_libdir}/%{name}/plugins/eventhandlers/distributed-monitoring/
install -d -m 0755 %{buildroot}%{_libdir}/%{name}/plugins/eventhandlers/redundancy-scenario1/
install -d -m 0755 %{buildroot}%{_localstatedir}/spool/%{name}/cmd
install -d -m 0755 %{buildroot}%{_localstatedir}/run/%{name}
install -d -m 0755 %{buildroot}%{_localstatedir}/run/%{name}
install -d -m 0755 %{buildroot}/%{_localstatedir}/log/
install -d -m 0755 %{buildroot}/%{_localstatedir}/log/%{name}/
install -d -m 0755 %{buildroot}/%{_localstatedir}/log/%{name}/archives
chmod 755 %{buildroot}%{_sbindir}/nagios %{buildroot}%{_bindir}/nagiostats
install -d -m 0755 %{buildroot}%{_datadir}/nagios/html/docs
%{__cp} -r Documentation/html/* %{buildroot}%{_datadir}/nagios/html/docs
%if 0%{?with_selinux}
install -pm 0644 %{SOURCE13} README.SELinux.rst
install -D -m 0644 %{name}.pp.bz2 %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}/%{name}.pp.bz2
install -D -p -m 0644 selinux/%{name}.if %{buildroot}%{_datadir}/selinux/devel/include/distributed/%{name}.if
%endif
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
chmod -R g-w %{buildroot}%{_datadir}/%{name} %{buildroot}%{_libdir}/%{name} %{buildroot}%{_sysconfdir} %{buildroot}%{_sbindir}
install -m0644 -D nagios.sysusers.conf %{buildroot}%{_sysusersdir}/nagios.conf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%{_sbindir}/usermod -a -G %{name} apache || :
if [ $1 -eq 1 ]; then
        /sbin/chkconfig --add %{name} || :
fi
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

if [ $1 -eq 0 ]; then
        /sbin/service %{name} stop >/dev/null 2>&1 || :
        /sbin/chkconfig --del %{name} || :
fi
%postun

%if 0%{?el5}%{?el6}
/sbin/service httpd condrestart > /dev/null 2>&1 || :
%else
/usr/bin/systemctl condrestart httpd  > /dev/null 2>&1 || :
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
%files -f %{oreon_filedir}/main.list
%files -n nagios-common -f %{oreon_filedir}/nagios-common.list
%files -n nagios-devel -f %{oreon_filedir}/nagios-devel.list
%files -n nagios-selinux -f %{oreon_filedir}/nagios-selinux.list
%files -n nagios-contrib -f %{oreon_filedir}/nagios-contrib.list

%changelog

%autochangelog
