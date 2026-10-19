%global source2_hash c6876aeee95e031392726ba4d02dbb2540da60e2030659d182c86e64ba9ff5e7
%global source0_hash 9cfdcd2bee8dc367afd9064f3b0849156a4c29fc70d98370dae62773594d04dd
%bcond check 0
%global debug_package %{nil}
%global crate delharc
Name:           rust-delharc
Version:        0.8.0
Release:        1%{?dist}
Summary:        Library for parsing and extracting files from LHA/LZH archives
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/delharc
Source0:        https://static.crates.io/crates/delharc/delharc-%{version}.crate
Source2:        https://github.com/royaltm/rust-delharc/archive/v%{version}/%{name}-%{version}-github.tar.gz
Patch:          delharc-fix-metadata.diff
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
tar xvf %SOURCE2 --strip-components=1 %{name}-%{version}/tests/\*
sed -i 's/\r//' *.md
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
%files -n rust-delharc-devel -f %{oreon_filedir}/rust-delharc-devel.list

%changelog

%autochangelog
