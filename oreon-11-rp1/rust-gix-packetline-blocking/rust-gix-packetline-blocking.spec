%global source0_hash 89c59c3ad41e68cb38547d849e9ef5ccfc0d00f282244ba1441ae856be54d001
%bcond check 1
%global debug_package %{nil}
%global crate gix-packetline-blocking
Name:           rust-gix-packetline-blocking
Version:        0.19.3
Release:        1%{?dist}
Summary:        Duplicate of gix-packetline with the blocking-io feature pre-selected
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gix-packetline-blocking
Source0:        https://static.crates.io/crates/gix-packetline-blocking/gix-packetline-blocking-%{version}.crate
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
Summary:        Duplicate of gix-packetline with the blocking-io feature pre-selected
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+async-io-devel
Summary:        Duplicate of gix-packetline with the blocking-io feature pre-selected
BuildArch:      noarch
%description -n %{name}+async-io-devel

This package contains library source intended for building other packages which
use the "async-io" feature of the "%{crate}" crate.

%package     -n %{name}+blocking-io-devel
Summary:        Duplicate of gix-packetline with the blocking-io feature pre-selected
BuildArch:      noarch
%description -n %{name}+blocking-io-devel

This package contains library source intended for building other packages which
use the "blocking-io" feature of the "%{crate}" crate.

%package     -n %{name}+document-features-devel
Summary:        Duplicate of gix-packetline with the blocking-io feature pre-selected
BuildArch:      noarch
%description -n %{name}+document-features-devel

This package contains library source intended for building other packages which
use the "document-features" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Duplicate of gix-packetline with the blocking-io feature pre-selected
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
%files -n rust-gix-packetline-blocking-devel -f %{oreon_filedir}/rust-gix-packetline-blocking-devel.list

%changelog

%autochangelog
