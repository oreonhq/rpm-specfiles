%global source0_hash 77c9303ee60b9bedf722012ea29ae3711ba13a67c9b9ae28993838b63057cb1b
%bcond check 0
%global debug_package %{nil}
%global crate tabled
Name:           rust-tabled
Version:        0.16.0
Release:        1%{?dist}
Summary:        Easy to use library for pretty print tables of Rust structs and enums
License:        MIT
URL:            https://crates.io/crates/tabled
Source0:        https://static.crates.io/crates/tabled/tabled-%{version}.crate
Patch:          tabled-fix-metadata.diff
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
Summary:        Easy to use library for pretty print tables of Rust structs and enums
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+ansi-devel
Summary:        Easy to use library for pretty print tables of Rust structs and enums
BuildArch:      noarch
%description -n %{name}+ansi-devel

This package contains library source intended for building other packages which
use the "ansi" feature of the "%{crate}" crate.

%package     -n %{name}+ansi-str-devel
Summary:        Easy to use library for pretty print tables of Rust structs and enums
BuildArch:      noarch
%description -n %{name}+ansi-str-devel

This package contains library source intended for building other packages which
use the "ansi-str" feature of the "%{crate}" crate.

%package     -n %{name}+ansitok-devel
Summary:        Easy to use library for pretty print tables of Rust structs and enums
BuildArch:      noarch
%description -n %{name}+ansitok-devel

This package contains library source intended for building other packages which
use the "ansitok" feature of the "%{crate}" crate.

%package     -n %{name}+derive-devel
Summary:        Easy to use library for pretty print tables of Rust structs and enums
BuildArch:      noarch
%description -n %{name}+derive-devel

This package contains library source intended for building other packages which
use the "derive" feature of the "%{crate}" crate.

%package     -n %{name}+macros-devel
Summary:        Easy to use library for pretty print tables of Rust structs and enums
BuildArch:      noarch
%description -n %{name}+macros-devel

This package contains library source intended for building other packages which
use the "macros" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Easy to use library for pretty print tables of Rust structs and enums
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+tabled_derive-devel
Summary:        Easy to use library for pretty print tables of Rust structs and enums
BuildArch:      noarch
%description -n %{name}+tabled_derive-devel

This package contains library source intended for building other packages which
use the "tabled_derive" feature of the "%{crate}" crate.

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

%cargo_test -- -- --exact --skip core::table_test::derived::table_emojie_multiline --skip settings::render_settings::tab_isnot_handled_by_default_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-tabled-devel -f %{oreon_filedir}/rust-tabled-devel.list

%changelog

%autochangelog
