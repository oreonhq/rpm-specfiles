%global source0_hash 11c3aea32bc97b500c9ca6a72b768a26e558264303d101d3409cf6d57a9ed0cf
%bcond check 0
%global debug_package %{nil}
%global crate escargot
Name:           rust-escargot
Version:        0.5.15
Release:        1%{?dist}
Summary:        Cargo API written in Paris
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/escargot
Source0:        https://static.crates.io/crates/escargot/escargot-%{version}.crate
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
Summary:        Cargo API written in Paris
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+cargo_unstable-devel
Summary:        Cargo API written in Paris
BuildArch:      noarch
%description -n %{name}+cargo_unstable-devel

This package contains library source intended for building other packages which
use the "cargo_unstable" feature of the "%{crate}" crate.

%package     -n %{name}+print-devel
Summary:        Cargo API written in Paris
BuildArch:      noarch
%description -n %{name}+print-devel

This package contains library source intended for building other packages which
use the "print" feature of the "%{crate}" crate.

%package     -n %{name}+strict_unstable-devel
Summary:        Cargo API written in Paris
BuildArch:      noarch
%description -n %{name}+strict_unstable-devel

This package contains library source intended for building other packages which
use the "strict_unstable" feature of the "%{crate}" crate.

%package     -n %{name}+test_unstable-devel
Summary:        Cargo API written in Paris
BuildArch:      noarch
%description -n %{name}+test_unstable-devel

This package contains library source intended for building other packages which
use the "test_unstable" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%install
%cargo_install
rm -f %{buildroot}%{_bindir}/bin_fixture
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-escargot-devel -f %{oreon_filedir}/rust-escargot-devel.list

%changelog

%autochangelog
