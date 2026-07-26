%global source0_hash e60346ae303bea6b58b9d68dd70186d5be51b326ebcd92d739c017c24c2bd702

Name:           libacars
Version:        1.3.1
Release:        18%{?dist}
Summary:        A library for decoding various ACARS message payloads
License:        MIT
URL:            https://github.com/szpajder/libacars
Source0:        https://github.com/szpajder/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(zlib)
BuildRequires:  ninja-build

%description
libacars is a library for decoding various ACARS message payloads.

%package devel
Summary:        Development files for libacars
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
libacars is a library for decoding various ACARS message payloads.

This subpackage contains libraries and header files for developing
applications that want to make use of libacars.

%package -n acars-examples
Summary:        Example applications for libacars

%description -n acars-examples
Example applications for for libacars:

 * decode_arinc.c - decodes ARINC-622 messages supplied at the
   command line or from a file.
 * adsc_get_position - illustrates how to extract position-related
   fields from decoded ADS-C message.
 * cpdlc_get_position - illustrates how to extract position-related
   fields from CPDLC position reports.
 * media_advisory - decodes Media Advisory messages (ACARS label SA
   reports)

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
mkdir -p %{_target_platform}
sed -i -e "/acars_static/d" src/libacars/CMakeLists.txt

%build
# TODO: Please submit an issue to upstream (rhbz#2380704)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_LIBDIR:PATH=%{_lib} \
    -DCMAKE_SHARED_LINKER_FLAGS=""
%cmake_build

%install
%cmake_install
rm -rf %{buildroot}/%{_datadir}/doc

%files
%doc CHANGELOG.md README.md
%license LICENSE.md
%{_libdir}/%{name}.so.1

%files devel
%doc doc/API_REFERENCE.md doc/API_REFERENCE.md
%{_includedir}/%{name}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files -n acars-examples
%{_bindir}/adsc_get_position
%{_bindir}/cpdlc_get_position
%{_bindir}/decode_acars_apps
%{_bindir}/media_advisory

%changelog
%autochangelog
