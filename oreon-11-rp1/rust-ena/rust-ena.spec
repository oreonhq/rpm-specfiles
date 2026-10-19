%global source0_hash eabffdaee24bd1bf95c5ef7cec31260444317e72ea56c4c91750e8b7ee58d5f1
%bcond check 0
%global debug_package %{nil}
%global crate ena
Name:           rust-ena
Version:        0.14.4
Release:        1%{?dist}
Summary:        Union-find, congruence closure, and other unification code. Based on...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/ena
Source0:        https://static.crates.io/crates/ena/ena-%{version}.crate
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

%package     -n %{name}+bench-devel
Summary:        Union-find, congruence closure, and other unification code. Based on...
BuildArch:      noarch
%description -n %{name}+bench-devel

This package contains library source intended for building other packages which
use the "bench" feature of the "%{crate}" crate.

%package     -n %{name}+dogged-devel
Summary:        Union-find, congruence closure, and other unification code. Based on...
BuildArch:      noarch
%description -n %{name}+dogged-devel

This package contains library source intended for building other packages which
use the "dogged" feature of the "%{crate}" crate.

%package     -n %{name}+persistent-devel
Summary:        Union-find, congruence closure, and other unification code. Based on...
BuildArch:      noarch
%description -n %{name}+persistent-devel

This package contains library source intended for building other packages which
use the "persistent" feature of the "%{crate}" crate.

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
%files -n rust-ena-devel -f %{oreon_filedir}/rust-ena-devel.list

%changelog

%autochangelog
