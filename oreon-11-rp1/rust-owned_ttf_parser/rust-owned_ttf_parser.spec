%global source0_hash 36820e9051aca1014ddc75770aab4d68bc1e9e632f0f5627c4086bc216fb583b
%bcond check 0
%global debug_package %{nil}
%global crate owned_ttf_parser
Name:           rust-owned_ttf_parser
Version:        0.25.1
Release:        1%{?dist}
Summary:        Ttf-parser plus support for owned data
License:        Apache-2.0
URL:            https://crates.io/crates/owned_ttf_parser
Source0:        https://static.crates.io/crates/owned_ttf_parser/owned_ttf_parser-%{version}.crate
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
Summary:        Ttf-parser plus support for owned data
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+apple-layout-devel
Summary:        Ttf-parser plus support for owned data
BuildArch:      noarch
%description -n %{name}+apple-layout-devel

This package contains library source intended for building other packages which
use the "apple-layout" feature of the "%{crate}" crate.

%package     -n %{name}+glyph-names-devel
Summary:        Ttf-parser plus support for owned data
BuildArch:      noarch
%description -n %{name}+glyph-names-devel

This package contains library source intended for building other packages which
use the "glyph-names" feature of the "%{crate}" crate.

%package     -n %{name}+gvar-alloc-devel
Summary:        Ttf-parser plus support for owned data
BuildArch:      noarch
%description -n %{name}+gvar-alloc-devel

This package contains library source intended for building other packages which
use the "gvar-alloc" feature of the "%{crate}" crate.

%package     -n %{name}+opentype-layout-devel
Summary:        Ttf-parser plus support for owned data
BuildArch:      noarch
%description -n %{name}+opentype-layout-devel

This package contains library source intended for building other packages which
use the "opentype-layout" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Ttf-parser plus support for owned data
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+variable-fonts-devel
Summary:        Ttf-parser plus support for owned data
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

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-owned_ttf_parser-devel -f %{oreon_filedir}/rust-owned_ttf_parser-devel.list

%changelog

%autochangelog
