# build against xz?
%bcond_without xz
# build with plugins?
%bcond_without plugins
# build with libimaevm.so
%bcond_without libimaevm
# build with fsverity support?
%if 0%{?rhel}
%bcond_with fsverity
%else
%bcond_without fsverity
%endif
# build with zstd support?
%bcond_without zstd
# build with ndb backend?
%bcond_without ndb
# build with sqlite support?
%bcond_without sqlite

# https://fedoraproject.org/wiki/Changes/Unify_bin_and_sbin
%bcond merged_sbin 1

# https://fedoraproject.org/wiki/Changes/Enforcing_signature_checking_by_default
# Upstream defaults to enforcing in >= 6.0, this is backwards compat switch
%bcond legacy_verify 0

%define rpmhome /usr/lib/rpm

%global rpmver 6.0.1
#global snapver rc1
%global baserelease 5
%global sover 10

%global srcver %{rpmver}%{?snapver:-%{snapver}}
%global srcdir %{?snapver:testing}%{!?snapver:rpm-%(echo %{rpmver} | cut -d'.' -f1-2).x}

Summary: The RPM package management system
Name: rpm
Version: %{rpmver}
Release: %{?snapver:0.%{snapver}.}%{baserelease}%{?dist}
Url: https://rpm.org/
License: GPL-2.0-or-later
Source0: http://ftp.rpm.org/releases/%{srcdir}/rpm-%{srcver}.tar.bz2

Source10: rpmdb-rebuild.service

Requires: coreutils
Requires: popt%{_isa} >= 1.10.2.1
Requires: curl
Conflicts: systemd < 253.5-6

# RPM used to require an %%install hack (shipped by redhat-rpm-config) in order
# to enable debuginfo.  Version 4.19.91 implements this functionality properly
# so this hack is no longer necessary and, in fact, is no longer supported.
# More details: https://github.com/rpm-software-management/rpm/issues/2204
Conflicts: redhat-rpm-config < 291-1

Obsoletes: python2-rpm < %{version}-%{release}

# XXX generally assumed to be installed but make it explicit as rpm
# is a bit special...
BuildRequires: redhat-rpm-config >= 94
BuildRequires: systemd-rpm-macros
BuildRequires: gcc gcc-c++ make
BuildRequires: cmake >= 3.18
BuildRequires: gawk
BuildRequires: elfutils-devel >= 0.112
BuildRequires: elfutils-libelf-devel
BuildRequires: readline-devel zlib-devel
# The popt version here just documents an older known-good version
BuildRequires: popt-devel >= 1.10.2
BuildRequires: file-devel
BuildRequires: gettext-devel
BuildRequires: ncurses-devel
BuildRequires: bzip2-devel >= 0.9.0c-2
BuildRequires: lua-devel >= 5.1
BuildRequires: libcap-devel
BuildRequires: libacl-devel
%if %{with xz}
BuildRequires: xz-devel >= 4.999.8
%endif
BuildRequires: libarchive-devel
%if %{with zstd}
BuildRequires: libzstd-devel
%endif
%if %{with sqlite}
BuildRequires: sqlite-devel
%endif

BuildRequires: doxygen scdoc
BuildRequires: rpm-sequoia-devel >= 1.9.0

# Couple of patches change makefiles so, require for now...
BuildRequires: automake libtool

%if %{with plugins}
BuildRequires: libselinux-devel
BuildRequires: dbus-devel
BuildRequires: audit-libs-devel
%endif

%if %{with libimaevm}
BuildRequires: ima-evm-utils-devel >= 1.0
%endif

%if %{with fsverity}
BuildRequires: fsverity-utils-devel
%endif

%patchlist
# Set rpmdb path to /usr/lib/sysimage/rpm
rpm-4.17.x-rpm_dbpath.patch
# Disable autoconf config.site processing (#962837)
rpm-4.18.x-siteconfig.patch
# In current Fedora, man-pages pkg owns all the localized man directories
rpm-4.9.90-no-man-dirs.patch

# Use systemd-sysusers due to https://github.com/shadow-maint/shadow/issues/940
rpm-4.20-sysusers.patch
# Back out to v4 package format by default until the infra is updated
rpm-6.0-rpmformat.patch

# Temporarily disable the deprecation warning for
# %%clamp_mtime_to_source_date_epoch, details here:
# https://src.fedoraproject.org/rpms/redhat-rpm-config/pull-request/298
0001-Revert-Add-a-deprecation-warning-for-clamp_mtime_to_.patch

# Patches already upstream:

# These are not yet upstream
rpm-4.7.1-geode-i686.patch

