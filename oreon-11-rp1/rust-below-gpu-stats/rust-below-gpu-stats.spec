%global source0_hash ec38853e07395f62c8ba3e7429184dbfe763eae16ce2e3254b6c4d7824d40d71
%bcond check 1
%global debug_package %{nil}
%global crate below-gpu-stats
Name:           rust-below-gpu-stats
Version:        0.9.0
Release:        1%{?dist}
Summary:        GPU stats crate for below
License:        Apache-2.0
URL:            https://crates.io/crates/below-gpu-stats
Source0:        https://static.crates.io/crates/below-gpu-stats/below-gpu-stats-%{version}.crate
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
Summary:        GPU stats crate for below
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
%files -n rust-below-gpu-stats-devel -f %{oreon_filedir}/rust-below-gpu-stats-devel.list

%changelog

%autochangelog
