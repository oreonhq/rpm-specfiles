%global source0_hash b285c575532a33ef6fdd3a57640d0b1c70e6ca48644d6df7bbd4b7a0cfbbb12d
%bcond check 1
%global debug_package %{nil}
%global crate num-prime
Name:           rust-num-prime
Version:        0.5.0
Release:        1%{?dist}
Summary:        Utilities for prime number related functionalities
License:        Apache-2.0
URL:            https://crates.io/crates/num-prime
Source0:        https://static.crates.io/crates/num-prime/num-prime-%{version}.crate
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
Summary:        Utilities for prime number related functionalities
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+big-int-devel
Summary:        Utilities for prime number related functionalities
BuildArch:      noarch
%description -n %{name}+big-int-devel

This package contains library source intended for building other packages which
use the "big-int" feature of the "%{crate}" crate.

%package     -n %{name}+big-table-devel
Summary:        Utilities for prime number related functionalities
BuildArch:      noarch
%description -n %{name}+big-table-devel

This package contains library source intended for building other packages which
use the "big-table" feature of the "%{crate}" crate.

%package     -n %{name}+num-bigint-devel
Summary:        Utilities for prime number related functionalities
BuildArch:      noarch
%description -n %{name}+num-bigint-devel

This package contains library source intended for building other packages which
use the "num-bigint" feature of the "%{crate}" crate.

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
%files -n rust-num-prime-devel -f %{oreon_filedir}/rust-num-prime-devel.list

%changelog

%autochangelog
