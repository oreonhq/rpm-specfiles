%global source0_hash 46676ccec8213bcc35a7e8562a8459138b8ae82c380bbc9ae7ffcfa247352972
%bcond check 1
%global debug_package %{nil}
%global crate askalono
Name:           rust-askalono
Version:        0.5.0
Release:        1%{?dist}
Summary:        Library to detect the contents of license files
License:        Apache-2.0
URL:            https://crates.io/crates/askalono
Source0:        https://static.crates.io/crates/askalono/askalono-%{version}.crate
Patch:          askalono-fix-metadata-auto.diff
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
Summary:        Library to detect the contents of license files
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+gzip-devel
Summary:        Library to detect the contents of license files
BuildArch:      noarch
%description -n %{name}+gzip-devel

This package contains library source intended for building other packages which
use the "gzip" feature of the "%{crate}" crate.

%package     -n %{name}+serde_json-devel
Summary:        Library to detect the contents of license files
BuildArch:      noarch
%description -n %{name}+serde_json-devel

This package contains library source intended for building other packages which
use the "serde_json" feature of the "%{crate}" crate.

%package     -n %{name}+spdx-devel
Summary:        Library to detect the contents of license files
BuildArch:      noarch
%description -n %{name}+spdx-devel

This package contains library source intended for building other packages which
use the "spdx" feature of the "%{crate}" crate.

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
%files -n rust-askalono-devel -f %{oreon_filedir}/rust-askalono-devel.list

%changelog

%autochangelog
