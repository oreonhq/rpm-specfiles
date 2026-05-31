%global source0_hash 4d11f7ca6791a7ed3c3069984cb76418335c253563e264e8c178d8033302e421

# http://fedoraproject.org/wiki/Packaging:Guidelines#PIE
# http://fedoraproject.org/wiki/Hardened_Packages
%global _hardened_build 1

%if 0%{?fedora} || 0%{?rhel} > 7
# Enable python3 build by default
%bcond_without python3
%else
%bcond_with python3
%endif

%if 0%{?fedora} >= 41 || 0%{?rhel} >= 10
%bcond_with container_handler
%else
%bcond_without container_handler
%endif


%if 0%{?rhel}%{?suse_version}
    %bcond_with bodhi
%else
    %bcond_without bodhi
%endif

# build abrt-atomic subpackage
%bcond_without atomic

# build abrt-retrace-client by default
%bcond_without retrace

# rpmbuild --define 'desktopvendor mystring'
%if "x%{?desktopvendor}" == "x"
    %define desktopvendor %(source /etc/os-release; echo ${ID})
%endif

%if 0%{?suse_version}
%define dbus_devel dbus-1-devel
%define libjson_devel libjson-devel
%define shadow_utils pwdutils
%else
%define dbus_devel dbus-devel
%define libjson_devel json-c-devel
%define shadow_utils shadow-utils
%endif

# do not append package version to doc directory of subpackages in F20 and later; rhbz#993656
%if "%{_pkgdocdir}" == "%{_docdir}/%{name}"
    %define docdirversion %{nil}
%else
    %define docdirversion -%{version}
%endif

%define glib_ver 2.73.3
%define libreport_ver 2.17.13
%define satyr_ver 0.24

Summary: Automatic bug detection and reporting tool
Name: abrt
Version: 2.17.8
Release: 3%{?dist}
License: GPL-2.0-or-later
URL: https://abrt.readthedocs.org/
Source:        https://github.com/abrt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires: git-core
BuildRequires: %{dbus_devel}
BuildRequires: hostname
BuildRequires: gtk3-devel
BuildRequires: glib2-devel >= %{glib_ver}
BuildRequires: rpm-devel >= 6.0.0
BuildRequires: desktop-file-utils
BuildRequires: libnotify-devel
#why? BuildRequires: file-devel
BuildRequires: make
BuildRequires: gettext
BuildRequires: libxml2-devel
BuildRequires: intltool
BuildRequires: libtool
BuildRequires: libsoup3-devel
BuildRequires: asciidoc
BuildRequires: doxygen
BuildRequires: xmlto
BuildRequires: libreport-devel >= %{libreport_ver}
BuildRequires: satyr-devel >= %{satyr_ver}
BuildRequires: augeas
BuildRequires: libselinux-devel
# Required for the %%{_unitdir} and %%{_tmpfilesdir} macros.
BuildRequires: systemd-rpm-macros
%if %{with python3}
BuildRequires: python3-devel
BuildRequires: python3-systemd
BuildRequires: python3-argcomplete
BuildRequires: python3-dbus
%endif

Requires: libreport >= %{libreport_ver}
Requires: satyr >= %{satyr_ver}
# these only exist on suse
%if 0%{?suse_version}
BuildRequires: dbus-1-glib-devel
Requires: dbus-1-glib
%endif

%{?systemd_requires}
Requires: systemd
Requires: %{name}-libs = %{version}-%{release}
Requires: python3-%{name} = %{version}-%{release}
Requires(pre): %{shadow_utils}
%if %{with python3}
Requires: python3-augeas
Requires: python3-dbus
%endif
%ifarch aarch64 i686 x86_64
Requires: dmidecode
%endif
Requires: libreport-plugin-ureport
%if 0%{?fedora}
Requires: libreport-plugin-systemd-journal
%endif
# to fix upgrade path abrt-plugin-sosreport was removed in 2.14.5 version.
Obsoletes: abrt-plugin-sosreport < 2.14.5
# fros was retired 2025-07, and was initially added to comps to support
# abrt-desktop, so let's obsolete it here
Obsoletes: fros < 1.1-42
Obsoletes: fros-gnome < 1.1-42
Obsoletes: fros-recordmydesktop < 1.1-42

