%global source0_hash a9532581c6e4b60a147e1cabf35d6ba0ae74b2e75075a132c1ae9aa109c9c5eb

%global _description %{expand:
PerCetto is a minimal C wrapper for Perfetto SDK to enable app-specific
tracing. Internally, there is a minimal implementation of TrackEvent data
source.}

Name:           percetto
Version:        0.1.6
Release:        %autorelease
Summary:        Minimal C wrapper for Perfetto SDK to enable app tracing

License:        Apache-2.0
URL:            https://github.com/olvaffe/percetto
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# Disambiguate the type of atomic_fetch_xxx
Patch:          %{url}/commit/fd59d8b9bf05f4b0e7b681623156b99d41a8f6a7.patch
# fix build issues with v28.0 sdk
Patch:          %{url}/commit/90912f0e119f7b067e0e4a3d1d540225df8936e6.patch
# Add soversion to shared libraries
Patch:          percetto-soversion.patch

BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  perfetto-sdk

# Perfetto only supports these architectures
ExclusiveArch:  aarch64 x86_64

%description    %_description

%package        devel
Summary:        Development headers and libraries for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%meson -Dperfetto-sdk=%{_datadir}/perfetto/sdk -Dwerror=false
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_libdir}/libpercetto.so.0{,.*}
%{_libdir}/libpercetto-atrace.so.0{,.*}

%files devel
%{_includedir}/percetto.h
%{_includedir}/percetto-atrace.h
%{_libdir}/libpercetto.so
%{_libdir}/libpercetto-atrace.so
%{_libdir}/pkgconfig/percetto.pc
%{_libdir}/pkgconfig/percetto-atrace.pc

%changelog
%autochangelog
