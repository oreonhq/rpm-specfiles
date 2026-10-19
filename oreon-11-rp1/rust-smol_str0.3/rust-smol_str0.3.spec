%global source0_hash 4aaa7368fcf4852a4c2dd92df0cace6a71f2091ca0a23391ce7f3a31833f1523
%bcond check 0
%global debug_package %{nil}
%global crate smol_str
Name:           rust-smol_str0.3
Version:        0.3.6
Release:        1%{?dist}
Summary:        small-string optimized string type with O(1) clone
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/smol_str
Source0:        https://static.crates.io/crates/smol_str/smol_str-%{version}.crate
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
Summary:        small-string optimized string type with O(1) clone
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+arbitrary-devel
Summary:        small-string optimized string type with O(1) clone
BuildArch:      noarch
%description -n %{name}+arbitrary-devel

This package contains library source intended for building other packages which
use the "arbitrary" feature of the "%{crate}" crate.

%package     -n %{name}+borsh-devel
Summary:        small-string optimized string type with O(1) clone
BuildArch:      noarch
%description -n %{name}+borsh-devel

This package contains library source intended for building other packages which
use the "borsh" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        small-string optimized string type with O(1) clone
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde_core-devel
Summary:        small-string optimized string type with O(1) clone
BuildArch:      noarch
%description -n %{name}+serde_core-devel

This package contains library source intended for building other packages which
use the "serde_core" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        small-string optimized string type with O(1) clone
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
%files -n rust-smol_str0.3-devel -f %{oreon_filedir}/rust-smol_str0.3-devel.list

%changelog

%autochangelog
