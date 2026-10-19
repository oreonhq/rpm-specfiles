%global source0_hash b91e5b84611016120197efd7dc93ef76774f4e084cd73c9fb3ea4a86c570c56e
%bcond check 0
%global debug_package %{nil}
%global crate unicode_names2_generator
Name:           rust-unicode_names2_generator
Version:        1.3.0
Release:        1%{?dist}
Summary:        Generates the perfect-hash function used by unicode_names2
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/unicode_names2_generator
Source0:        https://static.crates.io/crates/unicode_names2_generator/unicode_names2_generator-%{version}.crate
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
Summary:        Generates the perfect-hash function used by unicode_names2
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+time-devel
Summary:        Generates the perfect-hash function used by unicode_names2
BuildArch:      noarch
%description -n %{name}+time-devel

This package contains library source intended for building other packages which
use the "time" feature of the "%{crate}" crate.

%package     -n %{name}+timing-devel
Summary:        Generates the perfect-hash function used by unicode_names2
BuildArch:      noarch
%description -n %{name}+timing-devel

This package contains library source intended for building other packages which
use the "timing" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-devel
Summary:        Generates the perfect-hash function used by unicode_names2
BuildArch:      noarch
%description -n %{name}+unstable-devel

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

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
%files -n rust-unicode_names2_generator-devel -f %{oreon_filedir}/rust-unicode_names2_generator-devel.list

%changelog

%autochangelog
