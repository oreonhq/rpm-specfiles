%global pypi_name pytest_mock
%global package_name pytest-mock
%global file_name pytest_mock

Name:           python-%{package_name}
Version:        3.15.1
Release:        2%{?dist}
Summary:        Thin-wrapper around the mock package for easier use with py.test

License:        MIT
URL:            https://github.com/pytest-dev/pytest-mock/
Source0:        https://files.pythonhosted.org/packages/source/p/pytest_mock/pytest_mock-3.15.1.tar.gz
# oreon url source checksums begin
%global source0_sha256 1849a238f6f396da19762269de72cb1814ab44416fa73a8686deac10b0d87a0f
%global source0_file pytest_mock-3.15.1.tar.gz
# oreon url source checksums end

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/pytest_mock-3.15.1.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "1849a238f6f396da19762269de72cb1814ab44416fa73a8686deac10b0d87a0f" || { echo "oreon: Source0 SHA256 mismatch for pytest_mock-3.15.1.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.15.1-2
- Prepare for Oreon 11 (RP1)