#gui
BuildRequires: libreport-gtk-devel >= %{libreport_ver}
BuildRequires: gsettings-desktop-schemas-devel >= 3.15
#addon-ccpp
BuildRequires: gdb-headless
#addon-kerneloops
BuildRequires: systemd-devel
BuildRequires: %{libjson_devel}
%if %{with bodhi}
# plugin-bodhi
BuildRequires: libreport-web-devel >= %{libreport_ver}
%endif
#desktop
#Default config of addon-ccpp requires gdb
BuildRequires: gdb-headless
#dbus
BuildRequires: polkit-devel
%if %{with python3}
#python3-abrt
BuildRequires: python3-pytest
BuildRequires: python3-sphinx
BuildRequires: python3-libreport
#python3-abrt-doc
BuildRequires: python3-devel
%endif

%description
%{name} is a tool to help users to detect defects in applications and
to create a bug report with all information needed by maintainer to fix it.
It uses plugin system to extend its functionality.

%package libs
Summary: Libraries for %{name}

%description libs
Libraries for %{name}.

%package devel
Summary: Development libraries for %{name}
Requires: abrt-libs = %{version}-%{release}

%description devel
Development libraries and headers for %{name}.

%package gui-libs
Summary: Libraries for %{name}-gui
Requires: %{name}-libs = %{version}-%{release}

%description gui-libs
Libraries for %{name}-gui.

%package gui-devel
Summary: Development libraries for %{name}-gui
Requires: abrt-gui-libs = %{version}-%{release}

%description gui-devel
Development libraries and headers for %{name}-gui.

%package gui
Summary: %{name}'s gui
Requires: %{name} = %{version}-%{release}
Requires: %{name}-dbus = %{version}-%{release}
Requires: gnome-abrt
Requires: gsettings-desktop-schemas >= 3.15
# we used to have abrt-applet, now abrt-gui includes it:
Provides: abrt-applet = %{version}-%{release}
Obsoletes: abrt-applet < 0.0.5
Conflicts: abrt-applet < 0.0.5
Requires: abrt-libs = %{version}-%{release}
Requires: abrt-gui-libs = %{version}-%{release}

%description gui
GTK+ wizard for convenient bug reporting.

%package addon-ccpp
Summary: %{name}'s C/C++ addon
Requires: cpio
Requires: gdb-headless
Requires: elfutils
# Required for local retracing with GDB.
Requires: elfutils-debuginfod-client
%if 0%{!?rhel:1}
%endif
Requires: %{name} = %{version}-%{release}
Requires: abrt-libs = %{version}-%{release}
%if %{with python3}
Requires: python3-libreport
%endif
Obsoletes: abrt-addon-coredump-helper <= 2.12.2
Obsoletes: abrt-retrace-client <= 2.15.1


%description addon-ccpp
This package contains %{name}'s C/C++ analyzer plugin.

%package addon-upload-watch
Summary: %{name}'s upload addon
Requires: %{name} = %{version}-%{release}
Requires: abrt-libs = %{version}-%{release}

%description addon-upload-watch
This package contains hook for uploaded problems.

%package addon-kerneloops
Summary: %{name}'s kerneloops addon
Requires: curl
Requires: %{name} = %{version}-%{release}
%if 0%{!?rhel:1}
Requires: libreport-plugin-kerneloops >= %{libreport_ver}
%endif
Requires: abrt-libs = %{version}-%{release}

%description addon-kerneloops
This package contains plugin for collecting kernel crash information from
system log.

%package addon-xorg
Summary: %{name}'s Xorg addon
Requires: curl
Requires: %{name} = %{version}-%{release}
Requires: abrt-libs = %{version}-%{release}

%description addon-xorg
This package contains plugin for collecting Xorg crash information from Xorg
log.

%package addon-vmcore
Summary: %{name}'s vmcore addon
Requires: %{name} = %{version}-%{release}
Requires: abrt-addon-kerneloops
# On riscv64, kexec-tools does not compile:
# "configure: error: unsupported architecture riscv64"
%ifnarch riscv64
Requires: kexec-tools
%endif
%if %{with python3}
Requires: python3-abrt
Requires: python3-augeas
Requires: python3-systemd
%endif
Requires: util-linux

%description addon-vmcore
This package contains plugin for collecting kernel crash information from
vmcore files.

%package addon-pstoreoops
Summary: %{name}'s pstore oops addon
Requires: %{name} = %{version}-%{release}
Requires: abrt-libs = %{version}-%{release}
Requires: abrt-addon-kerneloops
Obsoletes: abrt-addon-uefioops <= 2.1.6
Provides: abrt-addon-uefioops = %{version}-%{release}

%description addon-pstoreoops
This package contains plugin for collecting kernel oopses from pstore storage.

%if %{with bodhi}
%package plugin-bodhi
Summary: %{name}'s bodhi plugin
Requires: %{name} = %{version}-%{release}
Requires: abrt-libs = %{version}-%{release}
Obsoletes: libreport-plugin-bodhi <= 2.0.10
Provides: libreport-plugin-bodhi = %{version}-%{release}

