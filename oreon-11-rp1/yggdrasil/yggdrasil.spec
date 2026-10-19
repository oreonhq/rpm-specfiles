%global source0_hash 7c5ff02af7fae52e190819d4d440f9afe2c94c29a2d613211e9e0ae250c70d0a
%global source1_hash 4084f57b42b15e83acabb22e7f3ba8641d8001816801cb67a6dc2f36bcc99bea
%bcond check 1
%global go_vendor_license_check_disable 1
%global goipath         github.com/redhatinsights/yggdrasil
Version:                0.4.9
%gometa -L -f
Name:           yggdrasil
Release:        1%{?dist}
Summary:        Remote data transmission and processing client
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND EPL-2.0 AND GPL-3.0-only AND MIT AND MPL-2.0
URL:            %{gourl}
Source0:        https://github.com/redhatinsights/yggdrasil/archive/refs/tags/v%{version}.tar.gz#/yggdrasil-%{version}.tar.gz
Source1:        yggdrasil-%{version}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
Source3:        yggdrasil.sysusers
%{?systemd_requires}
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  meson
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
yggdrasil is a system daemon that subscribes to topics on an MQTT broker and
routes any data received on the topics to an appropriate child "worker" process,
exchanging data with its worker processes through a D-Bus message broker.

%package devel
Summary:        %{name} development files
%description devel
%{common_description}

Contains files needed for yggdrasil worker development.

%package examples
Summary:       %{name} example workers
Requires: %{name} = %{version}-%{release}
%description examples
%{common_description}

Contains example workers for yggdrasil.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%goprep -p1
tar -xf %{SOURCE1}

%build

%global gomodulesmode GO111MODULE=on
%meson -Dexamples=True "-Dgobuildflags=[%(echo %{expand:%gocompilerflags} | sed -e s/"^"/"'"/ -e s/" "/"', '"/g -e s/"$"/"'"/), '-tags', '"rpm_crashtraceback\ ${BUILDTAGS:-}"', '-a', '-v', '-x']" -Dgoldflags='%{?currentgoldflags} -B 0x%(head -c20 /dev/urandom|od -An -tx1|tr -d " \n") -compressdwarf=false -linkmode=external -extldflags "%{build_ldflags} %{?__golang_extldflags}"'
%meson_build
%global gosupfiles ./ipc/com.redhat.Yggdrasil1.Dispatcher1.xml ./ipc/com.redhat.Yggdrasil1.Worker1.xml
%install
%meson_install
install -d -m 0755 %{buildroot}%{_localstatedir}/lib/yggdrasil
install -D -m 0644 %{SOURCE3} %{buildroot}%{_sysusersdir}/yggdrasil.conf
%go_vendor_license_install -c %{S:2}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
%gocheck2
%endif
%post

%systemd_post %{name}.service
%systemd_user_post %{name}.service
%preun

%systemd_preun %{name}.service
%systemd_user_preun %{name}.service
%postun

%systemd_postun_with_restart %{name}.service
%systemd_user_postun_with_restart %{name}.service
%files -f %{oreon_filedir}/main.list
%files -n yggdrasil-devel -f %{oreon_filedir}/yggdrasil-devel.list
%files -n yggdrasil-examples -f %{oreon_filedir}/yggdrasil-examples.list

%changelog

* Thu May 28 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.4.9-1
- Import
