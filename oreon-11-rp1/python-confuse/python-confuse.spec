%global source0_hash 8e7600c3261852122eb5f17b24b06ab8e5437b21d6224853c1420c38ac469d3c
Name:           python-confuse
Version:        2.2.1
Release:        1%{?dist}
Summary:        Painless YAML config files
License:        MIT
URL:            https://github.com/beetbox/confuse
Source0:        https://files.pythonhosted.org/packages/source/c/confuse/confuse-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-confuse = %{version}-%{release}
# /oreon:deps
%package -n       python3-confuse+docs
Summary:        Metapackage for python3-confuse docs extras
Requires:       python3-confuse = %{version}-%{release}
Requires:       python3dist(sphinx) >= 7.4.7
Requires:       python3dist(sphinx-rtd-theme) >= 3.0.2
Provides:       python3dist(confuse[docs]) = %{version}-%{release}

%description -n python3-confuse+docs
Metapackage for python3-confuse docs extras.

%description

%package -n     python3-confuse
Summary:        Painless YAML config files
# oreon:reqs
Requires:       python3dist(typing-extensions) >= 4.4
# /oreon:reqs
%description -n python3-confuse

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir confuse-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-confuse usr/lib/python3*/site-packages/confuse* usr/lib64/python3*/site-packages/confuse* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/confuse* usr/lib64/python3*/site-packages/confuse* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-confuse -f %{oreon_filedir}/python3-confuse.list

%changelog

%autochangelog
