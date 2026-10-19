%global source0_hash 4ea269c3bd32f0a32c321907a2ae912ba6f4649bb0fc764a15627e99a7095a3f
%bcond check 0
%global debug_package %{nil}
%global crate zerotrie
Name:           rust-zerotrie
Version:        0.2.5
Release:        2%{?dist}
Summary:        A data structure that efficiently maps strings to integers
License:        Unicode-3.0
URL:            https://crates.io/crates/zerotrie
Source0:        https://static.crates.io/crates/zerotrie/zerotrie-%{version}.crate
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
Summary:        A data structure that efficiently maps strings to integers
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        A data structure that efficiently maps strings to integers
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+databake-devel
Summary:        A data structure that efficiently maps strings to integers
BuildArch:      noarch
%description -n %{name}+databake-devel

This package contains library source intended for building other packages which
use the "databake" feature of the "%{crate}" crate.

%package     -n %{name}+dense-devel
Summary:        A data structure that efficiently maps strings to integers
BuildArch:      noarch
%description -n %{name}+dense-devel

This package contains library source intended for building other packages which
use the "dense" feature of the "%{crate}" crate.

%package     -n %{name}+litemap-devel
Summary:        A data structure that efficiently maps strings to integers
BuildArch:      noarch
%description -n %{name}+litemap-devel

This package contains library source intended for building other packages which
use the "litemap" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        A data structure that efficiently maps strings to integers
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+yoke-devel
Summary:        A data structure that efficiently maps strings to integers
BuildArch:      noarch
%description -n %{name}+yoke-devel

This package contains library source intended for building other packages which
use the "yoke" feature of the "%{crate}" crate.

%package     -n %{name}+zerofrom-devel
Summary:        A data structure that efficiently maps strings to integers
BuildArch:      noarch
%description -n %{name}+zerofrom-devel

This package contains library source intended for building other packages which
use the "zerofrom" feature of the "%{crate}" crate.

%package     -n %{name}+zerovec-devel
Summary:        A data structure that efficiently maps strings to integers
BuildArch:      noarch
%description -n %{name}+zerovec-devel

This package contains library source intended for building other packages which
use the "zerovec" feature of the "%{crate}" crate.

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
%files -n rust-zerotrie-devel -f %{oreon_filedir}/rust-zerotrie-devel.list

%changelog

%autochangelog
