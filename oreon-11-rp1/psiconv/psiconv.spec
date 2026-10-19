%global source0_hash 1eee15b29ddcbfd2d15e0a0d26f59e28bac281c870b77418fa369dceed796806
Name:		psiconv
Version:	0.9.9
Release:        1%{?dist}
Summary:        A conversion utility for Psion files
License:	GPL-2.0-or-later
URL:		http://software.frodo.looijaard.name/psiconv/
Source0:        http://software.frodo.looijaard.name/psiconv/files/%{name}-%{version}.tar.gz
Patch0:	psiconv-0.9.8-gcc10.patch
Patch1: psiconv-checkuid-stdlib.h
Patch2: psiconv-configure-c99.patch
# oreon:deps
BuildRequires:  ImageMagick-devel
BuildRequires:  bc
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
%description
A conversion utility for the Psion files

%package devel
Summary:	Development files for psiconv
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description devel
Contains library and header files for psiconv

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

# assure use of system getopt
rm -f compat/getopt.{c,h}

%build

%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}
%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
mv $RPM_BUILD_ROOT%{_datadir}/%{name} _doc
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n psiconv-devel -f %{oreon_filedir}/psiconv-devel.list

%changelog

%autochangelog
