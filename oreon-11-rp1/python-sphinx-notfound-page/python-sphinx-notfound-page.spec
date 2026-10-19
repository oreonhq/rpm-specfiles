%global source0_hash 913e1754370bb3db201d9300d458a8b8b5fb22e9246a816643a819a9ea2b8067
Name:           python-sphinx-notfound-page
Version:        1.1.0
Release:        1%{?dist}
Summary:        Sphinx extension to build a 404 page with absolute URLs
License:        MIT
URL:            https://github.com/readthedocs/sphinx-notfound-page
Source0:        https://files.pythonhosted.org/packages/source/s/sphinx_notfound_page/sphinx_notfound_page-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.2
Requires:       python3-sphinx-notfound-page = %{version}-%{release}
# /oreon:deps
%package -n       python3-sphinx-notfound-page+test
Summary:        Metapackage for python3-sphinx-notfound-page test extras
Requires:       python3-sphinx-notfound-page = %{version}-%{release}
Provides:       python3dist(sphinx-notfound-page[test]) = %{version}-%{release}

%description -n python3-sphinx-notfound-page+test
Metapackage for python3-sphinx-notfound-page test extras.

%package -n       python3-sphinx-notfound-page+doc
Summary:        Metapackage for python3-sphinx-notfound-page doc extras
Requires:       python3-sphinx-notfound-page = %{version}-%{release}
Provides:       python3dist(sphinx-notfound-page[doc]) = %{version}-%{release}

%description -n python3-sphinx-notfound-page+doc
Metapackage for python3-sphinx-notfound-page doc extras.

%description

%package -n     python3-sphinx-notfound-page
Summary:        Sphinx extension to build a 404 page with absolute URLs
# oreon:reqs
Requires:       python3dist(sphinx) >= 5
# /oreon:reqs
%description -n python3-sphinx-notfound-page

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir sphinx_notfound_page-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-sphinx-notfound-page usr/lib/python3*/site-packages/sphinx_notfound_page* usr/lib64/python3*/site-packages/sphinx_notfound_page* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sphinx_notfound_page* usr/lib64/python3*/site-packages/sphinx_notfound_page* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-sphinx-notfound-page -f %{oreon_filedir}/python3-sphinx-notfound-page.list

%changelog

%autochangelog
