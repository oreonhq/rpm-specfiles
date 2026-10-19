%global source0_hash 5c1cb5db39152898a79168971543b1cb5020dff7fe43c8dc468b0885f5e29df5
%bcond check 1
%global debug_package %{nil}
%global crate unicode-bidi
Name:           rust-unicode-bidi
Version:        0.3.18
Release:        1%{?dist}
Summary:        Implementation of the Unicode Bidirectional Algorithm
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/unicode-bidi
Source0:        https://static.crates.io/crates/unicode-bidi/unicode-bidi-%{version}.crate
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
Summary:        Implementation of the Unicode Bidirectional Algorithm
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+bench_it-devel
Summary:        Implementation of the Unicode Bidirectional Algorithm
BuildArch:      noarch
%description -n %{name}+bench_it-devel

This package contains library source intended for building other packages which
use the "bench_it" feature of the "%{crate}" crate.

%package     -n %{name}+flame_it-devel
Summary:        Implementation of the Unicode Bidirectional Algorithm
BuildArch:      noarch
%description -n %{name}+flame_it-devel

This package contains library source intended for building other packages which
use the "flame_it" feature of the "%{crate}" crate.

%package     -n %{name}+hardcoded-data-devel
Summary:        Implementation of the Unicode Bidirectional Algorithm
BuildArch:      noarch
%description -n %{name}+hardcoded-data-devel

This package contains library source intended for building other packages which
use the "hardcoded-data" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Implementation of the Unicode Bidirectional Algorithm
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-devel
Summary:        Implementation of the Unicode Bidirectional Algorithm
BuildArch:      noarch
%description -n %{name}+unstable-devel

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

%package     -n %{name}+with_serde-devel
Summary:        Implementation of the Unicode Bidirectional Algorithm
BuildArch:      noarch
%description -n %{name}+with_serde-devel

This package contains library source intended for building other packages which
use the "with_serde" feature of the "%{crate}" crate.

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
%files -n rust-unicode-bidi-devel -f %{oreon_filedir}/rust-unicode-bidi-devel.list

%changelog

%autochangelog
