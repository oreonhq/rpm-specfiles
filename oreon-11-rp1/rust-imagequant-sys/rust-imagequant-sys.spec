%global source0_hash 399d307ead010ceffc6f45346b325f9de672da0fe05cfdfa5dec0e5551925e52

%bcond_without check

%global lib     libimagequant
%global crate   imagequant-sys

Name:           rust-imagequant-sys
Version:        4.0.3
Release:        2%{?dist}
Summary:        Convert 24/32-bit images to 8-bit palette with alpha channel

License:        GPL-3.0-or-later
URL:            https://crates.io/crates/imagequant-sys
Source0:        https://static.crates.io/crates/%{crate}/%{crate}-%{version}.crate
Patch:          0001-explicitly-set-version_suffix_components-for-recent-.patch

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Convert 24/32-bit images to 8-bit palette with alpha channel. C API/FFI
libimagequant that powers pngquant lossy PNG compressor. Dual-licensed
like pngquant. See https://pngquant.org for details.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/COPYRIGHT
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+capi-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+capi-devel %{_description}

This package contains library source intended for building other packages which
use the "capi" feature of the "%{crate}" crate.

%files       -n %{name}+capi-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+threads-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+threads-devel %{_description}

This package contains library source intended for building other packages which
use the "threads" feature of the "%{crate}" crate.

%files       -n %{name}+threads-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{lib}
Summary:        %{summary}
License:        Apache-2.0 AND GPL-3.0-or-later AND MIT
Obsoletes:     libimagequant < 4.0.0
Provides:      libimagequant%{_isa} = %{version}-%{release}

%description -n %{lib} %{_description}

%files       -n %{lib}
%license        COPYRIGHT
%license        LICENSE.dependencies
%doc            README.md
%{_libdir}/%{lib}.so.0{,.*}

%package     -n %{lib}-devel
Summary:        Development files for %{lib}
Requires:       %{lib}%{?_isa} = %{version}-%{release}
Obsoletes:     libimagequant-devel < 4.0.0
Provides:      libimagequant-devel%{_isa} = %{version}-%{release}
Provides:      libimagequant-devel = %{version}-%{release}

%description -n %{lib}-devel %{_description}

The %{lib}-devel package contains libraries and header files for
developing applications that use %{lib}.

%files       -n %{lib}-devel
%{_includedir}/%{lib}.h
%{_libdir}/%{lib}.so
%{_libdir}/pkgconfig/imagequant.pc

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires
echo "cargo-c"

%build
%cargo_build
%cargo_cbuild
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
%cargo_install
%cargo_cinstall
rm -f %{buildroot}%{_libdir}/%{lib}.a

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
