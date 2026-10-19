%global source0_hash ba4ebbd48ce411c1d10fb35185f5a51a7bfa3d8b24b4e330d30c9e3a34129501
%bcond check 0
%global debug_package %{nil}
%global crate lalrpop
Name:           rust-lalrpop
Version:        0.22.2
Release:        1%{?dist}
Summary:        convenient LR(1) parser generator
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/lalrpop
Source0:        https://static.crates.io/crates/lalrpop/lalrpop-%{version}.crate
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
Summary:        convenient LR(1) parser generator
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+lexer-devel
Summary:        convenient LR(1) parser generator
BuildArch:      noarch
%description -n %{name}+lexer-devel

This package contains library source intended for building other packages which
use the "lexer" feature of the "%{crate}" crate.

%package     -n %{name}+pico-args-devel
Summary:        convenient LR(1) parser generator
BuildArch:      noarch
%description -n %{name}+pico-args-devel

This package contains library source intended for building other packages which
use the "pico-args" feature of the "%{crate}" crate.

%package     -n %{name}+unicode-devel
Summary:        convenient LR(1) parser generator
BuildArch:      noarch
%description -n %{name}+unicode-devel

This package contains library source intended for building other packages which
use the "unicode" feature of the "%{crate}" crate.

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
%files -n rust-lalrpop-devel -f %{oreon_filedir}/rust-lalrpop-devel.list

%changelog

%autochangelog
