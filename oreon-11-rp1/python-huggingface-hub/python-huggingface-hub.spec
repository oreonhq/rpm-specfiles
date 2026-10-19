%global source0_hash ed70a45498abe86039df7c2f4e5f7575de524be908d3840e8f828d5525eafd6a
Name:           python-huggingface-hub
Version:        1.32.0
Release:        1%{?dist}
Summary:        Client library to download and publish models, datasets and other repos on the huggingface.co hub
License:        Apache-2.0
URL:            https://github.com/huggingface/huggingface_hub
Source0:        https://files.pythonhosted.org/packages/source/h/huggingface_hub/huggingface_hub-%{version}.tar.gz
BuildArch:      noarch
Patch:          %{url}/pull/3797.patch
Patch:          %{url}/pull/3798.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-huggingface-hub = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-huggingface-hub
Summary:        Client library to download and publish models, datasets and other repos on the huggingface.co hub
%description -n python3-huggingface-hub

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir huggingface_hub-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-huggingface-hub usr/lib/python3*/site-packages/huggingface_hub* usr/lib64/python3*/site-packages/huggingface_hub* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/huggingface_hub* usr/lib64/python3*/site-packages/huggingface_hub* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-huggingface-hub -f %{oreon_filedir}/python3-huggingface-hub.list

%changelog

%autochangelog
