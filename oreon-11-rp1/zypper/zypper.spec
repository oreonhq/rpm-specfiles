%global source0_hash 19387f72fb49177a3ff1ce07a6dd4030010bde1eaf30b5a40b1e35109850d99d

# Force out of source build
%undefine __cmake_in_source_build

%global min_libzypp_ver 17.37.12

Name:           zypper
Version:        1.14.94
Release:        1%{?dist}
Summary:        Command line package manager using libzypp

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://en.opensuse.org/Portal:Zypper
Source0:        https://github.com/openSUSE/zypper/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  %{_bindir}/asciidoctor
BuildRequires:  %{_bindir}/xsltproc
BuildRequires:  cmake >= 3.5
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  perl-generators
BuildRequires:  glibc-all-langpacks
BuildRequires:  augeas-devel
BuildRequires:  boost-devel
BuildRequires:  gettext-devel
BuildRequires:  readline-devel
BuildRequires:  libxml2-devel
BuildRequires:  libzypp-devel >= %{min_libzypp_ver}
Requires:       libzypp%{?_isa} >= %{min_libzypp_ver}

# Blech, apparently we don't want bash-completion always... Cf. rhbz#1652183
Recommends:     bash-completion

Recommends:     logrotate
Recommends:     cron
Recommends:     zypper-log

# Zypper specific virtual provides
Provides:       zypper(oldpackage)
Provides:       zypper(updatestack-only)
Provides:       zypper(auto-agree-with-product-licenses)
Provides:       zypper(purge-kernels)
Provides:       zypper(include-all-archs)

%description
Zypper is a command line package manager tool using libzypp,
which can be used to manage software for RPM based systems.

%package log
Summary:        Zypper log file command line tool
Requires:       %{name} = %{version}-%{release}
Requires:       xz
BuildArch:      noarch

%description log
This package provides a command line tool for
accessing the Zypper log file.

%package aptitude
Summary:        apt/aptitude CLI compatibility interface for Zypper
Provides:       %{name}-apt = %{version}-%{release}
Requires:       %{name} = %{version}-%{release}
Enhances:       zypper
BuildArch:      noarch

%description aptitude
This package provides apt-get and aptitude frontends for Zypper,
for those used to the Debian package manager's CLI structure.

These can be accessed with either of the following:
* %{_bindir}/zypp-apt-get
* %{_bindir}/zypp-aptitude

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Use correct libexecdir
find -type f -exec sed -i -e "s|/usr/lib/zypper|%{_libexecdir}/zypper|g" {} ';'
find -type f -exec sed -i -e "s|\${CMAKE_INSTALL_PREFIX}/lib/zypper|\${CMAKE_INSTALL_PREFIX}/libexec/zypper|g" {} ';'
find -type f -exec sed -i -e "s|\${CMAKE_INSTALL_PREFIX}/lib/\${PACKAGE}|\${CMAKE_INSTALL_PREFIX}/libexec/\${PACKAGE}|g" {} ';'

# Use correct docdir
find -type f -exec sed -i -e "s|\${INSTALL_PREFIX}/share/doc/packages/\${PACKAGE}|\${INSTALL_PREFIX}/share/doc/\${PACKAGE}|g" {} ';'

%build
%cmake  -DCMAKE_BUILD_TYPE=RelWithDebInfo -DDOC_INSTALL_DIR=%{_docdir} -DENABLE_BUILD_TESTS=ON -DENABLE_BUILD_TRANS=ON
%cmake_build

%install
%cmake_install

mkdir -p %{buildroot}%{_libexecdir}/zypper/commands

%find_lang %{name}

install -dm 0755 %{buildroot}%{_localstatedir}/log
touch %{buildroot}%{_localstatedir}/log/zypper.log

# Remove conflict with apt
mv %{buildroot}%{_bindir}/aptitude %{buildroot}%{_bindir}/zypp-aptitude
# Redo the symlink to point to the new binary name
rm %{buildroot}%{_bindir}/apt-get
ln -sf zypp-aptitude %{buildroot}%{_bindir}/zypp-apt-get
rm %{buildroot}%{_bindir}/apt
ln -sf zypp-aptitude %{buildroot}%{_bindir}/zypp-apt

%if "%{_sbindir}" != "/usr/sbin"
# If sbin-bin merge, move everything accordingly
mv %{buildroot}%{_prefix}/sbin/* %{buildroot}%{_sbindir}
rmdir %{buildroot}%{_prefix}/sbin
%endif

# Remove conflicting man page and rename needs-restarting
rm %{buildroot}%{_mandir}/man1/needs-restarting.1*
mv %{buildroot}%{_bindir}/needs-restarting %{buildroot}%{_bindir}/zypp-needs-restarting

%check
pushd %{_vpath_builddir}/tests
ctest -VV --output-on-failure .
popd

%files -f %{name}.lang
%license COPYING
%doc %{_docdir}/zypper/*
%config(noreplace) %{_sysconfdir}/zypp/zypper.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/zypper.lr
%config(noreplace) %{_sysconfdir}/logrotate.d/zypp-refresh.lr
# Co-own bash-completion directories... Cf. rhbz#1652183
## This really should be owned by filesystem...
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/zypper
%{_bindir}/zypper
%{_bindir}/installation_sources
%{_bindir}/zypp-needs-restarting
%{_sbindir}/zypp-refresh
%{_datadir}/zypper/
%{_libexecdir}/zypper/
%{_mandir}/man8/zypper.8.*
%{_mandir}/man8/zypp-refresh.8.*
%ghost %config(noreplace) %attr(640,root,root) %{_localstatedir}/log/zypper.log

%files log
%{_sbindir}/zypper-log
%{_mandir}/man8/zypper-log.8.*

%files aptitude
%{_bindir}/zypp-aptitude
%{_bindir}/zypp-apt-get
%{_bindir}/zypp-apt
%dir %{_sysconfdir}/zypp/apt-packagemap.d/
%config(noreplace) %{_sysconfdir}/zypp/apt-packagemap.d/*

%changelog
%autochangelog
