%global source0_hash 2d2f06b9cac1506ece98fe3231e3cc9c4410ec3d5b1f24ae1c8946f0742cdefc
%bcond check 0
%global debug_package %{nil}
%global crate error-chain
Name:           rust-error-chain
Version:        0.12.4
Release:        1%{?dist}
Summary:        Yet another error boilerplate library.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/error-chain
Source0:        https://static.crates.io/crates/error-chain/error-chain-%{version}.crate
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
Summary:        Yet another error boilerplate library.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+backtrace-devel
Summary:        Yet another error boilerplate library.
BuildArch:      noarch
%description -n %{name}+backtrace-devel

This package contains library source intended for building other packages which
use the "backtrace" feature of the "%{crate}" crate.

%package     -n %{name}+example_generated-devel
Summary:        Yet another error boilerplate library.
BuildArch:      noarch
%description -n %{name}+example_generated-devel

This package contains library source intended for building other packages which
use the "example_generated" feature of the "%{crate}" crate.

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
%files -n rust-error-chain-devel -f %{oreon_filedir}/rust-error-chain-devel.list

%changelog

%autochangelog
