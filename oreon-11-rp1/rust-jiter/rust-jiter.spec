%global source0_hash bc2f2b4e673d798b3dbad0af24bc23b92013e680a6b9ad300b4e5e52fafe0586
%bcond check 1
%global debug_package %{nil}
%global crate jiter
Name:           rust-jiter
Version:        0.17.0
Release:        1%{?dist}
Summary:        Fast Iterable JSON parser
License:        MIT
URL:            https://crates.io/crates/jiter
Source0:        https://static.crates.io/crates/jiter/jiter-%{version}.crate
Patch:          jiter-fix-metadata.diff
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
Summary:        Fast Iterable JSON parser
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+num-bigint-devel
Summary:        Fast Iterable JSON parser
BuildArch:      noarch
%description -n %{name}+num-bigint-devel

This package contains library source intended for building other packages which
use the "num-bigint" feature of the "%{crate}" crate.

%package     -n %{name}+python-devel
Summary:        Fast Iterable JSON parser
BuildArch:      noarch
%description -n %{name}+python-devel

This package contains library source intended for building other packages which
use the "python" feature of the "%{crate}" crate.

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
%files -n rust-jiter-devel -f %{oreon_filedir}/rust-jiter-devel.list

%changelog

%autochangelog
