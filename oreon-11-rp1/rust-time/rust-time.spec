%global source0_hash 3e1d5e639ff6bab73cb6885cc7e7b1de96c3f32c68ec55f3952614bec1092244
%bcond check 0
%global debug_package %{nil}
%global crate time
Name:           rust-time
Version:        0.3.54
Release:        1%{?dist}
Summary:        Date and time library. Fully interoperable with the standard library....
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/time
Source0:        https://static.crates.io/crates/time/time-%{version}.crate
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
Summary:        Date and time library. Fully interoperable with the standard library....
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Date and time library. Fully interoperable with the standard library....
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+formatting-devel
Summary:        Date and time library. Fully interoperable with the standard library....
BuildArch:      noarch
%description -n %{name}+formatting-devel

This package contains library source intended for building other packages which
use the "formatting" feature of the "%{crate}" crate.

%package     -n %{name}+large-dates-devel
Summary:        Date and time library. Fully interoperable with the standard library....
BuildArch:      noarch
%description -n %{name}+large-dates-devel

This package contains library source intended for building other packages which
use the "large-dates" feature of the "%{crate}" crate.

%package     -n %{name}+local-offset-devel
Summary:        Date and time library. Fully interoperable with the standard library....
BuildArch:      noarch
%description -n %{name}+local-offset-devel

This package contains library source intended for building other packages which
use the "local-offset" feature of the "%{crate}" crate.

%package     -n %{name}+macros-devel
Summary:        Date and time library. Fully interoperable with the standard library....
BuildArch:      noarch
%description -n %{name}+macros-devel

This package contains library source intended for building other packages which
use the "macros" feature of the "%{crate}" crate.

%package     -n %{name}+parsing-devel
Summary:        Date and time library. Fully interoperable with the standard library....
BuildArch:      noarch
%description -n %{name}+parsing-devel

This package contains library source intended for building other packages which
use the "parsing" feature of the "%{crate}" crate.

%package     -n %{name}+quickcheck-devel
Summary:        Date and time library. Fully interoperable with the standard library....
BuildArch:      noarch
%description -n %{name}+quickcheck-devel

This package contains library source intended for building other packages which
use the "quickcheck" feature of the "%{crate}" crate.

%package     -n %{name}+rand-devel
Summary:        Date and time library. Fully interoperable with the standard library....
BuildArch:      noarch
%description -n %{name}+rand-devel

This package contains library source intended for building other packages which
use the "rand" feature of the "%{crate}" crate.

%package     -n %{name}+rand010-devel
Summary:        Date and time library. Fully interoperable with the standard library....
BuildArch:      noarch
%description -n %{name}+rand010-devel

This package contains library source intended for building other packages which
use the "rand010" feature of the "%{crate}" crate.

%package     -n %{name}+rand08-devel
Summary:        Date and time library. Fully interoperable with the standard library....
BuildArch:      noarch
%description -n %{name}+rand08-devel

This package contains library source intended for building other packages which
use the "rand08" feature of the "%{crate}" crate.

%package     -n %{name}+rand09-devel
Summary:        Date and time library. Fully interoperable with the standard library....
BuildArch:      noarch
%description -n %{name}+rand09-devel

This package contains library source intended for building other packages which
use the "rand09" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Date and time library. Fully interoperable with the standard library....
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde-human-readable-devel
Summary:        Date and time library. Fully interoperable with the standard library....
BuildArch:      noarch
%description -n %{name}+serde-human-readable-devel

This package contains library source intended for building other packages which
use the "serde-human-readable" feature of the "%{crate}" crate.

%package     -n %{name}+serde-well-known-devel
Summary:        Date and time library. Fully interoperable with the standard library....
BuildArch:      noarch
%description -n %{name}+serde-well-known-devel

This package contains library source intended for building other packages which
use the "serde-well-known" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Date and time library. Fully interoperable with the standard library....
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+wasm-bindgen-devel
Summary:        Date and time library. Fully interoperable with the standard library....
BuildArch:      noarch
%description -n %{name}+wasm-bindgen-devel

This package contains library source intended for building other packages which
use the "wasm-bindgen" feature of the "%{crate}" crate.

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
%files -n rust-time-devel -f %{oreon_filedir}/rust-time-devel.list

%changelog

%autochangelog
