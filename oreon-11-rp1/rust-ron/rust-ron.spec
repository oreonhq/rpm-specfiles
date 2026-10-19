%global source0_hash 81116b9531d61eabc41aeb228e4b6b2435bcca3233b98cf3b3077d4e6e9debb3
%bcond check 0
%global debug_package %{nil}
%global crate ron
Name:           rust-ron
Version:        0.12.2
Release:        1%{?dist}
Summary:        Rusty Object Notation
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/ron
Source0:        https://static.crates.io/crates/ron/ron-%{version}.crate
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
Summary:        Rusty Object Notation
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+indexmap-devel
Summary:        Rusty Object Notation
BuildArch:      noarch
%description -n %{name}+indexmap-devel

This package contains library source intended for building other packages which
use the "indexmap" feature of the "%{crate}" crate.

%package     -n %{name}+integer128-devel
Summary:        Rusty Object Notation
BuildArch:      noarch
%description -n %{name}+integer128-devel

This package contains library source intended for building other packages which
use the "integer128" feature of the "%{crate}" crate.

%package     -n %{name}+internal-span-substring-test-devel
Summary:        Rusty Object Notation
BuildArch:      noarch
%description -n %{name}+internal-span-substring-test-devel

This package contains library source intended for building other packages which
use the "internal-span-substring-test" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Rusty Object Notation
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+unicode-segmentation-devel
Summary:        Rusty Object Notation
BuildArch:      noarch
%description -n %{name}+unicode-segmentation-devel

This package contains library source intended for building other packages which
use the "unicode-segmentation" feature of the "%{crate}" crate.

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
%files -n rust-ron-devel -f %{oreon_filedir}/rust-ron-devel.list

%changelog

%autochangelog
