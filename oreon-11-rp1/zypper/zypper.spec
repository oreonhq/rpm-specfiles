%global source0_hash ae3d4aa5282f621e6c54f791ca16e9db25c74f520a1520439a9e8d30a5e39f7b
%undefine __cmake_in_source_build
%global min_libzypp_ver 17.37.12
Name:           zypper
Version:        1.14.101
Release:        1%{?dist}
Summary:        Command line package manager using libzypp
License:        GPL-2.0-or-later
URL:            http://en.opensuse.org/Portal:Zypper
Source0:        https://github.com/openSUSE/zypper/archive/%{version}/%{name}-%{version}.tar.gz
Requires:       libzypp%{?_isa} >= %{min_libzypp_ver}
Recommends:     bash-completion
Recommends:     logrotate
Recommends:     cron
Recommends:     zypper-log
Provides:       zypper(oldpackage)
Provides:       zypper(updatestack-only)
Provides:       zypper(auto-agree-with-product-licenses)
Provides:       zypper(purge-kernels)
Provides:       zypper(include-all-archs)
# oreon:deps
BuildRequires:  /usr/bin/asciidoctor
BuildRequires:  /usr/bin/xsltproc
BuildRequires:  augeas-devel
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  glibc-all-langpacks
BuildRequires:  libxml2-devel
BuildRequires:  libzypp-devel
BuildRequires:  perl-generators
BuildRequires:  readline-devel
# /oreon:deps
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
mv %{buildroot}%{_bindir}/aptitude %{buildroot}%{_bindir}/zypp-aptitude
rm %{buildroot}%{_bindir}/apt-get
ln -sf zypp-aptitude %{buildroot}%{_bindir}/zypp-apt-get
rm %{buildroot}%{_bindir}/apt
ln -sf zypp-aptitude %{buildroot}%{_bindir}/zypp-apt
%if "%{_sbindir}" != "/usr/sbin"
mv %{buildroot}%{_prefix}/sbin/* %{buildroot}%{_sbindir}
rmdir %{buildroot}%{_prefix}/sbin
%endif
rm %{buildroot}%{_mandir}/man1/needs-restarting.1*
mv %{buildroot}%{_bindir}/needs-restarting %{buildroot}%{_bindir}/zypp-needs-restarting
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd %{_vpath_builddir}/tests
ctest -VV --output-on-failure .
popd
%files -f %{oreon_filedir}/main.list
%files -n zypper-log -f %{oreon_filedir}/zypper-log.list
%files -n zypper-aptitude -f %{oreon_filedir}/zypper-aptitude.list

%changelog

%autochangelog
