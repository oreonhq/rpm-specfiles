%global source0_hash 4178c7d349960efc8f6254ce4c12ebceaaa9f238d59c1701661e1d908e766381
%bcond network_tests 0
Name:           fastapi-new
Version:        0.0.7
Release:        1%{?dist}
Summary:        Create a new FastAPI project in one command
License:        MIT
URL:            https://github.com/fastapi/fastapi-new
Source0:        https://github.com/fastapi/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source10:       fastapi-new.1
Patch:          0001-Downstream-only-patch-out-coverage-from-script-test.patch
BuildArch:      noarch
%py_provides python3-fastapi-new
Requires:       uv
%global common_description %{expand:
Create a new FastAPI project in one command. ✨}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-fastapi-new = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%install
%pyproject_install
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 '%{SOURCE10}'
install -d \
    '%{buildroot}%{bash_completions_dir}' \
    '%{buildroot}%{zsh_completions_dir}' \
    '%{buildroot}%{fish_completions_dir}'
export PYTHONPATH='%{buildroot}%{python3_sitelib}'
export _TYPER_COMPLETE_TEST_DISABLE_SHELL_DETECTION=1
'%{buildroot}%{_bindir}/fastapi-new' --show-completion bash \
    > '%{buildroot}%{bash_completions_dir}/fastapi-new'
'%{buildroot}%{_bindir}/fastapi-new' --show-completion zsh \
    > '%{buildroot}%{zsh_completions_dir}/_fastapi-new'
'%{buildroot}%{_bindir}/fastapi-new' --show-completion fish \
    > '%{buildroot}%{fish_completions_dir}/fastapi-new.fish'
%oreon_autofiles main

%prep
%oreon_prep
%build

%pyproject_wheel
%check

%if %{without network_tests}
k="${k-}${k+ and }not test_creates_project_successfully"
k="${k-}${k+ and }not test_creates_project_with_python_version"
k="${k-}${k+ and }not test_validates_template_file_contents"
k="${k-}${k+ and }not test_initializes_in_current_directory"
k="${k-}${k+ and }not test_passes_single_digit_python_version_to_uv"
k="${k-}${k+ and }not test_creates_project_without_python_flag"
k="${k-}${k+ and }not test_file_write_failure"
%endif
%pytest -k "${k-}" -v
%files

%changelog

%autochangelog
