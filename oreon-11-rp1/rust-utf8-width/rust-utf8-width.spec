%global source0_hash 159a7cadce548703edd50d24069bc294c5415ecab0a480e0cd1ca06d112dc94a
%bcond check 0
%global debug_package %{nil}
%global crate utf8-width
Name:           rust-utf8-width
Version:        0.1.9
Release:        1%{?dist}
Summary:        To determine the width of a UTF-8 character by providing its first byte.
License:        MIT
URL:            https://crates.io/crates/utf8-width
Source0:        https://static.crates.io/crates/utf8-width/utf8-width-%{version}.crate
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
Summary:        To determine the width of a UTF-8 character by providing its first byte.
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
%files -n rust-utf8-width-devel -f %{oreon_filedir}/rust-utf8-width-devel.list

%changelog

%autochangelog
