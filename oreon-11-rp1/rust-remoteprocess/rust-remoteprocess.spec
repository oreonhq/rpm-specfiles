%global source0_hash 8192fa1e574a067848e404651275f19603ac4ec0d8957997597a0495614ddc85
%bcond check 1
%global debug_package %{nil}
%global crate remoteprocess
Name:           rust-remoteprocess
Version:        0.5.1
Release:        1%{?dist}
Summary:        Cross platform api for getting information on a running processes
License:        MIT
URL:            https://crates.io/crates/remoteprocess
Source0:        https://static.crates.io/crates/remoteprocess/remoteprocess-%{version}.crate
Patch:          remoteprocess-fix-metadata-auto.diff
Patch:          remoteprocess-fix-metadata.diff
Patch10:        https://github.com/benfred/remoteprocess/pull/112.patch
Patch11:        0001-Update-nix-from-0.26-to-0.31.patch
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
Summary:        Cross platform api for getting information on a running processes
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+unwind-devel
Summary:        Cross platform api for getting information on a running processes
BuildArch:      noarch
%description -n %{name}+unwind-devel

This package contains library source intended for building other packages which
use the "unwind" feature of the "%{crate}" crate.

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
%files -n rust-remoteprocess-devel -f %{oreon_filedir}/rust-remoteprocess-devel.list

%changelog

%autochangelog
