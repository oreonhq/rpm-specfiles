%global source0_hash 553867b135303dc4c25ab67c5f234d8e900a0e36e66e8484d99adc05fe1e8737
%bcond barcode 0%{?fedora}
Name:		mupdf
%global libname libmupdf
%global pypiname mupdf
Version:	1.27.2
%global somajor 27
%global sominor 2
%global soname %{somajor}.%{sominor}
%global pkgconfig %{_libdir}/pkgconfig
%global upversion %{version}
%global pyclang_version 21
Release:        1%{?dist}
Summary:        A lightweight PDF viewer and toolkit
License:	AGPL-3.0-or-later
URL:		http://mupdf.com/
Source0:        http://%{name}.com/downloads/archive/%{name}-%{version}-source.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}-gl.desktop
Patch:		0001-Bug-708990-Avoid-overflow-src_stride-calculation-in-.patch
Patch:		0001-Do-not-complain-to-your-friendly-local-distribution-.patch
Patch:		0001-setup.py-do-not-require-libclang-and-swig.patch
Patch:		0001-setup.py-do-not-bundle-c-and-c-libs-in-wheel.patch
Patch:		0001-pdf_choice_widget_options2-avoid-core-dump-with-_GLI.patch
Patch:		0001-do-not-use-CXXFLAGS-with-swig.patch
Patch:		0001-pdf_font-report-font-name-in-warning.patch
Patch:		0001-mupdfwrap_test-adjust-to-mupdf-1.27.x.patch
%if 0%{?fedora} >= 44 || 0%{?rhel} >= 11 || 0%{?oreon} >= 11
%else
%endif
%if %{with barcode}
%endif
Requires:	%{name}-libs%{_isa} = %{version}-%{release}
Provides:	bundled(lcms2-devel) = lcms2.16^65.gf75fad7
Provides:	bundled(mujs-devel) = 1.3.9-9.ge892c9f
Provides:	bundled(extract) = 10.05
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-mupdf = %{version}-%{release}
# /oreon:deps
%description
MuPDF is a lightweight PDF viewer and toolkit written in portable C.
The renderer in MuPDF is tailored for high quality anti-aliased
graphics. MuPDF renders text with metrics and spacing accurate to
within fractions of a pixel for the highest fidelity in reproducing
the look of a printed page on screen.
MuPDF has a small footprint. A binary that includes the standard
Roman fonts is only one megabyte. A build with full CJK support
(including an Asian font) is approximately seven megabytes.
MuPDF has support for all non-interactive PDF 1.7 features, and the
toolkit provides a simple API for accessing the internal structures of
the PDF document. Example code for navigating interactive links and
bookmarks, encrypting PDF files, extracting fonts, images, and
searchable text, and rendering pages to image files is provided.

%package devel
Summary:	C Development files for %{name}
Requires:	%{name}-libs%{_isa} = %{version}-%{release}
%description devel
The mupdf-devel package contains library and header files for developing
C applications that use the mupdf library.

%package libs
Summary:	C Library files for %{name}
%description libs
The mupdf-libs package contains the mupdf C library files.

%package cpp-devel
Summary:	C++ Development files for %{name}
Requires:	%{name}-cpp-libs%{_isa} = %{version}-%{release}
%description cpp-devel
The mupdf-cpp-devel package contains library and header files for developing
C++ applications that use the mupdf library.

%package cpp-libs
Summary:	C++ Library files for %{name}
Requires:	%{name}-libs%{_isa} = %{version}-%{release}
%description cpp-libs
The mupdf-cpp-libs package contains the mupdf C++ library files.

%package -n python3-%{pypiname}
Summary:	Python bindings for %{name}
Requires:	%{name}-libs%{_isa} = %{version}-%{release}
Requires:	%{name}-cpp-libs%{_isa} = %{version}-%{release}
%description -n python3-%{pypiname}
The python3-%{pypiname} package contains low level mupdf python bindings.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{upversion}-source
for d in $(ls thirdparty | grep -v -e extract -e lcms2 -e mujs)
do
	rm -rf thirdparty/$d
