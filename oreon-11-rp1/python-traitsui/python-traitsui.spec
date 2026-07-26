%global source0_hash 6e8e2887b607ebcf66f1503f3b87551c761dd45f4a0054002cedf0f8e6736395

%global modname traitsui 
Name:           python-%{modname}
Version:        8.0.0
Release:        12%{?dist}
Summary:        User interface tools designed to complement Traits

# Images have different licenses. For image license breakdown check
# image_LICENSE.txt file.
# All remaining source or image files are in BSD-3-clause license
License:        BSD-3-clause AND EPL-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-only
URL:            https://github.com/enthought/traitsui
Source0:        https://github.com/enthought/traitsui/archive/%{version}/traitsui-%{version}.tar.gz
# https://github.com/enthought/traitsui/pull/2028
Patch0:         python-traitsui-pyqt6.patch

Obsoletes:      %{name}-doc <= 5.0.0-2
BuildArch:      noarch
ExcludeArch:    ppc64le
BuildRequires:  /usr/bin/xvfb-run
BuildRequires:  mesa-dri-drivers

%description
The TraitsUI package is a set of user interface tools designed to complement
Traits. In the simplest case, it can automatically generate a user interface
for editing a Traits-based object, with no additional coding on the part of
the programmer-user. In more sophisticated uses, it can implement a Model-
View-Controller (MVC) design pattern for Traits-based objects.

%package -n python%{python3_pkgversion}-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{modname}}
BuildRequires:  dejavu-fonts-all
BuildRequires:  liberation-fonts
BuildRequires:  python%{python3_pkgversion}-devel
# pyproject install python3-pyqt5-base instead, this is needed for PyQt5.QtSvg
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

%generate_buildrequires
%pyproject_buildrequires -x pyqt5 -x pyqt6 -x test -x wx

%build
%pyproject_wheel

%install
%pyproject_install

%check
# Needed for wx tests
export LANG=en_US.UTF-8
export PYTHONPATH=%{buildroot}%{python3_sitelib}
export PYTHONUNBUFFERED=1
pushd build/lib/traitsui/tests/
status=0
# pyside6 is not packaged
for toolkit in null pyqt5 pyqt6 wx # pyside6
do
  # By default, fail build if tests fail
  fail=1
  # Decent default, overridded later if needed
  export QT_API=$toolkit
  case $toolkit in
    null) export ETS_TOOLKIT="null"; unset QT_API; export EXCLUDE_TESTS="(wx|qt)"; fail=0;;
    pyside2) export ETS_TOOLKIT="qt"; export EXCLUDE_TESTS="wx";;
    pyside6) export ETS_TOOLKIT="qt"; export EXCLUDE_TESTS="wx";;
    # pyqt5 test fails on s390x - https://github.com/enthought/traitsui/issues/2029
%ifarch s390x
    pyqt5) export ETS_TOOLKIT="qt"; export EXCLUDE_TESTS="wx"; fail=0;;
%else
    pyqt5) export ETS_TOOLKIT="qt"; export EXCLUDE_TESTS="wx";;
%endif
    # pyqt6 tests fail - https://github.com/enthought/traitsui/issues/2027
    # https://github.com/enthought/pyface/issues/1249
    pyqt6) export ETS_TOOLKIT="qt"; export EXCLUDE_TESTS="wx"; fail=0;;
    # wx currently failling - https://github.com/enthought/traitsui/issues/2030
    wx) export ETS_TOOLKIT="wx"; unset QT_API; export EXCLUDE_TESTS="qt"; fail=0;;
  esac
  # Adding -f can be helpful to debug missing components when tests segfault or similar
  xvfb-run %__python3 -s -X faulthandler -W default -m unittest discover -v traitsui || status=$(( $status + $fail ))
done
exit $status

popd

%files -n python%{python3_pkgversion}-%{modname}
%license LICENSE.txt image_LICENSE*.txt
%doc README.rst CHANGES.txt examples
%{python3_sitelib}/%{modname}*

%changelog
%autochangelog
