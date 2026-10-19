%global source0_hash d674d135b4a8c1d7e813e2f8d1c9a58308aee4a680323066025e53132218bd91
%bcond check 0
%global debug_package %{nil}
%global crate visibility
Name:           rust-visibility
Version:        0.1.1
Release:        1%{?dist}
Summary:        Attribute to override the visibility of items
License:        Zlib OR MIT OR Apache-2.0
URL:            https://crates.io/crates/visibility
Source0:        https://static.crates.io/crates/visibility/visibility-%{version}.crate
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
Summary:        Attribute to override the visibility of items
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+nightly-devel
Summary:        Attribute to override the visibility of items
BuildArch:      noarch
%description -n %{name}+nightly-devel

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

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
%files -n rust-visibility-devel -f %{oreon_filedir}/rust-visibility-devel.list

%changelog

%autochangelog
