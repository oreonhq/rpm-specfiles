%global source0_hash 179695deb91939eda0f5a4010ae854adea783b689da5590056da05ceeabdaf64

Name: gretl	
Version: 2026a
Release: 1%{?dist}
Summary: A tool for econometric analysis

%if 0%{?fedora} >= 33
%bcond_without flexiblas
%endif

# Automatically converted from old format: GPLv3+ and BSD and MIT - review is highly recommended.
License: GPL-3.0-or-later AND LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT
URL: http://gretl.sourceforge.net/
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
#Licensing of plugins used in gretl
Source1: gretl_plugins.txt
%if 0%{?fedora} >= 40
ExcludeArch: %{ix86}
%endif

BuildRequires:	bash-completion
%if %{with flexiblas}
BuildRequires:	flexiblas-devel
%else
BuildRequires:	blas-devel, lapack-devel
%endif
BuildRequires:	desktop-file-utils
BuildRequires:	fftw-devel
BuildRequires:	gcc-c++
BuildRequires:	gettext
BuildRequires:	glib2-devel
BuildRequires:	gmp-devel
BuildRequires:	gnuplot
BuildRequires:	gtk3-devel
BuildRequires:	gtksourceview3-devel
BuildRequires:	json-glib-devel
BuildRequires:	libcurl-devel
BuildRequires:	libxml2-devel
BuildRequires:	libgnomeui-devel
BuildRequires:	mpfr-devel
BuildRequires:	ncurses-devel
BuildRequires:	openmpi-devel
BuildRequires:	readline-devel
BuildRequires:	xdg-utils
BuildRequires:	tex(latex)
BuildRequires:	texlive-multirow
BuildRequires:	texlive-rsfs
BuildRequires:	texlive-palatino
BuildRequires:	texlive-mathpazo

Requires: gnuplot
Requires: gtksourceview3
Requires: libcurl

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
# Require explicitly for dir ownership and to guarantee the pickup of the right runtime
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
# Build OpenMPI version
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

#Fix the openmpi binary
mkdir -p %{buildroot}%{_libdir}/openmpi/bin
mv %{buildroot}/%{_bindir}/gretlmpi %{buildroot}/%{_libdir}/openmpi/bin/gretl_openmpi

desktop-file-install						\
--remove-category="Application;Science;Econometrics" \
--add-category="Education;Science;Math;Economy;"  \
--dir=%{buildroot}%{_datadir}/applications     \
%{buildroot}/%{_datadir}/applications/gretl.desktop
%{_openmpi_unload}
%ldconfig_scriptlets

%files -f %{name}.lang
%{_bindir}/gretl
%{_bindir}/gretlcli
%{_bindir}/gretl_edit
%{_bindir}/gretl_x11
%{_libdir}/gretl-gtk3
%{_datadir}/%{name}/
%{_mandir}/man1/*.gz
%{_libdir}/libgretl-1.0.so.*
%{_datadir}/mime/packages/gretl.xml
%{_datadir}/icons/hicolor/32x32/apps/gretl.png
%{_datadir}/icons/hicolor/32x32/mimetypes/*.png
%{_datadir}/icons/hicolor/48x48/apps/gretl.png
%{_datadir}/icons/hicolor/64x64/apps/gretl.png
%{_datadir}/applications/gretl*
%{_datadir}/metainfo/gretl.appdata.xml

%doc ChangeLog CompatLog README gretl_plugins.txt

%files devel
%{_libdir}/pkgconfig/gretl.pc
%{_libdir}/libgretl*.so
%{_includedir}/%{name}/

%files openmpi 
%{_libdir}/openmpi/bin/gretl_openmpi

%changelog
%autochangelog
