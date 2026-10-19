%global source0_hash 9cdf337090841a411e2a7f3deb9187445851f91b309c0c0a29e05f74a00a48c0
%bcond check 0
%global debug_package %{nil}
%global crate darling
Name:           rust-darling0.21
Version:        0.21.3
Release:        1%{?dist}
Summary:        A proc-macro library for reading attributes into structs when
License:        MIT
URL:            https://crates.io/crates/darling
Source0:        https://static.crates.io/crates/darling/darling-%{version}.crate
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
Summary:        A proc-macro library for reading attributes into structs when
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+diagnostics-devel
Summary:        A proc-macro library for reading attributes into structs when
BuildArch:      noarch
%description -n %{name}+diagnostics-devel

This package contains library source intended for building other packages which
use the "diagnostics" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        A proc-macro library for reading attributes into structs when
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+suggestions-devel
Summary:        A proc-macro library for reading attributes into structs when
BuildArch:      noarch
%description -n %{name}+suggestions-devel

This package contains library source intended for building other packages which
use the "suggestions" feature of the "%{crate}" crate.

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
%files -n rust-darling0.21-devel -f %{oreon_filedir}/rust-darling0.21-devel.list

%changelog

%autochangelog
