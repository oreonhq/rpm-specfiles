%global source0_hash 6e8e2887b607ebcf66f1503f3b87551c761dd45f4a0054002cedf0f8e6736395
%global modname traitsui 
Name:           python-%{modname}
Version:        8.0.0
Release:        1%{?dist}
Summary:        User interface tools designed to complement Traits
License:        BSD-3-clause AND EPL-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-only
URL:            https://github.com/enthought/traitsui
Source0:        https://github.com/enthought/traitsui/archive/%{version}/traitsui-%{version}.tar.gz
Patch0:         python-traitsui-pyqt6.patch
Obsoletes:      %{name}-doc <= 5.0.0-2
BuildArch:      noarch
ExcludeArch:    ppc64le
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61
Requires:       python3-traitsui = %{version}-%{release}
# /oreon:deps
%package -n       python3-traitsui+docs
Summary:        Metapackage for python3-traitsui docs extras
Requires:       python3-traitsui = %{version}-%{release}
Provides:       python3dist(traitsui[docs]) = %{version}-%{release}

%description -n python3-traitsui+docs
Metapackage for python3-traitsui docs extras.

%package -n       python3-traitsui+editors
Summary:        Metapackage for python3-traitsui editors extras
Requires:       python3-traitsui = %{version}-%{release}
Provides:       python3dist(traitsui[editors]) = %{version}-%{release}

%description -n python3-traitsui+editors
Metapackage for python3-traitsui editors extras.

%package -n       python3-traitsui+examples
Summary:        Metapackage for python3-traitsui examples extras
Requires:       python3-traitsui = %{version}-%{release}
Provides:       python3dist(traitsui[examples]) = %{version}-%{release}

%description -n python3-traitsui+examples
Metapackage for python3-traitsui examples extras.

%package -n       python3-traitsui+pyqt5
Summary:        Metapackage for python3-traitsui pyqt5 extras
Requires:       python3-traitsui = %{version}-%{release}
Provides:       python3dist(traitsui[pyqt5]) = %{version}-%{release}

%description -n python3-traitsui+pyqt5
Metapackage for python3-traitsui pyqt5 extras.

%package -n       python3-traitsui+pyqt6
Summary:        Metapackage for python3-traitsui pyqt6 extras
Requires:       python3-traitsui = %{version}-%{release}
Provides:       python3dist(traitsui[pyqt6]) = %{version}-%{release}

%description -n python3-traitsui+pyqt6
Metapackage for python3-traitsui pyqt6 extras.

%package -n       python3-traitsui+pyside2
Summary:        Metapackage for python3-traitsui pyside2 extras
Requires:       python3-traitsui = %{version}-%{release}
Provides:       python3dist(traitsui[pyside2]) = %{version}-%{release}

%description -n python3-traitsui+pyside2
Metapackage for python3-traitsui pyside2 extras.

%package -n       python3-traitsui+pyside6
Summary:        Metapackage for python3-traitsui pyside6 extras
Requires:       python3-traitsui = %{version}-%{release}
Provides:       python3dist(traitsui[pyside6]) = %{version}-%{release}

%description -n python3-traitsui+pyside6
Metapackage for python3-traitsui pyside6 extras.

%package -n       python3-traitsui+test
Summary:        Metapackage for python3-traitsui test extras
Requires:       python3-traitsui = %{version}-%{release}
Provides:       python3dist(traitsui[test]) = %{version}-%{release}

%description -n python3-traitsui+test
Metapackage for python3-traitsui test extras.

%package -n       python3-traitsui+wx
Summary:        Metapackage for python3-traitsui wx extras
Requires:       python3-traitsui = %{version}-%{release}
Requires:       python3dist(wxpython) >= 4
Provides:       python3dist(traitsui[wx]) = %{version}-%{release}

%description -n python3-traitsui+wx
Metapackage for python3-traitsui wx extras.

%description
The TraitsUI package is a set of user interface tools designed to complement
Traits. In the simplest case, it can automatically generate a user interface
for editing a Traits-based object, with no additional coding on the part of
the programmer-user. In more sophisticated uses, it can implement a Model-
View-Controller (MVC) design pattern for Traits-based objects.

%package -n python%{python3_pkgversion}-%{modname}
Summary:        User interface tools designed to complement Traits
%{?python_provide:%python_provide python%{python3_pkgversion}-%{modname}}
BuildRequires:  dejavu-fonts-all
BuildRequires:  liberation-fonts
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-qt5
%description -n python%{python3_pkgversion}-%{modname}
The TraitsUI package is a set of user interface tools designed to complement
Traits. In the simplest case, it can automatically generate a user interface
for editing a Traits-based object, with no additional coding on the part of
the programmer-user. In more sophisticated uses, it can implement a Model-
View-Controller (MVC) design pattern for Traits-based objects.

Python 3 version.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{modname}-%{version}
rm examples/demo

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/traitsui* usr/lib64/python3*/site-packages/traitsui* usr/bin/*

%check

export LANG=en_US.UTF-8
export PYTHONPATH=%{buildroot}%{python3_sitelib}
export PYTHONUNBUFFERED=1
pushd build/lib/traitsui/tests/
status=0
for toolkit in null pyqt5 pyqt6 wx # pyside6
do
  fail=1
  export QT_API=$toolkit
  case $toolkit in
    null) export ETS_TOOLKIT="null"; unset QT_API; export EXCLUDE_TESTS="(wx|qt)"; fail=0;;
    pyside2) export ETS_TOOLKIT="qt"; export EXCLUDE_TESTS="wx";;
    pyside6) export ETS_TOOLKIT="qt"; export EXCLUDE_TESTS="wx";;
%ifarch s390x
    pyqt5) export ETS_TOOLKIT="qt"; export EXCLUDE_TESTS="wx"; fail=0;;
%else
    pyqt5) export ETS_TOOLKIT="qt"; export EXCLUDE_TESTS="wx";;
%endif
    pyqt6) export ETS_TOOLKIT="qt"; export EXCLUDE_TESTS="wx"; fail=0;;
    wx) export ETS_TOOLKIT="wx"; unset QT_API; export EXCLUDE_TESTS="qt"; fail=0;;
  esac
  xvfb-run %__python3 -s -X faulthandler -W default -m unittest discover -v traitsui || status=$(( $status + $fail ))
done
exit $status
popd
%files
%files -n python3-traitsui -f %{oreon_filedir}/python3-traitsui.list

%changelog

%autochangelog
