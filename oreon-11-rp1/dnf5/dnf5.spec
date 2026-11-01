%global source0_hash 242f0e775bc8e1017a5bfec841c776beafa7ea6b5bd2e4d7bc0ff9d7c57998f3
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: dnf5
Version: 5.4.6.0
Release: 1%{?dist}
Summary: Command-line package manager
License: GPL-2.0-or-later AND LGPL-2.1-or-later
URL: https://github.com/rpm-software-management/dnf5
Source0: https://github.com/rpm-software-management/dnf5/archive/%{version}/dnf5-%{version}.tar.gz
Provides: libdnf5 = %{version}-%{release}
Provides: libdnf5-cli = %{version}-%{release}
Provides: dnf5daemon-server = %{version}-%{release}
Requires: rpm

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: patchelf
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: pkgconf
BuildRequires: gettext
BuildRequires: fmt-devel
BuildRequires: toml11-devel
BuildRequires: json-c-devel
BuildRequires: libsolv-devel
BuildRequires: librepo-devel
BuildRequires: libmodulemd-devel
BuildRequires: libcomps-devel
BuildRequires: rpm-devel
BuildRequires: sqlite-devel
BuildRequires: libxml2-devel
BuildRequires: glib2-devel
BuildRequires: libacl-devel
BuildRequires: libsmartcols-devel
BuildRequires: zchunk-devel
BuildRequires: systemd-devel
BuildRequires: sdbus-cpp-devel
BuildRequires: libcurl-devel
BuildRequires: openssl-devel

%description
DNF5 is the C++ rewrite of the DNF package manager, with libdnf5 and the
dnf5daemon D-Bus service.

%package devel
Summary: Development files for dnf5
Requires: dnf5%{?_isa} = %{version}-%{release}
Provides: libdnf5-devel = %{version}-%{release}
Provides: pkgconfig(libdnf5)
Provides: pkgconfig(libdnf5-cli)

%description devel
Headers and libraries for developing against dnf5.

%prep
%oreon_sha256
%autosetup -n dnf5-%{version} -p1

%build
%oreon_cmake \
  -DWITH_HTML=OFF -DWITH_MAN=OFF -DWITH_TESTS=OFF -DWITH_PERFORMANCE_TESTS=OFF \
  -DWITH_PERL5=OFF -DWITH_PYTHON3=OFF -DWITH_RUBY=OFF -DWITH_GO=OFF -DWITH_PYTHON_PLUGINS_LOADER=OFF \
  -DWITH_PLUGIN_APPSTREAM=OFF -DWITH_PLUGIN_MANIFEST=OFF -DWITH_PLUGIN_RHSM=OFF \
  -DWITH_DNF5_OBSOLETES_DNF=OFF -DWITH_SANITIZERS=OFF
%oreon_cmake_build

%install
%oreon_cmake_install
mkdir -p %{buildroot}%{_sysconfdir}/dnf/repos.d %{buildroot}%{_localstatedir}/cache/libdnf5
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_infodir}/dir
find %{buildroot} -type f | while read -r f; do
  file -b "$f" | grep -q '^ELF' || continue
  r=$(patchelf --print-rpath "$f" 2>/dev/null || true)
  if [ -n "$r" ]; then
    chmod u+w "$f"
    patchelf --remove-rpath "$f"
  fi
done
%oreon_filelist_devel

%files -f %{_builddir}/%{name}.files
%license COPYING.md
%dir %{_sysconfdir}/dnf/repos.d
%dir %{_localstatedir}/cache/libdnf5

%files devel -f %{_builddir}/%{name}-devel.files
