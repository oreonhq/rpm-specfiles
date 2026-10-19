%global source0_hash c3d036a3c4ab069c7b410a2ce876bd74808d2d0888a82667669f8e783a898bf1
%bcond check 1
%global debug_package %{nil}
%global crate arbitrary
Name:           rust-arbitrary
Version:        1.4.2
Release:        1%{?dist}
Summary:        Trait for generating structured data from unstructured data
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/arbitrary
Source0:        https://static.crates.io/crates/arbitrary/arbitrary-%{version}.crate
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
Summary:        Trait for generating structured data from unstructured data
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+derive-devel
Summary:        Trait for generating structured data from unstructured data
BuildArch:      noarch
%description -n %{name}+derive-devel

This package contains library source intended for building other packages which
use the "derive" feature of the "%{crate}" crate.

%package     -n %{name}+derive_arbitrary-devel
Summary:        Trait for generating structured data from unstructured data
BuildArch:      noarch
%description -n %{name}+derive_arbitrary-devel

This package contains library source intended for building other packages which
use the "derive_arbitrary" feature of the "%{crate}" crate.

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
%files -n rust-arbitrary-devel -f %{oreon_filedir}/rust-arbitrary-devel.list

%changelog

%autochangelog
