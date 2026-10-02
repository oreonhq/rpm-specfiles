%global source0_hash 5a8395528b8f498205f3718f575228d0edaed7425fff638f87d1a6c3e0383636

%global pypi_name pytest_mock
%global package_name pytest-mock
%global file_name pytest_mock

Name:           python-%{package_name}
Version:        3.16.0
Release:        1%{?dist}
Summary:        Thin-wrapper around the mock package for easier use with py.test

License:        MIT
URL:            https://github.com/pytest-dev/pytest-mock/
Source0:        https://files.pythonhosted.org/packages/source/p/pytest_mock/pytest_mock-3.16.0.tar.gz

BuildArch:      noarch

%description
This plugin installs a mocker fixture which is a thin-wrapper around the
patching API provided by the mock package, but with the benefit of not having
to worry about undoing patches at the end of a test.

%package -n     python3-%{package_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  %py3_dist setuptools
BuildRequires:  %py3_dist pytest
BuildRequires:  %py3_dist setuptools_scm
%if %{undefined rhel}
BuildRequires:  %py3_dist pytest-asyncio
%endif

%description -n python3-%{package_name}
This plugin installs a mocker fixture which is a thin-wrapper around the
patching API provided by the mock package, but with the benefit of not having
to worry about undoing patches at the end of a test.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{file_name}-%{version} -p1
# Correct end of line encoding for README
sed -i 's/\r$//' README.rst

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{file_name}

%check
%pyproject_check_import

%pytest -v tests \
  -k "not test_standalone_mock and not test_detailed_introspection and not test_detailed_introspection \
  and not test_assert_called_args_with_introspection and not test_assert_called_kwargs_with_introspection \
  and not test_plain_stopall and not test_used_with_class_scope and not est_used_with_module_scope \
  and not test_used_with_package_scope and not test_used_with_session_scope \
  %{?rhel:and not test_instance_async_method_spy}"

%files -n python3-%{package_name} -f %{pyproject_files}
%doc CHANGELOG.rst README.rst
%license LICENSE

%changelog
%autochangelog
