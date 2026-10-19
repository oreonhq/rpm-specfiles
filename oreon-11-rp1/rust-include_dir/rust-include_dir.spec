%global source0_hash 923d117408f1e49d914f1a379a309cffe4f18c05cf4e3d12e613a15fc81bd0dd
%bcond check 0
%global debug_package %{nil}
%global crate include_dir
Name:           rust-include_dir
Version:        0.7.4
Release:        1%{?dist}
Summary:        Embed the contents of a directory in your binary
License:        MIT
URL:            https://crates.io/crates/include_dir
Source0:        https://static.crates.io/crates/include_dir/include_dir-%{version}.crate
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
Summary:        Embed the contents of a directory in your binary
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+glob-devel
Summary:        Embed the contents of a directory in your binary
BuildArch:      noarch
%description -n %{name}+glob-devel

This package contains library source intended for building other packages which
use the "glob" feature of the "%{crate}" crate.

%package     -n %{name}+metadata-devel
Summary:        Embed the contents of a directory in your binary
BuildArch:      noarch
%description -n %{name}+metadata-devel

This package contains library source intended for building other packages which
use the "metadata" feature of the "%{crate}" crate.

%package     -n %{name}+nightly-devel
Summary:        Embed the contents of a directory in your binary
BuildArch:      noarch
%description -n %{name}+nightly-devel

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

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
%files -n rust-include_dir-devel -f %{oreon_filedir}/rust-include_dir-devel.list

%changelog

%autochangelog
