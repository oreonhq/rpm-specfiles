%global source0_hash 0b9b7f14688393e5bd7d26a6dc14dfd2b228a8cdfe5b598a6677589b2159d957
Name:           python-mkdocs-rss-plugin
Version:        1.19.0
Release:        1%{?dist}
Summary:        MkDocs plugin to generate RSS and JSON feeds using Mkdocs site configuration, git log and Mkdocs pages_meta.
License:        MIT
URL:            https://guts.github.io/mkdocs-rss-plugin/
Source0:        https://files.pythonhosted.org/packages/source/m/mkdocs_rss_plugin/mkdocs_rss_plugin-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 64
BuildRequires:  python3dist(setuptools-scm) >= 8
Requires:       python3-mkdocs-rss-plugin = %{version}-%{release}
# /oreon:deps
%package -n       python3-mkdocs-rss-plugin+dev
Summary:        Metapackage for python3-mkdocs-rss-plugin dev extras
Requires:       python3-mkdocs-rss-plugin = %{version}-%{release}
Requires:       python3dist(black) >= 25.9
Requires:       python3dist(flake8) >= 7.1
Requires:       python3dist(flake8-bugbear) >= 24.10
Requires:       python3dist(flake8-builtins) >= 2.5
Requires:       python3dist(flake8-eradicate) >= 1.5
Requires:       python3dist(flake8-isort) >= 6.1.1
Requires:       python3dist(flake8-pyproject) >= 1.2.3
Requires:       python3dist(pre-commit) >= 4
Requires:       python3dist(pre-commit) < 5
Provides:       python3dist(mkdocs-rss-plugin[dev]) = %{version}-%{release}

%description -n python3-mkdocs-rss-plugin+dev
Metapackage for python3-mkdocs-rss-plugin dev extras.

%package -n       python3-mkdocs-rss-plugin+docs
Summary:        Metapackage for python3-mkdocs-rss-plugin docs extras
Requires:       python3-mkdocs-rss-plugin = %{version}-%{release}
Requires:       python3dist(mkdocs-git-committers-plugin-2) >= 2.4.1
Requires:       python3dist(mkdocs-git-committers-plugin-2) < 2.6
Requires:       python3dist(mkdocs-git-revision-date-localized-plugin) >= 1.3
Requires:       python3dist(mkdocs-git-revision-date-localized-plugin) < 1.6
Requires:       python3dist(mkdocs-material[imaging]) >= 9.7
Requires:       python3dist(mkdocs-material[imaging]) < 9.8
Requires:       python3dist(mkdocs-minify-plugin) >= 0.8
Requires:       python3dist(mkdocs-minify-plugin) < 0.9
Requires:       python3dist(mkdocstrings-python) >= 1.16.2
Requires:       python3dist(mkdocstrings-python) < 2.1
Requires:       python3dist(termynal) >= 0.12.2
Requires:       python3dist(termynal) < 0.15
Provides:       python3dist(mkdocs-rss-plugin[docs]) = %{version}-%{release}

%description -n python3-mkdocs-rss-plugin+docs
Metapackage for python3-mkdocs-rss-plugin docs extras.

%package -n       python3-mkdocs-rss-plugin+test
Summary:        Metapackage for python3-mkdocs-rss-plugin test extras
Requires:       python3-mkdocs-rss-plugin = %{version}-%{release}
Requires:       python3dist(feedparser) >= 6.0.12
Requires:       python3dist(feedparser) < 6.1
Requires:       python3dist(jsonfeed-util) >= 1.2
Requires:       python3dist(jsonfeed-util) < 2
Requires:       python3dist(mkdocs-material[imaging]) >= 9.7
Requires:       python3dist(mkdocs-material[imaging]) < 9.8
Requires:       python3dist(mkdocs-materialx[imaging]) >= 10.1.3
Requires:       python3dist(mkdocs-materialx[imaging]) < 11
Requires:       python3dist(pytest-cov) >= 6.9.1
Requires:       python3dist(pytest-cov) < 8
Requires:       python3dist(validator-collection) >= 1.5
Requires:       python3dist(validator-collection) < 1.6
Provides:       python3dist(mkdocs-rss-plugin[test]) = %{version}-%{release}

%description -n python3-mkdocs-rss-plugin+test
Metapackage for python3-mkdocs-rss-plugin test extras.

%description

%package -n     python3-mkdocs-rss-plugin
Summary:        MkDocs plugin to generate RSS and JSON feeds using Mkdocs site configuration, git log and Mkdocs pages_meta.
# oreon:reqs
Requires:       python3dist(cachecontrol[filecache]) < 1
Requires:       python3dist(cachecontrol[filecache]) >= 0.14.3
Requires:       python3dist(gitpython) < 3.2
Requires:       python3dist(gitpython) >= 3.1.45
Requires:       python3dist(mkdocs) == 1.6.1
Requires:       python3dist(properdocs) < 2
Requires:       python3dist(properdocs) >= 1.6.5
Requires:       python3dist(requests) < 3
Requires:       python3dist(requests) >= 2.32.5
Requires:       python3dist(tzdata) < 2026
Requires:       python3dist(tzdata) >= 2024
# /oreon:reqs
%description -n python3-mkdocs-rss-plugin

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir mkdocs_rss_plugin-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-mkdocs-rss-plugin usr/lib/python3*/site-packages/mkdocs_rss_plugin* usr/lib64/python3*/site-packages/mkdocs_rss_plugin* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/mkdocs_rss_plugin* usr/lib64/python3*/site-packages/mkdocs_rss_plugin* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-mkdocs-rss-plugin -f %{oreon_filedir}/python3-mkdocs-rss-plugin.list

%changelog

%autochangelog
