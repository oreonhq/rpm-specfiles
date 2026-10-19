%global source2_hash 23f18e03dc49df91622fe2a76176497404e46ced8a715d9d2b67a7446571cca3
%global source1_hash a60eea817514531668d7e00765731449fe14d059d3249e0bc93b36de45f759f2
%global source0_hash aa4da3c766cd7a0db8242e326e9e4e081edd567072893ed320008189715366a4
%bcond check 1
%global debug_package %{nil}
%global crate failure_derive
Name:           rust-failure_derive
Version:        0.1.8
Release:        1%{?dist}
Summary:        Derives for the failure crate
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/failure_derive
Source0:        https://static.crates.io/crates/failure_derive/failure_derive-%{version}.crate
Source1:        https://github.com/rust-lang-deprecated/failure/raw/135e2a3/LICENSE-APACHE
Source2:        https://github.com/rust-lang-deprecated/failure/raw/135e2a3/LICENSE-MIT
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       deprecated()
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Derives for the failure crate
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Derives for the failure crate
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -pav %{SOURCE1} %{SOURCE2} .
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
%files -n rust-failure_derive-devel -f %{oreon_filedir}/rust-failure_derive-devel.list

%changelog

%autochangelog
