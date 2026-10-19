%global source0_hash b85697d713dfd1fcc1b0df3fee14289e345fbe0df576f695f8cf3ae1bfef2254
ExcludeArch: %{ix86}
Name:           galera
Version:        26.4.27
Release:        1%{?dist}
Summary:        Synchronous multi-master wsrep provider (replication engine)
License:        GPL-2.0-only
URL:            https://mariadb.com/docs/galera-cluster
Source0:        https://archive.mariadb.org/mariadb-11.8/%{name}-%{version}/src/%{name}-%{version}.tar.gz
Requires:       nmap-ncat
Requires:       procps-ng
%{?systemd_requires}
# oreon:deps
BuildRequires:  asio-devel
BuildRequires:  boost-devel
BuildRequires:  check-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  openssl-devel
BuildRequires:  systemd
# /oreon:deps
%description
Galera is a fast synchronous multimaster wsrep provider (replication engine)
for transactional databases and similar applications. For more information
about wsrep API see https://github.com/codership/wsrep-API repository. For a
description of Galera replication engine see https://www.galeracluster.com web.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
find . -type f \( -name '*.hpp' -o -name '*.cpp' -o -name '*.h' \) -exec sed -i 's/asio::io_service/asio::io_context/g; s/io_service\.hpp/io_context.hpp/g' {} +

# Create a sysusers.d config file
cat >galera.sysusers.conf <<EOF
u garb - 'Galera Arbitrator Daemon' /dev/null -
EOF

%build

%cmake \
       -DCMAKE_BUILD_TYPE="%{?with_debug:Debug}%{!?with_debug:RelWithDebInfo}" \
       -DINSTALL_LAYOUT=RPM \
       -DCMAKE_RULE_MESSAGES:BOOL=OFF \
       \
       -DBUILD_SHARED_LIBS:BOOL=OFF \
       \
       -DINSTALL_DOCDIR="share/doc/%{name}/" \
       -DINSTALL_GARBD="bin" \
       -DINSTALL_GARBD-SYSTEMD="bin" \
       -DINSTALL_CONFIGURATION="/etc/sysconfig/" \
       -DINSTALL_SYSTEMD_SERVICE="lib/systemd/system" \
       -DINSTALL_LIBDIR="%{_lib}/galera" \
       -DINSTALL_MANPAGE="share/man/man8"
cmake -B %_vpath_builddir -N -LAH
%cmake_build
%install
%cmake_install
sed -i 's/User=nobody/User=garb/g' %{buildroot}%{_unitdir}/garb.service
install -m0644 -D galera.sysusers.conf %{buildroot}%{_sysusersdir}/galera.conf
%oreon_autofiles main

%check

%ctest
%pre

unlink /etc/systemd/system/garb.service || :
%post

/sbin/ldconfig
%systemd_post garb.service
%preun

%systemd_preun garb.service
%postun

/sbin/ldconfig
%systemd_postun_with_restart garb.service
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 26.4.25-1
- Prepare for Oreon 11 (RP1)
