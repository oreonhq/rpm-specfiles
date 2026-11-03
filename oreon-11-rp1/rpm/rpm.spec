%global source0_hash f520810d27c74bf1c5d8b8885845c61e0c845f62d33e68b02e020633a8b62fe3
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}
%global _bindir %{_prefix}/bin
%global _sbindir %{_prefix}/bin
%global _libexecdir %{_prefix}/libexec
%global _includedir %{_prefix}/include
%global _infodir %{_prefix}/share/info
%global _mandir %{_prefix}/share/man
%global py3_sitelib %(python3 -c 'import sysconfig; print(sysconfig.get_path("purelib", "posix_prefix", {"base": "/usr"}))')

Name: rpm
Version: 6.1.0
Release: 3%{?dist}
Summary: RPM package manager
License: GPL-2.0-or-later
URL: https://rpm.org/
Source0: https://github.com/rpm-software-management/rpm/releases/download/rpm-%{version}-release/rpm-%{version}.tar.bz2

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: glibc-devel
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: pkgconf-pkg-config >= 3.0.10-4
BuildRequires: lua-devel
BuildRequires: zlib-devel
BuildRequires: bzip2-devel
BuildRequires: xz-devel
BuildRequires: libzstd-devel
BuildRequires: popt-devel
BuildRequires: readline-devel
BuildRequires: libarchive-devel
BuildRequires: file-devel
BuildRequires: sqlite-devel
BuildRequires: python3-devel
BuildRequires: libcap-devel
BuildRequires: libacl-devel
BuildRequires: libselinux-devel
BuildRequires: elfutils-libelf-devel
BuildRequires: elfutils-devel
BuildRequires: audit-libs-devel
BuildRequires: dbus-devel
BuildRequires: rpm-sequoia-devel
BuildRequires: gawk
BuildRequires: gettext
BuildRequires: fsverity-utils-devel
BuildRequires: ima-evm-utils-devel
BuildRequires: doxygen
BuildRequires: scdoc
BuildRequires: patchelf

Requires: rpm-libs%{?_isa} = %{version}-%{release}

%description
RPM package manager libraries and tools.

%package libs
Summary: Libraries for manipulating RPM packages
Requires: rpm = %{version}-%{release}

%description libs
Shared libraries used by RPM and programs that read or install packages.

%package build-libs
Summary: Libraries for building RPM packages
Requires: rpm-libs%{?_isa} = %{version}-%{release}

%description build-libs
Shared library used by rpmbuild and programs that build packages.

%package sign-libs
Summary: Libraries for signing RPM packages
Requires: rpm-libs%{?_isa} = %{version}-%{release}

%description sign-libs
Shared library used to sign RPM packages.

%package sign
Summary: Package signing support
Requires: rpm-sign-libs%{?_isa} = %{version}-%{release}

%description sign
rpmsign signs RPM packages.

%package -n python3-rpm
Summary: Python bindings for RPM
Requires: rpm-libs%{?_isa} = %{version}-%{release}
Requires: rpm-build-libs%{?_isa} = %{version}-%{release}
Requires: rpm-sign-libs%{?_isa} = %{version}-%{release}

%description -n python3-rpm
Python 3 module for reading and installing RPM packages.

%package devel
Summary: Development files for RPM
Requires: rpm-libs%{?_isa} = %{version}-%{release}
Requires: rpm-build-libs%{?_isa} = %{version}-%{release}
Requires: rpm-sign-libs%{?_isa} = %{version}-%{release}
Requires: popt-devel

%description devel
Headers, libraries and rpmgraph for programs that use RPM.

%package apidocs
Summary: API documentation for RPM libraries
BuildArch: noarch

%description apidocs
Doxygen API documentation for the RPM libraries.

%package plugin-audit
Summary: RPM plugin audit
Requires: rpm-libs%{?_isa} = %{version}-%{release}

%description plugin-audit
Logs transactions to the audit log.

%package plugin-dbus-announce
Summary: RPM plugin dbus-announce
Requires: rpm-libs%{?_isa} = %{version}-%{release}

%description plugin-dbus-announce
Announces transactions on the system D-Bus.

%package plugin-fapolicyd
Summary: RPM plugin fapolicyd
Requires: rpm-libs%{?_isa} = %{version}-%{release}

%description plugin-fapolicyd
Passes file data to fapolicyd.

%package plugin-fsverity
Summary: RPM plugin fsverity
Requires: rpm-libs%{?_isa} = %{version}-%{release}

%description plugin-fsverity
Installs fs-verity signatures.

%package plugin-ima
Summary: RPM plugin ima
Requires: rpm-libs%{?_isa} = %{version}-%{release}

%description plugin-ima
Installs IMA file signatures.

%package plugin-prioreset
Summary: RPM plugin prioreset
Requires: rpm-libs%{?_isa} = %{version}-%{release}

%description plugin-prioreset
Resets scheduler priority for scriptlets.

%package plugin-selinux
Summary: RPM plugin selinux
Requires: rpm-libs%{?_isa} = %{version}-%{release}

