%global source0_hash 05662a657c86ece56e21d7804f2c217c82f4dc535c5ad1d61c03b1fe43b0c188
Summary:        A library for generating Enhanced Metafiles
Summary(pl):	Biblioteka do generowania plików w formacie Enhanced Metafile
Name:		libEMF
Version:	1.0.14
Release:        1%{?dist}
License:	LGPL-2.1-or-later AND GPL-2.0-or-later
URL:		http://libemf.sourceforge.net/
Source0:        https://downloads.sourceforge.net/project/libemf/libemf/%{version}/libemf-%{version}.tar.gz
Patch:		add-riscv64-support.patch
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
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
%global oreon_srcdir libemf-%{version}
%oreon_prep
%build

%configure \
	--disable-static \
	--enable-editing
%make_build
%install
export CPPROG="cp -p"
%make_install
rm %{buildroot}%{_libdir}/libEMF.la
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%make_build check
%files -f %{oreon_filedir}/main.list
%files -n libEMF-devel -f %{oreon_filedir}/libEMF-devel.list

%changelog

%autochangelog
