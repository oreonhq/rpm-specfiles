%global source0_hash 5f3d238daef7136c29bf98cca18e7e745397ab295735ea0c045564f26bff11f9
%bcond check 0
%global debug_package %{nil}
%global crate nmstate
Name:           rust-nmstate
Version:        2.2.61
Release:        1%{?dist}
Summary:        Library for networking management in a declarative manner
License:        Apache-2.0
URL:            https://crates.io/crates/nmstate
Source0:        https://static.crates.io/crates/nmstate/nmstate-%{version}.crate
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
Summary:        Library for networking management in a declarative manner
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+gen_conf-devel
Summary:        Library for networking management in a declarative manner
BuildArch:      noarch
%description -n %{name}+gen_conf-devel

This package contains library source intended for building other packages which
use the "gen_conf" feature of the "%{crate}" crate.

%package     -n %{name}+gen_revert-devel
Summary:        Library for networking management in a declarative manner
BuildArch:      noarch
%description -n %{name}+gen_revert-devel

This package contains library source intended for building other packages which
use the "gen_revert" feature of the "%{crate}" crate.

%package     -n %{name}+nispor-devel
Summary:        Library for networking management in a declarative manner
BuildArch:      noarch
%description -n %{name}+nispor-devel

This package contains library source intended for building other packages which
use the "nispor" feature of the "%{crate}" crate.

%package     -n %{name}+nix-devel
Summary:        Library for networking management in a declarative manner
BuildArch:      noarch
%description -n %{name}+nix-devel

This package contains library source intended for building other packages which
use the "nix" feature of the "%{crate}" crate.

%package     -n %{name}+query_apply-devel
Summary:        Library for networking management in a declarative manner
BuildArch:      noarch
%description -n %{name}+query_apply-devel

This package contains library source intended for building other packages which
use the "query_apply" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        Library for networking management in a declarative manner
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%package     -n %{name}+zbus-devel
Summary:        Library for networking management in a declarative manner
BuildArch:      noarch
%description -n %{name}+zbus-devel

This package contains library source intended for building other packages which
use the "zbus" feature of the "%{crate}" crate.

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
%files -n rust-nmstate-devel -f %{oreon_filedir}/rust-nmstate-devel.list

%changelog

%autochangelog