%if %{with merged_sbin}
# Make %%_sbindir and %%_bindir the same
rpm-4.19.1-unify-bindir-sbindir.patch
%endif

%description
The RPM Package Manager (RPM) is a powerful command line driven
package management system capable of installing, uninstalling,
verifying, querying, and updating software packages. Each software
package consists of an archive of files along with information about
the package like its version, a description, etc.

%package libs
Summary:  Libraries for manipulating RPM packages
License:  GPL-2.0-or-later OR LGPL-2.1-or-later
# Either full systemd or systemd-standalone-sysusers
Requires: /usr/bin/systemd-sysusers
Requires(meta): %{name} = %{version}-%{release}
# >= 1.9.0 required for pgpDigParamsSalt()
Requires: rpm-sequoia%{_isa} >= 1.9.0
# Most systems should have a central package operations log
Recommends: rpm-plugin-audit

%description libs
This package contains the RPM shared libraries.

%package build-libs
Summary:  Libraries for building RPM packages
Requires: rpm-libs%{_isa} = %{version}-%{release}

%description build-libs
This package contains the RPM shared libraries for building packages.

%package sign-libs
Summary:  Libraries for signing RPM packages
Requires: rpm-libs%{_isa} = %{version}-%{release}
Requires: %{_bindir}/gpg2

%description sign-libs
This package contains the RPM shared libraries for signing packages.

%package devel
Summary:  Development files for manipulating RPM packages
License:  GPL-2.0-or-later OR LGPL-2.1-or-later
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libs%{_isa} = %{version}-%{release}
Requires: %{name}-build-libs%{_isa} = %{version}-%{release}
Requires: %{name}-sign-libs%{_isa} = %{version}-%{release}
Requires: popt-devel%{_isa}

%description devel
This package contains the RPM C library and header files. These
development files will simplify the process of writing programs that
manipulate RPM packages and databases. These files are intended to
simplify the process of creating graphical package managers or any
other tools that need an intimate knowledge of RPM packages in order
to function.

This package should be installed if you want to develop programs that
will manipulate RPM packages and databases.

%package build
Summary: Scripts and executable programs used to build packages
Requires: rpm = %{version}-%{release}
Requires: elfutils >= 0.128 binutils
Requires: findutils sed grep gawk diffutils file patch >= 2.5
Requires: tar unzip gzip bzip2 cpio xz
%if %{with zstd}
Requires: zstd
%endif
Requires: debugedit >= 0.3
Requires: pkgconfig >= 1:0.24
Requires: /usr/bin/gdb-add-index
# https://fedoraproject.org/wiki/Changes/Minimal_GDB_in_buildroot
Suggests: gdb-minimal
# Technically rpmbuild doesn't require any external configuration, but
# creating distro-compatible packages does. To make the common case
# "just work" while allowing for alternatives, depend on a virtual
# provide, typically coming from redhat-rpm-config.
Requires: system-rpm-config

%description build
The rpm-build package contains the scripts and executable programs
that are used to build packages using the RPM Package Manager.

%package sign
Summary: Package signing support
Requires: rpm-sign-libs%{_isa} = %{version}-%{release}

%description sign
This package contains support for digitally signing RPM packages.

%package -n python3-%{name}
Summary: Python 3 bindings for apps which will manipulate RPM packages
BuildRequires: python3-devel
%{?python_provide:%python_provide python3-%{name}}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Provides: %{name}-python3 = %{version}-%{release}
Obsoletes: %{name}-python3 < %{version}-%{release}

%description -n python3-%{name}
The python3-rpm package contains a module that permits applications
written in the Python programming language to use the interface
supplied by RPM Package Manager libraries.

This package should be installed if you want to develop Python 3
programs that will manipulate RPM packages and databases.

%package apidocs
Summary: API documentation for RPM libraries
BuildArch: noarch

%description apidocs
This package contains API documentation for developing applications
that will manipulate RPM packages and databases.

%package cron
Summary: Create daily logs of installed packages.
BuildArch: noarch
Requires: crontabs logrotate rpm = %{version}-%{release}

%description cron
This package contains a cron job which creates daily logs of installed
packages on a system.

%if %{with plugins}
%package plugin-selinux
Summary: Rpm plugin for SELinux functionality
Requires: rpm-libs%{_isa} = %{version}-%{release}
Requires(meta): selinux-policy-base

%description plugin-selinux
%{summary}.

%package plugin-unshare
Summary: Rpm plugin for Linux namespace isolation functionality
Requires: rpm-libs%{_isa} = %{version}-%{release}

