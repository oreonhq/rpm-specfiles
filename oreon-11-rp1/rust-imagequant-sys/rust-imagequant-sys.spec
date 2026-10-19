%global source0_hash b5361d7aab1d0c5623172cd6d18920bf21ef56f6e21d7290f1e31e0794c4a76e
%bcond_without check
%global lib     libimagequant
%global crate   imagequant-sys
Name:           rust-imagequant-sys
Version:        4.1.0
Release:        1%{?dist}
Summary:        Convert 24/32-bit images to 8-bit palette with alpha channel
License:        GPL-3.0-or-later
URL:            https://crates.io/crates/imagequant-sys
Source0:        https://static.crates.io/crates/%{crate}/%{crate}-%{version}.crate
Patch:          0001-explicitly-set-version_suffix_components-for-recent-.patch
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
Summary:        Convert 24/32-bit images to 8-bit palette with alpha channel
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+capi-devel
Summary:        Convert 24/32-bit images to 8-bit palette with alpha channel
BuildArch:      noarch
%description -n %{name}+capi-devel

This package contains library source intended for building other packages which
use the "capi" feature of the "%{crate}" crate.

%package     -n %{name}+threads-devel
Summary:        Convert 24/32-bit images to 8-bit palette with alpha channel
BuildArch:      noarch
%description -n %{name}+threads-devel

This package contains library source intended for building other packages which
use the "threads" feature of the "%{crate}" crate.

%package     -n %{lib}
Summary:        Convert 24/32-bit images to 8-bit palette with alpha channel
License:        Apache-2.0 AND GPL-3.0-or-later AND MIT
Obsoletes:     libimagequant < 4.0.0
Provides:      libimagequant%{_isa} = %{version}-%{release}
%description -n %{lib}

%package     -n %{lib}-devel
Summary:        Development files for %{lib}
Requires:       %{lib}%{?_isa} = %{version}-%{release}
Obsoletes:     libimagequant-devel < 4.0.0
Provides:      libimagequant-devel%{_isa} = %{version}-%{release}
Provides:      libimagequant-devel = %{version}-%{release}
%description -n %{lib}-devel

The %{lib}-devel package contains libraries and header files for
developing applications that use %{lib}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%cargo_cbuild
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%cargo_install
%cargo_cinstall
rm -f %{buildroot}%{_libdir}/%{lib}.a
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-imagequant-sys-devel -f %{oreon_filedir}/rust-imagequant-sys-devel.list
%files -n libimagequant -f %{oreon_filedir}/libimagequant.list
%files -n libimagequant-devel -f %{oreon_filedir}/libimagequant-devel.list

%changelog

%autochangelog
