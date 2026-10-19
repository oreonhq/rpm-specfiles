%global source0_hash d4fd87ae6e70e93bccb31290c60bdeea8ac1dca5571f71502d996f49213a8e92
%bcond check 0
%global debug_package %{nil}
%global crate is_terminal_polyfill
Name:           rust-is_terminal_polyfill
Version:        1.48.2
Release:        1%{?dist}
Summary:        Polyfill for `is_terminal` stdlib feature for use with older MSRVs
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/is_terminal_polyfill
Source0:        https://static.crates.io/crates/is_terminal_polyfill/is_terminal_polyfill-%{version}.crate
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
Summary:        Polyfill for `is_terminal` stdlib feature for use with older MSRVs
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
%install
%cargo_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-is_terminal_polyfill-devel -f %{oreon_filedir}/rust-is_terminal_polyfill-devel.list

%changelog

%autochangelog
