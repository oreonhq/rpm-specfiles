%global source0_hash 5aec2877d084955915f48086ae07f49f4c89e33e3826d1f7af33b342274f8100
%bcond check 1
%global debug_package %{nil}
%global crate ear
Name:           rust-ear0.5
Version:        0.5.0
Release:        1%{?dist}
Summary:        EAT Attestation Results implementation
License:        Apache-2.0
URL:            https://crates.io/crates/ear
Source0:        https://static.crates.io/crates/ear/ear-%{version}.crate
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
Summary:        EAT Attestation Results implementation
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
%files -n rust-ear0.5-devel -f %{oreon_filedir}/rust-ear0.5-devel.list

%changelog

%autochangelog
