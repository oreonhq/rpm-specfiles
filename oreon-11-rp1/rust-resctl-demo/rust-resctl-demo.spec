%global source0_hash d9d822bf0e4557fdf9a100bc19bd6be514c9e2d3ffc782197546a3b442ec3475
%bcond check 0
%global crate resctl-demo
Name:           rust-resctl-demo
Version:        2.2.5
Release:        1%{?dist}
Summary:        Guided tour of Linux resource control with live demos
License:        Apache-2.0
URL:            https://crates.io/crates/resctl-demo
Source0:        https://static.crates.io/crates/resctl-demo/resctl-demo-%{version}.crate
Patch:          resctl-demo-fix-metadata.diff
Patch:          resctl-demo-enum-iterator.patch
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Guided tour of Linux resource control with live demos
License:        ((MIT OR Apache-2.0) AND Unicode-DFS-2016) AND Apache-2.0 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND BSD-3-Clause AND MIT AND (MIT OR Apache-2.0) AND (Unlicense OR MIT)
Requires:       rd-agent = %{version}
Requires:       rd-hashd = %{version}
Requires:       gnuplot
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
%files -n resctl-demo -f %{oreon_filedir}/resctl-demo.list

%changelog

%autochangelog
