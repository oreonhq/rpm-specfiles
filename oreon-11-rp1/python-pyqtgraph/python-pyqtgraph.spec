%global source0_hash 30f41a2f27ec41fb7d4442dbb150b004520ba83e777cdf5bb9cce0d18017424f
%global _python_bytecompile_extra 0
%global srcname pyqtgraph
%global py3_deps python3-PyQt5 python3-numpy python3-pyopengl
%bcond_without docs
Name:           python-pyqtgraph
Version:        0.14.0
Release:        1%{?dist}
Summary:        Scientific Graphics and GUI Library for Python
License:        MIT
URL:            https://www.pyqtgraph.org/
Source0:        https://github.com/pyqtgraph/pyqtgraph/archive/refs/tags/pyqtgraph-%{version}.tar.gz
Patch0:         drop-unpackaged-sphinx-extensions.patch
BuildArch:      noarch
%if %{with docs}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pyqtgraph = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-pyqtgraph
Summary:        Scientific Graphics and GUI Library for Python
Requires:       %{py3_deps}
%description -n python3-pyqtgraph

%if %{with docs}
%package doc
Summary:        Documentation for the pyqtgraph library
%description doc
This package provides documentation for the pyqtgraph library.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{srcname}-%{version}

%build

%pyproject_wheel
%if %{with docs}
make -C doc html
%endif
%install
%pyproject_install
rm -f doc/build/html/.buildinfo
rm -f doc/build/html/objects.inv
%oreon_autofiles python3-pyqtgraph usr/lib/python3*/site-packages/pyqtgraph* usr/lib64/python3*/site-packages/pyqtgraph* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyqtgraph* usr/lib64/python3*/site-packages/pyqtgraph* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pytest -k "not (test_reload or test_PolyLineROI)"
%files
%files -n python3-pyqtgraph -f %{oreon_filedir}/python3-pyqtgraph.list
%files -n python-pyqtgraph-doc -f %{oreon_filedir}/python-pyqtgraph-doc.list

%changelog

%autochangelog
