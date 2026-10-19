%global source0_hash 537b4991a0996888e1c64872f2fd2eea978102418e0576a58c2e4a0e8c0e716e
%bcond check 1
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate uu_df
Name:           rust-uu_df
Version:        0.12.0
Release:        1%{?dist}
Summary:        df ~ (uutils) display file system information
License:        MIT
URL:            https://crates.io/crates/uu_df
Source0:        https://static.crates.io/crates/uu_df/uu_df-%{version}.crate
Patch:          uu_df-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        df ~ (uutils) display file system information
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%install
%cargo_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%{cargo_test -- -- --exact %{shrink:
    --skip table::tests::test_default_header
    --skip table::tests::test_header_with_block_size_1024
    --skip table::tests::test_header_with_fs_type
    --skip table::tests::test_header_with_inodes
    --skip table::tests::test_human_readable_header
    --skip table::tests::test_output_header
    --skip table::tests::test_posix_portability_header
    --skip table::tests::test_table_column_width_computation_include_total_row
    --skip table::tests::test_table_column_width_non_unicode
}}
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-uu_df-devel -f %{oreon_filedir}/rust-uu_df-devel.list

%changelog

%autochangelog
