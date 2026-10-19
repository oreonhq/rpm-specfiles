%global source0_hash 183a7b9f33ec0bda428d8ac463700a7386502babac83cef83398fcaed2cda6d2
%global giturl  https://github.com/flatsurf/e-antic
Name:           e-antic
Version:        2.1.1
Release:        1%{?dist}
Summary:        Real Embedded Algebraic Number Theory In C
License:        LGPL-3.0-or-later
URL:            https://flatsurf.github.io/e-antic/libeantic/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/%{version}/%{name}-%{version}.tar.gz
Patch:          %{name}-unpatch.patch
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  catch2-devel
BuildRequires:  cereal-devel
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(flint)
# /oreon:deps
%description
E-ANTIC is a C/C++ library to deal with real embedded number fields, built on
top of ANTIC.  Its aim is to have as fast as possible exact arithmetic
operations and comparisons.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       boost-devel%{?_isa}
Requires:       cereal-devel%{?_isa}
Requires:       flint-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%conf
# Upstream does not generate the configure script
autoreconf -fi .

# Make catch2 available for testing
mkdir -p libeantic/test/external/catch2/single_include
ln -s %{_includedir}/catch2 libeantic/test/external/catch2/single_include

# Make cereal available for testing
rmdir libeantic/test/external/cereal
ln -s %{_includedir}/cereal libeantic/test/external/cereal

%build

%configure \
  --disable-static \
  --disable-silent-rules \
  --without-doc \
  --without-pyeantic
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libeantic/libtool
%make_build
%install
%make_install
rm -fr %{buildroot}%{_docdir}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

LD_LIBRARY_PATH=%{buildroot}%{_libdir} make check
%files -f %{oreon_filedir}/main.list
%files -n e-antic-devel -f %{oreon_filedir}/e-antic-devel.list

%changelog

%autochangelog
