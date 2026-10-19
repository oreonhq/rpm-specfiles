%global source0_hash bd070e393353796e801d209ad339e89596eb4c8d430d18ede6a1cced8fafbd99
%bcond check 0
%global debug_package %{nil}
%global crate indexmap
Name:           rust-indexmap1
Version:        1.9.3
Release:        1%{?dist}
Summary:        A hash table with consistent order and fast iteration.
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/indexmap
Source0:        https://static.crates.io/crates/indexmap/indexmap-%{version}.crate
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
Summary:        A hash table with consistent order and fast iteration.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+arbitrary-devel
Summary:        A hash table with consistent order and fast iteration.
BuildArch:      noarch
%description -n %{name}+arbitrary-devel

This package contains library source intended for building other packages which
use the "arbitrary" feature of the "%{crate}" crate.

%package     -n %{name}+quickcheck-devel
Summary:        A hash table with consistent order and fast iteration.
BuildArch:      noarch
%description -n %{name}+quickcheck-devel

This package contains library source intended for building other packages which
use the "quickcheck" feature of the "%{crate}" crate.

%package     -n %{name}+rayon-devel
Summary:        A hash table with consistent order and fast iteration.
BuildArch:      noarch
%description -n %{name}+rayon-devel

This package contains library source intended for building other packages which
use the "rayon" feature of the "%{crate}" crate.

%package     -n %{name}+rustc-rayon-devel
Summary:        A hash table with consistent order and fast iteration.
BuildArch:      noarch
%description -n %{name}+rustc-rayon-devel

This package contains library source intended for building other packages which
use the "rustc-rayon" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        A hash table with consistent order and fast iteration.
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde-1-devel
Summary:        A hash table with consistent order and fast iteration.
BuildArch:      noarch
%description -n %{name}+serde-1-devel

This package contains library source intended for building other packages which
use the "serde-1" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        A hash table with consistent order and fast iteration.
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+test_debug-devel
Summary:        A hash table with consistent order and fast iteration.
BuildArch:      noarch
%description -n %{name}+test_debug-devel

This package contains library source intended for building other packages which
use the "test_debug" feature of the "%{crate}" crate.

%package     -n %{name}+test_low_transition_point-devel
Summary:        A hash table with consistent order and fast iteration.
BuildArch:      noarch
%description -n %{name}+test_low_transition_point-devel

This package contains library source intended for building other packages which
use the "test_low_transition_point" feature of the "%{crate}" crate.

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
%files -n rust-indexmap1-devel -f %{oreon_filedir}/rust-indexmap1-devel.list

%changelog

%autochangelog
