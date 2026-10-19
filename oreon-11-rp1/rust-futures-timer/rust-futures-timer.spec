%global source0_hash af43fadb8a98512d547e37b4e92e0ced13e205c061b87b4623eff01d918d6968
%bcond check 0
%global debug_package %{nil}
%global crate futures-timer
Name:           rust-futures-timer
Version:        3.0.4
Release:        2%{?dist}
Summary:        Timeouts for futures
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/futures-timer
Source0:        https://static.crates.io/crates/futures-timer/futures-timer-%{version}.crate
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
Summary:        Timeouts for futures
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
%files -n rust-futures-timer-devel -f %{oreon_filedir}/rust-futures-timer-devel.list

%changelog

%autochangelog
