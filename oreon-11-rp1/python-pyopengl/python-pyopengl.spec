%global source0_hash 82751c83f0a6f732b8b5923990edc2441d38176a98756b1718e8d6c4379f5a71

%global srcname pyopengl

Name:           python-pyopengl
Version:        3.1.10
Release:        3%{?dist}
Summary:        Python bindings for OpenGL
License:        BSD-3-Clause and X11-distribute-modifications-variant
URL:            https://github.com/mcfletch/pyopengl
Source0:        %{pypi_source}
Source1:        %{pypi_source pyopengl_accelerate}

BuildRequires:  gcc
BuildRequires:  python3-devel

# For tests
BuildRequires:  freeglut
BuildRequires:  libglvnd-egl
BuildRequires:  libglvnd-gles
BuildRequires:  libglvnd-opengl
BuildRequires:  libXi
BuildRequires:  mesa-dri-drivers
BuildRequires:  mesa-libEGL
BuildRequires:  mesa-libGLU
BuildRequires:  python3-psutil
BuildRequires:  python3-pygame
BuildRequires:  python3-pytest
BuildRequires:  python3-xlib
BuildRequires:  xorg-x11-server-Xvfb

%description
PyOpenGL is the cross platform Python binding to OpenGL and related APIs. It
includes support for OpenGL v1.1, GLU, GLUT v3.7, GLE 3 and WGL 4. It also
includes support for dozens of extensions (where supported in the underlying
implementation).

PyOpenGL is inter-operable with a large number of external GUI libraries
for Python including (Tkinter, wxPython, FxPy, PyGame, and Qt). 

%package -n     python3-pyopengl
Summary:        Python 3 bindings for OpenGL
Requires:       freeglut
Requires:       libglvnd-opengl
Requires:       python3-numpy

%description -n python3-pyopengl
PyOpenGL is the cross platform Python binding to OpenGL and related APIs. It
includes support for OpenGL v1.1, GLU, GLUT v3.7, GLE 3 and WGL 4. It also
includes support for dozens of extensions (where supported in the underlying
implementation).

PyOpenGL is inter-operable with a large number of external GUI libraries
for Python including (Tkinter, wxPython, FxPy, PyGame, and Qt). 

%package -n     python3-pyopengl-tk
Summary:        %{srcname} Python 3.x Tk widget
BuildArch:      noarch
Requires:       python3-pyopengl = %{version}-%{release}
Requires:       python3-tkinter

%description -n python3-pyopengl-tk
%{srcname} Togl (Tk OpenGL widget) 1.6 support for Python 3.x.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -n %{srcname}-%{version} -T -a0 -a1

%generate_buildrequires
for dir in %{srcname}-%{version} %{srcname}_accelerate-%{version} ; do
    pushd $dir >&2
    %pyproject_buildrequires
    popd >&2
done

%build
# Delete all Cython generated .c files to force a rebuild in py3_build
# (py2_build then reuses the Cython output)
pushd %{srcname}_accelerate-%{version}/src
for f in *.pyx ; do
    rm -f "${f%.pyx}.c"
done
popd

for dir in %{srcname}-%{version} %{srcname}_accelerate-%{version} ; do
    pushd $dir
    %pyproject_wheel
    popd
done

%install
for dir in %{srcname}-%{version} %{srcname}_accelerate-%{version} ; do
    pushd $dir
    %pyproject_install
    popd
done

# Fix up perms on compiled object files
find %{buildroot}%{python3_sitearch}/OpenGL_accelerate/ -name *.so -exec chmod 755 '{}' \;

# Remove shebangs - note that weirdly these files have a space between
# the #! and the /, so this sed recipe is not the usual one
pushd %{buildroot}%{python3_sitelib}/OpenGL/arrays
sed -i -e '/^#! \//, 1d' buffers.py _buffers.py
popd

%check
%ifarch s390x
export PYTEST_ADDOPTS="-k 'not test_buffer_api_basic and not test_glCallLists_twice2 and not test_check_egl_es2 and not test_egl_ext_enumerate'"
%else
export PYTEST_ADDOPTS="-k 'not test_glCallLists_twice2 and not test_check_egl_es2 and not test_egl_ext_enumerate'"
%endif
PYTHONPATH=%{buildroot}%{python3_sitearch}:%{buildroot}%{python3_sitelib} \
  xvfb-run -a -s "-screen 0 1024x768x24 -ac +extension GLX +render -noreset" \
  pytest %{srcname}-%{version}/tests

%files -n python3-pyopengl
%license %{srcname}-%{version}/license.txt
%{python3_sitelib}/pyopengl-%{version}.dist-info
%{python3_sitelib}/OpenGL/
%exclude %{python3_sitelib}/OpenGL/Tk
%{python3_sitearch}/OpenGL_accelerate/
%{python3_sitearch}/pyopengl_accelerate-%{version}.dist-info/

%files -n python3-pyopengl-tk
%{python3_sitelib}/OpenGL/Tk

%changelog
%autochangelog
