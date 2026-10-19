%global source0_hash b97fcaeba89edba30f044a10c6a3cc39df9c3f17d7cd829dd1446cab35f890e0
%bcond check 1
%global debug_package %{nil}
%global crate smallvec
Name:           rust-smallvec0.6
Version:        0.6.14
Release:        1%{?dist}
Summary:        'Small vector' optimization: store up to a small number of items on the stack
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/smallvec
Source0:        https://static.crates.io/crates/smallvec/smallvec-%{version}.crate
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
Summary:        'Small vector' optimization: store up to a small number of items on the stack
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+may_dangle-devel
Summary:        'Small vector' optimization: store up to a small number of items on the stack
BuildArch:      noarch
%description -n %{name}+may_dangle-devel

This package contains library source intended for building other packages which
use the "may_dangle" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        'Small vector' optimization: store up to a small number of items on the stack
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+specialization-devel
Summary:        'Small vector' optimization: store up to a small number of items on the stack
BuildArch:      noarch
%description -n %{name}+specialization-devel

This package contains library source intended for building other packages which
use the "specialization" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        'Small vector' optimization: store up to a small number of items on the stack
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+union-devel
Summary:        'Small vector' optimization: store up to a small number of items on the stack
BuildArch:      noarch
%description -n %{name}+union-devel

This package contains library source intended for building other packages which
use the "union" feature of the "%{crate}" crate.

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
%files -n rust-smallvec0.6-devel -f %{oreon_filedir}/rust-smallvec0.6-devel.list

%changelog

%autochangelog
