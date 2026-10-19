%global source0_hash 175812e0be2bccb6abe50bb8d566126198344f707e304f45c648fd8f2cc0365e
%bcond check 0
%global debug_package %{nil}
%global crate bytecount
Name:           rust-bytecount
Version:        0.6.9
Release:        1%{?dist}
Summary:        count occurrences of a given byte, or the number of UTF-8 code points...
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/bytecount
Source0:        https://static.crates.io/crates/bytecount/bytecount-%{version}.crate
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
Summary:        count occurrences of a given byte, or the number of UTF-8 code points...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+generic-simd-devel
Summary:        count occurrences of a given byte, or the number of UTF-8 code points...
BuildArch:      noarch
%description -n %{name}+generic-simd-devel

This package contains library source intended for building other packages which
use the "generic-simd" feature of the "%{crate}" crate.

%package     -n %{name}+html_report-devel
Summary:        count occurrences of a given byte, or the number of UTF-8 code points...
BuildArch:      noarch
%description -n %{name}+html_report-devel

This package contains library source intended for building other packages which
use the "html_report" feature of the "%{crate}" crate.

%package     -n %{name}+runtime-dispatch-simd-devel
Summary:        count occurrences of a given byte, or the number of UTF-8 code points...
BuildArch:      noarch
%description -n %{name}+runtime-dispatch-simd-devel

This package contains library source intended for building other packages which
use the "runtime-dispatch-simd" feature of the "%{crate}" crate.

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
%files -n rust-bytecount-devel -f %{oreon_filedir}/rust-bytecount-devel.list

%changelog

%autochangelog
