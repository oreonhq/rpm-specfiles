%global source0_hash cd0b0ec5f1c1ca621c432a25813d8d60c88abe6d3e08a3eb9cf37d97a0fe3d73
%bcond check 0
%global debug_package %{nil}
%global crate send_wrapper
Name:           rust-send_wrapper
Version:        0.6.0
Release:        1%{?dist}
Summary:        Wrapper type to allow moving non-Send types between threads
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/send_wrapper
Source0:        https://static.crates.io/crates/send_wrapper/send_wrapper-%{version}.crate
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
Summary:        Wrapper type to allow moving non-Send types between threads
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+futures-devel
Summary:        Wrapper type to allow moving non-Send types between threads
BuildArch:      noarch
%description -n %{name}+futures-devel

This package contains library source intended for building other packages which
use the "futures" feature of the "%{crate}" crate.

%package     -n %{name}+futures-core-devel
Summary:        Wrapper type to allow moving non-Send types between threads
BuildArch:      noarch
%description -n %{name}+futures-core-devel

This package contains library source intended for building other packages which
use the "futures-core" feature of the "%{crate}" crate.

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
%files -n rust-send_wrapper-devel -f %{oreon_filedir}/rust-send_wrapper-devel.list

%changelog

%autochangelog
