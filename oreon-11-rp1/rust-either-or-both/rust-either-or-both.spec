%global source0_hash 6717164c227120ba9ddf3e2b32305fc0122741d3ee41a54968eae7573ee01933
%bcond check 0
%global debug_package %{nil}
%global crate either-or-both
Name:           rust-either-or-both
Version:        0.3.1
Release:        1%{?dist}
Summary:        Enums EitherOrBoth with the three variants Left, Right, Both and Either with the Left and Right variants
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/either-or-both
Source0:        https://static.crates.io/crates/either-or-both/either-or-both-%{version}.crate
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
Summary:        Enums EitherOrBoth with the three variants Left, Right, Both and Either with the Left and Right variants
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+either-devel
Summary:        Enums EitherOrBoth with the three variants Left, Right, Both and Either with the Left and Right variants
BuildArch:      noarch
%description -n %{name}+either-devel

This package contains library source intended for building other packages which
use the "either" feature of the "%{crate}" crate.

%package     -n %{name}+indexmap-devel
Summary:        Enums EitherOrBoth with the three variants Left, Right, Both and Either with the Left and Right variants
BuildArch:      noarch
%description -n %{name}+indexmap-devel

This package contains library source intended for building other packages which
use the "indexmap" feature of the "%{crate}" crate.

%package     -n %{name}+schema-devel
Summary:        Enums EitherOrBoth with the three variants Left, Right, Both and Either with the Left and Right variants
BuildArch:      noarch
%description -n %{name}+schema-devel

This package contains library source intended for building other packages which
use the "schema" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Enums EitherOrBoth with the three variants Left, Right, Both and Either with the Left and Right variants
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Enums EitherOrBoth with the three variants Left, Right, Both and Either with the Left and Right variants
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-either-or-both-devel -f %{oreon_filedir}/rust-either-or-both-devel.list

%changelog

%autochangelog
