%global source0_hash 03251193000f4bd3b042892be858ee50e8b3719f2b08e5833ac4353724632430
%bcond check 0
%global debug_package %{nil}
%global crate reborrow
Name:           rust-reborrow
Version:        0.5.5
Release:        1%{?dist}
Summary:        Emulate reborrowing for user types.
License:        MIT
URL:            https://crates.io/crates/reborrow
Source0:        https://static.crates.io/crates/reborrow/reborrow-%{version}.crate
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
Summary:        Emulate reborrowing for user types.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+derive-devel
Summary:        Emulate reborrowing for user types.
BuildArch:      noarch
%description -n %{name}+derive-devel

This package contains library source intended for building other packages which
use the "derive" feature of the "%{crate}" crate.

%package     -n %{name}+reborrow-derive-devel
Summary:        Emulate reborrowing for user types.
BuildArch:      noarch
%description -n %{name}+reborrow-derive-devel

This package contains library source intended for building other packages which
use the "reborrow-derive" feature of the "%{crate}" crate.

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
%files -n rust-reborrow-devel -f %{oreon_filedir}/rust-reborrow-devel.list

%changelog

%autochangelog
