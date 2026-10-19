%global source0_hash 59230a63c37f3e18569bdb90e4a89cbf5bf8b06fea0b84e65ea10cc4df47addd
%bcond check 0
%global debug_package %{nil}
%global crate predicates
Name:           rust-predicates2
Version:        2.1.5
Release:        1%{?dist}
Summary:        Implementation of boolean-valued predicate functions
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/predicates
Source0:        https://static.crates.io/crates/predicates/predicates-%{version}.crate
Patch:          predicates-fix-metadata.diff
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
Summary:        Implementation of boolean-valued predicate functions
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+diff-devel
Summary:        Implementation of boolean-valued predicate functions
BuildArch:      noarch
%description -n %{name}+diff-devel

This package contains library source intended for building other packages which
use the "diff" feature of the "%{crate}" crate.

%package     -n %{name}+float-cmp-devel
Summary:        Implementation of boolean-valued predicate functions
BuildArch:      noarch
%description -n %{name}+float-cmp-devel

This package contains library source intended for building other packages which
use the "float-cmp" feature of the "%{crate}" crate.

%package     -n %{name}+normalize-line-endings-devel
Summary:        Implementation of boolean-valued predicate functions
BuildArch:      noarch
%description -n %{name}+normalize-line-endings-devel

This package contains library source intended for building other packages which
use the "normalize-line-endings" feature of the "%{crate}" crate.

%package     -n %{name}+regex-devel
Summary:        Implementation of boolean-valued predicate functions
BuildArch:      noarch
%description -n %{name}+regex-devel

This package contains library source intended for building other packages which
use the "regex" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-devel
Summary:        Implementation of boolean-valued predicate functions
BuildArch:      noarch
%description -n %{name}+unstable-devel

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

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

%cargo_test -- -- --skip path::fc::PredicateFileContentExt::from_file_path
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-predicates2-devel -f %{oreon_filedir}/rust-predicates2-devel.list

%changelog

%autochangelog
