%global source0_hash b18b06f80e6274b353dd091c12b3a83217033ce0bd80471b54cf486cc60c0251

Name:           mctc-lib
Version:        0.3.2
Release:        4%{?dist}
Summary:        Modular computation tool chain library
License:        Apache-2.0
URL:            https://grimme-lab.github.io/mctc-lib/
Source0:        https://github.com/grimme-lab/mctc-lib/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  gcc-gfortran
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  json-fortran-devel
# For docs
BuildRequires:  rubygem-asciidoctor

# Patch to use python3 instead of env python3
Patch0:         mctc-lib-0.3.2-python3.patch

%description
Common tool chain for working with molecular structure data in various
applications. This library provides a unified way to perform
operations on molecular structure data, like reading and writing to
common geometry file formats.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .python3

%build
export FFLAGS="%{optflags} -I%{_fmoddir} -fPIC"
export FCLAGS="%{optflags} -I%{_fmoddir} -fPIC"
%meson
%meson_build

%install
%meson_install
# Remove static libraries
rm -f %{buildroot}%{_libdir}/*.a

# Move module files
mkdir -p %{buildroot}%{_fmoddir}
mv %{buildroot}%{_includedir}/mctc-lib/*/*.mod %{buildroot}%{_fmoddir}
rm -rf %{buildroot}%{_includedir}/mctc-lib/

%files
%license LICENSE
%doc README.md
%{_bindir}/mctc-convert
%{_mandir}/man1/mctc-convert.1*
%{_libdir}/libmctc-lib*.so.0*

%files devel
%{_fmoddir}/mctc_*.mod
%{_libdir}/pkgconfig/mctc-lib.pc
%{_libdir}/libmctc-lib.so

%changelog
%autochangelog
