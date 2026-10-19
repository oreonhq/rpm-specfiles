%global source0_hash 4e901edd733a1472f944a45116df3f846f54d37e67e68640ac8bb69689aca2aa
%bcond check 1
%global debug_package %{nil}
%global crate cssparser
Name:           rust-cssparser0.35
Version:        0.35.0
Release:        1%{?dist}
Summary:        Rust implementation of CSS Syntax Level 3
License:        MPL-2.0
URL:            https://crates.io/crates/cssparser
Source0:        https://static.crates.io/crates/cssparser/cssparser-%{version}.crate
Patch:          0001-Fix-typo-in-code-block-attribute-to-fix-issues-with-.patch
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
Summary:        Rust implementation of CSS Syntax Level 3
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+bench-devel
Summary:        Rust implementation of CSS Syntax Level 3
BuildArch:      noarch
%description -n %{name}+bench-devel

This package contains library source intended for building other packages which
use the "bench" feature of the "%{crate}" crate.

%package     -n %{name}+dummy_match_byte-devel
Summary:        Rust implementation of CSS Syntax Level 3
BuildArch:      noarch
%description -n %{name}+dummy_match_byte-devel

This package contains library source intended for building other packages which
use the "dummy_match_byte" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Rust implementation of CSS Syntax Level 3
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

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

%cargo_test -- --doc
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-cssparser0.35-devel -f %{oreon_filedir}/rust-cssparser0.35-devel.list

%changelog

%autochangelog
