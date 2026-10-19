%global source2_hash b05785f9f18e6716bab63424b11454513b9943a222595b70411009202fc592b5
%global source1_hash cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30
%global source0_hash b993cd767a2bc7307dd87622311ca22c44329cc7a21366206bfa0896827b2bad
%ifarch %{ix86} %{arm}
%bcond check 0
%else
%bcond check 1
%endif
%global debug_package %{nil}
%global crate associative-cache
Name:           rust-associative-cache
Version:        2.0.0
Release:        1%{?dist}
Summary:        Generic N-way associative cache
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/associative-cache
Source0:        https://static.crates.io/crates/associative-cache/associative-cache-%{version}.crate
Source1:        https://www.apache.org/licenses/LICENSE-2.0.txt#/LICENSE-APACHE
Source2:        https://github.com/spdx/license-list-data/raw/main/text/MIT.txt#/LICENSE-MIT
Patch:          associative-cache-fix-metadata.diff
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
Summary:        Generic N-way associative cache
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+rand-devel
Summary:        Generic N-way associative cache
BuildArch:      noarch
%description -n %{name}+rand-devel

This package contains library source intended for building other packages which
use the "rand" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -p %{S:1} %{S:2} .
%oreon_vendor_cargo
%build

%cargo_build
%install
%cargo_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -- --lib
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-associative-cache-devel -f %{oreon_filedir}/rust-associative-cache-devel.list

%changelog

%autochangelog