%description plugin-unshare
%{summary}.

%package plugin-syslog
Summary: Rpm plugin for syslog functionality
Requires: rpm-libs%{_isa} = %{version}-%{release}

%description plugin-syslog
%{summary}.

%package plugin-systemd-inhibit
Summary: Rpm plugin for systemd inhibit functionality
Requires: rpm-libs%{_isa} = %{version}-%{release}

%description plugin-systemd-inhibit
This plugin blocks systemd from entering idle, sleep or shutdown while an rpm
transaction is running using the systemd-inhibit mechanism.

%if %{with libimaevm}
%package plugin-ima
Summary: Rpm plugin ima file signatures
Requires: rpm-libs%{_isa} = %{version}-%{release}

%description plugin-ima
%{summary}.
%endif

%package plugin-prioreset
Summary: Rpm plugin for resetting scriptlet priorities for SysV init
Requires: rpm-libs%{_isa} = %{version}-%{release}

%description plugin-prioreset
%{summary}.

Useful on legacy SysV init systems if you run rpm transactions with
nice/ionice priorities. Should not be used on systemd systems.

%package plugin-audit
Summary: Rpm plugin for logging audit events on package operations
Requires: rpm-libs%{_isa} = %{version}-%{release}

%description plugin-audit
%{summary}.

%if %{with fsverity}
%package plugin-fsverity
Summary: Rpm plugin for fsverity file signatures
Requires: rpm-libs%{_isa} = %{version}-%{release}

%description plugin-fsverity
%{summary}.
%endif

%package plugin-fapolicyd
Summary: Rpm plugin for fapolicyd support
Requires: rpm-libs%{_isa} = %{version}-%{release}
Provides: fapolicyd-plugin = %{version}-%{release}
# fapolicyd-dnf-plugin currently at 1.0.4
Obsoletes: fapolicyd-dnf-plugin < 1.0.5

%description plugin-fapolicyd
%{summary}.

See https://people.redhat.com/sgrubb/fapolicyd/ for information about
the fapolicyd daemon.

%package plugin-dbus-announce
Summary: Rpm plugin for announcing transactions on the DBUS
Requires: rpm-libs%{_isa} = %{version}-%{release}

%description plugin-dbus-announce
The plugin announces basic information about rpm transactions to the
system DBUS - like packages installed or removed.  Other programs can
subscribe to the signals to get notified when packages on the system
change.

# with plugins
%endif

%prep
%autosetup -n rpm-%{srcver} -p1

%if %{with legacy_verify}
sed -i -e "s:%%_pkgverify_level all:%%_pkgverify_level digest:g" macros.in
%endif

%build
%set_build_flags

mkdir _build
cd _build
cmake \
      -DCMAKE_INSTALL_PREFIX=%{_usr} \
      -DCMAKE_INSTALL_SHAREDSTATEDIR:PATH=%{_var}/lib \
      -DENABLE_BDB_RO=ON \
      %{!?with_ndb:-DENABLE_NDB=OFF} \
      %{!?with_sqlite:-DENABLE_SQLITE=OFF} \
      %{!?with_plugins:-DENABLE_PLUGINS=OFF} \
      %{?with_fsverity:-DWITH_FSVERITY=ON} \
      %{?with_libimaevm:-DWITH_IMAEVM=ON} \
      %{!?with_check:-DENABLE_TESTSUITE=OFF} \
      -DWITH_DOXYGEN=ON \
      -DRPM_VENDOR=redhat \
  ..

%make_build

%check
# We can't run the actual test-suite from %%check,
# at least check the Python module is importable:
LD_LIBRARY_PATH=%{buildroot}%{_libdir} %py3_check_import rpm rpm.transaction

%install
cd _build
%make_install
cd ..

mkdir -p $RPM_BUILD_ROOT%{_unitdir}
install -m 644 %{SOURCE10} $RPM_BUILD_ROOT/%{_unitdir}

# Save list of packages through cron
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/cron.daily
install -m 755 scripts/rpm.daily ${RPM_BUILD_ROOT}%{_sysconfdir}/cron.daily/rpm

mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d
install -m 644 scripts/rpm.log ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d/rpm

mkdir -p $RPM_BUILD_ROOT/usr/lib/sysimage/rpm
cd _build

# init an empty database for %ghost'ing for all supported backends
for be in %{?with_ndb:ndb} %{?with_sqlite:sqlite}; do
    mkdir ${be}
    tools/rpmdb --rcfile rpmrc --define "_db_backend ${be}" --dbpath=${PWD}/${be} --initdb
    cp -va ${be}/. $RPM_BUILD_ROOT/usr/lib/sysimage/rpm/
