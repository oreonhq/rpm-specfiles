%global source0_hash c60a23ffb90d527e23192f1246b14746e2f7f071cb84476dd879071696c18a4a
%bcond check 0
%global debug_package %{nil}
%global crate lzma-rust2
Name:           rust-lzma-rust2_0.13
Version:        0.13.0
Release:        1%{?dist}
Summary:        LZMA / LZMA2 / LZIP / XZ compression ported from 'tukaani xz for java'
License:        Apache-2.0
URL:            https://crates.io/crates/lzma-rust2
Source0:        https://static.crates.io/crates/lzma-rust2/lzma-rust2-%{version}.crate
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
Summary:        LZMA / LZMA2 / LZIP / XZ compression ported from 'tukaani xz for java'
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+crc-devel
Summary:        LZMA / LZMA2 / LZIP / XZ compression ported from 'tukaani xz for java'
BuildArch:      noarch
%description -n %{name}+crc-devel

This package contains library source intended for building other packages which
use the "crc" feature of the "%{crate}" crate.

%package     -n %{name}+encoder-devel
Summary:        LZMA / LZMA2 / LZIP / XZ compression ported from 'tukaani xz for java'
BuildArch:      noarch
%description -n %{name}+encoder-devel

This package contains library source intended for building other packages which
use the "encoder" feature of the "%{crate}" crate.

%package     -n %{name}+lzip-devel
Summary:        LZMA / LZMA2 / LZIP / XZ compression ported from 'tukaani xz for java'
BuildArch:      noarch
%description -n %{name}+lzip-devel

This package contains library source intended for building other packages which
use the "lzip" feature of the "%{crate}" crate.

%package     -n %{name}+optimization-devel
Summary:        LZMA / LZMA2 / LZIP / XZ compression ported from 'tukaani xz for java'
BuildArch:      noarch
%description -n %{name}+optimization-devel

This package contains library source intended for building other packages which
use the "optimization" feature of the "%{crate}" crate.

%package     -n %{name}+sha2-devel
Summary:        LZMA / LZMA2 / LZIP / XZ compression ported from 'tukaani xz for java'
BuildArch:      noarch
%description -n %{name}+sha2-devel

This package contains library source intended for building other packages which
use the "sha2" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        LZMA / LZMA2 / LZIP / XZ compression ported from 'tukaani xz for java'
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+xz-devel
Summary:        LZMA / LZMA2 / LZIP / XZ compression ported from 'tukaani xz for java'
BuildArch:      noarch
%description -n %{name}+xz-devel

This package contains library source intended for building other packages which
use the "xz" feature of the "%{crate}" crate.

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
%files -n rust-lzma-rust2_0.13-devel -f %{oreon_filedir}/rust-lzma-rust2_0.13-devel.list

%changelog

%autochangelog
