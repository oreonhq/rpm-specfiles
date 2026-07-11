%global source0_hash 1f3c2401af7b388a13ffed7e6f72b5e70f1bed7c82c34c218379d0ee45595616

#global prerelease  -rc

%global _hardened_build 1

## Fedora specific customization below...
%bcond_without  clamonacc
%bcond_with     unrar
# Failing with llvm 14 https://github.com/Cisco-Talos/clamav/issues/581
%bcond_with  llvm

# No ocaml on ix86
%ifarch %{ix86}
%bcond_with ocaml
%else
%bcond_without ocaml
%endif

%global scanuser    clamscan
%global updateuser  clamupdate
%global milteruser  clamilt

%global homedir         %{_var}/lib/clamav
%global quarantinedir   %{_var}/spool/quarantine
%global freshclamlog    %{_var}/log/freshclam.log

Summary:    End-user tools for the Clam Antivirus scanner
Name:       clamav
Version:    1.4.4
Release:    2%{?dist}
License:    %{?with_unrar:proprietary}%{!?with_unrar:GPL-2.0-only}
URL:        https://www.clamav.net/
Source0:    https://www.clamav.net/downloads/production/%{name}-%{version}%{?prerelease}.tar.gz
Source999:  https://www.clamav.net/downloads/production/%{name}-%{version}%{?prerelease}.tar.gz.sig
# Multilib headers
Source1:    clamav-types.h
#for server
Source3:    clamd.logrotate
Source5:    clamd-README
# pinned virus DB snapshots (local). refresh with update_clamav_data.sh
Source10:   main-63.cvd
Source11:   daily-27930.cvd
Source12:   bytecode-339.cvd
#for update
Source200:  freshclam-sleep
Source201:  freshclam.sysconfig
Source202:  clamav-update.crond
Source203:  clamav-update.logrotate
#for milter
Source300:  README.fedora.md
#for clamav-milter.systemd
Source330:  clamav-milter.systemd
#for scanner-systemd/server-systemd
Source530:  clamd@.service

# Change default config locations for Fedora
Patch1:     clamav-default_confs.patch
# Fix pkg-config flags for static linking, multilib
Patch2:     clamav-private.patch
# Modify clamav-clamonacc.service for Fedora compatibility
Patch5:     clamav-clamonacc-service.patch
# Allow freshclam service to run if cron.d file is present
Patch6:     clamav-freshclam.service.patch
# Debian big-endian pe.c fix, refreshed for 1.4.4 (salsa unstable dropped the old one)
Patch7:     libclamav-pe-Use-endian-wrapper-in-more-places.patch
# - Update the image crate dependency to 0.25, the current release,
#   https://github.com/Cisco-Talos/clamav/pull/1366/commits/24d1341e8e34aa325ac03718121e33a3b4e5b75e,
#   allowing 0.24 for backwards-compatibility with vendored dependencies in EPEL8
# - Allow version 1.0 of the hex-literal crate dependency; not suitable for
#   upstream yet due to MSRV
Patch8:     clamav-rust-dependency-versions.patch

BuildRequires:  cmake
BuildRequires:  gettext-devel
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  rust
%if 0%{?fedora} || 0%{?rhel} >= 9
BuildRequires:  rust-packaging
%else
# Undefining the appropriate __cmake*_in_source_build macro causes the
# build to use a separate build path, so the build does not output to
# the source path.  This separate build path is the default behavior
# for >=EL9 and fedora.
%if 0%{?rhel} == 8
# EL8 defines cmake_in_source_build
%undefine __cmake_in_source_build
%else
# EL7 defines cmake3_in_source_build
%undefine __cmake3_in_source_build
%endif
BuildRequires:  rust-toolset
%endif
BuildRequires:  cargo
BuildRequires:  bzip2-devel
BuildRequires:  check-devel
BuildRequires:  curl-devel
BuildRequires:  git-core
BuildRequires:  gmp-devel
BuildRequires:  json-c-devel
%if ! (0%{?fedora} > 40 || 0%{?rhel} > 9)
BuildRequires:  libprelude-devel
# libprelude-config --libs brings in gnutls, pcre
# https://bugzilla.redhat.com/show_bug.cgi?id=1830473
BuildRequires:  gnutls-devel
%endif
BuildRequires:  libxml2-devel
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  pcre2-devel
# Explicitly needed on EL8
BuildRequires:  python3
BuildRequires:  python3-pytest
%if 0%{?fedora} >= 41
BuildRequires:  python3-cgi
%endif
BuildRequires:  zlib-devel
#BuildRequires:  %%{_includedir}/tcpd.h
BuildRequires:  bc
BuildRequires:  tcl
BuildRequires:  groff
BuildRequires:  graphviz
%{?with_ocaml:BuildRequires: ocaml}
# nc required for tests
BuildRequires:  nc
%{?systemd_requires}
BuildRequires:  systemd
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
#for milter
BuildRequires:  sendmail-devel
%ifarch %{valgrind_arches}
BuildRequires:  valgrind
%endif

