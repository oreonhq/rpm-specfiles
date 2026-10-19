%global source0_hash 6f65939fc2a6ac4259c88b09169f0b72681cd4c03dd1d0cf91c57a1fa314e50b
Name:           python-sphinx-favicon
Version:        1.1.0
Release:        1%{?dist}
Summary:        Sphinx Extension adding support for custom favicons
License:        MIT
URL:            https://github.com/tcmetzger/sphinx-favicon
Source0:        https://files.pythonhosted.org/packages/source/s/sphinx_favicon/sphinx_favicon-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
Requires:       python3-sphinx-favicon = %{version}-%{release}
# /oreon:deps
%package -n       python3-sphinx-favicon+dev
Summary:        Metapackage for python3-sphinx-favicon dev extras
Requires:       python3-sphinx-favicon = %{version}-%{release}
Provides:       python3dist(sphinx-favicon[dev]) = %{version}-%{release}

%description -n python3-sphinx-favicon+dev
Metapackage for python3-sphinx-favicon dev extras.

%package -n       python3-sphinx-favicon+test
Summary:        Metapackage for python3-sphinx-favicon test extras
Requires:       python3-sphinx-favicon = %{version}-%{release}
Provides:       python3dist(sphinx-favicon[test]) = %{version}-%{release}

%description -n python3-sphinx-favicon+test
Metapackage for python3-sphinx-favicon test extras.

%package -n       python3-sphinx-favicon+doc
Summary:        Metapackage for python3-sphinx-favicon doc extras
Requires:       python3-sphinx-favicon = %{version}-%{release}
Requires:       python3dist(sphinx) >= 8.1
Requires:       python3dist(sphinx) < 10
Provides:       python3dist(sphinx-favicon[doc]) = %{version}-%{release}

%description -n python3-sphinx-favicon+doc
Metapackage for python3-sphinx-favicon doc extras.

%description

%package -n     python3-sphinx-favicon
Summary:        Sphinx Extension adding support for custom favicons
# oreon:reqs
Requires:       python3dist(imagesize) >= 1.3
Requires:       python3dist(requests) >= 2.30
Requires:       python3dist(sphinx) < 10
Requires:       python3dist(sphinx) >= 8.1
# /oreon:reqs
%description -n python3-sphinx-favicon

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir sphinx_favicon-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-sphinx-favicon usr/lib/python3*/site-packages/sphinx_favicon* usr/lib64/python3*/site-packages/sphinx_favicon* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sphinx_favicon* usr/lib64/python3*/site-packages/sphinx_favicon* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-sphinx-favicon -f %{oreon_filedir}/python3-sphinx-favicon.list

%changelog

%autochangelog
