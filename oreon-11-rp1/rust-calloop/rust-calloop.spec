%global source0_hash 4dbf9978365bac10f54d1d4b04f7ce4427e51f71d61f2fe15e3fed5166474df7
%bcond check 1
%global debug_package %{nil}
%global crate calloop
Name:           rust-calloop
Version:        0.14.4
Release:        1%{?dist}
Summary:        Callback-based event loop
License:        MIT
URL:            https://crates.io/crates/calloop
Source0:        https://static.crates.io/crates/calloop/calloop-%{version}.crate
Patch:          calloop-fix-metadata.diff
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
Summary:        Callback-based event loop
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+async-task-devel
Summary:        Callback-based event loop
BuildArch:      noarch
%description -n %{name}+async-task-devel

This package contains library source intended for building other packages which
use the "async-task" feature of the "%{crate}" crate.

%package     -n %{name}+block_on-devel
Summary:        Callback-based event loop
BuildArch:      noarch
%description -n %{name}+block_on-devel

This package contains library source intended for building other packages which
use the "block_on" feature of the "%{crate}" crate.

%package     -n %{name}+executor-devel
Summary:        Callback-based event loop
BuildArch:      noarch
%description -n %{name}+executor-devel

This package contains library source intended for building other packages which
use the "executor" feature of the "%{crate}" crate.

%package     -n %{name}+futures-core-devel
Summary:        Callback-based event loop
BuildArch:      noarch
%description -n %{name}+futures-core-devel

This package contains library source intended for building other packages which
use the "futures-core" feature of the "%{crate}" crate.

%package     -n %{name}+futures-io-devel
Summary:        Callback-based event loop
BuildArch:      noarch
%description -n %{name}+futures-io-devel

This package contains library source intended for building other packages which
use the "futures-io" feature of the "%{crate}" crate.

%package     -n %{name}+nix-devel
Summary:        Callback-based event loop
BuildArch:      noarch
%description -n %{name}+nix-devel

This package contains library source intended for building other packages which
use the "nix" feature of the "%{crate}" crate.

%package     -n %{name}+pin-utils-devel
Summary:        Callback-based event loop
BuildArch:      noarch
%description -n %{name}+pin-utils-devel

This package contains library source intended for building other packages which
use the "pin-utils" feature of the "%{crate}" crate.

%package     -n %{name}+signals-devel
Summary:        Callback-based event loop
BuildArch:      noarch
%description -n %{name}+signals-devel

This package contains library source intended for building other packages which
use the "signals" feature of the "%{crate}" crate.

%package     -n %{name}+stream-devel
Summary:        Callback-based event loop
BuildArch:      noarch
%description -n %{name}+stream-devel

This package contains library source intended for building other packages which
use the "stream" feature of the "%{crate}" crate.

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
%files -n rust-calloop-devel -f %{oreon_filedir}/rust-calloop-devel.list

%changelog

%autochangelog
