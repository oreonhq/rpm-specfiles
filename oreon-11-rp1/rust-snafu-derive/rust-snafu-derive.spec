%global source0_hash c1c97747dbf44bb1ca44a561ece23508e99cb592e862f22222dcf42f51d1e451
%bcond check 1
%global debug_package %{nil}
%global crate snafu-derive
Name:           rust-snafu-derive
Version:        0.8.9
Release:        1%{?dist}
Summary:        Ergonomic error handling library
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/snafu-derive
Source0:        https://static.crates.io/crates/snafu-derive/snafu-derive-%{version}.crate
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
Summary:        Ergonomic error handling library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+rust_1_61-devel
Summary:        Ergonomic error handling library
BuildArch:      noarch
%description -n %{name}+rust_1_61-devel

This package contains library source intended for building other packages which
use the "rust_1_61" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-provider-api-devel
Summary:        Ergonomic error handling library
BuildArch:      noarch
%description -n %{name}+unstable-provider-api-devel

This package contains library source intended for building other packages which
use the "unstable-provider-api" feature of the "%{crate}" crate.

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
%files -n rust-snafu-derive-devel -f %{oreon_filedir}/rust-snafu-derive-devel.list

%changelog

%autochangelog
