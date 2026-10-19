%global source0_hash 213b7324336b53d2414b2db8537e56544d981803139155afa84f76eeebb7a546
%bcond check 1
%global debug_package %{nil}
%global crate xdg
Name:           rust-xdg2
Version:        2.5.2
Release:        1%{?dist}
Summary:        Store and retrieve files according to XDG Base Directory specification
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/xdg
Source0:        https://static.crates.io/crates/xdg/xdg-%{version}.crate
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
Summary:        Store and retrieve files according to XDG Base Directory specification
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Store and retrieve files according to XDG Base Directory specification
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

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
%files -n rust-xdg2-devel -f %{oreon_filedir}/rust-xdg2-devel.list

%changelog

%autochangelog
