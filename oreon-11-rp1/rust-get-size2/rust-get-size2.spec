%global source0_hash d4d338de392104417fe6fdbe588c52383b9236956d8afe5654f0077176edc632
%bcond check 0
%global debug_package %{nil}
%global crate get-size2
Name:           rust-get-size2
Version:        0.11.0
Release:        1%{?dist}
Summary:        Determine the size in bytes an object occupies inside RAM
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/get-size2
Source0:        https://static.crates.io/crates/get-size2/get-size2-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  dos2unix
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
Summary:        Determine the size in bytes an object occupies inside RAM
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+bytes-devel
Summary:        Determine the size in bytes an object occupies inside RAM
BuildArch:      noarch
%description -n %{name}+bytes-devel

This package contains library source intended for building other packages which
use the "bytes" feature of the "%{crate}" crate.

%package     -n %{name}+chrono-devel
Summary:        Determine the size in bytes an object occupies inside RAM
BuildArch:      noarch
%description -n %{name}+chrono-devel

This package contains library source intended for building other packages which
use the "chrono" feature of the "%{crate}" crate.

%package     -n %{name}+chrono-tz-devel
Summary:        Determine the size in bytes an object occupies inside RAM
BuildArch:      noarch
%description -n %{name}+chrono-tz-devel

This package contains library source intended for building other packages which
use the "chrono-tz" feature of the "%{crate}" crate.

%package     -n %{name}+compact-str-devel
Summary:        Determine the size in bytes an object occupies inside RAM
BuildArch:      noarch
%description -n %{name}+compact-str-devel

This package contains library source intended for building other packages which
use the "compact-str" feature of the "%{crate}" crate.

%package     -n %{name}+derive-devel
Summary:        Determine the size in bytes an object occupies inside RAM
BuildArch:      noarch
%description -n %{name}+derive-devel

This package contains library source intended for building other packages which
use the "derive" feature of the "%{crate}" crate.

%package     -n %{name}+get-size-derive2-devel
Summary:        Determine the size in bytes an object occupies inside RAM
BuildArch:      noarch
%description -n %{name}+get-size-derive2-devel

This package contains library source intended for building other packages which
use the "get-size-derive2" feature of the "%{crate}" crate.

%package     -n %{name}+hashbrown-devel
Summary:        Determine the size in bytes an object occupies inside RAM
BuildArch:      noarch
%description -n %{name}+hashbrown-devel

This package contains library source intended for building other packages which
use the "hashbrown" feature of the "%{crate}" crate.

%package     -n %{name}+indexmap-devel
Summary:        Determine the size in bytes an object occupies inside RAM
BuildArch:      noarch
%description -n %{name}+indexmap-devel

This package contains library source intended for building other packages which
use the "indexmap" feature of the "%{crate}" crate.

%package     -n %{name}+ordermap-devel
Summary:        Determine the size in bytes an object occupies inside RAM
BuildArch:      noarch
%description -n %{name}+ordermap-devel

This package contains library source intended for building other packages which
use the "ordermap" feature of the "%{crate}" crate.

%package     -n %{name}+smallvec-devel
Summary:        Determine the size in bytes an object occupies inside RAM
BuildArch:      noarch
%description -n %{name}+smallvec-devel

This package contains library source intended for building other packages which
use the "smallvec" feature of the "%{crate}" crate.

%package     -n %{name}+thin-vec-devel
Summary:        Determine the size in bytes an object occupies inside RAM
BuildArch:      noarch
%description -n %{name}+thin-vec-devel

This package contains library source intended for building other packages which
use the "thin-vec" feature of the "%{crate}" crate.

%package     -n %{name}+url-devel
Summary:        Determine the size in bytes an object occupies inside RAM
BuildArch:      noarch
%description -n %{name}+url-devel

This package contains library source intended for building other packages which
use the "url" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
find . -type f -exec dos2unix --keepdate '{}' '+'
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
%files -n rust-get-size2-devel -f %{oreon_filedir}/rust-get-size2-devel.list

%changelog

%autochangelog
