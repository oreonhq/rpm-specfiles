%global source0_hash 10f9fa0e57ebc995d0a39f88c9972238760ac6d86501062ae9eeee75ec838bba
Name:           python-llm-echo
Version:        0.4
Release:        1%{?dist}
Summary:        Debug plugin for LLM
License:        Apache-2.0
URL:            https://github.com/simonw/llm-echo
Source0:        https://files.pythonhosted.org/packages/source/l/llm_echo/llm_echo-%{version}.tar.gz
BuildArch:      noarch
Patch:          python-llm-0.3a3-format-fix.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-llm-echo = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-llm-echo
Summary:        Debug plugin for LLM
# oreon:reqs
Requires:       python3dist(llm) >= 0.26
# /oreon:reqs
%description -n python3-llm-echo

%prep
%global oreon_srcdir llm_echo-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-llm-echo usr/lib/python3*/site-packages/llm_echo* usr/lib64/python3*/site-packages/llm_echo* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/llm_echo* usr/lib64/python3*/site-packages/llm_echo* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-llm-echo -f %{oreon_filedir}/python3-llm-echo.list

%changelog

%autochangelog
