%global source0_hash daf8762eb74d0e3b53126a15f88db5de3c8ee98cd3b5e3b58c1a9e21c6438873
%bcond check 1
%global debug_package %{nil}
%global crate string_cache
Name:           rust-string_cache0.10
Version:        0.10.0
Release:        1%{?dist}
Summary:        String interning library for Rust, developed as part of the Servo project
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/string_cache
Source0:        https://static.crates.io/crates/string_cache/string_cache-%{version}.crate
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
Summary:        String interning library for Rust, developed as part of the Servo project
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+malloc_size_of-devel
Summary:        String interning library for Rust, developed as part of the Servo project
BuildArch:      noarch
%description -n %{name}+malloc_size_of-devel

This package contains library source intended for building other packages which
use the "malloc_size_of" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        String interning library for Rust, developed as part of the Servo project
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde_support-devel
Summary:        String interning library for Rust, developed as part of the Servo project
BuildArch:      noarch
%description -n %{name}+serde_support-devel

This package contains library source intended for building other packages which
use the "serde_support" feature of the "%{crate}" crate.

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
%files -n rust-string_cache0.10-devel -f %{oreon_filedir}/rust-string_cache0.10-devel.list

%changelog

%autochangelog
