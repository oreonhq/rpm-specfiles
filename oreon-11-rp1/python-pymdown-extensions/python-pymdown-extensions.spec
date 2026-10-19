%global source0_hash 88fe2c97fb9153b9f2cc1da59f1d7c7cb74971110daf33cccb2a5514e0f7e970
Name:           python-pymdown-extensions
Version:        12.0.1
Release:        1%{?dist}
Summary:        Extension pack for Python Markdown.
License:        MIT
URL:            https://github.com/facelessuser/pymdown-extensions
Source0:        https://files.pythonhosted.org/packages/source/p/pymdown_extensions/pymdown_extensions-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) >= 1.26
Requires:       python3-pymdown-extensions = %{version}-%{release}
# /oreon:deps
%package -n       python3-pymdown-extensions+extra
Summary:        Metapackage for python3-pymdown-extensions extra extras
Requires:       python3-pymdown-extensions = %{version}-%{release}
Requires:       python3dist(pygments) >= 2.19.1
Provides:       python3dist(pymdown-extensions[extra]) = %{version}-%{release}

%description -n python3-pymdown-extensions+extra
Metapackage for python3-pymdown-extensions extra extras.

%description

%package -n     python3-pymdown-extensions
Summary:        Extension pack for Python Markdown.
# oreon:reqs
Requires:       python3dist(markdown) >= 3.6
# /oreon:reqs
%description -n python3-pymdown-extensions

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pymdown_extensions-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pymdown-extensions usr/lib/python3*/site-packages/pymdown_extensions* usr/lib64/python3*/site-packages/pymdown_extensions* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pymdown_extensions* usr/lib64/python3*/site-packages/pymdown_extensions* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pymdown-extensions -f %{oreon_filedir}/python3-pymdown-extensions.list

%changelog

%autochangelog
