%global source0_hash 7726b5a44555dbb9190fee15f21c21896f406063e657f17603f11543863ab35e
Name:           python-azure-ai-projects
Version:        2.6.1
Release:        1%{?dist}
Summary:        Microsoft Corporation Azure AI Projects Client Library for Python
License:        MIT
URL:            https://aka.ms/azsdk/azure-ai-projects-v2/python/code
Source0:        https://files.pythonhosted.org/packages/source/a/azure_ai_projects/azure_ai_projects-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0.3
Requires:       python3-azure-ai-projects = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-azure-ai-projects
Summary:        Microsoft Corporation Azure AI Projects Client Library for Python
# oreon:reqs
Requires:       python3dist(azure-core) >= 1.37.0
Requires:       python3dist(azure-identity) >= 1.15.0
Requires:       python3dist(azure-storage-blob) >= 12.15.0
Requires:       python3dist(isodate) >= 0.6.1
Requires:       python3dist(openai) >= 3.0.0
Requires:       python3dist(typing-extensions) >= 4.11
# /oreon:reqs
%description -n python3-azure-ai-projects

%prep
%global oreon_srcdir azure_ai_projects-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-azure-ai-projects usr/lib/python3*/site-packages/azure_ai_projects* usr/lib64/python3*/site-packages/azure_ai_projects* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/azure_ai_projects* usr/lib64/python3*/site-packages/azure_ai_projects* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-azure-ai-projects -f %{oreon_filedir}/python3-azure-ai-projects.list

%changelog

%autochangelog
