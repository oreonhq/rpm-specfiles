%global source0_hash ed900c2b631aa3a112811139fa97b8d2c3bad5e989656bba4b7e52c7852c18c1
Name:           python-traitlets
Version:        5.16.1
Release:        1%{?dist}
Summary:        Traitlets Python configuration system
License:        ...
URL:            https://github.com/ipython/traitlets
Source0:        https://files.pythonhosted.org/packages/source/t/traitlets/traitlets-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) >= 1.5
Requires:       python3-traitlets = %{version}-%{release}
# /oreon:deps
%package -n       python3-traitlets+test
Summary:        Metapackage for python3-traitlets test extras
Requires:       python3-traitlets = %{version}-%{release}
Requires:       python3dist(argcomplete) >= 3.0.3
Requires:       python3dist(argcomplete) >= 3.5.2
Requires:       python3dist(mypy) >= 2.0
Requires:       python3dist(pytest) >= 7.0
Requires:       python3dist(pytest) < 10.0
Provides:       python3dist(traitlets[test]) = %{version}-%{release}

%description -n python3-traitlets+test
Metapackage for python3-traitlets test extras.

%package -n       python3-traitlets+docs
Summary:        Metapackage for python3-traitlets docs extras
Requires:       python3-traitlets = %{version}-%{release}
Provides:       python3dist(traitlets[docs]) = %{version}-%{release}

%description -n python3-traitlets+docs
Metapackage for python3-traitlets docs extras.

%description

%package -n     python3-traitlets
Summary:        Traitlets Python configuration system
%description -n python3-traitlets

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir traitlets-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-traitlets usr/lib/python3*/site-packages/traitlets* usr/lib64/python3*/site-packages/traitlets* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/traitlets* usr/lib64/python3*/site-packages/traitlets* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-traitlets -f %{oreon_filedir}/python3-traitlets.list

%changelog

%autochangelog
