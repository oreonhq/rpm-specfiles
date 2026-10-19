%global source0_hash fb57f4922da546067c8be542aafc5a26be77faf2668b40e651ee8c90b702563d
Name: gretl	
Version: 2026b
Release:        1%{?dist}
Summary:        A tool for econometric analysis
License: GPL-3.0-or-later AND LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT
URL: http://gretl.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
Source1: gretl_plugins.txt
%if %{with flexiblas}
%else
%endif
Requires: gnuplot
Requires: gtksourceview3
Requires: libcurl
# oreon:deps
BuildRequires:  bash-completion
BuildRequires:  desktop-file-utils
BuildRequires:  fftw-devel
BuildRequires:  flexiblas-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gmp-devel
BuildRequires:  gnuplot
BuildRequires:  gtk3-devel
BuildRequires:  gtksourceview3-devel
BuildRequires:  json-glib-devel
BuildRequires:  libcurl-devel
BuildRequires:  libgnomeui-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  mpfr-devel
BuildRequires:  ncurses-devel
BuildRequires:  openmpi-devel
BuildRequires:  readline-devel
BuildRequires:  tex(latex)
BuildRequires:  texlive-mathpazo
BuildRequires:  texlive-multirow
BuildRequires:  texlive-palatino
BuildRequires:  texlive-rsfs
BuildRequires:  xdg-utils
# /oreon:deps
%description
A cross-platform software package for econometric analysis, 
written in the C programming language.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig
%description devel
This package contains the development files for %{name}.

%package openmpi
Summary: Binary openmpi files for %{name}
BuildRequires: openmpi-devel
BuildRequires: make
Requires: openmpi
Requires: %{name} = %{version}-%{release}
%description openmpi
This package contains the binary openmpi files for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

CC=mpicc
CXX=mpic++
FC=mpifort

%if %{with flexiblas}
sed -i -e 's/-lblas/-lflexiblas/g' -e 's/-llapack/-lflexiblas/g' configure
%endif

%build

%{_openmpi_load}
%configure	--disable-static \
		--disable-avx \
		--with-mpi \
		--with-mpi-lib=%{_libdir}/openmpi/lib/ \
		--enable-build-editor \
		--enable-build-addons \
		--enable-addons-doc \
	--with-mpi-include=%{_includedir}/openmpi-%_arch/
make %{?_smp_mflags}
cp %{SOURCE1} %{_builddir}/%{name}-%{version}/gretl_plugins.txt
%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
%find_lang %{name}
rm -rf %{buildroot}/%{_libdir}/libgretl*.la
rm -rf %{buildroot}/%{_libdir}/gretl-gtk2/*.la
rm -rf %{buildroot}/%{_datadir}/%{name}/doc
rm -rf %{buildroot}/debug/usr/bin/*.debug
mkdir -p %{buildroot}%{_libdir}/openmpi/bin
mv %{buildroot}/%{_bindir}/gretlmpi %{buildroot}/%{_libdir}/openmpi/bin/gretl_openmpi
desktop-file-install						\
--remove-category="Application;Science;Econometrics" \
--add-category="Education;Science;Math;Economy;"  \
--dir=%{buildroot}%{_datadir}/applications     \
%{buildroot}/%{_datadir}/applications/gretl.desktop
%{_openmpi_unload}
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gretl-devel -f %{oreon_filedir}/gretl-devel.list
%files -n gretl-openmpi -f %{oreon_filedir}/gretl-openmpi.list

%changelog

%autochangelog