%description plugin-bodhi
Search for a new updates in bodhi server.
%endif

%if %{with python3}
%package -n python3-abrt-addon
Summary: %{name}'s addon for catching and analyzing Python 3 exceptions
BuildArch: noarch
Requires: %{name} = %{version}-%{release}
Requires: python3-systemd
Requires: python3-abrt

%description -n python3-abrt-addon
This package contains python 3 hook and python analyzer plugin for handling
uncaught exception in python 3 programs.

%if %{with container_handler}
%package -n python3-abrt-container-addon
Summary: %{name}'s container addon for catching Python 3 exceptions
BuildArch: noarch
Conflicts: python3-abrt-addon
Requires: container-exception-logger

%description -n python3-abrt-container-addon
This package contains python 3 hook and handling uncaught exception in python 3
programs in container.
%endif

%endif

%package plugin-machine-id
Summary: %{name}'s plugin to generate machine_id based off dmidecode
Requires: %{name} = %{version}-%{release}

%description plugin-machine-id
This package contains a configuration snippet to enable automatic generation
of machine_id for abrt events.

%package tui
Summary: %{name}'s command line interface
BuildArch: noarch
Requires: %{name} = %{version}-%{release}
Requires: libreport-cli >= %{libreport_ver}
Requires: abrt-libs = %{version}-%{release}
Requires: abrt-dbus
%if %{with python3}
Requires: python3-abrt
Requires: abrt-addon-ccpp
Requires: python3-argcomplete

Provides: %{name}-cli-ng = %{version}-%{release}
Obsoletes: %{name}-cli-ng < 2.12.2
%endif

%description tui
This package contains a simple command line client for processing abrt reports
in command line environment.

%package cli
Summary: Virtual package to make easy default installation on non-graphical environments
Requires: %{name} = %{version}-%{release}
Requires: abrt-tui
Requires: abrt-addon-kerneloops
Requires: abrt-addon-pstoreoops
Requires: abrt-addon-vmcore
Requires: abrt-addon-ccpp
%if %{with python3}
Requires: python3-abrt-addon
%endif
Requires: abrt-addon-xorg
%if ! 0%{?rhel}
%if %{with bodhi}
Requires: abrt-plugin-bodhi
%endif
%if 0%{!?suse_version:1}
Requires: libreport-plugin-bugzilla >= %{libreport_ver}
%endif
Requires: libreport-plugin-logger >= %{libreport_ver}
Requires: libreport-plugin-ureport >= %{libreport_ver}
%if 0%{?fedora}
Requires: libreport-fedora >= %{libreport_ver}
%endif
%endif

%description cli
Virtual package to install all necessary packages for usage from command line
environment.

%package desktop
Summary: Virtual package to make easy default installation on desktop environments
# This package gets installed when anything requests bug-buddy -
# happens when users upgrade Fn to Fn+1;
# or if user just wants "typical desktop installation".
# Installing abrt-desktop should result in the abrt which works without
# any tweaking in abrt.conf (IOW: all plugins mentioned there must be installed)
Requires: %{name} = %{version}-%{release}
Requires: abrt-addon-kerneloops
Requires: abrt-addon-pstoreoops
Requires: abrt-addon-vmcore
Requires: abrt-addon-ccpp
%if %{with python3}
Requires: python3-abrt-addon
%endif
Requires: abrt-addon-xorg
Requires: gdb-headless
Requires: abrt-gui
Requires: gnome-abrt
%if ! 0%{?rhel}
%if %{with bodhi}
Requires: abrt-plugin-bodhi
%endif
%if 0%{!?suse_version:1}
Requires: libreport-plugin-bugzilla >= %{libreport_ver}
%endif
Requires: libreport-plugin-logger >= %{libreport_ver}
Requires: libreport-plugin-ureport >= %{libreport_ver}
%if 0%{?fedora}
Requires: libreport-fedora >= %{libreport_ver}
%endif
%endif
#Requires: abrt-plugin-firefox
Provides: bug-buddy = %{version}-%{release}

%description desktop
Virtual package to install all necessary packages for usage from desktop
environment.

%if %{with atomic}
%package atomic
Summary: Package to make easy default installation on Atomic hosts.
Requires: %{name}-libs = %{version}-%{release}
Conflicts: %{name}-addon-ccpp

%description atomic
Package to install all necessary packages for usage from Atomic
hosts.
%endif

%package dbus
Summary: ABRT DBus service
Requires: %{name} = %{version}-%{release}
Requires: abrt-libs = %{version}-%{release}
Requires: dbus-tools

