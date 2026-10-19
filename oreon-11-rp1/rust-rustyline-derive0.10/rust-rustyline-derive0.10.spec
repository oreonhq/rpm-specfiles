%global source2_hash c660c3a1ca6c7c0d736f249dbc7ca5bdf1cbc7bf4d57bc867d3b47ec1ba8374e
%global source0_hash e5af959c8bf6af1aff6d2b463a57f71aae53d1332da58419e30ad8dc7011d951
%bcond check 1
%global debug_package %{nil}
%global crate rustyline-derive
Name:           rust-rustyline-derive0.10
Version:        0.10.0
Release:        1%{?dist}
Summary:        Rustyline derive macros (Completer, Helper, Hinter, Highlighter)
License:        MIT
URL:            https://crates.io/crates/rustyline-derive
Source0:        https://static.crates.io/crates/rustyline-derive/rustyline-derive-%{version}.crate
Source2:        https://github.com/kkawakam/rustyline/raw/v14.0.0/LICENSE
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
Summary:        Rustyline derive macros (Completer, Helper, Hinter, Highlighter)
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -pav %{SOURCE2} .
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
%files -n rust-rustyline-derive0.10-devel -f %{oreon_filedir}/rust-rustyline-derive0.10-devel.list

%changelog

%autochangelog
