%global source0_hash 3658b90877f637514897c3dcbd628e0d290bcc7fee551a398b3994ebdc62d51e
%bcond check 0
%global debug_package %{nil}
%global crate delharc
Name:           rust-delharc0.6
Version:        0.6.2
Release:        1%{?dist}
Summary:        Library for parsing and extracting files from LHA/LZH archives
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/delharc
Source0:        https://static.crates.io/crates/delharc/delharc-%{version}.crate
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
Summary:        Library for parsing and extracting files from LHA/LZH archives
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+lh1-devel
Summary:        Library for parsing and extracting files from LHA/LZH archives
BuildArch:      noarch
%description -n %{name}+lh1-devel

This package contains library source intended for building other packages which
use the "lh1" feature of the "%{crate}" crate.

%package     -n %{name}+lhx-devel
Summary:        Library for parsing and extracting files from LHA/LZH archives
BuildArch:      noarch
%description -n %{name}+lhx-devel

This package contains library source intended for building other packages which
use the "lhx" feature of the "%{crate}" crate.

%package     -n %{name}+lz-devel
Summary:        Library for parsing and extracting files from LHA/LZH archives
BuildArch:      noarch
%description -n %{name}+lz-devel

This package contains library source intended for building other packages which
use the "lz" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Library for parsing and extracting files from LHA/LZH archives
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
%files -n rust-delharc0.6-devel -f %{oreon_filedir}/rust-delharc0.6-devel.list

%changelog

%autochangelog