%description dbus
ABRT DBus service which provides org.freedesktop.problems API on dbus and
uses PolicyKit to authorize to access the problem data.

%if %{with python3}
%package -n python3-abrt
Summary: ABRT Python 3 API
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libs = %{version}-%{release}
Requires: %{name}-dbus = %{version}-%{release}
Requires: python3-dbus
Requires: python3-libreport
Requires: python3-gobject-base

%description -n python3-abrt
High-level API for querying, creating and manipulating
problems handled by ABRT in Python 3.

%package -n python3-abrt-doc
Summary: ABRT Python API Documentation
BuildArch: noarch
Requires: %{name} = %{version}-%{release}
Requires: python3-%{name} = %{version}-%{release}

%description -n python3-abrt-doc
Examples and documentation for ABRT Python 3 API.
%endif

%package console-notification
Summary: ABRT console notification script
Requires: %{name} = %{version}-%{release}
Requires: %{name}-cli = %{version}-%{release}

%description console-notification
A small script which prints a count of detected problems when someone logs in
to the shell

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global __scm_apply_git(qp:m:) %{__git} am --exclude doc/design --exclude doc/project/abrt.tex
%autosetup -S git -p 0

# Create a sysusers.d config file
#uidgid pair 173:173 reserved in setup rhbz#670231
%global abrt_gid_uid 173
cat >abrt.sysusers.conf <<EOF
u abrt %{abrt_gid_uid} - /etc/abrt -
EOF

%build
./autogen.sh

%define default_dump_dir %{_localstatedir}/spool/abrt

CFLAGS="%{optflags} -Werror" %configure \
%if %{without python3}
        --without-python3 \
%endif
%if %{without bodhi}
        --without-bodhi \
%endif
%if %{without atomic}
        --without-atomic \
%endif
%ifnarch %{arm}
        --enable-native-unwinder \
%endif
        --with-defaultdumplocation=%{default_dump_dir} \
        --enable-doxygen-docs \
        --enable-dump-time-unwind \
        --disable-silent-rules

%make_build

%install
%make_install \
%if %{with python3}
             PYTHON=%{__python3} \
%endif
             dbusabrtdocdir=%{_defaultdocdir}/%{name}-dbus%{docdirversion}/html/

%find_lang %{name}

# Remove byte-compiled python files generated by automake.
# automake uses system's python for all *.py files, even
# for those which needs to be byte-compiled with different
# version (python2/python3).
# rpm can do this work and use the appropriate python version.
find %{buildroot} -name "*.py[co]" -delete

# remove all .la and .a files
find %{buildroot} -name '*.la' -or -name '*.a' | xargs rm -f
mkdir -p %{buildroot}%{_localstatedir}/cache/abrt-di
mkdir -p %{buildroot}%{_localstatedir}/lib/abrt
mkdir -p %{buildroot}%{_localstatedir}/run/abrt
mkdir -p %{buildroot}%{_localstatedir}/spool/abrt-upload
mkdir -p %{buildroot}%{default_dump_dir}

desktop-file-install \
        --dir %{buildroot}%{_datadir}/applications \
        src/applet/org.freedesktop.problems.applet.desktop

ln -sf %{_datadir}/applications/org.freedesktop.problems.applet.desktop %{buildroot}%{_sysconfdir}/xdg/autostart/
%if %{with python3}
ln -sf %{_bindir}/abrt %{buildroot}%{_bindir}/abrt-cli
ln -sf %{_mandir}/man1/abrt.1 %{buildroot}%{_mandir}/man1/abrt-cli.1

%if ! %{with container_handler}
rm -vf %{buildroot}%{python3_sitelib}/abrt3_container.pth
rm -vf %{buildroot}%{python3_sitelib}/abrt_exception_handler3_container.py
rm -vf %{buildroot}%{python3_sitelib}/__pycache__/abrt_exception_handler3_container.*
%endif

%endif

# After everything is installed, remove info dir
rm -f %{buildroot}%{_infodir}/dir

install -m0644 -D abrt.sysusers.conf %{buildroot}%{_sysusersdir}/abrt.conf

%check
make check|| {
    # find and print the logs of failed test
    # do not cat tests/testsuite.log because it contains a lot of bloat
    find src -name "test-suite.log" -print -exec cat '{}' \;
    find tests/testsuite.dir -name "testsuite.log" -print -exec cat '{}' \;
    exit 1
}

%post
# $1 == 1 if install; 2 if upgrade
%systemd_post abrtd.service

