%global source0_hash 00810f1d8b74be64b13dbf3db89ac67740615d6c891f0e7b6179326533011a07
%bcond check 0
%global debug_package %{nil}
%global crate jpeg-decoder
Name:           rust-jpeg-decoder
Version:        0.3.2
Release:        1%{?dist}
Summary:        JPEG decoder
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/jpeg-decoder
Source0:        https://static.crates.io/crates/jpeg-decoder/jpeg-decoder-%{version}.crate
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
Summary:        JPEG decoder
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+nightly_aarch64_neon-devel
Summary:        JPEG decoder
BuildArch:      noarch
%description -n %{name}+nightly_aarch64_neon-devel

This package contains library source intended for building other packages which
use the "nightly_aarch64_neon" feature of the "%{crate}" crate.

%package     -n %{name}+platform_independent-devel
Summary:        JPEG decoder
BuildArch:      noarch
%description -n %{name}+platform_independent-devel

This package contains library source intended for building other packages which
use the "platform_independent" feature of the "%{crate}" crate.

%package     -n %{name}+rayon-devel
Summary:        JPEG decoder
BuildArch:      noarch
%description -n %{name}+rayon-devel

This package contains library source intended for building other packages which
use the "rayon" feature of the "%{crate}" crate.

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
%files -n rust-jpeg-decoder-devel -f %{oreon_filedir}/rust-jpeg-decoder-devel.list

%changelog

%autochangelog
