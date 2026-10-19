%global source0_hash ce22bb851efd7494f08aad33b940803784434f6e77763d00679a0dc45fcf686a
Name:           python-datasets
Version:        5.0.1
Release:        1%{?dist}
Summary:        HuggingFace community-driven open-source library of datasets
License:        ...
URL:            https://github.com/huggingface/datasets
Source0:        https://files.pythonhosted.org/packages/source/d/datasets/datasets-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-datasets = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-datasets
Summary:        HuggingFace community-driven open-source library of datasets
%description -n python3-datasets

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir datasets-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-datasets usr/lib/python3*/site-packages/datasets* usr/lib64/python3*/site-packages/datasets* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/datasets* usr/lib64/python3*/site-packages/datasets* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-datasets -f %{oreon_filedir}/python3-datasets.list

%changelog

%autochangelog
