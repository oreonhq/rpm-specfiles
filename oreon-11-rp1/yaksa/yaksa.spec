%global source0_hash 380d5780c73b4d9623ed558daebf77f2497931783ed7403bab08682d6f25da86
%bcond tests 1
Name:           yaksa
Version:        0.4
Release:        1%{?dist}
Summary:        High-performance library for noncontiguous data
%global forgeurl https://github.com/pmodels/yaksa/
%forgemeta
%global soversion 0
License:        BSD-3-Clause
URL:            %forgeurl
Source0:        %{forgeurl}archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  python3
BuildRequires:  uthash-devel
# /oreon:deps
%description
Yaksa is a high-performance noncontiguous datatype engine that can be used to
express and manipulate noncontiguous data. The library sports features related
to packing/unpacking, I/O vectors, and flattening noncontiguous datatypes.

%package devel
Summary:        Development files for libyaksa
Requires:       %{name}%{_isa} = %{version}-%{release}
%description devel
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

# Poor man's unbundling: uthash is a header-only library, so we can
# effectively replace the local version with the system copy by symlinking.
ln -fvs /usr/include/uthash.h src/external/yuthash.h
ln -fvs /usr/include/utlist.h src/external/yutlist.h

%build

./autogen.sh
%configure \
    --disable-static
%make_build
%install
%make_install
rm %{buildroot}%{_libdir}/libyaksa.la
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with tests}
%check

timeout -v 2h make -j%{_smp_build_ncpus} testing
%endif
%files -f %{oreon_filedir}/main.list
%files -n yaksa-devel -f %{oreon_filedir}/yaksa-devel.list

%changelog

%autochangelog
