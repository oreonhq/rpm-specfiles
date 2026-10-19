%global source0_hash d93877bcde0eb80ca09131a08d23f0a5c18a620b01db137dba666d18cd9b30c2
%bcond check 0
%global debug_package %{nil}
%global crate event-listener
Name:           rust-event-listener3
Version:        3.1.0
Release:        1%{?dist}
Summary:        Notify async tasks or threads
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/event-listener
Source0:        https://static.crates.io/crates/event-listener/event-listener-%{version}.crate
Patch:          event-listener-fix-metadata-auto.diff
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
Summary:        Notify async tasks or threads
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+parking-devel
Summary:        Notify async tasks or threads
BuildArch:      noarch
%description -n %{name}+parking-devel

This package contains library source intended for building other packages which
use the "parking" feature of the "%{crate}" crate.

%package     -n %{name}+portable-atomic-devel
Summary:        Notify async tasks or threads
BuildArch:      noarch
%description -n %{name}+portable-atomic-devel

This package contains library source intended for building other packages which
use the "portable-atomic" feature of the "%{crate}" crate.

%package     -n %{name}+portable-atomic-util-devel
Summary:        Notify async tasks or threads
BuildArch:      noarch
%description -n %{name}+portable-atomic-util-devel

This package contains library source intended for building other packages which
use the "portable-atomic-util" feature of the "%{crate}" crate.

%package     -n %{name}+portable_atomic_crate-devel
Summary:        Notify async tasks or threads
BuildArch:      noarch
%description -n %{name}+portable_atomic_crate-devel

This package contains library source intended for building other packages which
use the "portable_atomic_crate" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Notify async tasks or threads
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-event-listener3-devel -f %{oreon_filedir}/rust-event-listener3-devel.list

%changelog

%autochangelog
