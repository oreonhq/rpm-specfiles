%global source0_hash a2bca0f039f39dbd35fb74ae1b5f998608c437463371f0ff7f49a19a17a114d0
Name:           python-mdit-py-plugins
Version:        0.6.1
Release:        1%{?dist}
Summary:        Collection of plugins for markdown-it-py
License:        MIT
URL:            https://github.com/executablebooks/mdit-py-plugins
Source0:        https://files.pythonhosted.org/packages/source/m/mdit_py_plugins/mdit_py_plugins-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.4
Requires:       python3-mdit-py-plugins = %{version}-%{release}
# /oreon:deps
%package -n       python3-mdit-py-plugins+code_style
Summary:        Metapackage for python3-mdit-py-plugins code_style extras
Requires:       python3-mdit-py-plugins = %{version}-%{release}
Provides:       python3dist(mdit-py-plugins[code_style]) = %{version}-%{release}

%description -n python3-mdit-py-plugins+code_style
Metapackage for python3-mdit-py-plugins code_style extras.

%package -n       python3-mdit-py-plugins+testing
Summary:        Metapackage for python3-mdit-py-plugins testing extras
Requires:       python3-mdit-py-plugins = %{version}-%{release}
Provides:       python3dist(mdit-py-plugins[testing]) = %{version}-%{release}

%description -n python3-mdit-py-plugins+testing
Metapackage for python3-mdit-py-plugins testing extras.

%package -n       python3-mdit-py-plugins+rtd
Summary:        Metapackage for python3-mdit-py-plugins rtd extras
Requires:       python3-mdit-py-plugins = %{version}-%{release}
Provides:       python3dist(mdit-py-plugins[rtd]) = %{version}-%{release}

%description -n python3-mdit-py-plugins+rtd
Metapackage for python3-mdit-py-plugins rtd extras.

%description

%package -n     python3-mdit-py-plugins
Summary:        Collection of plugins for markdown-it-py
# oreon:reqs
Requires:       python3dist(markdown-it-py) < 5.0.0
Requires:       python3dist(markdown-it-py) >= 2.0.0
# /oreon:reqs
%description -n python3-mdit-py-plugins

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir mdit_py_plugins-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-mdit-py-plugins usr/lib/python3*/site-packages/mdit_py_plugins* usr/lib64/python3*/site-packages/mdit_py_plugins* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/mdit_py_plugins* usr/lib64/python3*/site-packages/mdit_py_plugins* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-mdit-py-plugins -f %{oreon_filedir}/python3-mdit-py-plugins.list

%changelog

%autochangelog
