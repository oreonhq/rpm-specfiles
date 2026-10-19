%global source0_hash 3f106a9fbc73e39dd266c9712432087de78a6d644084c7c241d6a25c3169115b
Name:           python-textual
Version:        8.2.8
Release:        1%{?dist}
Summary:        Modern Text User Interface framework
License:        MIT
URL:            https://github.com/Textualize/textual
Source0:        https://files.pythonhosted.org/packages/source/t/textual/textual-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 1.2.0
Requires:       python3-textual = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-textual
Summary:        Modern Text User Interface framework
%description -n python3-textual

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir textual-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-textual usr/lib/python3*/site-packages/textual* usr/lib64/python3*/site-packages/textual* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/textual* usr/lib64/python3*/site-packages/textual* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-textual -f %{oreon_filedir}/python3-textual.list

%changelog

%autochangelog
