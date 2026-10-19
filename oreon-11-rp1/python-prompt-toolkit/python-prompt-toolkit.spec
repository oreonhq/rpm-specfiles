%global source0_hash 9ec8a0ad96d5c56148b3f914aa79c1564c3fde5d2e6b876e7bc327e353cf8fa6
Name:           python-prompt-toolkit
Version:        3.0.53
Release:        1%{?dist}
Summary:        Library for building powerful interactive command lines in Python
License:        ...
URL:            https://github.com/prompt-toolkit/python-prompt-toolkit
Source0:        https://files.pythonhosted.org/packages/source/p/prompt_toolkit/prompt_toolkit-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 68
Requires:       python3-prompt-toolkit = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-prompt-toolkit
Summary:        Library for building powerful interactive command lines in Python
# oreon:reqs
Requires:       python3dist(wcwidth) >= 0.1.4
# /oreon:reqs
%description -n python3-prompt-toolkit

%prep
%global oreon_srcdir prompt_toolkit-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-prompt-toolkit usr/lib/python3*/site-packages/prompt_toolkit* usr/lib64/python3*/site-packages/prompt_toolkit* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/prompt_toolkit* usr/lib64/python3*/site-packages/prompt_toolkit* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-prompt-toolkit -f %{oreon_filedir}/python3-prompt-toolkit.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.0.52-1
- Prepare for Oreon 11 (RP1)
