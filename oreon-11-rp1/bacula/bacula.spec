%global source20_hash 594eef0dd06a92a1b62def8b4c8018d78caf738ab85748774b3c826c1b6a7848
%global source0_hash 1148521f901b6623a7ee2bca51e3d742ba22b5644b83a10b936c27dc12a9d090
%global commit 66885387c9f761253988321de9c4bbfc1660717d
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global uid 133
%global username bacula
Name:               bacula
Version:            17.0.0
Release:        1%{?dist}
Summary:        Cross platform network backup for Linux, Unix, Mac and Windows
License:            LicenseRef-Bacula
URL:                http://www.bacula.org
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source2:            quickstart_postgresql.txt
Source3:            quickstart_mysql.txt
Source4:            quickstart_sqlite3.txt
Source5:            README.md
Source6:            %{name}.logrotate
Source7:            %{name}-storage.xml
Source8:            %{name}-director.xml
Source10:           %{name}-fd.service
Source11:           %{name}-dir.service
Source12:           %{name}-sd.service
Source15:           %{name}-fd.sysconfig
Source16:           %{name}-dir.sysconfig
Source17:           %{name}-sd.sysconfig
Source19:        bacula-tray-monitor.png
Source20:            https://gitlab.bacula.org/bacula-community-edition/libs3/-/archive/%{commit}/libs3-%{shortcommit}.tar.bz2
Source21:            libs3-openssl.patch
Patch1:             %{name}-openssl.patch
Patch2:             %{name}-seg-fault.patch
Patch3:             %{name}-non-free-code.patch
Patch4:             %{name}-traceback-man.patch
Patch5:             %{name}-compile-options.patch
Patch6:             %{name}-install.patch
Patch7:             %{name}-desktop.patch
Patch8:             %{name}-docker-plugin.patch
Patch9:             %{name}-autoconf.patch
Patch10:            %{name}-scripts.patch
Requires(post):     firewalld-filesystem
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  firewalld-filesystem
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  libacl-devel
BuildRequires:  libcap-devel
BuildRequires:  libcurl-devel
BuildRequires:  libpq-devel
BuildRequires:  libstdc++-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  libxml2-devel
BuildRequires:  libzstd-devel
BuildRequires:  lzo-devel
BuildRequires:  make
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  ncurses-devel
BuildRequires:  openldap-devel
BuildRequires:  openssl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  qt5-qtbase-devel
BuildRequires:  readline-devel
BuildRequires:  sed
BuildRequires:  sqlite-devel
BuildRequires:  systemd
BuildRequires:  zlib-devel
# /oreon:deps
%description
Bacula is a set of programs that allow you to manage the backup, recovery, and
verification of computer data across a network of different computers. It is
based on a client/server architecture and is efficient and relatively easy to
use, while offering many advanced storage management features that make it easy
to find and recover lost or damaged files.

%package libs
Summary:            Bacula libraries
%description libs
Bacula is a set of programs that allow you to manage the backup,
recovery, and verification of computer data across a network of
different computers. It is based on a client/server architecture.

This package contains basic Bacula libraries, which are used by all
Bacula programs.

%package libs-sql
Summary:            Bacula SQL libraries
%description libs-sql
Bacula is a set of programs that allow you to manage the backup, recovery, and
verification of computer data across a network of different computers. It is
based on a client/server architecture.

This package contains the SQL Bacula libraries, which are used by Director and
Storage daemons. You have to select your preferred catalog library through the
alternatives system.

%package common
Summary:            Common Bacula files
Provides:           group(%username) = %uid
Provides:           user(%username) = %uid
Requires:           bacula-libs%{?_isa} = %{version}-%{release}
Requires(postun):   shadow-utils
%description common
Bacula is a set of programs that allow you to manage the backup, recovery, and
verification of computer data across a network of different computers. It is
based on a client/server architecture.

This package contains files common to all Bacula daemons.

%package director
Summary:            Bacula Director files
Requires:           bacula-common%{?_isa} = %{version}-%{release}
Requires:           bacula-libs%{?_isa} = %{version}-%{release}
Requires:           bacula-libs-sql%{?_isa} = %{version}-%{release}
Requires(post):     systemd
Requires(preun):    systemd
Requires(postun):   systemd
Recommends:         qrencode
%description director
Bacula is a set of programs that allow you to manage the backup, recovery, and
verification of computer data across a network of different computers. It is
based on a client/server architecture.

This package contains the director files.

%package logwatch
Summary:            Bacula Director logwatch scripts
BuildArch:          noarch
Requires:           bacula-director = %{version}-%{release}
Requires:           logwatch
%description logwatch
Bacula is a set of programs that allow you to manage the backup, recovery, and
verification of computer data across a network of different computers. It is
based on a client/server architecture.

