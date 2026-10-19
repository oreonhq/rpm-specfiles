%global source0_hash b3a8fb4672e840a587a66fc577a5491375df51ddb88f2a2c2a792598c326fe14
%bcond check 0
%global debug_package %{nil}
%global crate rstest_reuse
Name:           rust-rstest_reuse
Version:        0.7.0
Release:        1%{?dist}
Summary:        Reusable test attributes for rstest
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/rstest_reuse
Source0:        https://static.crates.io/crates/rstest_reuse/rstest_reuse-%{version}.crate
Patch:          rstest_reuse-fix-metadata.diff
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
Summary:        Reusable test attributes for rstest
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

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
%files -n rust-rstest_reuse-devel -f %{oreon_filedir}/rust-rstest_reuse-devel.list

%changelog

%autochangelog
