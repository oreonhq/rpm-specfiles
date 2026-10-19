%global source0_hash 44fd2e1425885288ce8e8da8f18e6b85bd380332c2972554a85860af10f86d0f
%bcond_without xz
%bcond_without plugins
%bcond_without libimaevm
%bcond_without fsverity
%bcond_without zstd
%bcond_without ndb
%bcond_without sqlite
%bcond merged_sbin 1
%bcond legacy_verify 0
%define rpmhome /usr/lib/rpm
%global rpmver 6.0.1
%global baserelease 5
%global sover 10
%global srcver %{rpmver}%{?snapver:-%{snapver}}
%global srcdir %{?snapver:testing}%{!?snapver:rpm-%(echo %{rpmver} | cut -d'.' -f1-2).x}
Summary:        The RPM package management system
Name: rpm
Version: %{rpmver}
Release:        1%{?dist}
Url: https://rpm.org/
License: GPL-2.0-or-later
Source0:        http://ftp.%{name}.org/releases/%{name}-6.0.x/%{name}-%{version}.tar.bz2
Source10: rpmdb-rebuild.service
Requires: coreutils
Requires: popt%{_isa} >= 1.10.2.1
Requires: curl
Conflicts: systemd < 253.5-6
Conflicts: redhat-rpm-config < 291-1
Obsoletes: python2-rpm < %{version}-%{release}
%if %{with xz}
%endif
%if %{with zstd}
%endif
%if %{with sqlite}
%endif
%if %{with plugins}
%endif
%if %{with libimaevm}
%endif
%if %{with fsverity}
%endif
%patchlist
rpm-4.17.x-rpm_dbpath.patch
rpm-4.18.x-siteconfig.patch
rpm-4.9.90-no-man-dirs.patch
rpm-4.20-sysusers.patch
rpm-6.0-rpmformat.patch
0001-Revert-Add-a-deprecation-warning-for-clamp_mtime_to_.patch
rpm-4.7.1-geode-i686.patch
%if %{with merged_sbin}
rpm-4.19.1-unify-bindir-sbindir.patch
%endif
# oreon:deps
BuildRequires:  audit-libs-devel
BuildRequires:  automake
BuildRequires:  bzip2-devel
BuildRequires:  cmake
BuildRequires:  dbus-devel
BuildRequires:  doxygen
BuildRequires:  elfutils-devel
BuildRequires:  elfutils-libelf-devel
BuildRequires:  file-devel
BuildRequires:  fsverity-utils-devel
BuildRequires:  gawk
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  ima-evm-utils-devel
BuildRequires:  libacl-devel
BuildRequires:  libarchive-devel
BuildRequires:  libcap-devel
BuildRequires:  libselinux-devel
BuildRequires:  libtool
BuildRequires:  libzstd-devel
BuildRequires:  lua-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  popt-devel
BuildRequires:  python3-devel
BuildRequires:  readline-devel
BuildRequires:  redhat-rpm-config
BuildRequires:  rpm-sequoia-devel
BuildRequires:  scdoc
BuildRequires:  sqlite-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
The RPM Package Manager (RPM) is a powerful command line driven
package management system capable of installing, uninstalling,
verifying, querying, and updating software packages. Each software
package consists of an archive of files along with information about
the package like its version, a description, etc.

%package libs
Summary:  Libraries for manipulating RPM packages
License:  GPL-2.0-or-later OR LGPL-2.1-or-later
Requires: /usr/bin/systemd-sysusers
Requires(meta): %{name} = %{version}-%{release}
Requires: rpm-sequoia%{_isa} >= 1.9.0
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
Suggests: gdb-minimal
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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

LD_LIBRARY_PATH=%{buildroot}%{_libdir} %py3_check_import rpm rpm.transaction
%install
cd _build
%make_install
cd ..
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
install -m 644 %{SOURCE10} $RPM_BUILD_ROOT/%{_unitdir}
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/cron.daily
install -m 755 scripts/rpm.daily ${RPM_BUILD_ROOT}%{_sysconfdir}/cron.daily/rpm
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d
install -m 644 scripts/rpm.log ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d/rpm
mkdir -p $RPM_BUILD_ROOT/usr/lib/sysimage/rpm
cd _build
for be in %{?with_ndb:ndb} %{?with_sqlite:sqlite}; do
    mkdir ${be}
    tools/rpmdb --rcfile rpmrc --define "_db_backend ${be}" --dbpath=${PWD}/${be} --initdb
    cp -va ${be}/. $RPM_BUILD_ROOT/usr/lib/sysimage/rpm/
done
ln -s ../../bin/find-debuginfo $RPM_BUILD_ROOT/usr/lib/rpm/find-debuginfo.sh
%find_lang rpm
rm -f $RPM_BUILD_ROOT/%{rpmhome}/{perldeps.pl,perl.*,pythond*}
rm -f $RPM_BUILD_ROOT/%{_fileattrsdir}/{perl*,python*}
rm -rf $RPM_BUILD_ROOT/var/tmp
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%pre

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
%files -f %{oreon_filedir}/main.list
%files -n rpm-libs -f %{oreon_filedir}/rpm-libs.list
%files -n rpm-build-libs -f %{oreon_filedir}/rpm-build-libs.list
%files -n rpm-sign-libs -f %{oreon_filedir}/rpm-sign-libs.list
%files -n rpm-devel -f %{oreon_filedir}/rpm-devel.list
%files -n rpm-build -f %{oreon_filedir}/rpm-build.list
%files -n rpm-sign -f %{oreon_filedir}/rpm-sign.list
%files -n python3-rpm -f %{oreon_filedir}/python3-rpm.list
%files -n rpm-apidocs -f %{oreon_filedir}/rpm-apidocs.list
%files -n rpm-cron -f %{oreon_filedir}/rpm-cron.list
%files -n rpm-plugin-selinux -f %{oreon_filedir}/rpm-plugin-selinux.list
%files -n rpm-plugin-unshare -f %{oreon_filedir}/rpm-plugin-unshare.list
%files -n rpm-plugin-syslog -f %{oreon_filedir}/rpm-plugin-syslog.list
%files -n rpm-plugin-systemd-inhibit -f %{oreon_filedir}/rpm-plugin-systemd-inhibit.list
%files -n rpm-plugin-ima -f %{oreon_filedir}/rpm-plugin-ima.list
%files -n rpm-plugin-prioreset -f %{oreon_filedir}/rpm-plugin-prioreset.list
%files -n rpm-plugin-audit -f %{oreon_filedir}/rpm-plugin-audit.list
%files -n rpm-plugin-fsverity -f %{oreon_filedir}/rpm-plugin-fsverity.list
%files -n rpm-plugin-fapolicyd -f %{oreon_filedir}/rpm-plugin-fapolicyd.list
%files -n rpm-plugin-dbus-announce -f %{oreon_filedir}/rpm-plugin-dbus-announce.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - %{rpmver}-1
- Prepare for Oreon 11 (RP1)
