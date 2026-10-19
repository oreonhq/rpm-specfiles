%global source0_hash e4391a6a139ecb6f7bd883e10852e7a72cc0928715ec2e48119871c5bc6d48d1
%bcond check 1
%global crate cargo-deny
Name:           rust-cargo-deny
Version:        0.18.9
Release:        1%{?dist}
Summary:        Cargo plugin to help you manage large dependency graphs
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/cargo-deny
Source0:        https://static.crates.io/crates/cargo-deny/cargo-deny-%{version}.crate
Patch:          cargo-deny-fix-metadata.diff
Patch10:        0001-Downstream-temporarily-preserve-gix-0.73-compatibili.patch
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Cargo plugin to help you manage large dependency graphs
License:        %{shrink:
    Apache-2.0 AND
    Apache-2.0 WITH LLVM-exception AND
    BSD-3-Clause AND
    CC0-1.0 AND
    CDLA-Permissive-2.0 AND
    ISC AND
    MIT AND
    Unicode-3.0 AND
    Unicode-DFS-2016 AND
    Zlib AND
    (0BSD OR MIT OR Apache-2.0) AND
    (Apache-2.0 OR BSL-1.0) AND
    (Apache-2.0 OR ISC OR MIT) AND
    (Apache-2.0 OR MIT OR Zlib) AND
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    (Unlicense OR MIT)
}
%description -n %{crate}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Cargo plugin to help you manage large dependency graphs
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+native-certs-devel
Summary:        Cargo plugin to help you manage large dependency graphs
BuildArch:      noarch
%description -n %{name}+native-certs-devel

This package contains library source intended for building other packages which
use the "native-certs" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%cargo_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%{cargo_test -- -- --exact %{shrink:
    --skip advisories::cfg::test::deserializes_advisories_cfg
    --skip bans::cfg::test::deserializes_ban_cfg
    --skip cfg::package_spec::test::deserializes_package_id
    --skip licenses::cfg::test::deserializes_licenses_cfg
    --skip licenses::gather::test::normalizes_line_endings
    --skip sources::cfg::test::deserializes_sources_cfg
    --skip test::cli_snapshot
    --skip test::validate_crates_io_sparse_dir_name
}}
%endif
%files -f %{oreon_filedir}/main.list
%files -n cargo-deny -f %{oreon_filedir}/cargo-deny.list
%files -n rust-cargo-deny-devel -f %{oreon_filedir}/rust-cargo-deny-devel.list

%changelog

%autochangelog
