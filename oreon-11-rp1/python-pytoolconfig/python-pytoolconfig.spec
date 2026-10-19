%global source0_hash 51e6bd1a6f108238ae6aab6a65e5eed5e75d456be1c2bf29b04e5c1e7d7adbae
Name:           python-pytoolconfig
Version:        1.3.1
Release:        1%{?dist}
Summary:        Python tool configuration
License:        LGPL-3.0-or-later
URL:            https://github.com/bagel897/pytoolconfig
Source0:        https://files.pythonhosted.org/packages/source/p/pytoolconfig/pytoolconfig-%{version}.tar.gz
BuildArch:      noarch
%global common_description %{expand:
The goal of this project is to manage configuration for Python tools, such as
black and rope, and add support for a pyproject.toml configuration file.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(pdm-backend) >= 1.0.5
Requires:       python3-pytoolconfig = %{version}-%{release}
# /oreon:deps
%package -n       python3-pytoolconfig+validation
Summary:        Metapackage for python3-pytoolconfig validation extras
Requires:       python3-pytoolconfig = %{version}-%{release}
Requires:       python3dist(pydantic) >= 2.5.3
Provides:       python3dist(pytoolconfig[validation]) = %{version}-%{release}

%description -n python3-pytoolconfig+validation
Metapackage for python3-pytoolconfig validation extras.

%package -n       python3-pytoolconfig+global
Summary:        Metapackage for python3-pytoolconfig global extras
Requires:       python3-pytoolconfig = %{version}-%{release}
Requires:       python3dist(platformdirs) >= 3.11.0
Provides:       python3dist(pytoolconfig[global]) = %{version}-%{release}

%description -n python3-pytoolconfig+global
Metapackage for python3-pytoolconfig global extras.

%package -n       python3-pytoolconfig+doc
Summary:        Metapackage for python3-pytoolconfig doc extras
Requires:       python3-pytoolconfig = %{version}-%{release}
Requires:       python3dist(tabulate) >= 0.9.0
Requires:       python3dist(sphinx) >= 7.1.2
Provides:       python3dist(pytoolconfig[doc]) = %{version}-%{release}

%description -n python3-pytoolconfig+doc
Metapackage for python3-pytoolconfig doc extras.

%package -n       python3-pytoolconfig+gendocs
Summary:        Metapackage for python3-pytoolconfig gendocs extras
Requires:       python3-pytoolconfig = %{version}-%{release}
Requires:       python3dist(sphinx) >= 7.1.2
Requires:       python3dist(sphinx-autodoc-typehints) >= 1.25.2
Requires:       python3dist(sphinx-rtd-theme) >= 2.0.0
Provides:       python3dist(pytoolconfig[gendocs]) = %{version}-%{release}

%description -n python3-pytoolconfig+gendocs
Metapackage for python3-pytoolconfig gendocs extras.

%description %{common_description}

%package -n     python3-pytoolconfig
Summary:        Python tool configuration
# oreon:reqs
Requires:       python3dist(packaging) >= 23.2
Requires:       python3dist(tomli) >= 2.0.1
# /oreon:reqs
%description -n python3-pytoolconfig %{common_description}

# The doc extra is potentially useful for dependent packages; for example,
# rope[doc] depends on pytoolconfig[doc]. However, the gendoc extra appears to
# be solely for building the documentation of this package, so we do not build
# a corresponding metapackage, nor do we generate BR’s from it.

%prep
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pytoolconfig usr/lib/python3*/site-packages/pytoolconfig* usr/lib64/python3*/site-packages/pytoolconfig* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytoolconfig* usr/lib64/python3*/site-packages/pytoolconfig* usr/bin/*

%check

%pytest -v
%files
%files -n python3-pytoolconfig -f %{oreon_filedir}/python3-pytoolconfig.list

%changelog

%autochangelog
