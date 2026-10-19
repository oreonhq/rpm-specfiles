%global source0_hash 3580962861589c0b69efd6b385ff92ad8fdf688c91d1a0edc1a83278205e28e8
%ifnarch s390x
%bcond_without tests
%else
%if 0%{?el8}
%bcond_with    tests
%else
%bcond_without tests
%endif
%endif
%ifarch s390x
%bcond_with    unwind
%else
%bcond_without unwind
%endif
%global _firewalld_dir %{_prefix}/lib/firewalld
Name:           et
Version:        7.0.0
Release:        1%{?dist}
Summary:        Remote shell that survives IP roaming and disconnect
License:        Apache-2.0
URL:            https://mistertea.github.io/EternalTerminal/
Source0:        https://github.com/MisterTea/EternalTerminal/archive/et-v%{version}/EternalTerminal-%{version}.tar.gz
Source1:        et.xml
Patch0:         et-use-system-dependency.patch
ExcludeArch: %{ix86}
%if %{with unwind}
%endif
Provides:       bundled(base64) = 0
Provides:       bundled(cotire) = 1.8.0
Provides:       bundled(msgpack) = 3.3.0
Provides:       bundled(PlatformFolders) = 4.0.0
%ifnarch ppc64le s390x
Provides:       bundled(sentry-native) = 0.6.0
%endif
Provides:       bundled(sole) = 1.0.1
Provides:       bundled(ThreadPool) = 0
Provides:       bundled(UniversalStacktrace) = 0.0.1
%{?systemd_requires}
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  catch-devel
BuildRequires:  cmake
BuildRequires:  cpp-httplib-devel
BuildRequires:  cpp-httplib-static
BuildRequires:  cxxopts-devel
BuildRequires:  cxxopts-static
BuildRequires:  easyloggingpp-devel
BuildRequires:  easyloggingpp-static
BuildRequires:  firewalld-filesystem
BuildRequires:  gcc-c++
BuildRequires:  gflags-devel
BuildRequires:  json-devel
BuildRequires:  json-static
BuildRequires:  libatomic
BuildRequires:  libcurl-devel
BuildRequires:  libselinux-devel
BuildRequires:  libsodium-devel
BuildRequires:  libunwind-devel
BuildRequires:  libutempter-devel
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  protobuf-compiler
BuildRequires:  protobuf-lite-devel
BuildRequires:  simpleini-devel
BuildRequires:  systemd
# /oreon:deps
%description
Eternal Terminal (ET) is a remote shell that automatically reconnects without
interrupting the session.

%prep

%autosetup -p1 -n EternalTerminal-et-v%{version}
# use this if we have patches we need to apply by hand
# %%setup -q -n EternalTerminal-et-v%%{version}

# Remove bundled Catch2 test framework
rm -rf external_imported/Catch2

# Unbundle cpp-httplib
rm -rf external_imported/cpp-httplib

# Unbundle cxxopts
rm -rf external_imported/cxxopts

# Unbundle easyloggingpp
mkdir -p external_imported/easyloggingpp/src
ln -sf %{_includedir} external_imported/easyloggingpp/src

# Unbundle “JSON for Modern C++”
rm -rf external_imported/json
# both /usr/share/cmake/nlohmann_json/nlohmann_jsonConfig.cmake
# and /usr/share/pkgconfig/nlohmann_json.pc are wrong
# so we can't use find_package / pkg_check_module without further hacks anyway
#sed -r -i 's@\$\{.*\}/json/include@%{_includedir}/nlohmann@' \
#    CMakeLists.txt

# Unbundle simpleini
rm -rf external_imported/simpleini

%build

%cmake \
%ifarch ppc64le s390x
  -DDISABLE_SENTRY=ON \
%endif
  -DDISABLE_VCPKG=ON
%cmake_build
%install
%cmake_install
mkdir -p \
  %{buildroot}%{_unitdir} \
  %{buildroot}%{_sysconfdir} \
  %{buildroot}%{_firewalld_dir}/services
install -m 0644 -p systemctl/et.service %{buildroot}%{_unitdir}/et.service
install -m 0644 -p etc/et.cfg %{buildroot}%{_sysconfdir}/et.cfg
install -m 0644 %{SOURCE1} %{buildroot}%{_firewalld_dir}/services/et.xml
rm -vf %{buildroot}%{_bindir}/crashpad_handler
rm -rf %{buildroot}%{_libdir}/cmake/sentry
rm -vf %{buildroot}%{_libdir}/*.a
%oreon_autofiles main
%if %{with tests}
%check

%ctest --verbose
%endif
%post

%systemd_post et.service
%firewalld_reload
%preun

%systemd_preun et.service
%postun

%systemd_postun_with_restart et.service
%firewalld_reload
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
