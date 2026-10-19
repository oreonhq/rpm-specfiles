%global source2_hash fab3dd6bdab226f1c08630b1dd917e11fcb4ec5e1e020e2c16f83a0a13863e85
%global source0_hash cc0e59e8bcc238f0f9b9f29f4d649e5c192dbf277999d0c23d1a312af3fb7a3e
%bcond check 1
%global debug_package %{nil}
%global crate cssparser-color
Name:           rust-cssparser-color
Version:        0.6.0
Release:        1%{?dist}
Summary:        Color implementation based on cssparser
License:        MPL-2.0
URL:            https://crates.io/crates/cssparser-color
Source0:        https://static.crates.io/crates/cssparser-color/cssparser-color-%{version}.crate
Source2:        https://github.com/servo/rust-cssparser/raw/refs/tags/v0.35.0/LICENSE
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
Summary:        Color implementation based on cssparser
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Color implementation based on cssparser
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -pav %{SOURCE2} .
%oreon_vendor_cargo
%build

%cargo_build
%install
%cargo_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -- --doc
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-cssparser-color-devel -f %{oreon_filedir}/rust-cssparser-color-devel.list

%changelog

%autochangelog
