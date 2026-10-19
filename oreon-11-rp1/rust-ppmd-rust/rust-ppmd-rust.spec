%global source10_hash 0def91e4b686769a27afaf094a302f93fbf611f447070340f49ba640a9fbf708
%global source0_hash 196a7c80b9a7652aba7cc070827516c2abe4ccdf53d128e1944003cf5726cff1
%bcond check 1
%global debug_package %{nil}
%global crate ppmd-rust
Name:           rust-ppmd-rust
Version:        1.5.0
Release:        1%{?dist}
Summary:        PPMd compression / decompression
License:        MIT-0
URL:            https://crates.io/crates/ppmd-rust
Source0:        https://static.crates.io/crates/ppmd-rust/ppmd-rust-%{version}.crate
Source10:       https://github.com/hasenbanck/ppmd-rust/archive/v%{version}/ppmd-rust-%{version}.tar.gz
Patch:          ppmd-rust-fix-metadata.diff
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
Summary:        PPMd compression / decompression
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
rm LICENSE-CC0.md
%oreon_vendor_cargo
%build

%cargo_build
%install
%cargo_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

tar -xzvf '%{SOURCE10}' --strip-components=1 \
    ppmd-rust-%{version}/tests/fixtures
%if 0%{?__isa_bits} == 32
export RUST_TEST_THREADS=1
%endif
%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-ppmd-rust-devel -f %{oreon_filedir}/rust-ppmd-rust-devel.list

%changelog

%autochangelog
