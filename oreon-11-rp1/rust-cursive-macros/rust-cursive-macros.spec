%global source2_hash 34732cfadbccc51ae3660f332b609c491005993d21735c9b949a0b6821b34c1d
%global source0_hash ac7ac0eb0cede3dfdfebf4d5f22354e05a730b79c25fd03481fc69fcfba0a73e
%bcond check 1
%global debug_package %{nil}
%global crate cursive-macros
Name:           rust-cursive-macros
Version:        0.1.0
Release:        1%{?dist}
Summary:        Proc-macros for the cursive TUI library
License:        MIT
URL:            https://crates.io/crates/cursive-macros
Source0:        https://static.crates.io/crates/cursive-macros/cursive-macros-%{version}.crate
Source2:        https://github.com/gyscos/cursive/raw/main/LICENSE
Patch:          cursive-macros-fix-metadata.diff
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
Summary:        Proc-macros for the cursive TUI library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+builder-devel
Summary:        Proc-macros for the cursive TUI library
BuildArch:      noarch
%description -n %{name}+builder-devel

This package contains library source intended for building other packages which
use the "builder" feature of the "%{crate}" crate.

%package     -n %{name}+find-crate-devel
Summary:        Proc-macros for the cursive TUI library
BuildArch:      noarch
%description -n %{name}+find-crate-devel

This package contains library source intended for building other packages which
use the "find-crate" feature of the "%{crate}" crate.

%package     -n %{name}+quote-devel
Summary:        Proc-macros for the cursive TUI library
BuildArch:      noarch
%description -n %{name}+quote-devel

This package contains library source intended for building other packages which
use the "quote" feature of the "%{crate}" crate.

%package     -n %{name}+syn-devel
Summary:        Proc-macros for the cursive TUI library
BuildArch:      noarch
%description -n %{name}+syn-devel

This package contains library source intended for building other packages which
use the "syn" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -pav %{SOURCE2} .
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
%files -n rust-cursive-macros-devel -f %{oreon_filedir}/rust-cursive-macros-devel.list

%changelog

%autochangelog
