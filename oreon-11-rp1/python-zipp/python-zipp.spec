%global source0_hash 4cb57381f544315db7688e976e922a2b18cdb513d21cc194eb42232ba2a3e602
Name:           python-zipp
Version:        4.1.0
Release:        1%{?dist}
Summary:        Backport of pathlib-compatible object wrapper for zip files
License:        MIT
URL:            https://github.com/jaraco/zipp
Source0:        https://files.pythonhosted.org/packages/source/z/zipp/zipp-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
BuildRequires:  python3dist(setuptools-scm[toml]) >= 3.4.1
Requires:       python3-zipp = %{version}-%{release}
# /oreon:deps
%package -n       python3-zipp+test
Summary:        Metapackage for python3-zipp test extras
Requires:       python3-zipp = %{version}-%{release}
Requires:       python3dist(pytest) >= 6
Provides:       python3dist(zipp[test]) = %{version}-%{release}

%description -n python3-zipp+test
Metapackage for python3-zipp test extras.

%package -n       python3-zipp+doc
Summary:        Metapackage for python3-zipp doc extras
Requires:       python3-zipp = %{version}-%{release}
Requires:       python3dist(sphinx) >= 3.5
Requires:       python3dist(jaraco.packaging) >= 9.3
Requires:       python3dist(rst.linker) >= 1.9
Requires:       python3dist(jaraco.tidelift) >= 1.4
Provides:       python3dist(zipp[doc]) = %{version}-%{release}

%description -n python3-zipp+doc
Metapackage for python3-zipp doc extras.

%package -n       python3-zipp+check
Summary:        Metapackage for python3-zipp check extras
Requires:       python3-zipp = %{version}-%{release}
Requires:       python3dist(pytest-checkdocs) >= 2.14
Requires:       python3dist(pytest-ruff) >= 0.2.1
Provides:       python3dist(zipp[check]) = %{version}-%{release}

%description -n python3-zipp+check
Metapackage for python3-zipp check extras.

%package -n       python3-zipp+cover
Summary:        Metapackage for python3-zipp cover extras
Requires:       python3-zipp = %{version}-%{release}
Provides:       python3dist(zipp[cover]) = %{version}-%{release}

%description -n python3-zipp+cover
Metapackage for python3-zipp cover extras.

%package -n       python3-zipp+enabler
Summary:        Metapackage for python3-zipp enabler extras
Requires:       python3-zipp = %{version}-%{release}
Requires:       python3dist(pytest-enabler) >= 3.4
Provides:       python3dist(zipp[enabler]) = %{version}-%{release}

%description -n python3-zipp+enabler
Metapackage for python3-zipp enabler extras.

%package -n       python3-zipp+type
Summary:        Metapackage for python3-zipp type extras
Requires:       python3-zipp = %{version}-%{release}
Requires:       python3dist(pytest-mypy) >= 1.0.1
Provides:       python3dist(zipp[type]) = %{version}-%{release}

%description -n python3-zipp+type
Metapackage for python3-zipp type extras.

%description

%package -n     python3-zipp
Summary:        Backport of pathlib-compatible object wrapper for zip files
%description -n python3-zipp

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir zipp-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-zipp usr/lib/python3*/site-packages/zipp* usr/lib64/python3*/site-packages/zipp* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/zipp* usr/lib64/python3*/site-packages/zipp* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-zipp -f %{oreon_filedir}/python3-zipp.list

%changelog

%autochangelog
