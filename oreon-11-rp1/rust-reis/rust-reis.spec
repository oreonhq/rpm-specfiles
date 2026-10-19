%global source0_hash 827073dbe443c57fd72ae05491c6b94213218627ac6ac169850673b0cb7034f1
%bcond check 0
%global debug_package %{nil}
%global crate reis
Name:           rust-reis
Version:        0.4.0
Release:        1%{?dist}
Summary:        Pure Rust implementation of libei/libeis protocol
License:        MIT
URL:            https://crates.io/crates/reis
Source0:        https://static.crates.io/crates/reis/reis-%{version}.crate
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
Summary:        Pure Rust implementation of libei/libeis protocol
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+calloop-devel
Summary:        Pure Rust implementation of libei/libeis protocol
BuildArch:      noarch
%description -n %{name}+calloop-devel

This package contains library source intended for building other packages which
use the "calloop" feature of the "%{crate}" crate.

%package     -n %{name}+futures-devel
Summary:        Pure Rust implementation of libei/libeis protocol
BuildArch:      noarch
%description -n %{name}+futures-devel

This package contains library source intended for building other packages which
use the "futures" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        Pure Rust implementation of libei/libeis protocol
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

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
%files -n rust-reis-devel -f %{oreon_filedir}/rust-reis-devel.list

%changelog

%autochangelog
