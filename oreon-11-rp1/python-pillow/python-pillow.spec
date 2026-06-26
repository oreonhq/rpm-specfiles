%global source0_hash d29fefc0ba637833b59cafc7649e1237186741c31b210178b0a4e9cd9e01ffdf

%global py3_incdir %(RPM_BUILD_ROOT= %{python3} -Ic 'import sysconfig; print(sysconfig.get_path("include"))')

%global srcname pillow

# Dependencies are missing to build the documentation
%bcond_with doc

%if 0%{?rhel} || 0%{?flatpak} || (0%{?oreon} >= 11)
%bcond_with mingw
%else
%bcond_without mingw
%endif
%if 0%{?rhel} || (0%{?oreon} >= 11)
%bcond_with qt
%else
%bcond_without qt
%endif

Name:           python-%{srcname}
Version:        12.1.1
Release:        2%{?dist}
Summary:        Python image processing library

# License: see http://www.pythonware.com/products/pil/license.htm
License:        MIT
URL:            http://python-pillow.github.io/
Source0:        https://github.com/python-pillow/Pillow/archive/refs/tags/%{version}.tar.gz#/Pillow-%{version}.tar.gz

# MinGW build fixes
Patch0:         pillow_mingw.patch

BuildRequires:  freetype-devel
BuildRequires:  gcc
BuildRequires:  ghostscript
BuildRequires:  lcms2-devel
BuildRequires:  libimagequant-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libraqm-devel
BuildRequires:  libtiff-devel
BuildRequires:  libwebp-devel
BuildRequires:  openjpeg2-devel
BuildRequires:  python3-pybind11
BuildRequires:  tk-devel
BuildRequires:  zlib-devel

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest

%if %{with doc}
BuildRequires:  make
BuildRequires:  python%{python3_pkgversion}-sphinx
BuildRequires:  python%{python3_pkgversion}-sphinx-copybutton
BuildRequires:  python%{python3_pkgversion}-sphinx_rtd_theme
BuildRequires:  python%{python3_pkgversion}-sphinx-removed-in
%endif


%if %{with mingw}
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-python3
BuildRequires:  mingw32-python3-setuptools
BuildRequires:  mingw32-dlfcn
BuildRequires:  mingw32-freetype
BuildRequires:  mingw32-lcms2
BuildRequires:  mingw32-libimagequant
BuildRequires:  mingw32-libjpeg
BuildRequires:  mingw32-libtiff
BuildRequires:  mingw32-libwebp
BuildRequires:  mingw32-openjpeg2
BuildRequires:  mingw32-tk
BuildRequires:  mingw32-zlib

BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-python3
BuildRequires:  mingw64-python3-setuptools
BuildRequires:  mingw64-dlfcn
BuildRequires:  mingw64-freetype
BuildRequires:  mingw64-lcms2
BuildRequires:  mingw64-libimagequant
BuildRequires:  mingw64-libjpeg
BuildRequires:  mingw64-libtiff
BuildRequires:  mingw64-libwebp
BuildRequires:  mingw64-openjpeg2
BuildRequires:  mingw64-tk
BuildRequires:  mingw64-zlib
%endif

# For EpsImagePlugin.py
Requires:       ghostscript

%global __provides_exclude_from ^%{python3_sitearch}/PIL/.*\\.so$

%description
Python image processing library, fork of the Python Imaging Library (PIL)

This library provides extensive file format support, an efficient
internal representation, and powerful image processing capabilities.

There are four subpackages: tk (tk interface), qt (PIL image wrapper for Qt),
devel (development) and doc (documentation).


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        Python 3 image processing library
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
Provides:       python%{python3_pkgversion}-imaging = %{version}-%{release}
# For MicImagePlugin.py, FpxImagePlugin.py
Requires:       python%{python3_pkgversion}-olefile

%description -n python%{python3_pkgversion}-%{srcname}
Python image processing library, fork of the Python Imaging Library (PIL)

This library provides extensive file format support, an efficient
internal representation, and powerful image processing capabilities.

There are four subpackages: tk (tk interface), qt (PIL image wrapper for Qt),
devel (development) and doc (documentation).


%package -n python%{python3_pkgversion}-%{srcname}-devel
Summary:        Development files for %{srcname}
Requires:       python%{python3_pkgversion}-devel, libjpeg-devel, zlib-devel
Requires:       python%{python3_pkgversion}-%{srcname}%{?_isa} = %{version}-%{release}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}-devel}
Provides:       python%{python3_pkgversion}-imaging-devel = %{version}-%{release}

%description -n python%{python3_pkgversion}-%{srcname}-devel
Development files for %{srcname}.


%package -n python%{python3_pkgversion}-%{srcname}-doc
Summary:        Documentation for %{srcname}
BuildArch:      noarch
Requires:       python%{python3_pkgversion}-%{srcname} = %{version}-%{release}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}-doc}
Provides:       python%{python3_pkgversion}-imaging-doc = %{version}-%{release}

%description -n python%{python3_pkgversion}-%{srcname}-doc
Documentation for %{srcname}.


%package -n python%{python3_pkgversion}-%{srcname}-tk
Summary:        Tk interface for %{srcname}
Requires:       python%{python3_pkgversion}-tkinter
Requires:       python%{python3_pkgversion}-%{srcname}%{?_isa} = %{version}-%{release}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}-tk}
Provides:       python%{python3_pkgversion}-imaging-tk = %{version}-%{release}

%description -n python%{python3_pkgversion}-%{srcname}-tk
Tk interface for %{srcname}.


