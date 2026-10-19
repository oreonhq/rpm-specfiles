%global source0_hash 4d0261df8cda95c8f2a5ea7f9af08a68fb7d8bea478a66fa5e04e4e3b0973ce2
%bcond check 0
%global crate scx_rusty
Name:           rust-scx_rusty
Version:        0.5.4
Release:        1%{?dist}
Summary:        A multi-domain, BPF / user space hybrid scheduler
License:        GPL-2.0-only
URL:            https://crates.io/crates/scx_rusty
Source0:        https://static.crates.io/crates/scx_rusty/scx_rusty-%{version}.crate
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        A multi-domain, BPF / user space hybrid scheduler
License:        GPL-2.0-only AND (MIT OR Apache-2.0) AND Unicode-3.0 AND Unicode-DFS-2016 AND Apache-2.0 AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND BSD-2-Clause AND BSD-3-Clause AND (BSD-3-Clause OR MIT OR Apache-2.0) AND ISC AND (LGPL-2.1-only OR BSD-2-Clause) AND MIT AND (Unlicense OR MIT) AND Zlib
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
%files -n scx_rusty -f %{oreon_filedir}/scx_rusty.list

%changelog

%autochangelog
