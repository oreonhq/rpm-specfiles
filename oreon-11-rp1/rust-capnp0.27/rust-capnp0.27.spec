%global source0_hash 93f7ce2b1b49d58b2b754f9146ef07e3244f9b67e7563bc1292fbd5f01b142f0
%bcond check 0
%global debug_package %{nil}
%global crate capnp
Name:           rust-capnp0.27
Version:        0.27.2
Release:        1%{?dist}
Summary:        Runtime library for Cap'n Proto data encoding
License:        MIT
URL:            https://crates.io/crates/capnp
Source0:        https://static.crates.io/crates/capnp/capnp-%{version}.crate
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
Summary:        Runtime library for Cap'n Proto data encoding
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Runtime library for Cap'n Proto data encoding
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+embedded-io-devel
Summary:        Runtime library for Cap'n Proto data encoding
BuildArch:      noarch
%description -n %{name}+embedded-io-devel

This package contains library source intended for building other packages which
use the "embedded-io" feature of the "%{crate}" crate.

%package     -n %{name}+quickcheck-devel
Summary:        Runtime library for Cap'n Proto data encoding
BuildArch:      noarch
%description -n %{name}+quickcheck-devel

This package contains library source intended for building other packages which
use the "quickcheck" feature of the "%{crate}" crate.

%package     -n %{name}+rpc_try-devel
Summary:        Runtime library for Cap'n Proto data encoding
BuildArch:      noarch
%description -n %{name}+rpc_try-devel

This package contains library source intended for building other packages which
use the "rpc_try" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Runtime library for Cap'n Proto data encoding
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+sync_reader-devel
Summary:        Runtime library for Cap'n Proto data encoding
BuildArch:      noarch
%description -n %{name}+sync_reader-devel

This package contains library source intended for building other packages which
use the "sync_reader" feature of the "%{crate}" crate.

%package     -n %{name}+unaligned-devel
Summary:        Runtime library for Cap'n Proto data encoding
BuildArch:      noarch
%description -n %{name}+unaligned-devel

This package contains library source intended for building other packages which
use the "unaligned" feature of the "%{crate}" crate.

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
%files -n rust-capnp0.27-devel -f %{oreon_filedir}/rust-capnp0.27-devel.list

%changelog

%autochangelog
