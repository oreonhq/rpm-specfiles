%global source0_hash 54f0d287c53ffd184d04d8677f590f4ac5379785529e5e08b1c8083acdd5c198
%bcond check 1
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate fluent-syntax
Name:           rust-fluent-syntax
Version:        0.12.0
Release:        1%{?dist}
Summary:        Low-level parser, AST, and serializer API for the syntax used by Project Fluent
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/fluent-syntax
Source0:        https://static.crates.io/crates/fluent-syntax/fluent-syntax-%{version}.crate
Patch:          fluent-syntax-fix-metadata.diff
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
Summary:        Low-level parser, AST, and serializer API for the syntax used by Project Fluent
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+json-devel
Summary:        Low-level parser, AST, and serializer API for the syntax used by Project Fluent
BuildArch:      noarch
%description -n %{name}+json-devel

This package contains library source intended for building other packages which
use the "json" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Low-level parser, AST, and serializer API for the syntax used by Project Fluent
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build -f json
%install
%cargo_install -f json
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -f json
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-fluent-syntax-devel -f %{oreon_filedir}/rust-fluent-syntax-devel.list

%changelog

%autochangelog
