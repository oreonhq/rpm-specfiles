%global source0_hash 74d92c017e8beb41730a8be07c2c6e4ff6547660c84bf91f832d8f325dd0cf82

Summary:	A library for generating Enhanced Metafiles
Summary(pl):	Biblioteka do generowania plików w formacie Enhanced Metafile
Name:		libEMF
Version:	1.0.13
Release:	17%{?dist}
# include/libEMF/emf.h: LGPL-2.1-or-later
# libemf/libemf.{cpp,h}: LGPL-2.1-or-later
# src/printemf.c: GPL-2.0-or-later
License:	LGPL-2.1-or-later AND GPL-2.0-or-later
URL:		http://libemf.sourceforge.net/
Source0:        https://downloads.sourceforge.net/project/libemf/libemf/%{version}/libemf-%{version}.tar.gz
Patch:		add-riscv64-support.patch
BuildRequires:	gcc-c++
BuildRequires: make

%description
libEMF is a library for generating Enhanced Metafiles on systems which
don't natively support the ECMA-234 Graphics Device Interface
(GDI). The library is intended to be used as a driver for other
graphics programs such as Grace or gnuplot. Therefore, it implements a
very limited subset of the GDI.

%description -l pl
libEMF to biblioteka do generowania plików w formacie Enhanced
Metafile na systemach nie obsługujących natywnie systemu graficznego
ECMA-234 GDI. Biblioteka ma służyć jako sterownik dla innych programów
graficznych, takich jak Grace czy gnuplot. Z tego powodu ma
zaimplementowany bardzo ograniczony podzbiór GDI.

%package devel
Summary:	libEMF header files
Summary(pl):	Pliki nagłówkowe libEMF
Requires:	%{name}%{_isa} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
libEMF header files.

%description devel -l pl
Pliki nagłówkowe libEMF.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n libemf-%{version} -p1

%build
%configure \
	--disable-static \
	--enable-editing

%make_build

%install
export CPPROG="cp -p"
%make_install
rm %{buildroot}%{_libdir}/libEMF.la

%check
%make_build check

%files
%license COPYING COPYING.LIB
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/printemf
%{_libdir}/libEMF.so.1*

%files devel
%doc doc/html/*
%{_libdir}/libEMF.so
%{_includedir}/libEMF

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.13-17
- Prepare for Oreon 11 (RP1)