%post addon-ccpp
# migration from 2.14.1.18
if [ ! -e "%{_localstatedir}/cache/abrt-di/.migration-group-add" ]; then
  chmod -R g+w %{_localstatedir}/cache/abrt-di
  touch "%{_localstatedir}/cache/abrt-di/.migration-group-add"
fi

%systemd_post abrt-journal-core.service
%journal_catalog_update

%post addon-kerneloops
%systemd_post abrt-oops.service
%journal_catalog_update

%post addon-xorg
%systemd_post abrt-xorg.service
%journal_catalog_update

%if %{with python3}
%post -n python3-abrt-addon
%journal_catalog_update
%endif

%post addon-vmcore
%systemd_post abrt-vmcore.service
%journal_catalog_update

%post addon-pstoreoops
%systemd_post abrt-pstoreoops.service

%post addon-upload-watch
%systemd_post abrt-upload-watch.service

%preun
%systemd_preun abrtd.service

%preun addon-ccpp
%systemd_preun abrt-journal-core.service

%preun addon-kerneloops
%systemd_preun abrt-oops.service

%preun addon-xorg
%systemd_preun abrt-xorg.service

%preun addon-vmcore
%systemd_preun abrt-vmcore.service

%preun addon-pstoreoops
%systemd_preun abrt-pstoreoops.service

%preun addon-upload-watch
%systemd_preun abrt-upload-watch.service

%postun
%systemd_postun_with_restart abrtd.service

%postun addon-ccpp
%systemd_postun_with_restart abrt-journal-core.service

%postun addon-kerneloops
%systemd_postun_with_restart abrt-oops.service

%postun addon-xorg
%systemd_postun_with_restart abrt-xorg.service

%postun addon-vmcore
%systemd_postun_with_restart abrt-vmcore.service

%postun addon-pstoreoops
%systemd_postun_with_restart abrt-pstoreoops.service

%postun addon-upload-watch
%systemd_postun_with_restart abrt-upload-watch.service

%post gui
# update icon cache
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%if %{with atomic}
%post atomic
if [ -f /etc/abrt/plugins/CCpp.conf ]; then
    mv /etc/abrt/plugins/CCpp.conf /etc/abrt/plugins/CCpp.conf.rpmsave.atomic || exit 1;
fi

%preun atomic
if [ -L /etc/abrt/plugins/CCpp.conf ]; then
    rm /etc/abrt/plugins/CCpp.conf
fi
if [ -f /etc/abrt/plugins/CCpp.conf.rpmsave.atomic ]; then
    mv /etc/abrt/plugins/CCpp.conf.rpmsave.atomic /etc/abrt/plugins/CCpp.conf || exit 1
fi
%endif

%if 0%{?rhel} && 0%{?rhel} <= 7
%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%post gui-libs -p /sbin/ldconfig

%postun gui-libs -p /sbin/ldconfig

%postun gui
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi
%endif

%posttrans
# update the old problem dirs to contain "type" element
service abrtd condrestart >/dev/null 2>&1 || :

%posttrans addon-ccpp
# Regenerate core_backtraces because of missing crash threads
abrtdir=$(grep "^\s*DumpLocation\b" /etc/abrt/abrt.conf | tail -1 | cut -d'=' -f2 | tr -d ' ')
if test -z "$abrtdir"; then
    abrtdir=%{default_dump_dir}
fi
if test -d "$abrtdir"; then
    for DD in `find "$abrtdir" -mindepth 1 -maxdepth 1 -type d`
    do
        if test -f "$DD/analyzer" && grep -q "^CCpp$" "$DD/analyzer"; then
            /usr/bin/abrt-action-generate-core-backtrace -d "$DD" -- >/dev/null 2>&1 || :
            test -f "$DD/core_backtrace" && chown `stat --format=%U:abrt $DD` "$DD/core_backtrace" || :
        fi
    done
fi

%posttrans addon-kerneloops
service abrt-oops condrestart >/dev/null 2>&1 || :

%posttrans addon-xorg
service abrt-xorg condrestart >/dev/null 2>&1 || :

%posttrans addon-vmcore
service abrt-vmcore condrestart >/dev/null 2>&1 || :
# Copy the configuration file to plugin's directory
test -f /etc/abrt/abrt-harvest-vmcore.conf && {
    echo "Moving /etc/abrt/abrt-harvest-vmcore.conf to /etc/abrt/plugins/vmcore.conf"
    mv -b /etc/abrt/abrt-harvest-vmcore.conf /etc/abrt/plugins/vmcore.conf
}
exit 0

%posttrans addon-pstoreoops
service abrt-pstoreoops condrestart >/dev/null 2>&1 || :

