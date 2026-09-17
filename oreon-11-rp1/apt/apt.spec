%global source0_hash 07dc462c87833aab9862c9b1f815cfeb6b8dd40cb05eb368d8f7007571347cb3

# Force out of source build
%undefine __cmake_in_source_build

%{!?jobs:%global jobs %(/usr/bin/getconf _NPROCESSORS_ONLN)}

# apt library somajor...
%global libsomajor 7.0
%global libprivsomajor 0.0

# Disable integration tests by default,
# as there is a bunch of failures on non-Debian systems currently.
# Additionally, these tests take a long time to run.
%bcond check_integration 1

Name:           apt
Version:        3.1.16
Release:        2%{?dist}
Summary:        Command-line package manager for Debian packages

License:        GPL-2.0-or-later
URL:            https://tracker.debian.org/pkg/apt
Source0:        https://salsa.debian.org/apt-team/%{name}/-/archive/%{version}/%{name}-%{version}.tar.gz
Patch1:         apt_include_cstdint.patch
Patch2:         apt-2.9.27-cstdint.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake >= 3.4
BuildRequires:  ninja-build
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig(gnutls) >= 3.4.6
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libxxhash)
%{?el9:BuildRequires: gcc-toolset-15}
%{?el9:BuildRequires: gcc-toolset-15-gcc-plugin-annobin}

# Package manager BRs
BuildRequires:  dpkg-dev

# These BRs lack pkgconfig() names
BuildRequires:  libdb-devel
BuildRequires:  gtest-devel
BuildRequires:  bzip2-devel

# Misc BRs
BuildRequires:  triehash
BuildRequires:  po4a >= 0.35
BuildRequires:  docbook-style-xsl, docbook-dtds
BuildRequires:  gettext >= 0.19
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  w3m
BuildRequires:  %{_bindir}/xsltproc

%if %{with check_integration}
BuildRequires:  coreutils, moreutils,
BuildRequires:  moreutils-parallel
BuildRequires:  fakeroot, lsof, sed
BuildRequires:  tar, wget, stunnel
BuildRequires:  gnupg, gnupg2
BuildRequires:  perl(File::FcntlLock)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  debhelper >= 9
# Unbreak running tests in non-interactive terminals
BuildRequires:  expect
%endif

# For ensuring the user is created
%{?el9:Requires(pre): shadow-utils}

# Apt is essentially broken without dpkg
Requires:       dpkg >= 1.17.14

# To ensure matching apt libs are installed
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

# These is one optional script in apt that still requires perl, so let's make
# perl a recommended dependency as apt can be used without perl.
%global __requires_exclude_from ^%{_libexecdir}/dpkg/methods/apt/setup$
Recommends: /usr/bin/perl

# apt-transport-curl-https is gone...
Provides:       %{name}-transport-https = %{version}-%{release}
Provides:       %{name}-transport-curl-https = %{version}-%{release}

%description
This package provides commandline tools for searching and
managing as well as querying information about packages
as a low-level access to all features of the libapt-pkg library.

These include:
  * apt-get for retrieval of packages and information about them
    from authenticated sources and for installation, upgrade and
    removal of packages together with their dependencies
  * apt-cache for querying available information about installed
    as well as installable packages
  * apt-cdrom to use removable media as a source for packages
  * apt-config as an interface to the configuration settings
  * apt-key as an interface to manage authentication keys

%package libs
Summary:        Runtime libraries for %{name}

%description libs
This package includes the libapt-pkg library.

libapt-pkg provides the common functionality for searching and
managing packages as well as information about packages.
Higher-level package managers can depend upon this library.

This includes:
  * retrieval of information about packages from multiple sources
  * retrieval of packages and all dependent packages
    needed to satisfy a request either through an internal
    solver or by interfacing with an external one
  * authenticating the sources and validating the retrieved data
  * installation and removal of packages in the system
  * providing different transports to retrieve data over cdrom, ftp,
    http, rsh as well as an interface to add more transports like
    debtorrent (apt-transport-debtorrent).

%package doc
Summary:        Documentation for APT
BuildArch:      noarch

%description doc
This package contains the user guide and offline guide for various
APT tools which are provided in a html and a text-only version.

%package devel
Summary:        Development files for APT's libraries
Provides:       libapt-pkg-devel%{?_isa} = %{version}-%{release}
Provides:       libapt-pkg-devel = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
This package contains the header files and libraries for
developing with APT's libapt-pkg Debian package manipulation
library.

%package apidoc
Summary:        Documentation for developing against APT libraries
Provides:       libapt-pkg-doc = %{version}-%{release}
Obsoletes:      %{name}-devel-doc < 1.9.7-1
Provides:       %{name}-devel-doc = %{version}-%{release}
BuildArch:      noarch

%description apidoc
This package contains documentation for development of the APT
Debian package manipulation program and its libraries.

This includes the source code documentation generated by doxygen
in html format.

%package utils
Summary:        Package management related utility programs
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description utils
This package contains some less used commandline utilities related
to package management with APT.

  * apt-extracttemplates is used by debconf to prompt for configuration
    questions before installation.
  * apt-ftparchive is used to create Packages and other index files
    needed to publish an archive of Debian packages
  * apt-sortpkgs is a Packages/Sources file normalizer.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Create a sysusers.d config file
cat >apt.sysusers.conf <<EOF
u _apt - 'APT account for owning persistent & cache data' %{_sharedstatedir}/apt -
EOF

%build
%{?el9:source /opt/rh/gcc-toolset-15/enable}
%cmake -GNinja
%cmake_build

%install
%{?el9:source /opt/rh/gcc-toolset-15/enable}
%cmake_install

%find_lang %{name}
%find_lang %{name}-utils
%find_lang libapt-pkg%{libsomajor}

