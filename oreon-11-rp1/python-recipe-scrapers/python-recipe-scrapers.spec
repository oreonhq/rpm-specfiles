%global source0_hash 7610139233ca2ffb139038e97839cc17c17af1e7a3cb39e126075882121d6ee0
Name:           python-recipe-scrapers
Version:        15.12.0
Release:        1%{?dist}
Summary:        Python package, scraping recipes from all over the internet
License:        MIT
URL:            https://github.com/hhursev/recipe-scrapers/
Source0:        https://files.pythonhosted.org/packages/source/r/recipe_scrapers/recipe_scrapers-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-recipe-scrapers = %{version}-%{release}
# /oreon:deps
%package -n       python3-recipe-scrapers+online
Summary:        Metapackage for python3-recipe-scrapers online extras
Requires:       python3-recipe-scrapers = %{version}-%{release}
Requires:       python3dist(requests) >= 2.31.0
Provides:       python3dist(recipe-scrapers[online]) = %{version}-%{release}

%description -n python3-recipe-scrapers+online
Metapackage for python3-recipe-scrapers online extras.

%package -n       python3-recipe-scrapers+docs
Summary:        Metapackage for python3-recipe-scrapers docs extras
Requires:       python3-recipe-scrapers = %{version}-%{release}
Requires:       python3dist(mkdocs) >= 1.6.1
Requires:       python3dist(mkdocs-material) >= 9.5.48
Requires:       python3dist(mkdocstrings) >= 0.27.0
Requires:       python3dist(mkdocstrings-python) >= 1.12.2
Requires:       python3dist(markdown-exec) >= 1.10.0
Provides:       python3dist(recipe-scrapers[docs]) = %{version}-%{release}

%description -n python3-recipe-scrapers+docs
Metapackage for python3-recipe-scrapers docs extras.

%package -n       python3-recipe-scrapers+tests
Summary:        Metapackage for python3-recipe-scrapers tests extras
Requires:       python3-recipe-scrapers = %{version}-%{release}
Requires:       python3dist(coverage) >= 7.6.9
Requires:       python3dist(unittest-parallel) >= 1.7.0
Provides:       python3dist(recipe-scrapers[tests]) = %{version}-%{release}

%description -n python3-recipe-scrapers+tests
Metapackage for python3-recipe-scrapers tests extras.

%package -n       python3-recipe-scrapers+linters
Summary:        Metapackage for python3-recipe-scrapers linters extras
Requires:       python3-recipe-scrapers = %{version}-%{release}
Requires:       python3dist(pre-commit) == 4.0.1
Requires:       python3dist(black) == 24.10.0
Requires:       python3dist(flake8) == 7.1.1
Requires:       python3dist(pep8-naming) == 0.14.1
Requires:       python3dist(mypy) == 1.14.0
Provides:       python3dist(recipe-scrapers[linters]) = %{version}-%{release}

%description -n python3-recipe-scrapers+linters
Metapackage for python3-recipe-scrapers linters extras.

%package -n       python3-recipe-scrapers+dev
Summary:        Metapackage for python3-recipe-scrapers dev extras
Requires:       python3-recipe-scrapers = %{version}-%{release}
Provides:       python3dist(recipe-scrapers[dev]) = %{version}-%{release}

%description -n python3-recipe-scrapers+dev
Metapackage for python3-recipe-scrapers dev extras.

%package -n       python3-recipe-scrapers+all
Summary:        Metapackage for python3-recipe-scrapers all extras
Requires:       python3-recipe-scrapers = %{version}-%{release}
Provides:       python3dist(recipe-scrapers[all]) = %{version}-%{release}

%description -n python3-recipe-scrapers+all
Metapackage for python3-recipe-scrapers all extras.

%description

%package -n     python3-recipe-scrapers
Summary:        Python package, scraping recipes from all over the internet
# oreon:reqs
Requires:       python3dist(beautifulsoup4) >= 4.12.3
Requires:       python3dist(extruct) >= 0.17.0
Requires:       python3dist(isodate) >= 0.6.1
# /oreon:reqs
%description -n python3-recipe-scrapers

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir recipe_scrapers-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-recipe-scrapers usr/lib/python3*/site-packages/recipe_scrapers* usr/lib64/python3*/site-packages/recipe_scrapers* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/recipe_scrapers* usr/lib64/python3*/site-packages/recipe_scrapers* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-recipe-scrapers -f %{oreon_filedir}/python3-recipe-scrapers.list

%changelog

%autochangelog
