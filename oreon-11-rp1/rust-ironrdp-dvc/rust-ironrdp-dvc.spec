%global source0_hash a002e6f7fc9040685250862548e80b12519b0be1b3988857ec285be8a2915b3d
%bcond check 1
%global debug_package %{nil}
%global crate ironrdp-dvc
Name:           rust-ironrdp-dvc
Version:        0.3.1
Release:        1%{?dist}
Summary:        DRDYNVC implementation and traits to implement dynamic virtual channels
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/ironrdp-dvc
Source0:        https://static.crates.io/crates/ironrdp-dvc/ironrdp-dvc-%{version}.crate
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
Summary:        DRDYNVC implementation and traits to implement dynamic virtual channels
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        DRDYNVC implementation and traits to implement dynamic virtual channels
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-ironrdp-dvc-devel -f %{oreon_filedir}/rust-ironrdp-dvc-devel.list

%changelog

%autochangelog
