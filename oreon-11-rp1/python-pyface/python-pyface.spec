%global source0_hash e34f8fb285517e25bfe41a4b8d1d54860d2636bd5fa5b9bff26ab96c1a098895
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%bcond_with bootstrap
%global modname pyface
Name:           python-%{modname}
Version:        8.0.0
Release:        1%{?dist}
Summary:        Generic User Interface objects
License:        BSD-3-Clause AND EPL-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-or-later and LicenseRef-Fedora-Public-Domain
URL:            https://github.com/enthought/pyface
Source0:        https://github.com/enthought/pyface/archive/%{version}/pyface-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61
Requires:       python3-pyface = %{version}-%{release}
# /oreon:deps
%package -n       python3-pyface+docs
Summary:        Metapackage for python3-pyface docs extras
Requires:       python3-pyface = %{version}-%{release}
Provides:       python3dist(pyface[docs]) = %{version}-%{release}

%description -n python3-pyface+docs
Metapackage for python3-pyface docs extras.

%package -n       python3-pyface+examples
Summary:        Metapackage for python3-pyface examples extras
Requires:       python3-pyface = %{version}-%{release}
Provides:       python3dist(pyface[examples]) = %{version}-%{release}

%description -n python3-pyface+examples
Metapackage for python3-pyface examples extras.

%package -n       python3-pyface+pillow
Summary:        Metapackage for python3-pyface pillow extras
Requires:       python3-pyface = %{version}-%{release}
Provides:       python3dist(pyface[pillow]) = %{version}-%{release}

%description -n python3-pyface+pillow
Metapackage for python3-pyface pillow extras.

%package -n       python3-pyface+pyqt5
Summary:        Metapackage for python3-pyface pyqt5 extras
Requires:       python3-pyface = %{version}-%{release}
Provides:       python3dist(pyface[pyqt5]) = %{version}-%{release}

%description -n python3-pyface+pyqt5
Metapackage for python3-pyface pyqt5 extras.

%package -n       python3-pyface+pyqt6
Summary:        Metapackage for python3-pyface pyqt6 extras
Requires:       python3-pyface = %{version}-%{release}
Provides:       python3dist(pyface[pyqt6]) = %{version}-%{release}

%description -n python3-pyface+pyqt6
Metapackage for python3-pyface pyqt6 extras.

%package -n       python3-pyface+pyside2
Summary:        Metapackage for python3-pyface pyside2 extras
Requires:       python3-pyface = %{version}-%{release}
Provides:       python3dist(pyface[pyside2]) = %{version}-%{release}

%description -n python3-pyface+pyside2
Metapackage for python3-pyface pyside2 extras.

%package -n       python3-pyface+pyside6
Summary:        Metapackage for python3-pyface pyside6 extras
Requires:       python3-pyface = %{version}-%{release}
Provides:       python3dist(pyface[pyside6]) = %{version}-%{release}

%description -n python3-pyface+pyside6
Metapackage for python3-pyface pyside6 extras.

%package -n       python3-pyface+numpy
Summary:        Metapackage for python3-pyface numpy extras
Requires:       python3-pyface = %{version}-%{release}
Provides:       python3dist(pyface[numpy]) = %{version}-%{release}

%description -n python3-pyface+numpy
Metapackage for python3-pyface numpy extras.

%package -n       python3-pyface+traitsui
Summary:        Metapackage for python3-pyface traitsui extras
Requires:       python3-pyface = %{version}-%{release}
Provides:       python3dist(pyface[traitsui]) = %{version}-%{release}

%description -n python3-pyface+traitsui
Metapackage for python3-pyface traitsui extras.

%package -n       python3-pyface+test
Summary:        Metapackage for python3-pyface test extras
Requires:       python3-pyface = %{version}-%{release}
Provides:       python3dist(pyface[test]) = %{version}-%{release}

%description -n python3-pyface+test
Metapackage for python3-pyface test extras.

%package -n       python3-pyface+wx
Summary:        Metapackage for python3-pyface wx extras
Requires:       python3-pyface = %{version}-%{release}
Requires:       python3dist(wxpython) >= 4
Provides:       python3dist(pyface[wx]) = %{version}-%{release}

