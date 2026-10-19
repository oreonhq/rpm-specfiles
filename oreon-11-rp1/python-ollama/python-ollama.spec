%global source0_hash 936d55daa684f474364c098611c933626f8d6c7d67065c5b7ae0c477b508b07f
Name:           python-ollama
Version:        0.6.2
Release:        1%{?dist}
Summary:        The official Python client for Ollama.
License:        MIT
URL:            https://ollama.com
Source0:        https://files.pythonhosted.org/packages/source/o/ollama/ollama-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-ollama = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-ollama
Summary:        The official Python client for Ollama.
# oreon:reqs
Requires:       python3dist(httpx) >= 0.27
Requires:       python3dist(pydantic) >= 2.9
# /oreon:reqs
%description -n python3-ollama

%prep
%global oreon_srcdir ollama-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-ollama usr/lib/python3*/site-packages/ollama* usr/lib64/python3*/site-packages/ollama* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/ollama* usr/lib64/python3*/site-packages/ollama* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-ollama -f %{oreon_filedir}/python3-ollama.list

%changelog

%autochangelog
