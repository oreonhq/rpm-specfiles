%global source0_hash 89e8bf7e0eb2dd7b4228cc1b6821fc5114cd6841ae59f652a85488c016091e5f
%bcond check 0
%global debug_package %{nil}
%global crate tester
Name:           rust-tester
Version:        0.9.1
Release:        1%{?dist}
Summary:        Fork of Rust’s test crate that doesn’t require unstable language features
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/tester
Source0:        https://static.crates.io/crates/tester/tester-%{version}.crate
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
Summary:        Fork of Rust’s test crate that doesn’t require unstable language features
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+asm_black_box-devel
Summary:        Fork of Rust’s test crate that doesn’t require unstable language features
BuildArch:      noarch
%description -n %{name}+asm_black_box-devel

This package contains library source intended for building other packages which
use the "asm_black_box" feature of the "%{crate}" crate.

%package     -n %{name}+capture-devel
Summary:        Fork of Rust’s test crate that doesn’t require unstable language features
BuildArch:      noarch
%description -n %{name}+capture-devel

This package contains library source intended for building other packages which
use the "capture" feature of the "%{crate}" crate.

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

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-tester-devel -f %{oreon_filedir}/rust-tester-devel.list

%changelog

%autochangelog
