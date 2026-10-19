%global source0_hash 7d3a067bc7699a1a65fe2ea0b092a925855bb711a05adc1e65c5b9ba307acea4
Name:           python-cyclopts
Version:        4.25.3
Release:        1%{?dist}
Summary:        Intuitive, easy CLIs based on type hints.
License:        Apache-2.0
URL:            https://github.com/BrianPugh/cyclopts
Source0:        https://files.pythonhosted.org/packages/source/c/cyclopts/cyclopts-%{version}.tar.gz
BuildArch:      noarch
Patch:          patch-docs-conf-for-downstream-build.diff
Patch1:         exclude-init-members-from-exception-class.diff
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-cyclopts = %{version}-%{release}
# /oreon:deps
%package -n       python3-cyclopts+toml
Summary:        Metapackage for python3-cyclopts toml extras
Requires:       python3-cyclopts = %{version}-%{release}
Requires:       python3dist(tomli) >= 2.0.0
Provides:       python3dist(cyclopts[toml]) = %{version}-%{release}

%description -n python3-cyclopts+toml
Metapackage for python3-cyclopts toml extras.

%package -n       python3-cyclopts+trio
Summary:        Metapackage for python3-cyclopts trio extras
Requires:       python3-cyclopts = %{version}-%{release}
Requires:       python3dist(trio) >= 0.10.0
Provides:       python3dist(cyclopts[trio]) = %{version}-%{release}

%description -n python3-cyclopts+trio
Metapackage for python3-cyclopts trio extras.

%package -n       python3-cyclopts+yaml
Summary:        Metapackage for python3-cyclopts yaml extras
Requires:       python3-cyclopts = %{version}-%{release}
Requires:       python3dist(pyyaml) >= 6.0.1
Provides:       python3dist(cyclopts[yaml]) = %{version}-%{release}

%description -n python3-cyclopts+yaml
Metapackage for python3-cyclopts yaml extras.

%package -n       python3-cyclopts+docs
Summary:        Metapackage for python3-cyclopts docs extras
Requires:       python3-cyclopts = %{version}-%{release}
Requires:       python3dist(sphinx) >= 7.4.7
Requires:       python3dist(sphinx) < 8.2.0
Requires:       python3dist(sphinx-rtd-theme) >= 3.0.0
Requires:       python3dist(sphinx-rtd-theme) < 4.0.0
Requires:       python3dist(gitpython) >= 3.1.31
Requires:       python3dist(sphinx-copybutton) >= 0.5
Requires:       python3dist(sphinx-copybutton) < 1.0
Requires:       python3dist(myst-parser[linkify]) >= 3.0.1
Requires:       python3dist(myst-parser[linkify]) < 5.0.0
Requires:       python3dist(sphinx-autodoc-typehints) >= 1.25.2
Requires:       python3dist(sphinx-autodoc-typehints) < 4.0.0
Requires:       python3dist(sphinx-rtd-dark-mode) >= 1.3.0
Requires:       python3dist(sphinx-rtd-dark-mode) < 2.0.0
Provides:       python3dist(cyclopts[docs]) = %{version}-%{release}

%description -n python3-cyclopts+docs
Metapackage for python3-cyclopts docs extras.

%package -n       python3-cyclopts+mkdocs
Summary:        Metapackage for python3-cyclopts mkdocs extras
Requires:       python3-cyclopts = %{version}-%{release}
Requires:       python3dist(mkdocs) >= 1.4.0
Requires:       python3dist(markdown) >= 3.3
Requires:       python3dist(pymdown-extensions) >= 10.0
Provides:       python3dist(cyclopts[mkdocs]) = %{version}-%{release}

%description -n python3-cyclopts+mkdocs
Metapackage for python3-cyclopts mkdocs extras.

%package -n       python3-cyclopts+dev
Summary:        Metapackage for python3-cyclopts dev extras
Requires:       python3-cyclopts = %{version}-%{release}
Requires:       python3dist(coverage[toml]) >= 5.1
Requires:       python3dist(pre-commit) >= 2.16.0
Requires:       python3dist(pytest) >= 8.2.0
Requires:       python3dist(pytest-cov) >= 3.0.0
Requires:       python3dist(pytest-mock) >= 3.7.0
Requires:       python3dist(pytest-timeout) >= 2.3.0
Requires:       python3dist(pydantic) >= 2.11.2
Requires:       python3dist(pydantic) < 3.0.0
Requires:       python3dist(syrupy) >= 4.0.0
Requires:       python3dist(toml) >= 0.10.2
Requires:       python3dist(toml) < 1.0.0
Requires:       python3dist(trio) >= 0.10.0
Requires:       python3dist(pyyaml) >= 6.0.1
Requires:       python3dist(mkdocs) >= 1.4.0
Requires:       python3dist(pexpect) >= 4.9.0
Provides:       python3dist(cyclopts[dev]) = %{version}-%{release}

%description -n python3-cyclopts+dev
Metapackage for python3-cyclopts dev extras.

%package -n       python3-cyclopts+debug
Summary:        Metapackage for python3-cyclopts debug extras
Requires:       python3-cyclopts = %{version}-%{release}
Requires:       python3dist(ipdb) >= 0.13.9
Requires:       python3dist(line-profiler) >= 3.5.1
Provides:       python3dist(cyclopts[debug]) = %{version}-%{release}

%description -n python3-cyclopts+debug
Metapackage for python3-cyclopts debug extras.

%description

%package -n     python3-cyclopts
Summary:        Intuitive, easy CLIs based on type hints.
# oreon:reqs
Requires:       python3dist(attrs) >= 23.1.0
Requires:       python3dist(docstring-parser) < 4.0
Requires:       python3dist(docstring-parser) >= 0.15
Requires:       python3dist(rich) >= 13.6.0
Requires:       python3dist(rich-rst) < 3.0.0
Requires:       python3dist(rich-rst) >= 1.3.1
Requires:       python3dist(tomli) >= 2.0.0
Requires:       python3dist(typing-extensions) >= 4.8.0
# /oreon:reqs
%description -n python3-cyclopts

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir cyclopts-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-cyclopts usr/lib/python3*/site-packages/cyclopts* usr/lib64/python3*/site-packages/cyclopts* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/cyclopts* usr/lib64/python3*/site-packages/cyclopts* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-cyclopts -f %{oreon_filedir}/python3-cyclopts.list

%changelog

%autochangelog