done

# some packages invoke find-debuginfo directly, preserve compat for now
ln -s ../../bin/find-debuginfo $RPM_BUILD_ROOT/usr/lib/rpm/find-debuginfo.sh

%find_lang rpm

# These live in perl-generators and python-rpm-generators now
rm -f $RPM_BUILD_ROOT/%{rpmhome}/{perldeps.pl,perl.*,pythond*}
rm -f $RPM_BUILD_ROOT/%{_fileattrsdir}/{perl*,python*}
rm -rf $RPM_BUILD_ROOT/var/tmp

%pre
# Symlink all rpmdb files to the new location if we're still using /var/lib/rpm
if [ -d /var/lib/rpm ]; then
    mkdir -p /usr/lib/sysimage/rpm
    rpmdb_files=$(find /var/lib/rpm -maxdepth 1 -type f | sed 's|^/var/lib/rpm/||g' | sort)
    for rpmdb_file in ${rpmdb_files[@]}; do
        ln -sfr /var/lib/rpm/${rpmdb_file} /usr/lib/sysimage/rpm/${rpmdb_file}
    done
fi

%post
%systemd_post rpmdb-rebuild.service

%preun
%systemd_preun rpmdb-rebuild.service

%postun
%systemd_postun rpmdb-rebuild.service

%files -f _build/rpm.lang
%license COPYING
%doc CREDITS docs/manual/[a-z]*
%doc %{_defaultdocdir}/rpm/CONTRIBUTING.md
%doc %{_defaultdocdir}/rpm/COPYING
%doc %{_defaultdocdir}/rpm/INSTALL
%doc %{_defaultdocdir}/rpm/README

%{_unitdir}/rpmdb-rebuild.service

%dir %{_sysconfdir}/rpm

