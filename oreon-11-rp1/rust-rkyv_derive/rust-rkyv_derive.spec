%global source0_hash 84d7b42d4b8d06048d3ac8db0eb31bcb942cbeb709f0b5f2b2ebde398d3038f5
%bcond check 0
%global debug_package %{nil}
%global crate rkyv_derive
Name:           rust-rkyv_derive
Version:        0.7.46
Release:        1%{?dist}
Summary:        Derive macro for rkyv
License:        MIT
URL:            https://crates.io/crates/rkyv_derive
Source0:        https://static.crates.io/crates/rkyv_derive/rkyv_derive-%{version}.crate
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
Summary:        Derive macro for rkyv
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+arbitrary_enum_discriminant-devel
Summary:        Derive macro for rkyv
BuildArch:      noarch
%description -n %{name}+arbitrary_enum_discriminant-devel

This package contains library source intended for building other packages which
use the "arbitrary_enum_discriminant" feature of the "%{crate}" crate.

%package     -n %{name}+archive_be-devel
Summary:        Derive macro for rkyv
BuildArch:      noarch
%description -n %{name}+archive_be-devel

This package contains library source intended for building other packages which
use the "archive_be" feature of the "%{crate}" crate.

%package     -n %{name}+archive_le-devel
Summary:        Derive macro for rkyv
BuildArch:      noarch
%description -n %{name}+archive_le-devel

This package contains library source intended for building other packages which
use the "archive_le" feature of the "%{crate}" crate.

%package     -n %{name}+copy-devel
Summary:        Derive macro for rkyv
BuildArch:      noarch
%description -n %{name}+copy-devel

This package contains library source intended for building other packages which
use the "copy" feature of the "%{crate}" crate.

%package     -n %{name}+strict-devel
Summary:        Derive macro for rkyv
BuildArch:      noarch
%description -n %{name}+strict-devel

This package contains library source intended for building other packages which
use the "strict" feature of the "%{crate}" crate.

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
%files -n rust-rkyv_derive-devel -f %{oreon_filedir}/rust-rkyv_derive-devel.list

%changelog

%autochangelog
