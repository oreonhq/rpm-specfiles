%global source0_hash 622696e514e0b2922a4deed3bcdb599fd4c92bc3e45eeb4fa915cdb1d993e931
%bcond check 1
%global crate resctl-bench
Name:           rust-resctl-bench
Version:        2.2.5
Release:        1%{?dist}
Summary:        Whole system resource control benchmarks with realistic scenarios
License:        Apache-2.0
URL:            https://crates.io/crates/resctl-bench
Source0:        https://static.crates.io/crates/resctl-bench/resctl-bench-%{version}.crate
Patch:          resctl-bench-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Whole system resource control benchmarks with realistic scenarios
License:        %{shrink:
                0BSD AND
                Apache-2.0 AND
                ISC AND
                MIT AND
                MPL-2.0 AND
                Unicode-DFS-2016 AND
                Zlib AND
                (0BSD OR MIT OR Apache-2.0) AND
                (Apache-2.0 OR ISC OR MIT) AND
                (Apache-2.0 OR MIT) AND
                (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
                (BSD-2-Clause OR Apache-2.0 OR MIT) AND
                (MIT OR Zlib OR Apache-2.0) AND
                (Unlicense OR MIT)
                }
Requires:       rd-agent = %{version}
Requires:       rd-hashd = %{version}
%description -n %{crate}

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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n resctl-bench -f %{oreon_filedir}/resctl-bench.list

%changelog

%autochangelog
