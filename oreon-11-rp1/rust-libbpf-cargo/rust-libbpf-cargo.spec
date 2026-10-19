%global source0_hash 626c6fbcb5088716de86d0ccbdccedc17b13e59f41a605a3274029335e71fcbb
%bcond check 0
%global crate libbpf-cargo
Name:           rust-libbpf-cargo
Version:        0.25.0
Release:        1%{?dist}
Summary:        Cargo plugin to build bpf programs
License:        LGPL-2.1-only OR BSD-2-Clause
URL:            https://crates.io/crates/libbpf-cargo
Source0:        https://static.crates.io/crates/libbpf-cargo/libbpf-cargo-%{version}.crate
Patch:          libbpf-cargo-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  clang
BuildRequires:  rustc
BuildRequires:  rustfmt
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Cargo plugin to build bpf programs
License:        %{shrink:
    (LGPL-2.1-only OR BSD-2-Clause)
    AND BSD-2-Clause
    AND MIT
    AND (Apache-2.0 OR MIT)
    AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT)
    AND (Unlicense OR MIT)
}
Requires:       clang
Requires:       rustfmt
%description -n %{crate}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       clang
Requires:       rustfmt
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Cargo plugin to build bpf programs
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
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%cargo_install
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n libbpf-cargo -f %{oreon_filedir}/libbpf-cargo.list
%files -n rust-libbpf-cargo-devel -f %{oreon_filedir}/rust-libbpf-cargo-devel.list

%changelog

%autochangelog
