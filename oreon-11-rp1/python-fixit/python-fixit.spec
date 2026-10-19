%global source0_hash 98f7e30be083b4002fde8da47ae6d817e4dd174f675b848577d3a4f6e0c84954
Name:           python-fixit
Version:        2.2.1
Release:        1%{?dist}
Summary:        A lint framework that writes better Python code for you.
License:        MIT
URL:            https://github.com/Instagram/Fixit
Source0:        https://files.pythonhosted.org/packages/source/f/fixit/fixit-%{version}.tar.gz
BuildArch:      noarch
Patch:          %{name}-pregenerate_version.diff
Patch:          %{name}-rm-unused-inventories.diff
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-fixit = %{version}-%{release}
# /oreon:deps
%package -n       python3-fixit+docs
Summary:        Metapackage for python3-fixit docs extras
Requires:       python3-fixit = %{version}-%{release}
Requires:       python3dist(jinja2) == 3.1.6
Requires:       python3dist(sphinx) == 8.0.2
Requires:       python3dist(sphinx-mdinclude) == 0.6.2
Provides:       python3dist(fixit[docs]) = %{version}-%{release}

%description -n python3-fixit+docs
Metapackage for python3-fixit docs extras.

%package -n       python3-fixit+dev
Summary:        Metapackage for python3-fixit dev extras
Requires:       python3-fixit = %{version}-%{release}
Requires:       python3dist(attribution) == 1.8.0
Requires:       python3dist(black) == 25.9.0
Requires:       python3dist(build) > 1
Requires:       python3dist(flake8) == 7.3.0
Requires:       python3dist(flake8-bugbear) == 24.12.12
Requires:       python3dist(mypy) == 1.18.2
Requires:       python3dist(ufmt) == 2.8.0
Requires:       python3dist(usort) == 1.0.8.post1
Requires:       python3dist(pyrefly) == 0.39.4
Provides:       python3dist(fixit[dev]) = %{version}-%{release}

%description -n python3-fixit+dev
Metapackage for python3-fixit dev extras.

%package -n       python3-fixit+lsp
Summary:        Metapackage for python3-fixit lsp extras
Requires:       python3-fixit = %{version}-%{release}
Requires:       python3dist(pygls[ws]) >= 2.0.0
Provides:       python3dist(fixit[lsp]) = %{version}-%{release}

%description -n python3-fixit+lsp
Metapackage for python3-fixit lsp extras.

%package -n       python3-fixit+pretty
Summary:        Metapackage for python3-fixit pretty extras
Requires:       python3-fixit = %{version}-%{release}
Requires:       python3dist(rich) >= 12.6.0
Provides:       python3dist(fixit[pretty]) = %{version}-%{release}

%description -n python3-fixit+pretty
Metapackage for python3-fixit pretty extras.

%description

%package -n     python3-fixit
Summary:        A lint framework that writes better Python code for you.
# oreon:reqs
Requires:       python3dist(click) < 8.2
Requires:       python3dist(click) >= 8.0
Requires:       python3dist(libcst) >= 0.3.18
Requires:       python3dist(moreorless) >= 0.4.0
Requires:       python3dist(packaging) >= 21
Requires:       python3dist(tomli) >= 2.0
Requires:       python3dist(trailrunner) >= 1.2
# /oreon:reqs
%description -n python3-fixit

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir fixit-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-fixit usr/lib/python3*/site-packages/fixit* usr/lib64/python3*/site-packages/fixit* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/fixit* usr/lib64/python3*/site-packages/fixit* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-fixit -f %{oreon_filedir}/python3-fixit.list

%changelog

%autochangelog
