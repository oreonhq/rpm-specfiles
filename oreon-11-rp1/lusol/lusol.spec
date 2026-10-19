%global source0_hash 1d4a51aa49871bc7f4f4eb9340a465ed16f2ccb059d2bf52564aa64a768f578a
%global upver 2016-01-26
%global commit  e35b66d23729936bd475b31d933feca2b0021a13
%global date    20221005
%global forgeurl https://github.com/nwh/lusol
Name:           lusol
Version:        %(sed 's/-//g' <<< %{upver})
Summary:        LU factors of a square or rectangular sparse matrix
%forgemeta
Release:        1%{?dist}
License:        BSD-3-Clause OR MIT
URL:            https://web.stanford.edu/group/SOL/software/lusol/
VCS:            git:%{forgeurl}.git
Source0:        %{forgeurl}/archive/%{commit}/%{name}-%{commit}.tar.gz
Patch:          0001-Add-missing-parameter-to-lu1rec-calls.patch
Patch:          0002-Give-zero-a-value-before-use-in-lu8mod.patch
Patch:          0003-Fix-race-when-building-src-lusol.o.patch
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gcc-gfortran
BuildRequires:  make
BuildRequires:  python3
# /oreon:deps
%description
LUSOL computes LU factors of a square or rectangular sparse matrix.

%package        devel
Summary:        Header files and library links for LUSOL
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gcc-gfortran%{?_isa}
%description    devel
Header files and library links for developing applications that use LUSOL.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

# Force generated files to be regenerated
rm src/clusol.{c,h}

%build

sed -e 's|\(CFLAGS := \).*|\1%{build_cflags}|' \
    -e 's|\(F77FLAGS := \).*|\1%{build_fflags} -fdefault-integer-8|' \
    -e 's|\(F90FLAGS := \).*|\1%{build_fflags} -Jsrc|' \
    -e 's|\(LDFLAGS := \)-m64 -shared|\1%{build_ldflags} -shared -Wl,-h,libclusol.so.0|' \
    -e 's| -Wl,-rpath,/usr/lib||' \
    -i makefile
%make_build
%install
mkdir -p %{buildroot}%{_libdir}
cp -p src/libclusol.so %{buildroot}%{_libdir}/libclusol.so.0.0.0
ln -s libclusol.so.0.0.0 %{buildroot}%{_libdir}/libclusol.so.0
ln -s libclusol.so.0 %{buildroot}%{_libdir}/libclusol.so
mkdir -p %{buildroot}%{_includedir}
cp -p src/clusol.h %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_fmoddir}
cp -p src/lusol*.mod %{buildroot}%{_fmoddir}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n lusol-devel -f %{oreon_filedir}/lusol-devel.list

%changelog

%autochangelog