done
# avoid overwriting the proper README by the doc build instructions
rm -f docs/README

echo > user.make "\
	USE_SYSTEM_LIBS := yes
	USE_SYSTEM_MUJS := no # build needs source anyways
	USE_TESSERACT := yes
	VENV_FLAG :=
	barcode := %{?with_barcode:yes}%{!?with_barcode:no}
	build := release
	shared := yes
	verbose := yes
"

# c++ and python install targets rebuild unconditionally. Avoid multiple rebuilds:
sed -i -e '/^install-shared-c++:/s/ c++//' Makefile
sed -i -e '/^install-shared-python:/s/ python//' Makefile
# distribution builds are without experimental API:
sed -i -e '/DZXING_EXPERIMENTAL_API/ d' Makelists
%if %{without barcode}
# enforce same setting as above for py bindings:
sed -i -e 's/barcode=yes/barcode=no/' scripts/wrap/__main__.py
%endif

%build

export XCFLAGS="%{build_cflags} -fPIC -DJBIG_NO_MEMENTO -DTOFU -DTOFU_CJK_EXT"
export XCXXFLAGS="%{build_cxxflags} -fPIC -DJBIG_NO_MEMENTO -DTOFU -DTOFU_CJK_EXT"
export PYTHONPATH=$(find /usr/%{_lib}/llvm*/ -name site-packages | head -1)
make %{?_smp_mflags} shared c++
export MUPDF_SETUP_BUILD_DIR=build/shared-release%{?with_barcode:-barcode}
export MUPDF_SETUP_VERSION=%{version}
%pyproject_wheel
cat > mupdf.pc << EOF
prefix=%{_prefix}
exec_prefix=%{_exec_prefix}
libdir=%{_libdir}
includedir=%{_includedir}
Name: mupdf
Description: Library for rendering PDF documents
Requires.private: freetype2
Version: %{version}
Libs: -L${libdir} -lmupdf
Libs.private: -lmujs -lgumbo -lopenjp2 -ljbig2dec -ljpeg -lz -lm
Cflags: -I${includedir}
EOF
%install
make DESTDIR=%{buildroot} install install-shared-c install-shared-c++ prefix=%{_prefix} libdir=%{_libdir} pydir=%{python3_sitearch} SO_INSTALL_MODE=755
%pyproject_install
rm -rf %{buildroot}/%{_docdir}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE2}
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
install -p -m644 docs/logo/mupdf-logo.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/mupdf.svg
install -p -m644 docs/logo/mupdf-logo.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/mupdf-gl.svg
mkdir -p %{buildroot}/%{pkgconfig}
install -p -m 0644 mupdf.pc %{buildroot}/%{pkgconfig}
find %{buildroot}/%{_mandir} -type f -exec chmod 0644 {} \;
find %{buildroot}/%{_includedir} -type f -exec chmod 0644 {} \;
cd %{buildroot}/%{_bindir} && ln -s %{name}-x11 %{name}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/lib/python3*/site-packages/mupdf* usr/lib64/python3*/site-packages/mupdf* usr/bin/*

%check

LD_LIBRARY_PATH='%{buildroot}%{_libdir}' %{py3_test_envvars} %{python3} scripts/mupdfwrap_test.py thirdparty/lcms2/doc/*.pdf
%files
%files -n mupdf-devel -f %{oreon_filedir}/mupdf-devel.list
%files -n mupdf-libs -f %{oreon_filedir}/mupdf-libs.list
%files -n mupdf-cpp-devel -f %{oreon_filedir}/mupdf-cpp-devel.list
%files -n mupdf-cpp-libs -f %{oreon_filedir}/mupdf-cpp-libs.list
%files -n python3-mupdf -f %{oreon_filedir}/python3-mupdf.list

%changelog

%autochangelog

