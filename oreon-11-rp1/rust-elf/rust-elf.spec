%global source2_hash ecdd912ab2073ef3be3af1ef48dc907dad4cf58d4dfde43a8a4a59bac785d4df
%global source0_hash 55dd888a213fc57e957abf2aa305ee3e8a28dbe05687a251f33b637cd46b0070
%bcond check 1
%global debug_package %{nil}
%global crate elf
Name:           rust-elf
Version:        0.8.0
Release:        1%{?dist}
Summary:        Pure-rust library for parsing ELF files
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/elf
Source0:        https://static.crates.io/crates/elf/elf-%{version}.crate
Source2:        https://github.com/cole14/rust-elf/archive/refs/tags/v%{version}.tar.gz
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
Summary:        Pure-rust library for parsing ELF files
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+nightly-devel
Summary:        Pure-rust library for parsing ELF files
BuildArch:      noarch
%description -n %{name}+nightly-devel

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Pure-rust library for parsing ELF files
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+to_str-devel
Summary:        Pure-rust library for parsing ELF files
BuildArch:      noarch
%description -n %{name}+to_str-devel

This package contains library source intended for building other packages which
use the "to_str" feature of the "%{crate}" crate.

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

tar xf %{SOURCE2} --strip-components=1 %{name}-%{version}/sample-objects
%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-elf-devel -f %{oreon_filedir}/rust-elf-devel.list

%changelog

%autochangelog
