%global source0_hash 383d29d513d8764dcdc42ea295d979eb99c3c9f00607b3692cf68a431f7dca72
%bcond check 0
%global debug_package %{nil}
%global crate binascii
Name:           rust-binascii
Version:        0.1.4
Release:        1%{?dist}
Summary:        Useful no-std binascii operations including base64, base32 and base16...
License:        MIT
URL:            https://crates.io/crates/binascii
Source0:        https://static.crates.io/crates/binascii/binascii-%{version}.crate
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
Summary:        Useful no-std binascii operations including base64, base32 and base16...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+decode-devel
Summary:        Useful no-std binascii operations including base64, base32 and base16...
BuildArch:      noarch
%description -n %{name}+decode-devel

This package contains library source intended for building other packages which
use the "decode" feature of the "%{crate}" crate.

%package     -n %{name}+encode-devel
Summary:        Useful no-std binascii operations including base64, base32 and base16...
BuildArch:      noarch
%description -n %{name}+encode-devel

This package contains library source intended for building other packages which
use the "encode" feature of the "%{crate}" crate.

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
%files -n rust-binascii-devel -f %{oreon_filedir}/rust-binascii-devel.list

%changelog

%autochangelog
