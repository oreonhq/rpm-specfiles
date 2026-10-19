%global source0_hash 9a5f4ca7214c0353837ad9f9f7ac48df4da212aa0333b1adf5a515f1bae1e171
%global crate dolby_vision
%bcond check 1
Name:           libdovi
Version:        3.4.0
Release:        1%{?dist}
Summary:        Dolby Vision metadata parsing and writing
License:        MIT AND (Apache-2.0 OR MIT) AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT)
URL:            https://github.com/quietvoid/dovi_tool
Source0:        https://static.crates.io/crates/dolby_vision/dolby_vision-%{version}.crate#/dolby_vision-%{version}.crate
Patch0:         dolby_vision-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-c
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

This package contains the C library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

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
%cargo_cinstall -a
rm -f %{buildroot}%{_libdir}/libdovi.a
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%{cargo_test -a -- -- %{shrink:
    --skip rpu::generate::tests::config_with_frame_edits
    --skip xml::tests::parse
}}
%endif
%files -f %{oreon_filedir}/main.list
%files -n libdovi-devel -f %{oreon_filedir}/libdovi-devel.list

%changelog

%autochangelog
