%global source0_hash 493b156ba895c97602655b620a8456caa2ce08c1aa389f5a7addec065e6e855c
Name:           python-jsonschema-path
Version:        0.5.0
Release:        1%{?dist}
Summary:        JSONSchema Spec with object-oriented paths
License:        Apache-2.0
URL:            https://github.com/p1c2u/jsonschema-path
Source0:        https://files.pythonhosted.org/packages/source/j/jsonschema_path/jsonschema_path-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 1.0.0
Requires:       python3-jsonschema-path = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-jsonschema-path
Summary:        JSONSchema Spec with object-oriented paths
%description -n python3-jsonschema-path

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir jsonschema_path-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-jsonschema-path usr/lib/python3*/site-packages/jsonschema_path* usr/lib64/python3*/site-packages/jsonschema_path* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/jsonschema_path* usr/lib64/python3*/site-packages/jsonschema_path* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-jsonschema-path -f %{oreon_filedir}/python3-jsonschema-path.list

%changelog

%autochangelog
