%global source0_hash 25b2a3d18343079e92449b9c8d73a23fa8dc0ede2faf5c94ad6cfa4676355133
Name:           mctc-lib
Version:        0.5.2
Release:        1%{?dist}
Summary:        Modular computation tool chain library
License:        Apache-2.0
URL:            https://grimme-lab.github.io/mctc-lib/
Source0:        https://github.com/grimme-lab/mctc-lib/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         mctc-lib-0.3.2-python3.patch
# oreon:deps
BuildRequires:  gcc-gfortran
BuildRequires:  json-fortran-devel
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  python3-devel
BuildRequires:  rubygem-asciidoctor
# /oreon:deps
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
rm -f %{buildroot}%{_libdir}/*.a
mkdir -p %{buildroot}%{_fmoddir}
mv %{buildroot}%{_includedir}/mctc-lib/*/*.mod %{buildroot}%{_fmoddir}
rm -rf %{buildroot}%{_includedir}/mctc-lib/
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n mctc-lib-devel -f %{oreon_filedir}/mctc-lib-devel.list

%changelog

%autochangelog
