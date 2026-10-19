%global source0_hash 4ae047235e33e2829703574b54fdec96bfbad892062d97fed2f76022287de61b
%bcond check 0
%global debug_package %{nil}
%global crate gif
Name:           rust-gif0.13
Version:        0.13.3
Release:        1%{?dist}
Summary:        GIF de- and encoder
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gif
Source0:        https://static.crates.io/crates/gif/gif-%{version}.crate
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
Summary:        GIF de- and encoder
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+color_quant-devel
Summary:        GIF de- and encoder
BuildArch:      noarch
%description -n %{name}+color_quant-devel

This package contains library source intended for building other packages which
use the "color_quant" feature of the "%{crate}" crate.

%package     -n %{name}+raii_no_panic-devel
Summary:        GIF de- and encoder
BuildArch:      noarch
%description -n %{name}+raii_no_panic-devel

This package contains library source intended for building other packages which
use the "raii_no_panic" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        GIF de- and encoder
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
%files -n rust-gif0.13-devel -f %{oreon_filedir}/rust-gif0.13-devel.list

%changelog

%autochangelog
