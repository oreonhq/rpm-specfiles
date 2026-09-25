%global source0_hash 9a5f4ca7214c0353837ad9f9f7ac48df4da212aa0333b1adf5a515f1bae1e171
%global crate dolby_vision

%bcond check 1

Name:           libdovi
Version:        3.4.0
Release:        %autorelease
Summary:        Dolby Vision metadata parsing and writing

License:        MIT AND (Apache-2.0 OR MIT) AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT)
URL:            https://github.com/quietvoid/dovi_tool
Source0:        https://static.crates.io/crates/dolby_vision/dolby_vision-%{version}.crate#/dolby_vision-%{version}.crate

Patch0:         dolby_vision-fix-metadata.diff

BuildRequires:  cargo-c
BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Dolby Vision metadata parsing and writing.}

%description %{_description}

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
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires -a

%build
%cargo_build -a
%{cargo_license_summary -a}
%{cargo_license -a} > LICENSE.dependencies
%cargo_cbuild -a

%install
%cargo_cinstall -a
rm -f %{buildroot}%{_libdir}/libdovi.a

%if %{with check}
%check
%{cargo_test -a -- -- %{shrink:
    --skip rpu::generate::tests::config_with_frame_edits
    --skip xml::tests::parse
}}
%endif

%files
%license LICENSE
%license LICENSE.dependencies
%doc CHANGELOG.md README.md
%{_libdir}/libdovi.so.3{,.*}

%files devel
%{_libdir}/libdovi.so
%{_libdir}/pkgconfig/dovi.pc
%dir %{_includedir}/libdovi
%{_includedir}/libdovi/rpu_parser.h

%changelog
%autochangelog
