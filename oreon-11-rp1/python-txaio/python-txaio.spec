%global source0_hash 3ee900b2331c93457530fddbccc1a320c4e2d7ac8f9073d01c3fbe87762ccb35
Name:           python-txaio
Version:        26.6.1
Release:        1%{?dist}
Summary:        Compatibility API between asyncio/Twisted/Trollius
License:        MIT
URL:            https://txaio.readthedocs.io/
Source0:        https://files.pythonhosted.org/packages/source/t/txaio/txaio-%{version}.tar.gz
BuildArch:      noarch
Patch0:         remove-unpackaged-sphinx-ext.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-txaio = %{version}-%{release}
# /oreon:deps
%package -n       python3-txaio+twisted
Summary:        Metapackage for python3-txaio twisted extras
Requires:       python3-txaio = %{version}-%{release}
Requires:       python3dist(zope.interface) >= 5.2.0
Requires:       python3dist(twisted) >= 22.10.0
Provides:       python3dist(txaio[twisted]) = %{version}-%{release}

%description -n python3-txaio+twisted
Metapackage for python3-txaio twisted extras.

%package -n       python3-txaio+asyncio
Summary:        Metapackage for python3-txaio asyncio extras
Requires:       python3-txaio = %{version}-%{release}
Provides:       python3dist(txaio[asyncio]) = %{version}-%{release}

%description -n python3-txaio+asyncio
Metapackage for python3-txaio asyncio extras.

%package -n       python3-txaio+docs
Summary:        Metapackage for python3-txaio docs extras
Requires:       python3-txaio = %{version}-%{release}
Requires:       python3dist(sphinx) >= 8.2.3
Requires:       python3dist(myst-parser) >= 2.0
Requires:       python3dist(furo) >= 2024.7.0
Requires:       python3dist(sphinx-autoapi) >= 2.1.0
Requires:       python3dist(sphinx-copybutton) >= 0.5
Requires:       python3dist(sphinx-design) >= 0.5
Requires:       python3dist(sphinxcontrib-images) >= 0.9
Requires:       python3dist(sphinxcontrib-spelling) >= 8.0
Requires:       python3dist(pyenchant) >= 3.2
Requires:       python3dist(scour) >= 0.38
Requires:       python3dist(sphinxext-opengraph) >= 0.9
Requires:       python3dist(linkify-it-py) >= 2.0.0
Provides:       python3dist(txaio[docs]) = %{version}-%{release}

%description -n python3-txaio+docs
Metapackage for python3-txaio docs extras.

%package -n       python3-txaio+dev
Summary:        Metapackage for python3-txaio dev extras
Requires:       python3-txaio = %{version}-%{release}
Requires:       python3dist(build) >= 1.0.0
Requires:       python3dist(wheel) >= 0.42.0
Requires:       python3dist(twine) >= 5.0.0
Requires:       python3dist(pytest) >= 8.0.0
Requires:       python3dist(pytest-cov) >= 4.0.0
Requires:       python3dist(coverage) >= 7.0.0
Requires:       python3dist(ruff) >= 0.4.0
Requires:       python3dist(ty) >= 0.0.44
Provides:       python3dist(txaio[dev]) = %{version}-%{release}

%description -n python3-txaio+dev
Metapackage for python3-txaio dev extras.

%package -n       python3-txaio+all
Summary:        Metapackage for python3-txaio all extras
Requires:       python3-txaio = %{version}-%{release}
Requires:       python3dist(zope.interface) >= 5.2.0
Requires:       python3dist(twisted) >= 22.10.0
Provides:       python3dist(txaio[all]) = %{version}-%{release}

%description -n python3-txaio+all
Metapackage for python3-txaio all extras.

%description

%package -n     python3-txaio
Summary:        Compatibility API between asyncio/Twisted/Trollius
%description -n python3-txaio

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir txaio-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-txaio usr/lib/python3*/site-packages/txaio* usr/lib64/python3*/site-packages/txaio* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/txaio* usr/lib64/python3*/site-packages/txaio* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-txaio -f %{oreon_filedir}/python3-txaio.list

%changelog

%autochangelog
