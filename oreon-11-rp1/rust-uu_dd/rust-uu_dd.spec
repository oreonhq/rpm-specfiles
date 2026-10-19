%global source0_hash 1e14a3ee96607b62ca4d65807be7ec1c2b5782b36d22fe7998307a0d08b85d94
%bcond check 1
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate uu_dd
Name:           rust-uu_dd
Version:        0.7.0
Release:        1%{?dist}
Summary:        dd ~ (uutils) copy and convert files
License:        MIT
URL:            https://crates.io/crates/uu_dd
Source0:        https://static.crates.io/crates/uu_dd/uu_dd-%{version}.crate
Patch:          uu_dd-fix-metadata.diff
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
Summary:        dd ~ (uutils) copy and convert files
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
    --skip progress::tests::test_duration_precision
    --skip progress::tests::test_prog_update_write_io_lines
    --skip progress::tests::test_prog_update_write_prog_line
    --skip progress::tests::test_read_stat_report
    --skip progress::tests::test_write_stat_report
    --skip progress::tests::write_final_transfer_stats
    --skip progress::tests::write_transfer_stats
}}
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-uu_dd-devel -f %{oreon_filedir}/rust-uu_dd-devel.list

%changelog

%autochangelog
