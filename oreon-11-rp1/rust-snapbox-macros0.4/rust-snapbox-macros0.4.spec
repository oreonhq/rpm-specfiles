%global source0_hash 3b750c344002d7cc69afb9da00ebd9b5c0f8ac2eb7d115d9d45d5b5f47718d74
%bcond check 1
%global debug_package %{nil}
%global crate snapbox-macros
Name:           rust-snapbox-macros0.4
Version:        0.4.0
Release:        2%{?dist}
Summary:        Snapshot testing toolbox
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/snapbox-macros
Source0:        https://static.crates.io/crates/snapbox-macros/snapbox-macros-%{version}.crate
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
Summary:        Snapshot testing toolbox
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+color-devel
Summary:        Snapshot testing toolbox
BuildArch:      noarch
%description -n %{name}+color-devel

This package contains library source intended for building other packages which
use the "color" feature of the "%{crate}" crate.

%package     -n %{name}+debug-devel
Summary:        Snapshot testing toolbox
BuildArch:      noarch
%description -n %{name}+debug-devel

This package contains library source intended for building other packages which
use the "debug" feature of the "%{crate}" crate.

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
%files -n rust-snapbox-macros0.4-devel -f %{oreon_filedir}/rust-snapbox-macros0.4-devel.list

%changelog

%autochangelog
