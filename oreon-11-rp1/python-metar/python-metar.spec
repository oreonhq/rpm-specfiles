%global source0_hash 2f096e101aaf8e952bedf2d5c327a1589081e50fe42e33af72a006e56c47b913
Name:           python-metar
Version:        2.0.1
Release:        1%{?dist}
Summary:        Metar - a package to parse METAR-coded weather reports
License:        ...
URL:            https://github.com/python-metar/python-metar/
Source0:        https://files.pythonhosted.org/packages/source/m/metar/metar-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 64
BuildRequires:  python3dist(setuptools-scm) >= 8
Requires:       python3-metar = %{version}-%{release}
# /oreon:deps
%package -n       python3-metar+tests
Summary:        Metapackage for python3-metar tests extras
Requires:       python3-metar = %{version}-%{release}
Provides:       python3dist(metar[tests]) = %{version}-%{release}

%description -n python3-metar+tests
Metapackage for python3-metar tests extras.

%package -n       python3-metar+codecov
Summary:        Metapackage for python3-metar codecov extras
Requires:       python3-metar = %{version}-%{release}
Provides:       python3dist(metar[codecov]) = %{version}-%{release}

%description -n python3-metar+codecov
Metapackage for python3-metar codecov extras.

%package -n       python3-metar+typing
Summary:        Metapackage for python3-metar typing extras
Requires:       python3-metar = %{version}-%{release}
Requires:       python3dist(mypy) == 1.3.0
Provides:       python3dist(metar[typing]) = %{version}-%{release}

%description -n python3-metar+typing
Metapackage for python3-metar typing extras.

%description

%package -n     python3-metar
Summary:        Metar - a package to parse METAR-coded weather reports
%description -n python3-metar

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir metar-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-metar usr/lib/python3*/site-packages/metar* usr/lib64/python3*/site-packages/metar* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/metar* usr/lib64/python3*/site-packages/metar* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-metar -f %{oreon_filedir}/python3-metar.list

%changelog

%autochangelog
