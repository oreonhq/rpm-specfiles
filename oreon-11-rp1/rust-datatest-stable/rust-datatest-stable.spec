%global source0_hash a867d7322eb69cf3a68a5426387a25b45cb3b9c5ee41023ee6cea92e2afadd82
%bcond check 1
%global debug_package %{nil}
%global crate datatest-stable
Name:           rust-datatest-stable
Version:        0.3.3
Release:        1%{?dist}
Summary:        Data-driven tests that work on stable Rust
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/datatest-stable
Source0:        https://static.crates.io/crates/datatest-stable/datatest-stable-%{version}.crate
Patch:          datatest-stable-fix-metadata.diff
Patch10:        https://github.com/nextest-rs/datatest-stable/pull/449.patch
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
Summary:        Data-driven tests that work on stable Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+include-dir-devel
Summary:        Data-driven tests that work on stable Rust
BuildArch:      noarch
%description -n %{name}+include-dir-devel

This package contains library source intended for building other packages which
use the "include-dir" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build -f include-dir
%install
%cargo_install -f include-dir
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%{cargo_test -f include-dir -- -- --exact %{shrink:
    --skip run_example
    --skip unix::run_example_with_colons
}}
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-datatest-stable-devel -f %{oreon_filedir}/rust-datatest-stable-devel.list

%changelog

%autochangelog
