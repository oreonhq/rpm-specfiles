%global source0_hash 7e689342a48d2ea927c87ea50cabf8594854bf940e9310208848d680d668ed85
%bcond check 0
%global debug_package %{nil}
%global crate time-macros
Name:           rust-time-macros
Version:        0.2.32
Release:        1%{?dist}
Summary:        Procedural macros for the time crate.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/time-macros
Source0:        https://static.crates.io/crates/time-macros/time-macros-%{version}.crate
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
Summary:        Procedural macros for the time crate.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+formatting-devel
Summary:        Procedural macros for the time crate.
BuildArch:      noarch
%description -n %{name}+formatting-devel

This package contains library source intended for building other packages which
use the "formatting" feature of the "%{crate}" crate.

%package     -n %{name}+large-dates-devel
Summary:        Procedural macros for the time crate.
BuildArch:      noarch
%description -n %{name}+large-dates-devel

This package contains library source intended for building other packages which
use the "large-dates" feature of the "%{crate}" crate.

%package     -n %{name}+parsing-devel
Summary:        Procedural macros for the time crate.
BuildArch:      noarch
%description -n %{name}+parsing-devel

This package contains library source intended for building other packages which
use the "parsing" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Procedural macros for the time crate.
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

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
%files -n rust-time-macros-devel -f %{oreon_filedir}/rust-time-macros-devel.list

%changelog

%autochangelog
