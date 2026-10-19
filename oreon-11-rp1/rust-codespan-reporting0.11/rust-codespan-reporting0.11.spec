%global source1_hash c71d239df91726fc519c6eb72d318ec65820627232b2f796219e87dcf35d0ab4
%global source0_hash 3538270d33cc669650c4b093848450d380def10c331d38c768e34cac80576e6e
%bcond check 0
%global debug_package %{nil}
%global crate codespan-reporting
Name:           rust-codespan-reporting0.11
Version:        0.11.1
Release:        1%{?dist}
Summary:        Beautiful diagnostic reporting for text-based programming languages
License:        Apache-2.0
URL:            https://crates.io/crates/codespan-reporting
Source0:        https://static.crates.io/crates/codespan-reporting/codespan-reporting-%{version}.crate
Source1:        https://github.com/brendanzab/codespan/raw/fd389a1/LICENSE
Patch:          codespan-reporting-fix-metadata.diff
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
Summary:        Beautiful diagnostic reporting for text-based programming languages
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+ascii-only-devel
Summary:        Beautiful diagnostic reporting for text-based programming languages
BuildArch:      noarch
%description -n %{name}+ascii-only-devel

This package contains library source intended for building other packages which
use the "ascii-only" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Beautiful diagnostic reporting for text-based programming languages
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serialization-devel
Summary:        Beautiful diagnostic reporting for text-based programming languages
BuildArch:      noarch
%description -n %{name}+serialization-devel

This package contains library source intended for building other packages which
use the "serialization" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -pav %{SOURCE1} .
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
%files -n rust-codespan-reporting0.11-devel -f %{oreon_filedir}/rust-codespan-reporting0.11-devel.list

%changelog

%autochangelog
