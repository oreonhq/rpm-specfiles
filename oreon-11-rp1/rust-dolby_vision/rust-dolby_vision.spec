%global source0_hash 9a5f4ca7214c0353837ad9f9f7ac48df4da212aa0333b1adf5a515f1bae1e171
%bcond check 1
%global crate dolby_vision
Name:           rust-dolby_vision
Version:        3.4.0
Release:        1%{?dist}
Summary:        Dolby Vision metadata parsing and writing
License:        MIT
URL:            https://crates.io/crates/dolby_vision
Source0:        https://static.crates.io/crates/dolby_vision/dolby_vision-%{version}.crate
Patch:          dolby_vision-fix-metadata.diff
Patch:          dolby_vision-a8e639d.patch
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-c
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n libdovi
Summary:        Dolby Vision metadata parsing and writing
License:        MIT AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT)
%description -n libdovi

This package contains the C library.

%package     -n libdovi-devel
Summary:        Dolby Vision metadata parsing and writing
Requires:       libdovi%{?_isa} = %{version}-%{release}
%description -n libdovi-devel

This package contains the C library development files.

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Dolby Vision metadata parsing and writing
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+capi-devel
Summary:        Dolby Vision metadata parsing and writing
BuildArch:      noarch
%description -n %{name}+capi-devel

This package contains library source intended for building other packages which
use the "capi" feature of the "%{crate}" crate.

%package     -n %{name}+libc-devel
Summary:        Dolby Vision metadata parsing and writing
BuildArch:      noarch
%description -n %{name}+libc-devel

This package contains library source intended for building other packages which
use the "libc" feature of the "%{crate}" crate.

%package     -n %{name}+roxmltree-devel
Summary:        Dolby Vision metadata parsing and writing
BuildArch:      noarch
%description -n %{name}+roxmltree-devel

This package contains library source intended for building other packages which
use the "roxmltree" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Dolby Vision metadata parsing and writing
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+xml-devel
Summary:        Dolby Vision metadata parsing and writing
BuildArch:      noarch
%description -n %{name}+xml-devel

This package contains library source intended for building other packages which
use the "xml" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build -a
%{cargo_license_summary -a}
%{cargo_license -a} > LICENSE.dependencies
%cargo_cbuild -a
%install
%cargo_install -a
%cargo_cinstall -a
rm %{buildroot}/%{_libdir}/libdovi.a
%oreon_autofiles libdovi usr/*/lib*.so.*
%oreon_autofiles libdovi-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%{cargo_test -a -- -- %{shrink:
    --skip rpu::generate::tests::config_with_frame_edits
    --skip xml::tests::parse
}}
%endif
%files -f %{oreon_filedir}/main.list
%files -n libdovi -f %{oreon_filedir}/libdovi.list
%files -n libdovi-devel -f %{oreon_filedir}/libdovi-devel.list
%files -n rust-dolby_vision-devel -f %{oreon_filedir}/rust-dolby_vision-devel.list

%changelog

%autochangelog
