%global source0_hash 66206513958a47cab82617c80165e71d93ade90d12817edb718ac2470283ca22
Name:           python-rst-linker
Version:        2.6.0
Release:        1%{?dist}
Summary:        Tools for adding metadata and hyperlinks to reStructuredText
License:        MIT
URL:            https://github.com/jaraco/rst.linker
Source0:        https://files.pythonhosted.org/packages/source/r/rst_linker/rst_linker-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.2
BuildRequires:  python3dist(setuptools-scm[toml]) >= 3.4.1
Requires:       python3-rst-linker = %{version}-%{release}
# /oreon:deps
%package -n       python3-rst-linker+testing
Summary:        Metapackage for python3-rst-linker testing extras
Requires:       python3-rst-linker = %{version}-%{release}
Requires:       python3dist(pytest) >= 6
Requires:       python3dist(pytest-checkdocs) >= 2.4
Requires:       python3dist(pytest-enabler) >= 2.2
Requires:       python3dist(pytest-ruff) >= 0.2.1
Provides:       python3dist(rst-linker[testing]) = %{version}-%{release}

%description -n python3-rst-linker+testing
Metapackage for python3-rst-linker testing extras.

%package -n       python3-rst-linker+docs
Summary:        Metapackage for python3-rst-linker docs extras
Requires:       python3-rst-linker = %{version}-%{release}
Requires:       python3dist(sphinx) >= 3.5
Requires:       python3dist(jaraco.packaging) >= 9.3
Requires:       python3dist(rst.linker) >= 1.9
Provides:       python3dist(rst-linker[docs]) = %{version}-%{release}

%description -n python3-rst-linker+docs
Metapackage for python3-rst-linker docs extras.

%description

%package -n     python3-rst-linker
Summary:        Tools for adding metadata and hyperlinks to reStructuredText
# oreon:reqs
Requires:       python3dist(jaraco.vcs) >= 2.1
# /oreon:reqs
%description -n python3-rst-linker

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir rst_linker-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-rst-linker usr/lib/python3*/site-packages/rst_linker* usr/lib64/python3*/site-packages/rst_linker* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/rst_linker* usr/lib64/python3*/site-packages/rst_linker* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-rst-linker -f %{oreon_filedir}/python3-rst-linker.list

%changelog

%autochangelog
