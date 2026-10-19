%global source0_hash 3440e1cb8d0d2ec5dda3ccbcdcfd7153dd494576381c2ac974becb9a3368b8a1
%bcond check 0
%bcond bundled_rust_deps %{defined:rhel}
%global crate vhost-device-scmi
Name:           rust-vhost-device-scmi
Version:        0.4.0
Release:        1%{?dist}
Summary:        Vhost-user SCMI backend device
License:        Apache-2.0 OR BSD-3-Clause
URL:            https://crates.io/crates/vhost-device-scmi
Source0:        https://static.crates.io/crates/vhost-device-scmi/vhost-device-scmi-%{version}.crate
%if %{with bundled_rust_deps}
Source1: rust-vhost-device-scmi-%{version}-vendor.tar.xz
%endif
Patch0:         rust-vhost-device-scmi-man-page.patch
ExcludeArch:    %{ix86} %{?rhel:ppc64le} s390x
%if %{with bundled_rust_deps}
%else
%endif
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Vhost-user SCMI backend device
License:        (Apache-2.0 OR BSD-3-Clause) AND ((MIT OR Apache-2.0) AND Unicode-DFS-2016) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND BSD-3-Clause AND MIT AND (Unlicense OR MIT)
%description -n %{crate}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1 -N %{?with_bundled_rust_deps:-a1}
%autopatch -p1
%if %{without bundled_rust_deps}
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%if %{with bundled_rust_deps}
%cargo_vendor_manifest
%endif
%install
%cargo_install
mkdir -p %{buildroot}/%{_mandir}/man1
install -m 644 vhost-device-scmi.1 %{buildroot}/%{_mandir}/man1/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n vhost-device-scmi -f %{oreon_filedir}/vhost-device-scmi.list

%changelog

%autochangelog
%endif
