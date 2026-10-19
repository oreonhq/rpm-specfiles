%global source0_hash a69f28bfc245608781205e912faae437c2b2165773afa4e7b979d77447a69dd2
Name:           python-setuptools-scm
Version:        10.3.4
Release:        1%{?dist}
Summary:        the blessed package to manage your versions by scm tags
License:        MIT
URL:            https://github.com/pypa/setuptools-scm/
Source0:        https://files.pythonhosted.org/packages/source/s/setuptools_scm/setuptools_scm-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 45
BuildRequires:  python3dist(tomli) >= 1
BuildRequires:  python3dist(typing-extensions) >= 4.1
BuildRequires:  python3dist(vcs-versioning) < 3
BuildRequires:  python3dist(vcs-versioning) >= 2.5.0.dev0
Requires:       python3-setuptools-scm = %{version}-%{release}
# /oreon:deps
%package -n       python3-setuptools-scm+rich
Summary:        Metapackage for python3-setuptools-scm rich extras
Requires:       python3-setuptools-scm = %{version}-%{release}
Requires:       python3dist(rich) >= 13
Provides:       python3dist(setuptools-scm[rich]) = %{version}-%{release}

%description -n python3-setuptools-scm+rich
Metapackage for python3-setuptools-scm rich extras.

%package -n       python3-setuptools-scm+simple
Summary:        Metapackage for python3-setuptools-scm simple extras
Requires:       python3-setuptools-scm = %{version}-%{release}
Provides:       python3dist(setuptools-scm[simple]) = %{version}-%{release}

%description -n python3-setuptools-scm+simple
Metapackage for python3-setuptools-scm simple extras.

%package -n       python3-setuptools-scm+toml
Summary:        Metapackage for python3-setuptools-scm toml extras
Requires:       python3-setuptools-scm = %{version}-%{release}
Provides:       python3dist(setuptools-scm[toml]) = %{version}-%{release}

%description -n python3-setuptools-scm+toml
Metapackage for python3-setuptools-scm toml extras.

%description

%package -n     python3-setuptools-scm
Summary:        the blessed package to manage your versions by scm tags
# oreon:reqs
Requires:       python3dist(packaging) >= 20
Requires:       python3dist(tomli) >= 1
Requires:       python3dist(typing-extensions) >= 4.1
Requires:       python3dist(vcs-versioning) < 3
Requires:       python3dist(vcs-versioning) >= 2.5.0.dev0
# /oreon:reqs
%description -n python3-setuptools-scm

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir setuptools_scm-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-setuptools-scm usr/lib/python3*/site-packages/setuptools_scm* usr/lib64/python3*/site-packages/setuptools_scm* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/setuptools_scm* usr/lib64/python3*/site-packages/setuptools_scm* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-setuptools-scm -f %{oreon_filedir}/python3-setuptools-scm.list

%changelog

%autochangelog