%posttrans dbus
# Force abrt-dbus to restart like we do with the other services
killall abrt-dbus >/dev/null 2>&1 || :

%files -f %{name}.lang
%doc README.md COPYING
%{_unitdir}/abrtd.service
%{_tmpfilesdir}/abrt.conf
%{_sbindir}/abrtd
%{_sbindir}/abrt-server
%{_sbindir}/abrt-auto-reporting
%{_libexecdir}/abrt-handle-event
%{_libexecdir}/abrt-action-ureport
%{_libexecdir}/abrt-action-save-container-data
%{_bindir}/abrt-handle-upload
%{_bindir}/abrt-action-notify
%{_mandir}/man1/abrt-action-notify.1*
%{_bindir}/abrt-action-save-package-data
%{_bindir}/abrt-watch-log
%{_bindir}/abrt-action-analyze-python
%{_bindir}/abrt-action-analyze-xorg
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.problems.daemon.conf
%config(noreplace) %{_sysconfdir}/%{name}/abrt.conf
%config(noreplace) %{_sysconfdir}/%{name}/abrt-action-save-package-data.conf
%config(noreplace) %{_sysconfdir}/%{name}/gpg_keys.conf
%config(noreplace) %{_sysconfdir}/libreport/events.d/abrt_event.conf
%{_mandir}/man5/abrt_event.conf.5*
%config(noreplace) %{_sysconfdir}/libreport/events.d/smart_event.conf
%{_mandir}/man5/smart_event.conf.5*
%dir %attr(0751, root, abrt) %{default_dump_dir}
%dir %attr(0700, abrt, abrt) %{_localstatedir}/spool/%{name}-upload
# abrtd runs as root
%ghost %dir %attr(0755, root, root) %{_localstatedir}/run/%{name}
%ghost %attr(0666, -, -) %{_localstatedir}/run/%{name}/abrt.socket
%ghost %attr(0644, -, -) %{_localstatedir}/run/%{name}/abrtd.pid

%{_mandir}/man1/abrt-handle-upload.1*
%{_mandir}/man1/abrt-server.1*
%{_mandir}/man1/abrt-action-save-package-data.1*
%{_mandir}/man1/abrt-watch-log.1*
%{_mandir}/man1/abrt-action-analyze-python.1*
%{_mandir}/man1/abrt-action-analyze-xorg.1*
%{_mandir}/man1/abrt-auto-reporting.1*
%{_mandir}/man5/abrt.conf.5*
%{_mandir}/man5/abrt-action-save-package-data.conf.5*
%{_mandir}/man5/gpg_keys.conf.5*
%{_mandir}/man8/abrtd.8*
%{_sysusersdir}/abrt.conf

%files libs
%{_libdir}/libabrt.so.*
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/plugins
%dir %{_datadir}/%{name}

# filesystem package should own /usr/share/augeas/lenses directory
%{_datadir}/augeas/lenses/abrt.aug