This package contains logwatch scripts for Bacula Director.

%package storage
Summary:            Bacula storage daemon files
Requires:           bacula-common%{?_isa} = %{version}-%{release}
Requires:           bacula-libs%{?_isa} = %{version}-%{release}
Requires:           bacula-libs-sql%{?_isa} = %{version}-%{release}
Requires:           mt-st
Requires:           mtx
Requires:           sdparm
Provides:           bundled(libs3) = 4.1.bac
Requires(post):     systemd
Requires(preun):    systemd
Requires(postun):   systemd
%description storage
Bacula is a set of programs that allow you to manage the backup, recovery, and
verification of computer data across a network of different computers. It is
based on a client/server architecture.

This package contains the storage daemon, the daemon responsible for writing
the data received from the clients onto tape drives or other mass storage
devices.

%package client
Summary:            Bacula backup client
Requires:           bacula-common%{?_isa} = %{version}-%{release}
Requires:           bacula-libs%{?_isa} = %{version}-%{release}
Requires(post):     systemd
Requires(preun):    systemd
Requires(postun):   systemd
%description client
Bacula is a set of programs that allow you to manage the backup, recovery, and
verification of computer data across a network of different computers. It is
based on a client/server architecture.

This package contains the bacula client, the daemon running on the system to be
backed up.

%package console
Summary:            Bacula management console
Obsoletes:          bacula-console-wxwidgets <= 5.0.3
Requires:           bacula-libs%{?_isa} = %{version}-%{release}
%description console
Bacula is a set of programs that allow you to manage the backup, recovery, and
verification of computer data across a network of different computers. It is
based on a client/server architecture.

This package contains the command-line management console for the bacula backup
system.

%package console-bat
Summary:            Bacula bat console
Requires:           bacula-libs%{?_isa} = %{version}-%{release}
Requires:           dejavu-lgc-sans-fonts
%description console-bat
Bacula is a set of programs that allow you to manage the backup, recovery, and
verification of computer data across a network of different computers. It is
based on a client/server architecture.

This package contains the bat version of the bacula management console.

%package traymonitor
Summary:            Bacula system tray monitor
Requires:           bacula-libs%{?_isa} = %{version}-%{release}
Requires:           dejavu-lgc-sans-fonts
%description traymonitor
Bacula is a set of programs that allow you to manage the backup, recovery, and
verification of computer data across a network of different computers. It is
based on a client/server architecture.

This package contains the Gnome and KDE compatible tray monitor to monitor your
bacula server.

%package devel
Summary:            Bacula development files
Requires:           bacula-libs%{?_isa} = %{version}-%{release}
Requires:           bacula-libs-sql%{?_isa} = %{version}-%{release}
%description devel
Bacula is a set of programs that allow you to manage the backup, recovery, and
verification of computer data across a network of different computers. It is
based on a client/server architecture.

This development package contains static libraries and header files.

%package -n nagios-plugins-bacula
Summary:            Nagios Plugin - check_bacula
Requires:           bacula-libs%{?_isa} = %{version}-%{release}
Requires:           nagios-common%{?_isa}
%description -n nagios-plugins-bacula
Provides check_bacula support for Nagios.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -a20 -p1
perl -pi -e 's/cram_md5_respond\(([^,\)]+,[^,\)]+,[^,\)]+,[^,\)]+)\)/cram_md5_respond($1, false)/g' $(grep -rl cram_md5_respond src)

cp %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} .

# Regenerate configure
pushd autoconf
aclocal -I bacula-macros/ -I gettext-macros/ -I libtool/
popd
autoconf -I autoconf/ -o configure autoconf/configure.in

# Remove execution permissions from files we're packaging as docs later on
find updatedb -type f | xargs chmod -x

# Create a sysusers.d config file
cat >bacula.sysusers.conf <<EOF
u bacula %uid 'Bacula Backup System' /var/spool/bacula -
EOF

%build

