%global source0_hash a00109accc170f0bdb141fed3e393c565b6f5e072365c3bd58f5b062591560a3
%bcond check 0
%global debug_package %{nil}
%global crate jni-macros
Name:           rust-jni-macros
Version:        0.22.4
Release:        1%{?dist}
Summary:        Procedural macros for the jni crate
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/jni-macros
Source0:        https://static.crates.io/crates/jni-macros/jni-macros-%{version}.crate
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
Summary:        Procedural macros for the jni crate
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
%files -n rust-jni-macros-devel -f %{oreon_filedir}/rust-jni-macros-devel.list

%changelog

%autochangelog
