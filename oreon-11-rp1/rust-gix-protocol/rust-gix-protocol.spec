%global source0_hash 68878c37ae168b474c762d70adc8a8e0f9323ed0d80444a672e2eb561fa16691
%bcond check 0
%global debug_package %{nil}
%global crate gix-protocol
Name:           rust-gix-protocol
Version:        0.65.1
Release:        1%{?dist}
Summary:        A crate of the gitoxide project for implementing git protocols
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gix-protocol
Source0:        https://static.crates.io/crates/gix-protocol/gix-protocol-%{version}.crate
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

%package     -n %{name}+async-client-devel
Summary:        A crate of the gitoxide project for implementing git protocols
BuildArch:      noarch
%description -n %{name}+async-client-devel

This package contains library source intended for building other packages which
use the "async-client" feature of the "%{crate}" crate.

%package     -n %{name}+blocking-client-devel
Summary:        A crate of the gitoxide project for implementing git protocols
BuildArch:      noarch
%description -n %{name}+blocking-client-devel

This package contains library source intended for building other packages which
use the "blocking-client" feature of the "%{crate}" crate.

%package     -n %{name}+document-features-devel
Summary:        A crate of the gitoxide project for implementing git protocols
BuildArch:      noarch
%description -n %{name}+document-features-devel

This package contains library source intended for building other packages which
use the "document-features" feature of the "%{crate}" crate.

%package     -n %{name}+fetch-devel
Summary:        A crate of the gitoxide project for implementing git protocols
BuildArch:      noarch
%description -n %{name}+fetch-devel

This package contains library source intended for building other packages which
use the "fetch" feature of the "%{crate}" crate.

%package     -n %{name}+futures-lite-devel
Summary:        A crate of the gitoxide project for implementing git protocols
BuildArch:      noarch
%description -n %{name}+futures-lite-devel

This package contains library source intended for building other packages which
use the "futures-lite" feature of the "%{crate}" crate.

%package     -n %{name}+handshake-devel
Summary:        A crate of the gitoxide project for implementing git protocols
BuildArch:      noarch
%description -n %{name}+handshake-devel

This package contains library source intended for building other packages which
use the "handshake" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        A crate of the gitoxide project for implementing git protocols
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
%files -n rust-gix-protocol-devel -f %{oreon_filedir}/rust-gix-protocol-devel.list

%changelog

%autochangelog