%description plugin-selinux
Sets SELinux contexts on installed files.

%package plugin-syslog
Summary: RPM plugin syslog
Requires: rpm-libs%{?_isa} = %{version}-%{release}

%description plugin-syslog
Logs transactions to syslog.

%package plugin-systemd-inhibit
Summary: RPM plugin systemd-inhibit
Requires: rpm-libs%{?_isa} = %{version}-%{release}

%description plugin-systemd-inhibit
Blocks shutdown during transactions.

%package plugin-unshare
Summary: RPM plugin unshare
Requires: rpm-libs%{?_isa} = %{version}-%{release}

%description plugin-unshare
Runs scriptlets in private namespaces.

%package build
Summary: Scripts and programs used to build RPM packages
Requires: rpm = %{version}-%{release}
Requires: rpm-build-libs%{?_isa} = %{version}-%{release}
Requires: elfutils
Requires: binutils
Requires: findutils
Requires: sed
Requires: grep
Requires: gawk
Requires: diffutils
Requires: file
Requires: patch
Requires: tar
Requires: unzip
Requires: gzip
Requires: bzip2
Requires: cpio
Requires: xz
Requires: zstd
Requires: debugedit
Requires: pkgconf
Requires: system-rpm-config

%description build
rpmbuild and the scripts it runs.

%prep
%oreon_sha256
%autosetup -p1

%build
%oreon_cmake \
  -DCMAKE_SKIP_RPATH=ON \
  -DRPM_VENDOR=oreon \
  -DENABLE_TESTSUITE=OFF \
  -DENABLE_NLS=ON \
  -DENABLE_OPENMP=ON \
  -DENABLE_PYTHON=ON \
  -DWITH_SEQUOIA=ON \
  -DWITH_OPENSSL=OFF \
  -DWITH_LIBELF=ON \
  -DWITH_LIBDW=ON \
  -DWITH_AUDIT=ON \
  -DWITH_FSVERITY=ON \
  -DWITH_FAPOLICYD=ON \
  -DWITH_IMAEVM=ON \
  -DWITH_DOXYGEN=ON \
  -DWITH_CAP=ON \
  -DWITH_ACL=ON \
  -DWITH_SELINUX=ON \
  -DWITH_DBUS=ON \
  -DWITH_READLINE=ON \
  -DWITH_BZIP2=ON \
  -DWITH_ZSTD=ON \
  -DWITH_LIBLZMA=ON \
  -DENABLE_SQLITE=ON \
  -DCMAKE_INSTALL_BINDIR=bin \
  -DCMAKE_INSTALL_SBINDIR=bin \
  -DCMAKE_INSTALL_LIBEXECDIR=libexec \
  -DCMAKE_INSTALL_INCLUDEDIR=include \
  -DCMAKE_INSTALL_DATADIR=share \
  -DCMAKE_INSTALL_INFODIR=share/info \
  -DCMAKE_INSTALL_MANDIR=share/man
%oreon_cmake_build

