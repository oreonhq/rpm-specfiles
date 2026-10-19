%global source0_hash 3dfabe9a8d0155f142467be6f549b972b34c19e9b100d5984883d4704d5ec871
Name:           python-promptml
Version:        0.7.1
Release:        1%{?dist}
Summary:        A simple markup language for defining AI Prompts as Code (APaC)
License:        MIT
URL:            https://github.com/narenaryan/promptml/
Source0:        https://files.pythonhosted.org/packages/source/p/promptml/promptml-%{version}.tar.gz
Patch1:         soften-requirements.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-promptml = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-promptml
Summary:        A simple markup language for defining AI Prompts as Code (APaC)
# oreon:reqs
Requires:       python3dist(lark) == 1.1.9
Requires:       python3dist(pyyaml) == 6.0.1
# /oreon:reqs
%description -n python3-promptml

%prep
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-promptml usr/lib/python3*/site-packages/promptml* usr/lib64/python3*/site-packages/promptml* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/promptml* usr/lib64/python3*/site-packages/promptml* usr/bin/*

%check

%{py3_test_envvars} %{python3} -m unittest
%files
%files -n python3-promptml -f %{oreon_filedir}/python3-promptml.list

%changelog

%autochangelog
