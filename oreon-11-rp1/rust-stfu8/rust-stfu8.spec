%global source0_hash e51f1e89f093f99e7432c491c382b88a6860a5adbe6bf02574bf0a08efff1978
%bcond check 0
%global debug_package %{nil}
%global crate stfu8
Name:           rust-stfu8
Version:        0.2.7
Release:        1%{?dist}
Summary:        Sorta Text Format in UTF-8
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/stfu8
Source0:        https://static.crates.io/crates/stfu8/stfu8-%{version}.crate
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
Summary:        Sorta Text Format in UTF-8
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+testing-devel
Summary:        Sorta Text Format in UTF-8
BuildArch:      noarch
%description -n %{name}+testing-devel

This package contains library source intended for building other packages which
use the "testing" feature of the "%{crate}" crate.

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
%files -n rust-stfu8-devel -f %{oreon_filedir}/rust-stfu8-devel.list

%changelog

%autochangelog
