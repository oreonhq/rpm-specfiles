%global source0_hash 10872b55cfb02a821b69dc7cf8dc6a71d6af25eb9a79662bec4a9d016056b3be
%bcond check 0
%global debug_package %{nil}
%global crate h3
Name:           rust-h3
Version:        0.0.8
Release:        1%{?dist}
Summary:        An async HTTP/3 implementation.
License:        MIT
URL:            https://crates.io/crates/h3
Source0:        https://static.crates.io/crates/h3/h3-%{version}.crate
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

%package     -n %{name}+i-implement-a-third-party-backend-and-opt-into-breaking-changes-devel
Summary:        An async HTTP/3 implementation.
BuildArch:      noarch
%description -n %{name}+i-implement-a-third-party-backend-and-opt-into-breaking-changes-devel

This package contains library source intended for building other packages which
use the "i-implement-a-third-party-backend-and-opt-into-breaking-changes" feature of the "%{crate}" crate.

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
%files -n rust-h3-devel -f %{oreon_filedir}/rust-h3-devel.list

%changelog

%autochangelog
