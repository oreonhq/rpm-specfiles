%global source0_hash 2a2a2320eb7ec0ebe8da8f744d7812d9fc4cb4d09344ac01898dbcb6a20ae69b
%bcond check 0
%global debug_package %{nil}
%global crate hmac
Name:           rust-hmac0.11
Version:        0.11.0
Release:        1%{?dist}
Summary:        Generic implementation of Hash-based Message Authentication Code (HMAC)
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/hmac
Source0:        https://static.crates.io/crates/hmac/hmac-%{version}.crate
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
Summary:        Generic implementation of Hash-based Message Authentication Code (HMAC)
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Generic implementation of Hash-based Message Authentication Code (HMAC)
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-hmac0.11-devel -f %{oreon_filedir}/rust-hmac0.11-devel.list

%changelog

%autochangelog
