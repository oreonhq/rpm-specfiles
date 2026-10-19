%global source0_hash d817e038c30374a4bcb22f94d0a8a0e216958d4c3dcde369b1439fec4bdda6e6
%bcond check 1
%global debug_package %{nil}
%global crate esaxx-rs
Name:           rust-esaxx-rs
Version:        0.1.10
Release:        1%{?dist}
Summary:        Wrapping around sentencepiece's esaxxx library
License:        Apache-2.0 AND MIT
URL:            https://crates.io/crates/esaxx-rs
Source0:        https://static.crates.io/crates/esaxx-rs/esaxx-rs-%{version}.crate
Source2:        LICENSE-MIT
Patch:          esaxx-rs-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  gcc-c++
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
Summary:        Wrapping around sentencepiece's esaxxx library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+cc-devel
Summary:        Wrapping around sentencepiece's esaxxx library
BuildArch:      noarch
%description -n %{name}+cc-devel

This package contains library source intended for building other packages which
use the "cc" feature of the "%{crate}" crate.

%package     -n %{name}+cpp-devel
Summary:        Wrapping around sentencepiece's esaxxx library
BuildArch:      noarch
%description -n %{name}+cpp-devel

This package contains library source intended for building other packages which
use the "cpp" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -pL %{SOURCE2} .
rm -r benches/ data/ examples/
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
%files -n rust-esaxx-rs-devel -f %{oreon_filedir}/rust-esaxx-rs-devel.list

%changelog

%autochangelog
