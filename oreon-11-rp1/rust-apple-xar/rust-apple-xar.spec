%global source0_hash 9631e781df71ebd049d7b4988cdae88712324cb20eb127fd79026bc8f1335d93
%bcond check 1
%global debug_package %{nil}
%global crate apple-xar
Name:           rust-apple-xar
Version:        0.20.0
Release:        1%{?dist}
Summary:        XAR archive reading and writing
License:        MPL-2.0
URL:            https://crates.io/crates/apple-xar
Source0:        https://static.crates.io/crates/apple-xar/apple-xar-%{version}.crate
Patch:          apple-xar-fix-metadata.diff
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
Summary:        XAR archive reading and writing
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+signing-devel
Summary:        XAR archive reading and writing
BuildArch:      noarch
%description -n %{name}+signing-devel

This package contains library source intended for building other packages which
use the "signing" feature of the "%{crate}" crate.

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
%files -n rust-apple-xar-devel -f %{oreon_filedir}/rust-apple-xar-devel.list

%changelog

%autochangelog
