%global source0_hash 13de944a44b5064ee5d3a5ceccc49a41bfec50f2580e66f82e87703acdb88b53
%bcond check 1
%global debug_package %{nil}
%global crate chardetng
Name:           rust-chardetng
Version:        1.0.0
Release:        1%{?dist}
Summary:        Character encoding detector for legacy Web content
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/chardetng
Source0:        https://static.crates.io/crates/chardetng/chardetng-%{version}.crate
Patch:          chardetng-fix-metadata.diff
Patch10:        fix-missing-std-import.diff
Patch11:        arrayvec-0.7.patch
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
Summary:        Character encoding detector for legacy Web content
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+arrayvec-devel
Summary:        Character encoding detector for legacy Web content
BuildArch:      noarch
%description -n %{name}+arrayvec-devel

This package contains library source intended for building other packages which
use the "arrayvec" feature of the "%{crate}" crate.

%package     -n %{name}+multithreading-devel
Summary:        Character encoding detector for legacy Web content
BuildArch:      noarch
%description -n %{name}+multithreading-devel

This package contains library source intended for building other packages which
use the "multithreading" feature of the "%{crate}" crate.

%package     -n %{name}+rayon-devel
Summary:        Character encoding detector for legacy Web content
BuildArch:      noarch
%description -n %{name}+rayon-devel

This package contains library source intended for building other packages which
use the "rayon" feature of the "%{crate}" crate.

%package     -n %{name}+testing-only-no-semver-guarantees-do-not-use-devel
Summary:        Character encoding detector for legacy Web content
BuildArch:      noarch
%description -n %{name}+testing-only-no-semver-guarantees-do-not-use-devel

This package contains library source intended for building other packages which
use the "testing-only-no-semver-guarantees-do-not-use" feature of the "%{crate}" crate.

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
%files -n rust-chardetng-devel -f %{oreon_filedir}/rust-chardetng-devel.list

%changelog

%autochangelog