%install
%oreon_cmake_install
rm -f %{buildroot}%{_libdir}/*.a
find %{buildroot} -type f | while read -r f; do
  file -b "$f" | grep -q '^ELF' || continue
  r=$(patchelf --print-rpath "$f")
  if [ -n "$r" ]; then
    chmod u+w "$f"
    patchelf --remove-rpath "$f"
  fi
done
%find_lang rpm

%ldconfig_scriptlets libs
%ldconfig_scriptlets build-libs
%ldconfig_scriptlets sign-libs

%files -f rpm.lang
%license COPYING
%{_bindir}/rpm
%{_bindir}/rpm2archive
%{_bindir}/rpm2cpio
%{_bindir}/rpmdb
%{_bindir}/rpmkeys
%{_bindir}/rpmquery
%{_bindir}/rpmsort
%{_bindir}/rpmverify
%dir %{_rpmconfigdir}
%dir %{_rpmmacrodir}
%{_rpmconfigdir}/macros
%{_rpmconfigdir}/rpmrc
%{_rpmconfigdir}/rpmpopt-%{version}
%{_rpmconfigdir}/platform/
%{_rpmconfigdir}/rpm.daily
%{_rpmconfigdir}/rpm.log
%{_rpmconfigdir}/rpm.supp
%{_rpmconfigdir}/rpm2cpio.sh
%{_rpmconfigdir}/rpmdb_dump
%{_rpmconfigdir}/rpmdb_load
%{_rpmconfigdir}/sysusers.sh
%{_rpmconfigdir}/tgpg
%{_docdir}/rpm/
%exclude %{_docdir}/rpm/API
%{_mandir}/man1/rpm2archive.1*
%{_mandir}/man1/rpm2cpio.1*
%{_mandir}/man1/rpmsort.1*
%{_mandir}/man5/rpm-config.5*
%{_mandir}/man5/rpm-macrofile.5*
%{_mandir}/man5/rpm-manifest.5*
%{_mandir}/man5/rpm-rpmrc.5*
%{_mandir}/man7/rpm-*.7*
%{_mandir}/man8/rpm.8*
%{_mandir}/man8/rpm-common.8*
%{_mandir}/man8/rpm-plugins.8*
%{_mandir}/man8/rpmdb.8*
%{_mandir}/man8/rpmkeys.8*

%files libs
%license COPYING
%{_libdir}/librpm.so.10*
%{_libdir}/librpmio.so.10*
%dir %{_libdir}/rpm-plugins

%files build-libs
%{_libdir}/librpmbuild.so.10*

%files sign-libs
%{_libdir}/librpmsign.so.10*

%files sign
%{_bindir}/rpmsign
%{_bindir}/rpm-setup-autosign
%{_rpmconfigdir}/rpm-setup-autosign
%{_mandir}/man1/rpmsign.1*
%{_mandir}/man1/rpm-setup-autosign.1*

%files -n python3-rpm
%{py3_sitelib}/rpm/
%{py3_sitelib}/rpm-%{version}-py*.egg-info

%files plugin-audit
%{_libdir}/rpm-plugins/audit.so
%{_rpmmacrodir}/macros.transaction_audit
%{_mandir}/man8/rpm-plugin-audit.8*

%files plugin-dbus-announce
%{_datadir}/dbus-1/system.d/org.rpm.conf
%{_libdir}/rpm-plugins/dbus_announce.so
%{_rpmmacrodir}/macros.transaction_dbus_announce
%{_mandir}/man8/rpm-plugin-dbus-announce.8*

%files plugin-fapolicyd
%{_libdir}/rpm-plugins/fapolicyd.so
%{_rpmmacrodir}/macros.transaction_fapolicyd
%{_mandir}/man8/rpm-plugin-fapolicyd.8*

%files plugin-ima
%{_libdir}/rpm-plugins/ima.so
%{_rpmmacrodir}/macros.transaction_ima
%{_mandir}/man8/rpm-plugin-ima.8*

%files plugin-prioreset
%{_libdir}/rpm-plugins/prioreset.so
%{_rpmmacrodir}/macros.transaction_prioreset
%{_mandir}/man8/rpm-plugin-prioreset.8*

%files plugin-selinux
%{_libdir}/rpm-plugins/selinux.so
%{_rpmmacrodir}/macros.transaction_selinux
%{_mandir}/man8/rpm-plugin-selinux.8*

%files plugin-syslog
%{_libdir}/rpm-plugins/syslog.so
%{_rpmmacrodir}/macros.transaction_syslog
%{_mandir}/man8/rpm-plugin-syslog.8*

%files plugin-systemd-inhibit
%{_libdir}/rpm-plugins/systemd_inhibit.so
%{_rpmmacrodir}/macros.transaction_systemd_inhibit
%{_mandir}/man8/rpm-plugin-systemd-inhibit.8*

%files plugin-unshare
%{_libdir}/rpm-plugins/unshare.so
%{_rpmmacrodir}/macros.transaction_unshare
%{_mandir}/man8/rpm-plugin-unshare.8*

%files plugin-fsverity
%{_libdir}/rpm-plugins/fsverity.so
%{_rpmmacrodir}/macros.transaction_fsverity

%files build
%{_bindir}/gendiff
%{_bindir}/rpmbuild
%{_bindir}/rpmlua
%{_bindir}/rpmspec
%{_bindir}/rpmuncompress
%{_rpmconfigdir}/brp-*
%{_rpmconfigdir}/check-*
%{_rpmconfigdir}/elfdeps
%{_rpmconfigdir}/fileattrs/
%{_rpmconfigdir}/find-lang.sh
%{_rpmconfigdir}/find-provides
%{_rpmconfigdir}/find-requires
%{_rpmconfigdir}/fontconfig.prov
%{_rpmconfigdir}/ocamldeps.sh
%{_rpmconfigdir}/pkgconfigdeps.sh
%{_rpmconfigdir}/rpm_macros_provides.sh
%{_rpmconfigdir}/rpmdeps
%{_rpmconfigdir}/rpmdump
%{_rpmconfigdir}/rpmuncompress
%{_rpmconfigdir}/script.req
%{_mandir}/man1/elfdeps.1*
%{_mandir}/man1/gendiff.1*
%{_mandir}/man1/rpmbuild.1*
%{_mandir}/man1/rpmdeps.1*
%{_mandir}/man1/rpmlua.1*
%{_mandir}/man1/rpmspec.1*
%{_mandir}/man1/rpmuncompress.1*
%{_mandir}/man5/rpmbuild-config.5*

%files devel
%{_bindir}/rpmgraph
%{_includedir}/rpm/
%{_libdir}/librpm.so
%{_libdir}/librpmbuild.so
%{_libdir}/librpmio.so
%{_libdir}/librpmsign.so
%{_libdir}/pkgconfig/rpm.pc
%{_libdir}/cmake/rpm/
%{_mandir}/man1/rpmgraph.1*

%files apidocs
%{_docdir}/rpm/API/