%attr(0755, root, root) %dir /usr/lib/sysimage/rpm
%attr(0644, root, root) %ghost %config(missingok,noreplace) /usr/lib/sysimage/rpm/*
%attr(0644, root, root) %ghost /usr/lib/sysimage/rpm/.*.lock

%{_bindir}/rpm
%{_bindir}/rpm2archive
%{_bindir}/rpm2cpio
%{_bindir}/rpmdb
%{_bindir}/rpmkeys
%{_bindir}/rpmquery
%{_bindir}/rpmverify
%{_bindir}/rpmsort

%{_mandir}/man1/rpm2archive.1*
%{_mandir}/man1/rpm2cpio.1*
%{_mandir}/man1/rpmsort.1*
%{_mandir}/man5/rpm-config.5*
%{_mandir}/man5/rpm-macrofile.5*
%{_mandir}/man5/rpm-manifest.5*
%{_mandir}/man5/rpm-rpmrc.5*
%{_mandir}/man7/rpm-lua.7*
%{_mandir}/man7/rpm-macros.7*
%{_mandir}/man7/rpm-payloadflags.7*
%{_mandir}/man7/rpm-queryformat.7*
%{_mandir}/man7/rpm-version.7*
%{_mandir}/man8/rpm.8*
%{_mandir}/man8/rpmdb.8*
%{_mandir}/man8/rpmkeys.8*
%{_mandir}/man8/rpm-common.8*
%{_mandir}/man8/rpm-plugins.8*

%attr(0755, root, root) %dir %{rpmhome}
%{rpmhome}/macros
%exclude %{rpmhome}/macros.d/macros.transaction*
%{rpmhome}/macros.d
%{rpmhome}/lua
%{rpmhome}/rpmpopt*
%{rpmhome}/rpmrc

%{rpmhome}/rpmdb_*
%{rpmhome}/rpm.daily
%{rpmhome}/rpm.log
%{rpmhome}/rpm.supp
%{rpmhome}/rpm2cpio.sh
%{rpmhome}/tgpg

%{rpmhome}/platform
%{rpmhome}/sysusers.sh

%dir %{rpmhome}/fileattrs

%files libs
%{_libdir}/librpmio.so.%{sover}
%{_libdir}/librpm.so.%{sover}
%{_libdir}/librpmio.so.%{sover}.*
%{_libdir}/librpm.so.%{sover}.*
%if %{with plugins}
%dir %{_libdir}/rpm-plugins

%files plugin-syslog
%{rpmhome}/macros.d/macros.transaction_syslog
%{_libdir}/rpm-plugins/syslog.so
%{_mandir}/man8/rpm-plugin-syslog.8*

%files plugin-selinux
%{rpmhome}/macros.d/macros.transaction_selinux
%{_libdir}/rpm-plugins/selinux.so
%{_mandir}/man8/rpm-plugin-selinux.8*

%files plugin-systemd-inhibit
%{rpmhome}/macros.d/macros.transaction_systemd_inhibit
%{_libdir}/rpm-plugins/systemd_inhibit.so
%{_mandir}/man8/rpm-plugin-systemd-inhibit.8*

%if %{with libimaevm}
%files plugin-ima
%{rpmhome}/macros.d/macros.transaction_ima
%{_libdir}/rpm-plugins/ima.so
%{_mandir}/man8/rpm-plugin-ima.8*
%endif

%if %{with fsverity}
%{rpmhome}/macros.d/macros.transaction_fsverity
%files plugin-fsverity
%{_libdir}/rpm-plugins/fsverity.so
%endif

%files plugin-fapolicyd
%{rpmhome}/macros.d/macros.transaction_fapolicyd
%{_libdir}/rpm-plugins/fapolicyd.so
%{_mandir}/man8/rpm-plugin-fapolicyd.8*

%files plugin-prioreset
%{rpmhome}/macros.d/macros.transaction_prioreset
%{_libdir}/rpm-plugins/prioreset.so
%{_mandir}/man8/rpm-plugin-prioreset.8*

%files plugin-audit
%{rpmhome}/macros.d/macros.transaction_audit
%{_libdir}/rpm-plugins/audit.so
%{_mandir}/man8/rpm-plugin-audit.8*
# with plugins

%files plugin-dbus-announce
%{rpmhome}/macros.d/macros.transaction_dbus_announce
%{_libdir}/rpm-plugins/dbus_announce.so
%{_mandir}/man8/rpm-plugin-dbus-announce.8*
%{_datadir}/dbus-1/system.d/org.rpm.conf
%endif

%files plugin-unshare
%{rpmhome}/macros.d/macros.transaction_unshare
%{_libdir}/rpm-plugins/unshare.so
%{_mandir}/man8/rpm-plugin-unshare.8*

%files build-libs
%{_libdir}/librpmbuild.so.%{sover}
%{_libdir}/librpmbuild.so.%{sover}.*

%files sign-libs
%{_libdir}/librpmsign.so.%{sover}
%{_libdir}/librpmsign.so.%{sover}.*

%files build
%{_bindir}/rpmbuild
%{_bindir}/gendiff
%{_bindir}/rpmspec
%{_bindir}/rpmlua

%{_mandir}/man1/gendiff.1*
%{_mandir}/man1/rpmbuild.1*
%{_mandir}/man1/rpmdeps.1*
%{_mandir}/man1/rpmspec.1*
%{_mandir}/man1/rpmlua.1*
%{_mandir}/man1/rpm-setup-autosign.1*
%{_mandir}/man1/rpmuncompress.1*
%{_mandir}/man5/rpmbuild-config.5.*

%{rpmhome}/brp-*
%{rpmhome}/check-*
%{rpmhome}/find-lang.sh
%{rpmhome}/*provides*
%{rpmhome}/*requires*
%{rpmhome}/*deps*
%{rpmhome}/*.prov
%{rpmhome}/*.req
%{rpmhome}/fileattrs/*
%{rpmhome}/find-debuginfo.sh
%{rpmhome}/rpmuncompress
%{rpmhome}/rpmdump
%{rpmhome}/rpm-setup-autosign

%files sign
%{_bindir}/rpmsign
%{_mandir}/man1/rpmsign.1*

%files -n python3-%{name}
%dir %{python3_sitearch}/rpm
%{python3_sitearch}/rpm-%{rpmver}*.egg-info
%{python3_sitearch}/rpm/__init__.py
%{python3_sitearch}/rpm/transaction.py
%{python3_sitearch}/rpm/_rpm.so
%artifact %{python3_sitearch}/rpm/__pycache__/

# Python examples
%{_defaultdocdir}/rpm/examples/

%files devel
%{_mandir}/man1/rpmgraph.1*
%{_bindir}/rpmgraph
%{_libdir}/librp*[a-z].so
%{_libdir}/pkgconfig/rpm.pc
%{_libdir}/cmake/rpm/
%{_includedir}/rpm/

%files cron
%{_sysconfdir}/cron.daily/rpm
%config(noreplace) %{_sysconfdir}/logrotate.d/rpm

%files apidocs
%license COPYING
%doc %{_defaultdocdir}/rpm/API/

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - %{rpmver}-1
- Prepare for Oreon 11 (RP1)
