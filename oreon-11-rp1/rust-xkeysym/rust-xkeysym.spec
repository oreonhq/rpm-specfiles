%global source0_hash b9cc00251562a284751c9973bace760d86c0276c471b4be569fe6b068ee97a56
%bcond check 0
%global debug_package %{nil}
%global crate xkeysym
Name:           rust-xkeysym
Version:        0.2.1
Release:        1%{?dist}
Summary:        Library for working with X11 keysyms
License:        MIT OR Apache-2.0 OR Zlib
URL:            https://crates.io/crates/xkeysym
Source0:        https://static.crates.io/crates/xkeysym/xkeysym-%{version}.crate
Patch:          xkeysym-fix-metadata.diff
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
Summary:        Library for working with X11 keysyms
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+bytemuck-devel
Summary:        Library for working with X11 keysyms
BuildArch:      noarch
%description -n %{name}+bytemuck-devel

This package contains library source intended for building other packages which
use the "bytemuck" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Library for working with X11 keysyms
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
%files -n rust-xkeysym-devel -f %{oreon_filedir}/rust-xkeysym-devel.list

%changelog

%autochangelog