Requires:   clamav-filesystem = %{version}-%{release}
Requires:   clamav-lib = %{version}-%{release}
Requires:   data(clamav)

%description
Clam AntiVirus is an anti-virus toolkit for UNIX. The main purpose of this
software is the integration with mail servers (attachment scanning). The
package provides a flexible and scalable multi-threaded daemon, a command
line scanner, and a tool for automatic updating via Internet. The programs
are based on a shared library distributed with the Clam AntiVirus package,
which you can use with your own software. The virus database is based on
the virus database from OpenAntiVirus, but contains additional signatures
(including signatures for popular polymorphic viruses, too) and is KEPT UP
TO DATE.

%package filesystem
Summary:    Filesystem structure for clamav
# Prevent version mix
Conflicts:  %{name} < %{version}-%{release}
Conflicts:  %{name} > %{version}-%{release}
BuildArch:  noarch

%description filesystem
This package provides the filesystem structure and contains the
user-creation scripts required by clamav.


%package lib
Summary:    Dynamic libraries for the Clam Antivirus scanner
Provides:   bundled(libmspack) = 0.5-0.1.alpha.modified_by_clamav

# LICENSE.dependencies contains a full license breakdown
# From the output of %%{cargo_license_summary}:
#
%if 0%{?fedora} || 0%{?rhel} >= 9
# 0BSD OR MIT OR Apache-2.0
# Apache-2.0
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSD-2-Clause
# BSD-2-Clause AND ISC
# BSD-3-Clause
# MIT
# MIT OR Apache-2.0 (duplicate)
# MIT OR Apache-2.0 OR Zlib
# MIT OR Zlib OR Apache-2.0 (duplicate)
# Unlicense OR MIT
# Zlib OR Apache-2.0 OR MIT (duplicate)
License:    %{shrink:
            %{?with_unrar:proprietary}%{!?with_unrar:GPL-2.0-only} AND
            (0BSD OR MIT OR Apache-2.0) AND
            Apache-2.0 AND
            (Apache-2.0 OR MIT) AND
            (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
            BSD-2-Clause AND
            BSD-3-Clause AND
            ISC AND
            MIT AND
            (MIT OR Zlib OR Apache-2.0) AND
            (Unlicense OR MIT) AND
            Zlib
            }
%else
# 0BSD OR MIT OR Apache-2.0
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSD-3-Clause
# MIT
# MIT OR Apache-2.0 (duplicate)
# MIT OR Zlib OR Apache-2.0
# Unlicense OR MIT
# Zlib
# Zlib OR Apache-2.0 OR MIT (duplicate)
License:    %{shrink:
            %{?with_unrar:proprietary}%{!?with_unrar:GPL-2.0-only} AND
            (0BSD OR MIT OR Apache-2.0) AND
            (Apache-2.0 OR MIT) AND
            (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
            BSD-3-Clause AND
            MIT AND
            (MIT OR Zlib OR Apache-2.0) AND
            (Unlicense OR MIT) AND
            Zlib
            }
%endif

%description lib
This package contains dynamic libraries shared between applications
using the Clam Antivirus scanner.


%package devel
Summary:    Header files and libraries for the Clam Antivirus scanner
Requires:   clamav-lib        = %{version}-%{release}
Requires:   clamav-filesystem = %{version}-%{release}
Requires:   openssl-devel

%description devel
This package contains headerfiles and libraries which are needed to
build applications using clamav.


%package data
Summary:    Virus signature data for the Clam Antivirus scanner
Requires:   clamav-filesystem = %{version}-%{release}
Provides:   data(clamav) = full
Provides:   clamav-db = %{version}-%{release}
Obsoletes:  clamav-db < %{version}-%{release}
BuildArch:  noarch

%description data
This package contains the virus-database needed by clamav. This
database should be updated regularly; the 'clamav-update' package
ships a corresponding cron-job. Use this package when you want a
working (but perhaps outdated) virus scanner immediately after package
installation.


%package doc
Summary:    Documentation for the Clam Antivirus scanner
Requires:   clamav-filesystem = %{version}-%{release}
BuildArch:  noarch

%description doc
This package contains the documentation for clamav.


%package freshclam
Summary:    Auto-updater for the Clam Antivirus scanner data-files
Requires:   clamav-filesystem = %{version}-%{release}
Requires:   clamav-lib        = %{version}-%{release}
%if 0%{?fedora} || 0%{?rhel} >= 8
Supplements:clamd
%endif
Provides:   data(clamav) = empty
Provides:   clamav-data-empty = %{version}-%{release}
Obsoletes:  clamav-data-empty < %{version}-%{release}
Provides:   clamav-update = %{version}-%{release}
Obsoletes:  clamav-update < %{version}-%{release}

%description freshclam
This package contains the freshclam(1) program and clamav-freshclam
service which can be used to update the clamav anti-virus database
automatically. Most users should install this package in order to
keep their definitions up to date.


%package -n clamd
Summary: The Clam AntiVirus Daemon
Requires:   data(clamav)
Requires:   clamav-filesystem = %{version}-%{release}
Requires:   clamav-lib        = %{version}-%{release}
Requires:   coreutils
# This is still used by clamsmtp and exim-clamav
Provides: clamav-server = %{version}-%{release}
Provides: clamav-scanner-systemd = %{version}-%{release}
Provides: clamav-server-systemd = %{version}-%{release}
Obsoletes: clamav-scanner-systemd < %{version}-%{release}
Obsoletes: clamav-server-systemd < %{version}-%{release}

%description -n clamd
The Clam AntiVirus Daemon
See the README file how this can be done with a minimum of effort.
This package contains a generic system wide clamd service which is
e.g. used by the clamav-milter package.


%package milter
Summary:    Milter module for the Clam Antivirus scanner
# clamav-milter could work without clamd and without sendmail
#Requires: clamd = %%{version}-%%{release}
#Requires: /usr/sbin/sendmail
Requires:   clamav-filesystem = %{version}-%{release}
Provides: clamav-milter-systemd = %{version}-%{release}
Obsoletes: clamav-milter-systemd < %{version}-%{release}
Requires: group(clamscan)

%description milter
This package contains files which are needed to run the clamav-milter.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}%{?prerelease}
%if 0%{?fedora} || 0%{?rhel} >= 9
# EL8 and earlier do not have the Rust cargo dependencies that are
# defined by the generate_buildrequires stage in EL9 and later, so the
# vendored packages included in the ClamAV sources suffice.
%cargo_prep
cd libclamav_rust
sed -i -e '/^base64 *=/s/= .*/= "0.22"/' Cargo.toml
sed -i -e '/^bindgen *=/s/= .*/= "0.72"/' Cargo.toml
sed -i -e '/^cbindgen *=/s/= *".*"/= "0.26"/' Cargo.toml
sed -i -e '/^onenote_parser *=/s/= *.*/= "0.3.1"/' Cargo.toml
%cargo_prep
cd ..
%endif

%patch -P1 -p1 -b .default_confs
%patch -P2 -p1 -b .private
%patch -P5 -p1 -b .clamonacc-service
%patch -P6 -p1 -b .freshclam-service
%patch -P7 -p1 -b .big-endian
%patch -P8 -p1 -b .rust-dependencies

install -p -m0644 %{SOURCE300} clamav-milter/

# drop GPL-incompatible unrar tree from the upstream tarball
%if %{without unrar}
rm -rf libclamunrar/*
%endif
mkdir -p libclamunrar{,_iface}
%{!?with_unrar:touch libclamunrar/{Makefile.in,all,install}}

# Create sysusers.d config files
cat >clamav.sysusers.conf <<EOF
g virusgroup -
u clamupdate - 'Clamav database update user' %{homedir} -
m clamupdate virusgroup
EOF
cat >clamd.sysusers.conf <<EOF
u clamscan - 'Clamav scanner user' - -
m clamscan virusgroup
EOF
cat >clamav-milter.sysusers.conf <<EOF
u clamilt - 'Clamav milter user' %{_rundir}/clamav-milter -
m clamilt virusgroup
m clamilt clamscan
EOF

%if 0%{?fedora} || 0%{?rhel} >= 9
%generate_buildrequires
# The generate_buildrequires stage doesn't exist prior to EL9, so this
# section is conditionally removed in these build environments.
cd libclamav_rust
%cargo_generate_buildrequires
%endif

%build
# add -Wl,--as-needed if not exist
export LDFLAGS=$(echo %{?__global_ldflags} | sed '/-Wl,--as-needed/!s/$/ -Wl,--as-needed/')
# IPv6 check is buggy and does not work when there are no IPv6 interface on build machine
export have_cv_ipv6=yes

%cmake \
%if 0%{?fedora} || 0%{?rhel} >= 8
    -DRUSTFLAGS="%build_rustflags" \
%else
    -DRUSTFLAGS="%__global_rustflags" \
%endif
    -DAPP_CONFIG_DIRECTORY=%{_sysconfdir} \
    -DCMAKE_INSTALL_DOCDIR=%{_pkgdocdir} \
    -DCLAMAV_USER=%{updateuser} -DCLAMAV_GROUP=%{updateuser} \
    -DDATABASE_DIRECTORY=%{homedir} \
    -DDO_NOT_SET_RPATH=ON \
    %{!?with_clamonacc:-DENABLE_CLAMONACC=OFF} \
    %{?with_llvm:-DBYTECODE_RUNTIME=llvm -D LLVM_FIND_VERSION="3.6.0"} \
    %{!?with_unrar:-DENABLE_UNRAR=OFF}

# TODO: check periodically that CLAMAVUSER is used for freshclam only

%cmake_build

cd libclamav_rust
%cargo_license_summary
%{cargo_license} > ../LICENSES.dependencies


%install
rm -rf _doc*
%cmake_install

install -d -m 0755 \
    %{buildroot}%{_tmpfilesdir} \
    %{buildroot}%{homedir} \
    %{buildroot}%{quarantinedir}

### data
install -D -m 0644 -p %{SOURCE10}     %{buildroot}%{homedir}/main.cvd
install -D -m 0644 -p %{SOURCE11}     %{buildroot}%{homedir}/daily.cvd
install -D -m 0644 -p %{SOURCE12}     %{buildroot}%{homedir}/bytecode.cvd

### The freshclam stuff
sed -ri \
    -e 's!^Example!#Example!' \
    -e 's!^#?(UpdateLogFile )!#\1!g;' \
    -e 's!(DatabaseOwner *)clamav$!\1%{updateuser}!g' %{buildroot}%{_sysconfdir}/freshclam.conf.sample

mv %{buildroot}%{_sysconfdir}/freshclam.conf{.sample,}
# Can contain HTTPProxyPassword (bugz#1733112)
chmod 600 %{buildroot}%{_sysconfdir}/freshclam.conf

### The scanner stuff
install -D -m 0644 -p %{SOURCE3}      _doc_server/clamd.logrotate
install -D -m 0644 -p %{SOURCE5}      _doc_server/README
## Fixup URL for EPEL
%{?epel:sed -i -e s/product=Fedora/product=Fedora%20EPEL/ _doc_server/README}

## For compatibility with 0.102.2-7
ln -s clamav-clamonacc.service      %{buildroot}%{_unitdir}/clamonacc.service

install -D -p -m 0644 %{SOURCE530}    %{buildroot}%{_unitdir}/clamd@.service

sed -ri \
    -e 's!^Example!#Example!' \
    -e 's!^#?(LogFile ).*!#\1/var/log/clamd.<SERVICE>!g' \
    -e 's!^#?(LocalSocket ).*!#\1%{_rundir}/clamd.<SERVICE>/clamd.sock!g' \
    -e 's!^(#?PidFile ).*!\1%{_rundir}/clamd.<SERVICE>/clamd.pid!g' \
    -e 's!^#?(User ).*!\1<USER>!g' \
    -e 's!^#?(AllowSupplementaryGroups|LogSyslog).*!\1 yes!g' \
    -e 's! /usr/local/share/clamav,! %{homedir},!g' \
    %{buildroot}%{_sysconfdir}/clamd.conf.sample

install -d -m 0755 %{buildroot}%{_sysconfdir}/clamd.d
sed -e 's!<SERVICE>!scan!g;s!<USER>!%{scanuser}!g' \
    %{buildroot}%{_sysconfdir}/clamd.conf.sample > %{buildroot}%{_sysconfdir}/clamd.d/scan.conf

mv %{buildroot}%{_sysconfdir}/clamd.conf.sample _doc_server/clamd.conf

cat << EOF > %{buildroot}%{_tmpfilesdir}/clamd.scan.conf
d %{_rundir}/clamd.scan 0710 %{scanuser} virusgroup
EOF

### The milter stuff
sed -ri \
    -e 's!^#?(User).*!\1 %{milteruser}!g' \
    -e 's!^#?(AllowSupplementaryGroups|LogSyslog) .*!\1 yes!g' \
    -e 's! /tmp/clamav-milter.socket! %{_rundir}/clamav-milter/clamav-milter.socket!g' \
    -e 's! /var/run/clamav-milter.pid! %{_rundir}/clamav-milter/clamav-milter.pid!g' \
    -e 's!:/var/run/clamd/clamd.socket!:%{_rundir}/clamd.scan/clamd.sock!g' \
    -e 's! /tmp/clamav-milter.log! %{_var}/log/clamav-milter.log!g' \
    %{buildroot}%{_sysconfdir}/clamav-milter.conf.sample

install -d -m 0755 %{buildroot}%{_sysconfdir}/mail
mv %{buildroot}%{_sysconfdir}/clamav-milter.conf.sample %{buildroot}%{_sysconfdir}/mail/clamav-milter.conf

install -D -p -m 0644 %{SOURCE330} %{buildroot}%{_unitdir}/clamav-milter.service

cat << EOF > %{buildroot}%{_tmpfilesdir}/clamav-milter.conf
d %{_rundir}/clamav-milter 0710 %{milteruser} %{milteruser}
EOF

#Fixup headers and scripts for multilib
%if 0%{?__isa_bits} == 64
mv %{buildroot}%{_includedir}/clamav-types.h \
   %{buildroot}%{_includedir}/clamav-types-64.h
%else
mv %{buildroot}%{_includedir}/clamav-types.h \
   %{buildroot}%{_includedir}/clamav-types-32.h
%endif
install -m 0644 %SOURCE1 %{buildroot}%{_includedir}/clamav-types.h

# TODO: Evaluate using upstream's unit with clamav-daemon.socket
rm %{buildroot}%{_unitdir}/clamav-daemon.*

install -m0644 -D clamav.sysusers.conf %{buildroot}%{_sysusersdir}/clamav.conf
install -m0644 -D clamd.sysusers.conf %{buildroot}%{_sysusersdir}/clamd.conf
install -m0644 -D clamav-milter.sysusers.conf %{buildroot}%{_sysusersdir}/clamav-milter.conf


%check
%ifarch s390x
# Tests fail on s390x
# https://github.com/Cisco-Talos/clamav/issues/759
%ctest -E valgrind || :
%else
%ctest -E valgrind
%endif
# valgrind tests fail https://github.com/Cisco-Talos/clamav/issues/584
%ctest -R valgrind || :


%post
%systemd_post clamav-clamonacc.service

%preun
%systemd_preun clamav-clamonacc.service

%postun
%systemd_postun_with_restart clamav-clamonacc.service


%post data
# nullglob. If set, Bash allows filename patterns which match no files to expand to a null string, rather than themselves
shopt -s nullglob
# Let newer .cld files take precedence over the shipped .cvd files
for f in %{homedir}/*.cld
do
    cvd=${f/.cld/.cvd}
    [ -f $f -a $f -nt $cvd ] && rm -f $cvd || :
done

%post -n clamd
# Point to the new service unit
[ -L /etc/systemd/system/multi-user.target.wants/clamd@scan.service ] &&
    ln -sf /usr/lib/systemd/system/clamd@.service /etc/systemd/system/multi-user.target.wants/clamd@scan.service || :
%systemd_post clamd@scan.service

%preun -n clamd
%systemd_preun clamd@scan.service

%postun -n clamd
%systemd_postun_with_restart clamd@scan.service

%post milter
%systemd_post clamav-milter.service

%preun milter
%systemd_preun clamav-milter.service

%postun milter
%systemd_postun_with_restart clamav-milter.service

%post freshclam
%systemd_post clamav-freshclam.service

%preun freshclam
%systemd_preun clamav-freshclam.service

%postun freshclam
%systemd_postun_with_restart clamav-freshclam.service

%ldconfig_scriptlets   lib


%files
%license COPYING
%doc NEWS.md README.md
%{_bindir}/clambc
%{_bindir}/clamconf
%{_bindir}/clamdscan
%{_bindir}/clamdtop
%{_bindir}/clamscan
%{_bindir}/clamsubmit
%{_bindir}/sigtool
%if %{with clamonacc}
%{_sbindir}/clamonacc
%endif
%{_mandir}/man[15]/*
%{_mandir}/man8/clamonacc.8*
%exclude %{_mandir}/*/freshclam*
%exclude %{_mandir}/man5/clamd.conf.5*
%{_unitdir}/clamonacc.service
%{_unitdir}/clamav-clamonacc.service
%attr(0750,root,root) %dir %{quarantinedir}


%files lib
# Licenses for statically linked Rust dependencies in libclamav
%license LICENSES.dependencies
%{_libdir}/libclamav.so.12*
%{_libdir}/libclammspack.so.0*
%if %{with unrar}
%{_libdir}/libclamunrar*.so.12*
%endif


%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/libclamav_rust.a
%{_libdir}/pkgconfig/*
%{_bindir}/clamav-config


%files filesystem
%attr(-,%{updateuser},%{updateuser}) %dir %{homedir}
%dir %{_sysconfdir}/clamd.d
# Used by both clamd, clamdscan, and clamonacc
%config(noreplace) %{_sysconfdir}/clamd.d/scan.conf
%{_sysusersdir}/clamav.conf


%files data
%defattr(-,%{updateuser},%{updateuser},-)
# use %%config to keep files which were updated by 'freshclam'
# already. Without this tag, they would be overridden with older
# versions whenever a new -data package is installed.
%config %verify(not size md5 mtime) %{homedir}/*.cvd


%files doc
%license COPYING
%{_pkgdocdir}/html/


%files freshclam
%{_bindir}/freshclam
%{_libdir}/libfreshclam.so.3*
%{_mandir}/*/freshclam*
%{_unitdir}/clamav-freshclam.service
%{_unitdir}/clamav-freshclam-once.service
%{_unitdir}/clamav-freshclam-once.timer
%config(noreplace) %verify(not mtime)    %{_sysconfdir}/freshclam.conf
%ghost %attr(0644,%{updateuser},%{updateuser}) %{homedir}/bytecode.cld
%ghost %attr(0644,%{updateuser},%{updateuser}) %{homedir}/bytecode.cvd
%ghost %attr(0644,%{updateuser},%{updateuser}) %{homedir}/freshclam.dat
%ghost %attr(0644,%{updateuser},%{updateuser}) %{homedir}/daily.cld
%ghost %attr(0644,%{updateuser},%{updateuser}) %{homedir}/daily.cvd
%ghost %attr(0644,%{updateuser},%{updateuser}) %{homedir}/main.cld
%ghost %attr(0644,%{updateuser},%{updateuser}) %{homedir}/main.cvd


%files -n clamd
%doc _doc_server/*
%{_mandir}/man5/clamd.conf.5*
%{_mandir}/man8/clamd.8*
%{_sbindir}/clamd
%{_unitdir}/clamd@.service
%{_tmpfilesdir}/clamd.scan.conf
%{_sysusersdir}/clamd.conf


%files milter
%doc clamav-milter/README.fedora.md
%{_sbindir}/*milter*
%{_unitdir}/clamav-milter.service
%{_mandir}/man8/clamav-milter*
%dir %{_sysconfdir}/mail
%config(noreplace) %{_sysconfdir}/mail/clamav-milter.conf
%{_tmpfilesdir}/clamav-milter.conf
%{_sysusersdir}/clamav-milter.conf


%changelog
%autochangelog

