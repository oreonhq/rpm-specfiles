%global source0_hash d2911bc1f0e3033b2d1921ff7be36ecadd47a482d4a87a6352392b2f6dd69991
%bcond check 0
%global debug_package %{nil}
%global crate lv2-worker
Name:           rust-lv2-worker
Version:        0.1.1
Release:        1%{?dist}
Summary:        Rust-lv2's work offloading library
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/lv2-worker
Source0:        https://static.crates.io/crates/lv2-worker/lv2-worker-%{version}.crate
Patch2:        lv2-worker-fix-tests-rust-1.81.0.patch
ExcludeArch:    ppc64le s390x
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
Summary:        Rust-lv2's work offloading library
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

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-lv2-worker-devel -f %{oreon_filedir}/rust-lv2-worker-devel.list

%changelog

%autochangelog
