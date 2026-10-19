%global source0_hash c81831f43828dbc3987ee247eb198241a0152b8e7ceab10977cc3808eb388ac7
Name:           python-dependency-groups
Version:        1.3.2
Release:        1%{?dist}
Summary:        A tool for resolving PEP 735 Dependency Group data
License:        MIT
URL:            https://github.com/pypa/dependency-groups
Source0:        https://files.pythonhosted.org/packages/source/d/dependency_groups/dependency_groups-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) >= 3.11
Requires:       python3-dependency-groups = %{version}-%{release}
# /oreon:deps
%package -n       python3-dependency-groups+cli
Summary:        Metapackage for python3-dependency-groups cli extras
Requires:       python3-dependency-groups = %{version}-%{release}
Provides:       python3dist(dependency-groups[cli]) = %{version}-%{release}

%description -n python3-dependency-groups+cli
Metapackage for python3-dependency-groups cli extras.

%description

%package -n     python3-dependency-groups
Summary:        A tool for resolving PEP 735 Dependency Group data
%description -n python3-dependency-groups

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir dependency_groups-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-dependency-groups usr/lib/python3*/site-packages/dependency_groups* usr/lib64/python3*/site-packages/dependency_groups* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/dependency_groups* usr/lib64/python3*/site-packages/dependency_groups* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-dependency-groups -f %{oreon_filedir}/python3-dependency-groups.list

%changelog

%autochangelog
