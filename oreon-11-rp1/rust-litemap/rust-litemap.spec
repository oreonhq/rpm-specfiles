%global source0_hash 47d9d19d1d6efa0109d2f65ff4c85cddd50bd572e5a00127ab10987290bcefae
%bcond check 0
%global debug_package %{nil}
%global crate litemap
Name:           rust-litemap
Version:        0.8.3
Release:        1%{?dist}
Summary:        A key-value Map implementation based on a flat, sorted Vec.
License:        Unicode-3.0
URL:            https://crates.io/crates/litemap
Source0:        https://static.crates.io/crates/litemap/litemap-%{version}.crate
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
Summary:        A key-value Map implementation based on a flat, sorted Vec.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        A key-value Map implementation based on a flat, sorted Vec.
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+databake-devel
Summary:        A key-value Map implementation based on a flat, sorted Vec.
BuildArch:      noarch
%description -n %{name}+databake-devel

This package contains library source intended for building other packages which
use the "databake" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        A key-value Map implementation based on a flat, sorted Vec.
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+testing-devel
Summary:        A key-value Map implementation based on a flat, sorted Vec.
BuildArch:      noarch
%description -n %{name}+testing-devel

This package contains library source intended for building other packages which
use the "testing" feature of the "%{crate}" crate.

%package     -n %{name}+yoke-devel
Summary:        A key-value Map implementation based on a flat, sorted Vec.
BuildArch:      noarch
%description -n %{name}+yoke-devel

This package contains library source intended for building other packages which
use the "yoke" feature of the "%{crate}" crate.

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
%files -n rust-litemap-devel -f %{oreon_filedir}/rust-litemap-devel.list

%changelog

%autochangelog
