%global source0_hash f5022b5fbf9407086c180e9557be968742d839e68346af7792b8592489732197
%bcond check 0
%global debug_package %{nil}
%global crate vte
Name:           rust-vte0.11
Version:        0.11.1
Release:        1%{?dist}
Summary:        Parser for implementing terminal emulators
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/vte
Source0:        https://static.crates.io/crates/vte/vte-%{version}.crate
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
Summary:        Parser for implementing terminal emulators
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+ansi-devel
Summary:        Parser for implementing terminal emulators
BuildArch:      noarch
%description -n %{name}+ansi-devel

This package contains library source intended for building other packages which
use the "ansi" feature of the "%{crate}" crate.

%package     -n %{name}+arrayvec-devel
Summary:        Parser for implementing terminal emulators
BuildArch:      noarch
%description -n %{name}+arrayvec-devel

This package contains library source intended for building other packages which
use the "arrayvec" feature of the "%{crate}" crate.

%package     -n %{name}+log-devel
Summary:        Parser for implementing terminal emulators
BuildArch:      noarch
%description -n %{name}+log-devel

This package contains library source intended for building other packages which
use the "log" feature of the "%{crate}" crate.

%package     -n %{name}+nightly-devel
Summary:        Parser for implementing terminal emulators
BuildArch:      noarch
%description -n %{name}+nightly-devel

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

%package     -n %{name}+no_std-devel
Summary:        Parser for implementing terminal emulators
BuildArch:      noarch
%description -n %{name}+no_std-devel

This package contains library source intended for building other packages which
use the "no_std" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Parser for implementing terminal emulators
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
%files -n rust-vte0.11-devel -f %{oreon_filedir}/rust-vte0.11-devel.list

%changelog

%autochangelog