%files devel
# The complex pattern below (instead of simlpy *) excludes Makefile{.am,.in}:
%doc apidoc/html/*.{html,png,css,js}
%{_includedir}/abrt/abrt-dbus.h
%{_includedir}/abrt/hooklib.h
%{_includedir}/abrt/libabrt.h
%{_includedir}/abrt/problem_api.h
%{_libdir}/libabrt.so
%{_libdir}/pkgconfig/abrt.pc

%files gui-libs
%{_libdir}/libabrt_gui.so.*

%files gui-devel
%{_includedir}/abrt/abrt-config-widget.h
%{_includedir}/abrt/system-config-abrt.h
%{_libdir}/libabrt_gui.so
%{_libdir}/pkgconfig/abrt_gui.pc

%files gui
%dir %{_datadir}/%{name}
# all glade, gtkbuilder and py files for gui
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/%{name}/ui/*
%{_bindir}/abrt-applet
%{_bindir}/system-config-abrt
#%%{_bindir}/test-report
%{_datadir}/applications/org.freedesktop.problems.applet.desktop
%config(noreplace) %{_sysconfdir}/xdg/autostart/org.freedesktop.problems.applet.desktop
%{_datadir}/dbus-1/services/org.freedesktop.problems.applet.service
%{_mandir}/man1/abrt-applet.1*
%{_mandir}/man1/system-config-abrt.1*

%files addon-ccpp
%dir %attr(0775, abrt, abrt) %{_localstatedir}/cache/abrt-di
%config(noreplace) %{_sysconfdir}/%{name}/plugins/CCpp.conf
%{_mandir}/man5/abrt-CCpp.conf.5*
%{_libexecdir}/abrt-gdb-exploitable
%{_libexecdir}/abrt-action-coredump
%config(noreplace) %{_sysconfdir}/libreport/plugins/catalog_journal_ccpp_format.conf
%{_unitdir}/abrt-journal-core.service
%{_journalcatalogdir}/abrt_ccpp.catalog

%dir %{_localstatedir}/lib/abrt

%{_bindir}/abrt-action-analyze-c
%{_bindir}/abrt-action-trim-files
%{_bindir}/abrt-action-analyze-vulnerability
%{_bindir}/abrt-action-generate-backtrace
%{_bindir}/abrt-action-generate-core-backtrace
%{_bindir}/abrt-action-analyze-backtrace
%{_bindir}/abrt-action-list-dsos
%{_bindir}/abrt-action-analyze-ccpp-local
%{_bindir}/abrt-dump-journal-core
%config(noreplace) %{_sysconfdir}/libreport/events.d/ccpp_event.conf
%{_mandir}/man5/ccpp_event.conf.5*
%config(noreplace) %{_sysconfdir}/libreport/events.d/gconf_event.conf
%{_mandir}/man5/gconf_event.conf.5*
%config(noreplace) %{_sysconfdir}/libreport/events.d/vimrc_event.conf
%{_mandir}/man5/vimrc_event.conf.5*
%{_datadir}/libreport/events/analyze_CCpp.xml
%{_datadir}/libreport/events/analyze_LocalGDB.xml
%{_datadir}/libreport/events/collect_xsession_errors.xml
%{_datadir}/libreport/events/collect_GConf.xml
%{_datadir}/libreport/events/collect_vimrc_user.xml
%{_datadir}/libreport/events/collect_vimrc_system.xml
%{_datadir}/libreport/events/post_report.xml
%{_mandir}/man*/abrt-action-analyze-c.*
%{_mandir}/man*/abrt-action-trim-files.*
%{_mandir}/man*/abrt-action-generate-backtrace.*
%{_mandir}/man*/abrt-action-generate-core-backtrace.*
%{_mandir}/man*/abrt-action-analyze-backtrace.*
%{_mandir}/man*/abrt-action-list-dsos.*
%{_mandir}/man*/abrt-action-analyze-ccpp-local.*
%{_mandir}/man*/abrt-action-analyze-vulnerability.*
%{_mandir}/man1/abrt-dump-journal-core.1*

%files addon-upload-watch
%{_sbindir}/abrt-upload-watch
%{_unitdir}/abrt-upload-watch.service
%{_mandir}/man*/abrt-upload-watch.*


%files addon-kerneloops
%config(noreplace) %{_sysconfdir}/libreport/events.d/koops_event.conf
%{_journalcatalogdir}/abrt_koops.catalog
%config(noreplace) %{_sysconfdir}/libreport/plugins/catalog_koops_format.conf
%{_mandir}/man5/koops_event.conf.5*
%config(noreplace) %{_sysconfdir}/%{name}/plugins/oops.conf
%{_unitdir}/abrt-oops.service

%dir %{_localstatedir}/lib/abrt

%{_bindir}/abrt-dump-oops
%{_bindir}/abrt-dump-journal-oops
%{_bindir}/abrt-action-analyze-oops
%{_mandir}/man1/abrt-dump-oops.1*
%{_mandir}/man1/abrt-dump-journal-oops.1*
%{_mandir}/man1/abrt-action-analyze-oops.1*
%{_mandir}/man5/abrt-oops.conf.5*

%files addon-xorg
%config(noreplace) %{_sysconfdir}/libreport/events.d/xorg_event.conf
%{_journalcatalogdir}/abrt_xorg.catalog
%config(noreplace) %{_sysconfdir}/libreport/plugins/catalog_xorg_format.conf
%config(noreplace) %{_sysconfdir}/%{name}/plugins/xorg.conf
%{_unitdir}/abrt-xorg.service
%{_bindir}/abrt-dump-xorg
%{_bindir}/abrt-dump-journal-xorg
%{_mandir}/man1/abrt-dump-xorg.1*
%{_mandir}/man1/abrt-dump-journal-xorg.1*
%{_mandir}/man5/abrt-xorg.conf.5*
%{_mandir}/man5/xorg_event.conf.5*

