%global source0_hash 2a1a1c0bc9823338a3bdf8c61f994f23ac004c6fa32c08cd152984499b445e8d
%bcond check 0
%global debug_package %{nil}
%global crate yaml-rust2
Name:           rust-yaml-rust2
Version:        0.9.0
Release:        1%{?dist}
Summary:        A fully YAML 1.2 compliant YAML parser
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/yaml-rust2
Source0:        https://static.crates.io/crates/yaml-rust2/yaml-rust2-%{version}.crate
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
Summary:        A fully YAML 1.2 compliant YAML parser
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+debug_prints-devel
Summary:        A fully YAML 1.2 compliant YAML parser
BuildArch:      noarch
%description -n %{name}+debug_prints-devel

This package contains library source intended for building other packages which
use the "debug_prints" feature of the "%{crate}" crate.

%package     -n %{name}+encoding-devel
Summary:        A fully YAML 1.2 compliant YAML parser
BuildArch:      noarch
%description -n %{name}+encoding-devel

This package contains library source intended for building other packages which
use the "encoding" feature of the "%{crate}" crate.

%package     -n %{name}+encoding_rs-devel
Summary:        A fully YAML 1.2 compliant YAML parser
BuildArch:      noarch
%description -n %{name}+encoding_rs-devel

This package contains library source intended for building other packages which
use the "encoding_rs" feature of the "%{crate}" crate.

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
%files -n rust-yaml-rust2-devel -f %{oreon_filedir}/rust-yaml-rust2-devel.list

%changelog

%autochangelog
