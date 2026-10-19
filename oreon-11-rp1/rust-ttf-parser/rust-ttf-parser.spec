%global source0_hash d2df906b07856748fa3f6e0ad0cbaa047052d4a7dd609e231c4f72cee8c36f31
%bcond check 0
%global debug_package %{nil}
%global crate ttf-parser
Name:           rust-ttf-parser
Version:        0.25.1
Release:        1%{?dist}
Summary:        High-level, safe, zero-allocation font parser for TrueType, OpenType, and AAT
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/ttf-parser
Source0:        https://static.crates.io/crates/ttf-parser/ttf-parser-%{version}.crate
Patch:          ttf-parser-fix-metadata.diff
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
Summary:        High-level, safe, zero-allocation font parser for TrueType, OpenType, and AAT
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+apple-layout-devel
Summary:        High-level, safe, zero-allocation font parser for TrueType, OpenType, and AAT
BuildArch:      noarch
%description -n %{name}+apple-layout-devel

This package contains library source intended for building other packages which
use the "apple-layout" feature of the "%{crate}" crate.

%package     -n %{name}+glyph-names-devel
Summary:        High-level, safe, zero-allocation font parser for TrueType, OpenType, and AAT
BuildArch:      noarch
%description -n %{name}+glyph-names-devel

This package contains library source intended for building other packages which
use the "glyph-names" feature of the "%{crate}" crate.

%package     -n %{name}+gvar-alloc-devel
Summary:        High-level, safe, zero-allocation font parser for TrueType, OpenType, and AAT
BuildArch:      noarch
%description -n %{name}+gvar-alloc-devel

This package contains library source intended for building other packages which
use the "gvar-alloc" feature of the "%{crate}" crate.

%package     -n %{name}+opentype-layout-devel
Summary:        High-level, safe, zero-allocation font parser for TrueType, OpenType, and AAT
BuildArch:      noarch
%description -n %{name}+opentype-layout-devel

This package contains library source intended for building other packages which
use the "opentype-layout" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        High-level, safe, zero-allocation font parser for TrueType, OpenType, and AAT
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+variable-fonts-devel
Summary:        High-level, safe, zero-allocation font parser for TrueType, OpenType, and AAT
BuildArch:      noarch
%description -n %{name}+variable-fonts-devel

This package contains library source intended for building other packages which
use the "variable-fonts" feature of the "%{crate}" crate.

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

%cargo_test -- --lib
%cargo_test -- --doc
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-ttf-parser-devel -f %{oreon_filedir}/rust-ttf-parser-devel.list

%changelog

%autochangelog
