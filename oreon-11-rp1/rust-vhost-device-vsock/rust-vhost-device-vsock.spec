%global source0_hash 52ce95d81af89ad693d067c650e42df0f217addfbc96cc4820f7c62eb4a28b13
%bcond check 1
%bcond bundled_rust_deps 0%{?rhel:1}
%global crate vhost-device-vsock
Name:           rust-vhost-device-vsock
Version:        0.3.0
Release:        1%{?dist}
Summary:        Virtio-vsock device using the vhost-user protocol
License:        Apache-2.0 OR BSD-3-Clause
URL:            https://crates.io/crates/vhost-device-vsock
Source0:        https://static.crates.io/crates/vhost-device-vsock/vhost-device-vsock-%{version}.crate
%if %{with bundled_rust_deps}
Source1:        %{name}-%{version}-vendor.tar.xz
%endif
ExclusiveArch:  aarch64 %{!?rhel:ppc64le} riscv64 x86_64
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
Summary:        Virtio-vsock device using the vhost-user protocol
License:        Apache-2.0 AND (Apache-2.0 OR BSD-2-Clause OR MIT) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT OR Zlib) AND BSD-3-Clause AND MIT AND (MIT OR Unlicense) AND MPL-2.0 AND Unicode-DFS-2016
%description -n %{crate}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1 %{?with_bundled_rust_deps:-a1}
%if %{without bundled_rust_deps}
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{?with_bundled_rust_deps:%cargo_vendor_manifest}
%install
%cargo_install
install -pm 0644 -Dt %{buildroot}%{_mandir}/man1 %{crate}.1
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n vhost-device-vsock -f %{oreon_filedir}/vhost-device-vsock.list

%changelog

%autochangelog
%endif
