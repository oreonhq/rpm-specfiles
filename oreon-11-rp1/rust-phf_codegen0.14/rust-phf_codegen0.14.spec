%global source0_hash 41b585a510fb76fdebead6897982ef2a03a21d8e6cbcca904999742a4afc6ffe
%bcond check 1
%global debug_package %{nil}
%global crate phf_codegen
Name:           rust-phf_codegen0.14
Version:        0.14.0
Release:        1%{?dist}
Summary:        Codegen library for PHF types
License:        MIT
URL:            https://crates.io/crates/phf_codegen
Source0:        https://static.crates.io/crates/phf_codegen/phf_codegen-%{version}.crate
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
Summary:        Codegen library for PHF types
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+ptrhash-devel
Summary:        Codegen library for PHF types
BuildArch:      noarch
%description -n %{name}+ptrhash-devel

This package contains library source intended for building other packages which
use the "ptrhash" feature of the "%{crate}" crate.

%package     -n %{name}+quote-devel
Summary:        Codegen library for PHF types
BuildArch:      noarch
%description -n %{name}+quote-devel

This package contains library source intended for building other packages which
use the "quote" feature of the "%{crate}" crate.

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
%files -n rust-phf_codegen0.14-devel -f %{oreon_filedir}/rust-phf_codegen0.14-devel.list

%changelog

%autochangelog
