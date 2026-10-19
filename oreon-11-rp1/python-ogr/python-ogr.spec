%global source0_hash 1fbd6ef62b491d1a24b7d9302354a66ca6ff12b412f787130be48d7e5c3b318d
Name:           python-ogr
Version:        0.63.0
Release:        1%{?dist}
Summary:        One API for multiple git forges.
License:        MIT
URL:            https://github.com/packit/ogr
Source0:        https://files.pythonhosted.org/packages/source/o/ogr/ogr-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-ogr = %{version}-%{release}
# /oreon:deps
%package -n       python3-ogr+testing
Summary:        Metapackage for python3-ogr testing extras
Requires:       python3-ogr = %{version}-%{release}
Provides:       python3dist(ogr[testing]) = %{version}-%{release}

%description -n python3-ogr+testing
Metapackage for python3-ogr testing extras.

%description

%package -n     python3-ogr
Summary:        One API for multiple git forges.
# oreon:reqs
Requires:       python3dist(pyforgejo) >= 2.0.0
# /oreon:reqs
%description -n python3-ogr

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir ogr-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-ogr usr/lib/python3*/site-packages/ogr* usr/lib64/python3*/site-packages/ogr* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/ogr* usr/lib64/python3*/site-packages/ogr* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-ogr -f %{oreon_filedir}/python3-ogr.list

%changelog

%autochangelog
