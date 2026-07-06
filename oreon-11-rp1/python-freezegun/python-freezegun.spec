%global source0_hash ac7742a6cc6c25a2c35e9292dfd554b897b517d2dec26891a2e8debf205cb94a

%global modname freezegun
%global sum Let your Python tests travel through time

Name:               python-freezegun
Version:            1.5.5
Release:            %autorelease
Summary:            %{sum}

License:            Apache-2.0
URL:                https://pypi.io/project/freezegun
Source0:            https://files.pythonhosted.org/packages/source/f/%{modname}/%{modname}-%{version}.tar.gz

Patch:              freezegun-1.5.1-no-coverage.patch

BuildArch:          noarch

%description
freezegun is a library that allows your python tests to travel through time by
mocking the datetime module.


%package -n python3-freezegun
Summary:            %{sum}

BuildRequires:      python3-devel

%{?python_provide:%python_provide python3-freezegun}

Requires:           python3-dateutil >= 2.7
BuildRequires:      python3-dateutil >= 2.7

%description -n python3-freezegun
freezegun is a library that allows your python tests to travel through time by
mocking the datetime module. This is the Python 3 library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{modname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l freezegun

%check
# Ignore two tests that are broken when run on systems in certain timezones.
# Reported upstream: https://github.com/spulec/freezegun/issues/348
pytest-3 --deselect tests/test_datetimes.py::TestUnitTestMethodDecorator::test_method_decorator_works_on_unittest_kwarg_frozen_time \
         --deselect tests/test_datetimes.py::TestUnitTestMethodDecorator::test_method_decorator_works_on_unittest_kwarg_hello

%files -n python3-freezegun -f %{pyproject_files}
%doc README.rst LICENSE

%changelog
%autochangelog
