%global source0_hash ff8705fc79b886ed392baac4c513363d92b8a13ee91f4726a79fe8a8695bf078
%bcond check 1
%global cargo_install_lib 0
%global crate sccache
Name:           rust-sccache
Version:        0.13.0
Release:        1%{?dist}
Summary:        Sccache is a ccache-like tool
License:        Apache-2.0 AND (Apache-2.0 OR MIT)
URL:            https://crates.io/crates/sccache
Source0:        https://static.crates.io/crates/sccache/sccache-%{version}.crate
Patch:          sccache-fix-metadata-auto.diff
Patch:          sccache-fix-metadata.diff
ExcludeArch:  %{ix86}
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Sccache is a ccache-like tool
License:        # FIXME
%description -n %{crate}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
rm -f tests/oauth.rs
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%cargo_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%{cargo_test -- -- %{shrink:
    --skip test_rust_cargo_build
    --skip test_rust_cargo_build_readonly
    --skip test_rust_cargo_check
    --skip test_rust_cargo_check_readonly
    --skip test_rust_cargo_cmd_readonly_preemtive_block
    --skip test_rust_cargo_run_with_env_dep_parsing
    --skip test_adv_cache_hit_rate
    --skip test_cache_hit_rate
    --skip test_generate_hash_key
    --skip test_rlib_dep_reader_call
}}
%endif
%files -f %{oreon_filedir}/main.list
%files -n sccache -f %{oreon_filedir}/sccache.list

%changelog

%autochangelog