%set_build_flags
export CFLAGS="%{optflags} -fPIC -Wno-error=attribute-warning -I%{_includedir}/ncurses"
export CXXFLAGS="%{optflags} -fPIC -Wno-error=attribute-warning -I%{_includedir}/ncurses"
export PATH="$PATH:%{_qt5_bindir}"
pushd libs3-%{commit}
patch -p1 -i %{SOURCE21}
%make_build exported
popd
%configure \
    --disable-conio \
    --disable-rpath \
    --docdir=%{_datadir}/bacula \
    --enable-antivirus-plugin \
    --enable-bat \
    --enable-antivirus-plugin \
    --enable-batch-insert \
    --enable-build-dird \
    --enable-build-stored \
    --enable-cdp-plugin \
    --enable-docker-plugin \
    --enable-includes \
    --enable-largefile \
    --enable-ldap-bpam \
    --enable-lzo \
    --enable-readline \
    --enable-smartalloc \
    --enable-totp-bpam \
    --enable-ldap-bpam \
    --sysconfdir=%{_sysconfdir}/bacula \
    --with-aws \
    --with-basename=bacula \
    --with-bsrdir=%{_localstatedir}/spool/bacula \
    --with-dir-password=@@DIR_PASSWORD@@ \
    --with-fd-password=@@FD_PASSWORD@@ \
    --with-hostname=localhost \
    --with-ldap \
    --with-logdir=%{_localstatedir}/log/bacula \
    --with-mon-dir-password=@@MON_DIR_PASSWORD@@ \
    --with-mon-fd-password=@@MON_FD_PASSWORD@@ \
    --with-mon-sd-password=@@MON_SD_PASSWORD@@ \
    --with-mysql \
    --with-openssl \
    --with-pid-dir=%{_localstatedir}/run \
    --with-plugindir=%{_libdir}/%{name} \
    --with-postgresql \
    --with-scriptdir=%{_libexecdir}/bacula \
    --with-sd-password=@@SD_PASSWORD@@ \
    --with-smtp-host=localhost \
    --with-s3=`pwd`/libs3-%{commit}/build \
    --with-sqlite3 \
    --with-subsys-dir=%{_localstatedir}/lock/subsys \
    --with-working-dir=%{_localstatedir}/spool/bacula \
    --with-x
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build
%make_build -C examples/nagios/check_bacula
%install
%make_install
%make_install -C examples/nagios/check_bacula
rm -f %{buildroot}%{_libdir}/%{name}/%{name}-sd-*-driver.so
rm -f %{buildroot}%{_libdir}/libbaccats.so
rm -f %{buildroot}%{_libexecdir}/%{name}/baculabackupreport
install -p -m 644 -D src/qt-console/images/bat_icon.png %{buildroot}%{_datadir}/pixmaps/bat_icon.png
install -p -m 644 -D scripts/bat.desktop %{buildroot}%{_datadir}/applications/bat.desktop
install -p -m 755 -D src/qt-console/.libs/bat %{buildroot}%{_sbindir}/bat
install -p -m 644 -D manpages/bacula-tray-monitor.1 %{buildroot}%{_mandir}/man1/bacula-tray-monitor.1
install -p -m 644 -D %{SOURCE19} %{buildroot}%{_datadir}/pixmaps/bacula-tray-monitor.png
install -p -m 644 -D scripts/bacula-tray-monitor.desktop %{buildroot}%{_datadir}/applications/bacula-tray-monitor.desktop
install -p -m 755 -D src/qt-console/tray-monitor/.libs/bacula-tray-monitor %{buildroot}%{_sbindir}/bacula-tray-monitor
mkdir -p %{buildroot}%{_localstatedir}/log/bacula
install -p -m 644 -D %{SOURCE6} %{buildroot}%{_sysconfdir}/logrotate.d/bacula
install -p -m 755 -D scripts/logwatch/bacula %{buildroot}%{_sysconfdir}/logwatch/scripts/services/bacula
install -p -m 755 -D scripts/logwatch/applybaculadate %{buildroot}%{_sysconfdir}/logwatch/scripts/shared/applybaculadate
install -p -m 644 -D scripts/logwatch/logfile.bacula.conf %{buildroot}%{_sysconfdir}/logwatch/conf/logfiles/bacula.conf
install -p -m 644 -D scripts/logwatch/services.bacula.conf %{buildroot}%{_sysconfdir}/logwatch/conf/services/bacula.conf
mkdir -p %{buildroot}%{_unitdir}
install -p -m 644 -D %{SOURCE10} %{buildroot}%{_unitdir}/bacula-fd.service
install -p -m 644 -D %{SOURCE11} %{buildroot}%{_unitdir}/bacula-dir.service
install -p -m 644 -D %{SOURCE12} %{buildroot}%{_unitdir}/bacula-sd.service
install -p -m 644 -D %{SOURCE15} %{buildroot}%{_sysconfdir}/sysconfig/bacula-fd
install -p -m 644 -D %{SOURCE16} %{buildroot}%{_sysconfdir}/sysconfig/bacula-dir
install -p -m 644 -D %{SOURCE17} %{buildroot}%{_sysconfdir}/sysconfig/bacula-sd
mkdir -p %{buildroot}%{_localstatedir}/spool/bacula
install -p -m 644 -D %{SOURCE7} %{buildroot}%{_prefix}/lib/firewalld/services/bacula-storage.xml
install -p -m 644 -D %{SOURCE8} %{buildroot}%{_prefix}/lib/firewalld/services/bacula-director.xml
rm -f %{buildroot}%{_libexecdir}/bacula/{bacula,bacula-ctl-*,startmysql,stopmysql,bconsole,make_catalog_backup}
rm -f %{buildroot}%{_sbindir}/bacula
rm -f %{buildroot}%{_mandir}/man8/bacula.8.gz
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_datadir}/bacula/{ChangeLog,INSTALL,LICENSE*,README,ReleaseNotes,VERIFYING,technotes}
chmod 755 %{buildroot}%{_sbindir}/*
chmod 755 %{buildroot}%{_libdir}/%{name}/*
chmod 755 %{buildroot}%{_libexecdir}/bacula/*
chmod 644 %{buildroot}%{_libexecdir}/bacula/btraceback.*
install -m0644 -D bacula.sysusers.conf %{buildroot}%{_sysusersdir}/bacula.conf
%oreon_autofiles bacula-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles bacula-libs-sql usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles bacula-common usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles bacula-director usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles bacula-logwatch usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles bacula-storage usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles bacula-client usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles bacula-console usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles bacula-console-bat usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles bacula-traymonitor usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles bacula-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles nagios-plugins-bacula usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post libs-sql

/usr/sbin/alternatives --install %{_libdir}/libbaccats.so libbaccats.so %{_libdir}/libbaccats-mysql.so 50
/usr/sbin/alternatives --install %{_libdir}/libbaccats.so libbaccats.so %{_libdir}/libbaccats-sqlite3.so 40
/usr/sbin/alternatives --install %{_libdir}/libbaccats.so libbaccats.so %{_libdir}/libbaccats-postgresql.so 60
if readlink /etc/alternatives/libbaccats.so | grep --silent mysql || \
    readlink /etc/alternatives/bacula-dir | grep --silent mysql || \
    readlink /etc/alternatives/bacula-sd | grep --silent mysql; then
    /usr/sbin/alternatives --set libbaccats.so %{_libdir}/libbaccats-mysql.so
elif readlink /etc/alternatives/libbaccats.so | grep --silent sqlite || \
    readlink /etc/alternatives/bacula-dir | grep --silent sqlite || \
    readlink /etc/alternatives/bacula-sd | grep --silent sqlite; then
    /usr/sbin/alternatives --set libbaccats.so %{_libdir}/libbaccats-sqlite3.so
else
    /usr/sbin/alternatives --set libbaccats.so %{_libdir}/libbaccats-postgresql.so
fi
%preun libs-sql

if [ "$1" = 0 ]; then
    /usr/sbin/alternatives --remove libbaccats.so %{_libdir}/libbaccats-mysql.so
    /usr/sbin/alternatives --remove libbaccats.so %{_libdir}/libbaccats-sqlite3.so
    /usr/sbin/alternatives --remove libbaccats.so %{_libdir}/libbaccats-postgresql.so
fi
%post common

%firewalld_reload
%post client

%systemd_post %{name}-fd.service
%preun client

%systemd_preun %{name}-fd.service
%postun client

%systemd_postun_with_restart %{name}-fd.service
%post director

%systemd_post %{name}-dir.service
%preun director

%systemd_preun %{name}-dir.service
%postun director

%systemd_postun_with_restart %{name}-dir.service
%post storage

%systemd_post %{name}-sd.service
%preun storage

%systemd_preun %{name}-sd.service
%postun storage

%systemd_postun_with_restart %{name}-sd.service
%files -f %{oreon_filedir}/main.list
%files -n bacula-libs -f %{oreon_filedir}/bacula-libs.list
%files -n bacula-libs-sql -f %{oreon_filedir}/bacula-libs-sql.list
%files -n bacula-common -f %{oreon_filedir}/bacula-common.list
%files -n bacula-director -f %{oreon_filedir}/bacula-director.list
%files -n bacula-logwatch -f %{oreon_filedir}/bacula-logwatch.list
%files -n bacula-storage -f %{oreon_filedir}/bacula-storage.list
%files -n bacula-client -f %{oreon_filedir}/bacula-client.list
%files -n bacula-console -f %{oreon_filedir}/bacula-console.list
%files -n bacula-console-bat -f %{oreon_filedir}/bacula-console-bat.list
%files -n bacula-traymonitor -f %{oreon_filedir}/bacula-traymonitor.list
%files -n bacula-devel -f %{oreon_filedir}/bacula-devel.list
%files -n nagios-plugins-bacula -f %{oreon_filedir}/nagios-plugins-bacula.list

%changelog

%autochangelog
