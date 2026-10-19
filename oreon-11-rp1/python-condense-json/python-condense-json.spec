%global source0_hash c455b54bbbab89a69f598b09f2003a89b738df20d30e6aa341c495401ec5b349
Name:           python-condense-json
Version:        1.1
Release:        1%{?dist}
Summary:        Python function for condensing JSON using replacement strings
License:        Apache-2.0
URL:            https://github.com/simonw/condense-json
Source0:        https://files.pythonhosted.org/packages/source/c/condense_json/condense_json-%{version}.tar.gz
BuildArch:      noarch
Patch:          python-condense-json-0.1.3-toml.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
Requires:       python3-condense-json = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-condense-json
Summary:        Python function for condensing JSON using replacement strings
%description -n python3-condense-json

%prep
%global oreon_srcdir condense_json-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-condense-json usr/lib/python3*/site-packages/condense_json* usr/lib64/python3*/site-packages/condense_json* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/condense_json* usr/lib64/python3*/site-packages/condense_json* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-condense-json -f %{oreon_filedir}/python3-condense-json.list

%changelog

%autochangelog
