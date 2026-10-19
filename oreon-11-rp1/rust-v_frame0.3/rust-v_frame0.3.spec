%global source0_hash 666b7727c8875d6ab5db9533418d7c764233ac9c0cff1d469aec8fa127597be2
%bcond check 1
%global debug_package %{nil}
%global crate v_frame
Name:           rust-v_frame0.3
Version:        0.3.9
Release:        1%{?dist}
Summary:        Video Frame data structures, originally part of rav1e
License:        BSD-2-Clause
URL:            https://crates.io/crates/v_frame
Source0:        https://static.crates.io/crates/v_frame/v_frame-%{version}.crate
Patch:          v_frame-fix-metadata-auto.diff
Patch:          v_frame-fix-metadata.diff
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
Summary:        Video Frame data structures, originally part of rav1e
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Video Frame data structures, originally part of rav1e
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serialize-devel
Summary:        Video Frame data structures, originally part of rav1e
BuildArch:      noarch
%description -n %{name}+serialize-devel

This package contains library source intended for building other packages which
use the "serialize" feature of the "%{crate}" crate.

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
%files -n rust-v_frame0.3-devel -f %{oreon_filedir}/rust-v_frame0.3-devel.list

%changelog

%autochangelog
