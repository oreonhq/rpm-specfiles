%global source0_hash d4b8a88685455ed29a21542a33abd9cb6510b6b129abadabdcef0f4c55bc8f61
%bcond check 1
%global debug_package %{nil}
%global crate document-features
Name:           rust-document-features
Version:        0.2.12
Release:        1%{?dist}
Summary:        Extract documentation for the feature flags from comments in Cargo.toml
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/document-features
Source0:        https://static.crates.io/crates/document-features/document-features-%{version}.crate
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
Summary:        Extract documentation for the feature flags from comments in Cargo.toml
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+self-test-devel
Summary:        Extract documentation for the feature flags from comments in Cargo.toml
BuildArch:      noarch
%description -n %{name}+self-test-devel

This package contains library source intended for building other packages which
use the "self-test" feature of the "%{crate}" crate.

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
%files -n rust-document-features-devel -f %{oreon_filedir}/rust-document-features-devel.list

%changelog

%autochangelog
