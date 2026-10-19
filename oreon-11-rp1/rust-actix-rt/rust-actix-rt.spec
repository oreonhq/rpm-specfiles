%global source0_hash 92589714878ca59a7626ea19734f0e07a6a875197eec751bb5d3f99e64998c63
%bcond check 0
%global debug_package %{nil}
%global crate actix-rt
Name:           rust-actix-rt
Version:        2.11.0
Release:        1%{?dist}
Summary:        Tokio-based single-threaded async runtime for the Actix ecosystem
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/actix-rt
Source0:        https://static.crates.io/crates/actix-rt/actix-rt-%{version}.crate
Patch:          actix-rt-fix-metadata.diff
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
Summary:        Tokio-based single-threaded async runtime for the Actix ecosystem
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+actix-macros-devel
Summary:        Tokio-based single-threaded async runtime for the Actix ecosystem
BuildArch:      noarch
%description -n %{name}+actix-macros-devel

This package contains library source intended for building other packages which
use the "actix-macros" feature of the "%{crate}" crate.

%package     -n %{name}+macros-devel
Summary:        Tokio-based single-threaded async runtime for the Actix ecosystem
BuildArch:      noarch
%description -n %{name}+macros-devel

This package contains library source intended for building other packages which
use the "macros" feature of the "%{crate}" crate.

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
%files -n rust-actix-rt-devel -f %{oreon_filedir}/rust-actix-rt-devel.list

%changelog

%autochangelog
