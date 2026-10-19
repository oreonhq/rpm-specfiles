%global source0_hash 475b9310e272827d34113bf8679b6dfb7fa0023ee049764ba003f8f984e8b5d1
%bcond check 0
%global debug_package %{nil}
%global crate serde_qs
Name:           rust-serde_qs
Version:        1.1.3
Release:        1%{?dist}
Summary:        Querystrings for Serde
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/serde_qs
Source0:        https://static.crates.io/crates/serde_qs/serde_qs-%{version}.crate
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
Summary:        Querystrings for Serde
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+actix-devel
Summary:        Querystrings for Serde
BuildArch:      noarch
%description -n %{name}+actix-devel

This package contains library source intended for building other packages which
use the "actix" feature of the "%{crate}" crate.

%package     -n %{name}+actix2-devel
Summary:        Querystrings for Serde
BuildArch:      noarch
%description -n %{name}+actix2-devel

This package contains library source intended for building other packages which
use the "actix2" feature of the "%{crate}" crate.

%package     -n %{name}+futures-devel
Summary:        Querystrings for Serde
BuildArch:      noarch
%description -n %{name}+futures-devel

This package contains library source intended for building other packages which
use the "futures" feature of the "%{crate}" crate.

%package     -n %{name}+tracing-devel
Summary:        Querystrings for Serde
BuildArch:      noarch
%description -n %{name}+tracing-devel

This package contains library source intended for building other packages which
use the "tracing" feature of the "%{crate}" crate.

%package     -n %{name}+warp-devel
Summary:        Querystrings for Serde
BuildArch:      noarch
%description -n %{name}+warp-devel

This package contains library source intended for building other packages which
use the "warp" feature of the "%{crate}" crate.

%package     -n %{name}+warp-framework-devel
Summary:        Querystrings for Serde
BuildArch:      noarch
%description -n %{name}+warp-framework-devel

This package contains library source intended for building other packages which
use the "warp-framework" feature of the "%{crate}" crate.

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
%files -n rust-serde_qs-devel -f %{oreon_filedir}/rust-serde_qs-devel.list

%changelog

%autochangelog
