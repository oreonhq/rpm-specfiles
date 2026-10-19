%global source0_hash cf6287f9e06f44558a3264976e70c51187482a0271d48abfd88f0d3af18d3ee6
%bcond check 1
%global debug_package %{nil}
%global crate cursive_buffered_backend
Name:           rust-cursive_buffered_backend
Version:        0.6.2
Release:        1%{?dist}
Summary:        Buffering backend for any Cursive backend
License:        MIT
URL:            https://crates.io/crates/cursive_buffered_backend
Source0:        https://static.crates.io/crates/cursive_buffered_backend/cursive_buffered_backend-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  dos2unix
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
Summary:        Buffering backend for any Cursive backend
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
for f in CHANGELOG.md LICENSE README.md ReleaseInstructions.md;
do dos2unix --keepdate $f; done
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
%files -n rust-cursive_buffered_backend-devel -f %{oreon_filedir}/rust-cursive_buffered_backend-devel.list

%changelog

%autochangelog