%files addon-vmcore
%config(noreplace) %{_sysconfdir}/libreport/events.d/vmcore_event.conf
%{_mandir}/man5/vmcore_event.conf.5*
%config(noreplace) %{_sysconfdir}/%{name}/plugins/vmcore.conf
%{_datadir}/libreport/events/analyze_VMcore.xml
%{_unitdir}/abrt-vmcore.service
%{_sbindir}/abrt-harvest-vmcore
%{_bindir}/abrt-action-analyze-vmcore
%{_bindir}/abrt-action-check-oops-for-alt-component
%{_bindir}/abrt-action-check-oops-for-hw-error
%{_mandir}/man1/abrt-harvest-vmcore.1*
%{_mandir}/man5/abrt-vmcore.conf.5*
%{_mandir}/man1/abrt-action-analyze-vmcore.1*
%{_mandir}/man1/abrt-action-check-oops-for-hw-error.1*
%{_journalcatalogdir}/abrt_vmcore.catalog
%config(noreplace) %{_sysconfdir}/libreport/plugins/catalog_vmcore_format.conf

%files addon-pstoreoops
%{_unitdir}/abrt-pstoreoops.service
%{_sbindir}/abrt-harvest-pstoreoops
%{_bindir}/abrt-merge-pstoreoops
%{_mandir}/man1/abrt-harvest-pstoreoops.1*
%{_mandir}/man1/abrt-merge-pstoreoops.1*

%if %{with python3}
%files -n python3-abrt-addon
%config(noreplace) %{_sysconfdir}/%{name}/plugins/python3.conf
%{_mandir}/man5/python3-abrt.conf.5*
%config(noreplace) %{_sysconfdir}/libreport/events.d/python3_event.conf
%{_journalcatalogdir}/python3_abrt.catalog
%config(noreplace) %{_sysconfdir}/libreport/plugins/catalog_python3_format.conf
%{_mandir}/man5/python3_event.conf.5*
%{python3_sitelib}/abrt3.pth
%{python3_sitelib}/abrt_exception_handler3.py
%{python3_sitelib}/__pycache__/abrt_exception_handler3.*

%if %{with container_handler}
%files -n python3-abrt-container-addon
%{python3_sitelib}/abrt3_container.pth
%{python3_sitelib}/abrt_exception_handler3_container.py
%{python3_sitelib}/__pycache__/abrt_exception_handler3_container.*
%endif

%endif

%files plugin-machine-id
%config(noreplace) %{_sysconfdir}/libreport/events.d/machine-id_event.conf
%{_libexecdir}/abrt-action-generate-machine-id

%files cli

%files tui
%if %{with python3}
%{_bindir}/abrt
%{_bindir}/abrt-cli
%{python3_sitelib}/abrtcli/
%{_mandir}/man1/abrt.1*
%{_mandir}/man1/abrt-cli.1*
%endif

%files desktop

%if %{with atomic}
%files atomic
%config(noreplace) %{_sysconfdir}/%{name}/abrt-action-save-package-data.conf
%{_bindir}/abrt-action-save-package-data
%{_mandir}/man1/abrt-action-save-package-data.1*
%{_mandir}/man5/abrt-action-save-package-data.conf.5*
%endif

%if %{with bodhi}
%files plugin-bodhi
%{_bindir}/abrt-bodhi
%{_bindir}/abrt-action-find-bodhi-update
%config(noreplace) %{_sysconfdir}/libreport/events.d/bodhi_event.conf
%{_datadir}/libreport/events/analyze_BodhiUpdates.xml
%{_mandir}/man1/abrt-bodhi.1*
%{_mandir}/man1/abrt-action-find-bodhi-update.1*
%endif

%files dbus
%{_sbindir}/abrt-dbus
%{_mandir}/man8/abrt-dbus.8*
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/dbus-abrt.conf
%{_datadir}/dbus-1/interfaces/org.freedesktop.Problems2.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.Problems2.Entry.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.Problems2.Session.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.Problems2.Task.xml
%{_datadir}/dbus-1/system-services/org.freedesktop.problems.service
%{_datadir}/polkit-1/actions/abrt_polkit.policy
%dir %{_defaultdocdir}/%{name}-dbus%{docdirversion}/
%dir %{_defaultdocdir}/%{name}-dbus%{docdirversion}/html/
%{_defaultdocdir}/%{name}-dbus%{docdirversion}/html/*.html
%{_defaultdocdir}/%{name}-dbus%{docdirversion}/html/*.css
%config(noreplace) %{_sysconfdir}/libreport/events.d/abrt_dbus_event.conf

%if %{with python3}
%files -n python3-abrt
%{python3_sitearch}/problem/
%{_mandir}/man5/python3-abrt.5*

%files -n python3-abrt-doc
%{python3_sitelib}/problem_examples
%endif

%files console-notification
%config(noreplace) %{_sysconfdir}/profile.d/abrt-console-notification.sh

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.17.8-3
- Prepare for Oreon 11 (RP1)
