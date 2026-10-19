%global source0_hash 824a212faf96e9acacdbd09febd34438f8f711fb84e09a8916013cd7815ca28d
%bcond check 0
%global debug_package %{nil}
%global crate anstream
Name:           rust-anstream
Version:        1.0.0
Release:        1%{?dist}
Summary:        IO stream adapters for writing colored text
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/anstream
Source0:        https://static.crates.io/crates/anstream/anstream-%{version}.crate
Patch:          anstream-fix-metadata-auto.diff
Patch:          anstream-fix-metadata.diff
Patch:          0001-drop-is_terminal_polyfill-and-replace-with-std-io-Is.patch
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
Summary:        IO stream adapters for writing colored text
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+auto-devel
Summary:        IO stream adapters for writing colored text
BuildArch:      noarch
%description -n %{name}+auto-devel

This package contains library source intended for building other packages which
use the "auto" feature of the "%{crate}" crate.

%package     -n %{name}+test-devel
Summary:        IO stream adapters for writing colored text
BuildArch:      noarch
%description -n %{name}+test-devel

This package contains library source intended for building other packages which
use the "test" feature of the "%{crate}" crate.

%package     -n %{name}+wincon-devel
Summary:        IO stream adapters for writing colored text
BuildArch:      noarch
%description -n %{name}+wincon-devel

This package contains library source intended for building other packages which
use the "wincon" feature of the "%{crate}" crate.

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
%files -n rust-anstream-devel -f %{oreon_filedir}/rust-anstream-devel.list

%changelog

%autochangelog