cat libapt*.lang >> %{name}-libs.lang

mkdir -p %{buildroot}%{_localstatedir}/log/apt
touch %{buildroot}%{_localstatedir}/log/apt/{term,history}.log
mkdir -p %{buildroot}%{_sysconfdir}/apt/{apt.conf,preferences,sources.list,trusted.gpg}.d
install -pm 644 doc/examples/apt.conf %{buildroot}%{_sysconfdir}/apt/
touch %{buildroot}%{_sysconfdir}/apt/sources.list
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
cat > %{buildroot}%{_sysconfdir}/logrotate.d/apt <<EOF
%{_localstatedir}/log/apt/term.log {
  rotate 12
  monthly
  compress
  missingok
  notifempty
}
%{_localstatedir}/log/apt/history.log {
  rotate 12
  monthly
  compress
  missingok
  notifempty
}
EOF

%if 0%{?fedora} || 0%{?rhel} > 9
install -m0644 -D apt.sysusers.conf %{buildroot}%{_sysusersdir}/apt.conf
%endif

%check
%{?el9:source /opt/rh/gcc-toolset-15/enable}
%ctest
%if %{with check_integration}
unbuffer ./test/integration/run-tests -q %{?jobs:-j %{jobs}}
%endif

# Create the _apt user+group for apt data
%pre
getent group _apt >/dev/null || groupadd -r _apt
getent passwd _apt >/dev/null || \
    useradd -r -g _apt -d %{_sharedstatedir}/apt -s /sbin/nologin \
    -c "APT account for owning persistent & cache data" _apt
exit 0

%ldconfig_scriptlets libs

%files -f %{name}.lang
%license COPYING*
%doc README.* AUTHORS
%{_bindir}/apt
%{_bindir}/apt-cache
%{_bindir}/apt-cdrom
%{_bindir}/apt-config
%{_bindir}/apt-get
%{_bindir}/apt-mark
%dir %{_libexecdir}/apt
%{_libexecdir}/apt/apt-helper
%{_libexecdir}/apt/methods
%{_libexecdir}/dpkg/methods/apt
%attr(-,_apt,_apt) %{_sharedstatedir}/apt
%attr(-,_apt,_apt) %{_localstatedir}/cache/apt
%dir %attr(-,_apt,_apt) %{_localstatedir}/log/apt
%ghost %{_localstatedir}/log/apt/history.log
%ghost %{_localstatedir}/log/apt/term.log
%dir %attr(-,_apt,_apt) %{_sysconfdir}/apt/apt.conf.d
%dir %attr(-,_apt,_apt) %{_sysconfdir}/apt/preferences.d
%dir %attr(-,_apt,_apt) %{_sysconfdir}/apt/sources.list.d
%dir %attr(-,_apt,_apt) %{_sysconfdir}/apt/trusted.gpg.d
%config(noreplace) %attr(-,_apt,_apt) %{_sysconfdir}/apt/apt.conf
%ghost %{_sysconfdir}/apt/sources.list
%config(noreplace) %{_sysconfdir}/logrotate.d/apt
%{_datadir}/bash-completion/completions/apt
%{_mandir}/*/*/apt.*
%{_mandir}/*/*/apt-cache.*
%{_mandir}/*/*/apt-cdrom.*
%{_mandir}/*/*/apt-config.*
%{_mandir}/*/*/apt-get.*
%{_mandir}/*/*/apt-mark.*
%{_mandir}/*/*/apt-patterns.*
%{_mandir}/*/*/apt-secure.*
%{_mandir}/*/*/apt-transport-http.*
%{_mandir}/*/*/apt-transport-https.*
%{_mandir}/*/*/apt-transport-mirror.*
%{_mandir}/*/*/apt_auth.*
%{_mandir}/*/*/apt_preferences.*
%{_mandir}/*/*/sources.list.*
%{_mandir}/*/apt.*
%{_mandir}/*/apt-cache.*
%{_mandir}/*/apt-cdrom.*
%{_mandir}/*/apt-config.*
%{_mandir}/*/apt-get.*
%{_mandir}/*/apt-mark.*
%{_mandir}/*/apt-patterns.*
%{_mandir}/*/apt-secure.*
%{_mandir}/*/apt-transport-http.*
%{_mandir}/*/apt-transport-https.*
%{_mandir}/*/apt-transport-mirror.*
%{_mandir}/*/apt_auth.*
%{_mandir}/*/apt_preferences.*
%{_mandir}/*/sources.list.*
%doc %{_docdir}/%{name}/*
%if 0%{?fedora} || 0%{?rhel} > 9
%{_sysusersdir}/apt.conf
%endif

%files libs -f %{name}-libs.lang
%license COPYING*
%{_libdir}/libapt-pkg.so.%{libsomajor}{,.*}
%{_libdir}/libapt-private.so.%{libprivsomajor}{,.*}

%files doc
%doc %{_docdir}/%{name}-doc

%files apidoc
%doc %{_docdir}/libapt-pkg-doc

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*

%files utils -f %{name}-utils.lang
%{_bindir}/apt-ftparchive
%{_bindir}/apt-sortpkgs
%{_libexecdir}/apt/apt-extracttemplates
%{_libexecdir}/apt/planners
%{_libexecdir}/apt/solvers
%{_mandir}/*/*/apt-extracttemplates.*
%{_mandir}/*/*/apt-ftparchive.*
%{_mandir}/*/*/apt-sortpkgs.*
%{_mandir}/*/apt-extracttemplates.*
%{_mandir}/*/apt-ftparchive.*
%{_mandir}/*/apt-sortpkgs.*
%doc %{_docdir}/%{name}-utils

%changelog
%autochangelog
