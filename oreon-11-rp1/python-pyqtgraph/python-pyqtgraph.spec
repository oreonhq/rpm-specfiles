%global source0_hash 30f41a2f27ec41fb7d4442dbb150b004520ba83e777cdf5bb9cce0d18017424f

%global _python_bytecompile_extra 0
%global srcname pyqtgraph
%global py3_deps python3-PyQt5 python3-numpy python3-pyopengl
%bcond_without docs

Name:           python-pyqtgraph
Version:        0.14.0
Release:        2%{?dist}
Summary:        Scientific Graphics and GUI Library for Python
License:        MIT
URL:            https://www.pyqtgraph.org/
Source0:        https://github.com/pyqtgraph/pyqtgraph/archive/refs/tags/pyqtgraph-%{version}.tar.gz
Patch0:         drop-unpackaged-sphinx-extensions.patch

BuildArch:      noarch
BuildRequires:  python3-devel
# For Docs
%if %{with docs}
BuildRequires:  make %{py3_dist pydata-sphinx-theme sphinx sphinx_design}
BuildRequires:  %{py3_dist sphinx_rtd_theme}
BuildRequires:  %{py3_dist sphinx_autodoc_typehints}
%endif
# For Tests
BuildRequires:  %{py3_dist h5py pytest pytest-xvfb scipy six}
BuildRequires:  mesa-dri-drivers %{py3_deps}

%global _description %{expand:
PyQtGraph is a pure-python graphics and GUI library built on PyQt4 / PySide and
numpy. It is intended for use in mathematics / scientific /engineering
applications. Despite being written entirely in python, the library is very
fast due to its heavy leverage of numpy for number crunching and Qt\'s
GraphicsView framework for fast display.}

%description %_description

%package -n python3-pyqtgraph
Summary:        %{summary}
Requires:       %{py3_deps}

%description -n python3-pyqtgraph %_description

%if %{with docs}
%package doc
Summary:        Documentation for the pyqtgraph library

%description doc
This package provides documentation for the pyqtgraph library.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
%if %{with docs}
make -C doc html
%endif

%install
%pyproject_install
%pyproject_save_files -l pyqtgraph
rm -f doc/build/html/.buildinfo
rm -f doc/build/html/objects.inv

%check
# https://github.com/pyqtgraph/pyqtgraph/issues/1475 (test_reload)
# https://github.com/pyqtgraph/pyqtgraph/issues/2110 (test_PolyLineROI)
%pytest -k "not (test_reload or test_PolyLineROI)"

%files -n python3-pyqtgraph -f %{pyproject_files}
%doc CHANGELOG README.md

%if %{with docs}
%files doc
%doc doc/build/html
%endif

%changelog
%autochangelog
