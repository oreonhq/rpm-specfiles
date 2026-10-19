%global source0_hash bfb70c49663f63b0440f2b54dbc6b0d1650e56dfe4e2641f59b2c6f727b44aca
Name:           python-cheroot
Version:        11.1.2
Release:        1%{?dist}
Summary:        Highly-optimized, pure-python HTTP server
License:        ...
URL:            https://cheroot.cherrypy.dev
Source0:        https://files.pythonhosted.org/packages/source/c/cheroot/cheroot-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.2
BuildRequires:  python3dist(setuptools-scm) >= 7.0.0
Requires:       python3-cheroot = %{version}-%{release}
# /oreon:deps
%package -n       python3-cheroot+docs
Summary:        Metapackage for python3-cheroot docs extras
Requires:       python3-cheroot = %{version}-%{release}
Requires:       python3dist(sphinx) >= 1.8.2
Requires:       python3dist(jaraco.packaging) >= 3.2
Requires:       python3dist(sphinx-tabs) >= 1.1.0
Requires:       python3dist(sphinxcontrib-apidoc) >= 0.3.0
Provides:       python3dist(cheroot[docs]) = %{version}-%{release}

%description -n python3-cheroot+docs
Metapackage for python3-cheroot docs extras.

%description

%package -n     python3-cheroot
Summary:        Highly-optimized, pure-python HTTP server
# oreon:reqs
Requires:       python3dist(more-itertools) >= 2.6
# /oreon:reqs
%description -n python3-cheroot

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir cheroot-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-cheroot usr/lib/python3*/site-packages/cheroot* usr/lib64/python3*/site-packages/cheroot* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/cheroot* usr/lib64/python3*/site-packages/cheroot* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-cheroot -f %{oreon_filedir}/python3-cheroot.list

%changelog

%autochangelog
