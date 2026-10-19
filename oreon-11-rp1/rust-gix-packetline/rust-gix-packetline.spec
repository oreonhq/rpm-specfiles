%global source0_hash 792bd92bea390087e6223b18d4d023decc36467de31e6b066b69b94beea1b9e2
%bcond check 0
%global debug_package %{nil}
%global crate gix-packetline
Name:           rust-gix-packetline
Version:        0.22.2
Release:        1%{?dist}
Summary:        A crate of the gitoxide project implementing the pkt-line serializati...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gix-packetline
Source0:        https://static.crates.io/crates/gix-packetline/gix-packetline-%{version}.crate
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
Summary:        A crate of the gitoxide project implementing the pkt-line serializati...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+async-io-devel
Summary:        A crate of the gitoxide project implementing the pkt-line serializati...
BuildArch:      noarch
%description -n %{name}+async-io-devel

This package contains library source intended for building other packages which
use the "async-io" feature of the "%{crate}" crate.

%package     -n %{name}+blocking-io-devel
Summary:        A crate of the gitoxide project implementing the pkt-line serializati...
BuildArch:      noarch
%description -n %{name}+blocking-io-devel

This package contains library source intended for building other packages which
use the "blocking-io" feature of the "%{crate}" crate.

%package     -n %{name}+document-features-devel
Summary:        A crate of the gitoxide project implementing the pkt-line serializati...
BuildArch:      noarch
%description -n %{name}+document-features-devel

This package contains library source intended for building other packages which
use the "document-features" feature of the "%{crate}" crate.

%package     -n %{name}+futures-lite-devel
Summary:        A crate of the gitoxide project implementing the pkt-line serializati...
BuildArch:      noarch
%description -n %{name}+futures-lite-devel

This package contains library source intended for building other packages which
use the "futures-lite" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        A crate of the gitoxide project implementing the pkt-line serializati...
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
%files -n rust-gix-packetline-devel -f %{oreon_filedir}/rust-gix-packetline-devel.list

%changelog

%autochangelog
