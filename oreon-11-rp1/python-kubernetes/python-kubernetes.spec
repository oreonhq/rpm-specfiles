%global source0_hash 36993ed25ce59b789c9341473a228fcf268504a2fec7c2b2b1531d73072e5ce7
Name:           python-kubernetes
Version:        36.0.3
Release:        1%{?dist}
Summary:        Kubernetes python client
License:        ...
URL:            https://github.com/kubernetes-client/python
Source0:        https://files.pythonhosted.org/packages/source/k/kubernetes/kubernetes-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-kubernetes = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-kubernetes
Summary:        Kubernetes python client
%description -n python3-kubernetes

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir kubernetes-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-kubernetes usr/lib/python3*/site-packages/kubernetes* usr/lib64/python3*/site-packages/kubernetes* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/kubernetes* usr/lib64/python3*/site-packages/kubernetes* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-kubernetes -f %{oreon_filedir}/python3-kubernetes.list

%changelog

%autochangelog

