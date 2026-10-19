%global source0_hash 0b690636d34b4e104bb3c40d9196cd8eab80c90f22e8058ffe57f78d0fd62e7f
%bcond check 1
%global crate rd-hashd
Name:           rust-rd-hashd
Version:        2.2.5
Release:        1%{?dist}
Summary:        Latency-sensitive pseudo workload for resctl-demo
License:        Apache-2.0
URL:            https://crates.io/crates/rd-hashd
Source0:        https://static.crates.io/crates/rd-hashd/rd-hashd-%{version}.crate
Patch:          rd-hashd-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Latency-sensitive pseudo workload for resctl-demo
License:        %{shrink:
                Apache-2.0 AND
                BSD-3-Clause AND
                MIT AND
                Unicode-DFS-2016 AND
                (Apache-2.0 OR BSL-1.0) AND
                (Apache-2.0 OR MIT) AND
                (BSD-2-Clause OR Apache-2.0 OR MIT) AND
                (Unlicense OR MIT)
                }
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
%files -n rd-hashd -f %{oreon_filedir}/rd-hashd.list

%changelog

%autochangelog