%description -n python3-pyface+wx
Metapackage for python3-pyface wx extras.

%description
Pyface enables programmers to interact with generic UI objects, such as
an "MDI Application Window", rather than with raw UI widgets. (Pyface is
named by analogy to JFace in Java.) Traits uses Pyface to implement
views and editors for displaying and editing Traits-based objects.

%package -n python%{python3_pkgversion}-%{modname}
Summary:        Generic User Interface objects
BuildRequires:  python%{python3_pkgversion}-devel >= 3.9
%description -n python%{python3_pkgversion}-%{modname}
Pyface enables programmers to interact with generic UI objects, such as
an "MDI Application Window", rather than with raw UI widgets. (Pyface is
named by analogy to JFace in Java.) Traits uses Pyface to implement
views and editors for displaying and editing Traits-based objects.

Python 3 version.

%package doc
Summary:        Documentation for pyface
%description doc
Documentation and examples for pyface.

%package -n python%{python3_pkgversion}-%{modname}-qt
Summary:        Qt backend placeholder for pyface
BuildRequires:  python%{python3_pkgversion}-pillow-qt
BuildRequires:  python%{python3_pkgversion}-pyqt6
Requires:       python%{python3_pkgversion}-%{modname} = %{version}-%{release}
%{?_sip_api:Requires: python3-pyqt5-sip-api(%{_sip_api_major}) >= %{_sip_api}}
Provides:       python%{python3_pkgversion}-%{modname}-backend
%description -n python%{python3_pkgversion}-%{modname}-qt
Qt backend placeholder for pyface.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n pyface-%{version}
# Tests in test_python_shell lead to core dump. We need pyface for bootstrap
# sequence of Python 3.10, thus they are temporarily disabled
# This can be removed once fixed.
# Downstream report: https://bugzilla.redhat.com/show_bug.cgi?id=1902175
rm pyface/tests/test_python_shell.py

%if %{with bootstrap}
# remove tests using traitsui
rm pyface/workbench/tests/test_workbench_window.py
rm pyface/dock/tests/test_dock_sizer.py
%endif

# file not utf-8
for f in image_LICENSE_{Eclipse,OOo}.txt
do
  iconv -f iso8859-1 -t utf-8 ${f} > ${f}.conv && mv -f ${f}.conv ${f}
done
# Use the standard lib function in 3.9+
find -name \*.py -exec sed -i -e s/importlib_resources/importlib.resources/g {} +
sed -i -e '/"importlib-[^"]*",/d' pyface/__init__.py
sed -i -e /importlib./d etstool.py

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/pyface* usr/lib64/python3*/site-packages/pyface* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export LANG=en_US.UTF-8
export PYTHONPATH=%{buildroot}%{python3_sitelib}
export PYTHONUNBUFFERED=1
mkdir -p test
cd test
status=0
for toolkit in null pyqt5 pyqt6 wx # pyside6
do
  fail=1
  export QT_API=$toolkit
  case $toolkit in
    pyside6) export ETS_TOOLKIT="qt"; export EXCLUDE_TESTS="wx";;
    pyqt5) export ETS_TOOLKIT="qt"; export EXCLUDE_TESTS="wx"; fail=0;;
    pyqt6) export ETS_TOOLKIT="qt"; export EXCLUDE_TESTS="wx"; fail=0;;
    wx) export ETS_TOOLKIT="wx"; unset QT_API; export EXCLUDE_TESTS="qt"; fail=0;;
    null) export ETS_TOOLKIT="null"; unset QT_API; export EXCLUDE_TESTS="(wx|qt)"; fail=0;;
  esac
  xvfb-run %{__python3} -Xfaulthandler -s -m unittest discover -v pyface || status=$(( $status + $fail ))
done
exit $status
%files
%files -n python3-pyface -f %{oreon_filedir}/python3-pyface.list
%files -n python-pyface-doc -f %{oreon_filedir}/python-pyface-doc.list
%files -n python3-pyface-qt -f %{oreon_filedir}/python3-pyface-qt.list

%changelog

%autochangelog
