%global source0_hash a28ac98ddc8b9274cb41bb4d9d4d5c425b6020c50c46f25559911905610b4a88
%bcond check 1
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate weezl
Name:           rust-weezl0.1
Version:        0.1.12
Release:        1%{?dist}
Summary:        Fast LZW compression and decompression
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/weezl
Source0:        https://static.crates.io/crates/weezl/weezl-%{version}.crate
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
Summary:        Fast LZW compression and decompression
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Fast LZW compression and decompression
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+async-devel
Summary:        Fast LZW compression and decompression
BuildArch:      noarch
%description -n %{name}+async-devel

This package contains library source intended for building other packages which
use the "async" feature of the "%{crate}" crate.

%package     -n %{name}+futures-devel
Summary:        Fast LZW compression and decompression
BuildArch:      noarch
%description -n %{name}+futures-devel

This package contains library source intended for building other packages which
use the "futures" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Fast LZW compression and decompression
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
%files -n rust-weezl0.1-devel -f %{oreon_filedir}/rust-weezl0.1-devel.list

%changelog

%autochangelog