%if %{with qt}
%package -n python%{python3_pkgversion}-%{srcname}-qt
Summary:        Qt %{srcname} image wrapper
Requires:       python%{python3_pkgversion}-qt5
Requires:       python%{python3_pkgversion}-%{srcname}%{?_isa} = %{version}-%{release}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}-qt}
Provides:       python%{python3_pkgversion}-imaging-qt = %{version}-%{release}

%description -n python%{python3_pkgversion}-%{srcname}-qt
Qt %{srcname} image wrapper.
%endif


%if %{with mingw}
%package -n mingw32-python3-%{srcname}
Summary:       MinGW Windows Python2 %{srcname} library
BuildArch:     noarch

%description -n mingw32-python3-%{srcname}
MinGW Windows Python2 %{srcname} library.


%package -n mingw64-python3-%{srcname}
Summary:       MinGW Windows Python2 %{srcname} library
BuildArch:     noarch

%description -n mingw64-python3-%{srcname}
MinGW Windows Python2 %{srcname} library.


%{?mingw_debug_package}
%endif


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n Pillow-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
# Native build
%pyproject_wheel

# MinGW build
%if %{with mingw}
PKG_CONFIG=mingw32-pkg-config %{mingw32_py3_build}
PKG_CONFIG=mingw64-pkg-config %{mingw64_py3_build}
%endif

# Doc build
%if %{with doc}
PYTHONPATH=$(echo $PWD/build/lib.linux-*) make -C docs html BUILDDIR=_build_py3 SPHINXBUILD=sphinx-build-%python3_version
rm -f docs/_build_py3/html/.buildinfo
%endif


%install
# Native build
%pyproject_install
install -d %{buildroot}/%{py3_incdir}/Imaging
install -m 644 src/libImaging/*.h %{buildroot}/%{py3_incdir}/Imaging

# MinGW build
%if %{with mingw}
(
%{mingw32_py3_install}
%{mingw64_py3_install}

install -d %{buildroot}/%{mingw32_py3_incdir}/Imaging
install -m 644 src/libImaging/*.h %{buildroot}/%{mingw32_py3_incdir}/Imaging

install -d %{buildroot}/%{mingw64_py3_incdir}/Imaging
install -m 644 src/libImaging/*.h %{buildroot}/%{mingw64_py3_incdir}/Imaging

# Remove sample scripts
rm -rf %{buildroot}%{mingw32_bindir}
rm -rf %{buildroot}%{mingw64_bindir}
)
%endif


%if %{with mingw}
%mingw_debug_install_post
%endif


%check
# Check Python 3 modules
ln -s $PWD/Images $(echo $PWD/build/lib.linux-*)/Images
cp -R $PWD/Tests $(echo $PWD/build/lib.linux-*)/Tests
cp -a $PWD/selftest.py $(echo $PWD/build/lib.linux-*)/selftest.py
pushd build/lib.linux-*
PYTHONPATH=$PWD %{__python3} selftest.py
popd
%ifnarch s390x
%pytest -v -k "not test_qt_image_qapplication" || :
%else
%pytest -v -k "not test_qt_image_qapplication" || :
%endif


%files -n python%{python3_pkgversion}-%{srcname}
%doc README.md CHANGES.rst
%license docs/COPYING
%{python3_sitearch}/PIL/
%{python3_sitearch}/pillow-%{version}.dist-info/
# These are in subpackages
%exclude %{python3_sitearch}/PIL/_imagingtk*
%exclude %{python3_sitearch}/PIL/ImageTk*
%exclude %{python3_sitearch}/PIL/SpiderImagePlugin*
%exclude %{python3_sitearch}/PIL/ImageQt*
%exclude %{python3_sitearch}/PIL/__pycache__/ImageTk*
%exclude %{python3_sitearch}/PIL/__pycache__/SpiderImagePlugin*
%exclude %{python3_sitearch}/PIL/__pycache__/ImageQt*

%files -n python%{python3_pkgversion}-%{srcname}-devel
%{py3_incdir}/Imaging/

%if %{with doc}
%files -n python%{python3_pkgversion}-%{srcname}-doc
%doc docs/_build_py3/html
%endif

%files -n python%{python3_pkgversion}-%{srcname}-tk
%{python3_sitearch}/PIL/_imagingtk*
%{python3_sitearch}/PIL/ImageTk*
%{python3_sitearch}/PIL/SpiderImagePlugin*
%{python3_sitearch}/PIL/__pycache__/ImageTk*
%{python3_sitearch}/PIL/__pycache__/SpiderImagePlugin*

%if %{with qt}
%files -n python%{python3_pkgversion}-%{srcname}-qt
%{python3_sitearch}/PIL/ImageQt*
%{python3_sitearch}/PIL/__pycache__/ImageQt*
%endif

%if %{with mingw}
%files -n mingw32-python3-%{srcname}
%license docs/COPYING
%{mingw32_python3_sitearch}/PIL/
%{mingw32_python3_sitearch}/pillow-%{version}-py%{mingw32_python3_version}.egg-info/
%{mingw32_py3_incdir}/Imaging/

%files -n mingw64-python3-%{srcname}
%license docs/COPYING
%{mingw64_python3_sitearch}/PIL/
%{mingw64_python3_sitearch}/pillow-%{version}-py%{mingw64_python3_version}.egg-info/
%{mingw64_py3_incdir}/Imaging/
%endif


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 12.1.1-1
- Prepare for Oreon 11 (RP1)
