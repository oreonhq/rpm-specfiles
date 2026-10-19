%global source0_hash f7c44f8e672c00fe5308fa235f821cb4198414e1c77935c1ab6948d3fd78550e
%bcond check 0
%global debug_package %{nil}
%global crate mime_guess
Name:           rust-mime_guess
Version:        2.0.5
Release:        1%{?dist}
Summary:        A simple crate for detection of a file's MIME type by its extension.
License:        MIT
URL:            https://crates.io/crates/mime_guess
Source0:        https://static.crates.io/crates/mime_guess/mime_guess-%{version}.crate
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
Summary:        A simple crate for detection of a file's MIME type by its extension.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+rev-mappings-devel
Summary:        A simple crate for detection of a file's MIME type by its extension.
BuildArch:      noarch
%description -n %{name}+rev-mappings-devel

This package contains library source intended for building other packages which
use the "rev-mappings" feature of the "%{crate}" crate.

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
%files -n rust-mime_guess-devel -f %{oreon_filedir}/rust-mime_guess-devel.list

%changelog

%autochangelog
