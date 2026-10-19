%global source0_hash 5f9dcc4cfb8124e6550119bb4f6fbda8628bbe653804015b76c392fa5f208009
Name:           python-cotyledon
Version:        2.2.0
Release:        1%{?dist}
Summary:        Cotyledon provides a framework for defining long-running services.
License:        Apache-2.0
URL:            https://github.com/sileht/cotyledon
Source0:        https://files.pythonhosted.org/packages/source/c/cotyledon/cotyledon-%{version}.tar.gz
BuildArch:      noarch
Patch0:         python-cotyledon-rm-python-mock-usage.diff
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-cotyledon = %{version}-%{release}
# /oreon:deps
%package -n       python3-cotyledon+test
Summary:        Metapackage for python3-cotyledon test extras
Requires:       python3-cotyledon = %{version}-%{release}
Provides:       python3dist(cotyledon[test]) = %{version}-%{release}

%description -n python3-cotyledon+test
Metapackage for python3-cotyledon test extras.

%package -n       python3-cotyledon+oslo
Summary:        Metapackage for python3-cotyledon oslo extras
Requires:       python3-cotyledon = %{version}-%{release}
Requires:       python3dist(oslo.config) >= 3.14.0
Provides:       python3dist(cotyledon[oslo]) = %{version}-%{release}

%description -n python3-cotyledon+oslo
Metapackage for python3-cotyledon oslo extras.

%package -n       python3-cotyledon+doc
Summary:        Metapackage for python3-cotyledon doc extras
Requires:       python3-cotyledon = %{version}-%{release}
Provides:       python3dist(cotyledon[doc]) = %{version}-%{release}

%description -n python3-cotyledon+doc
Metapackage for python3-cotyledon doc extras.

%description

%package -n     python3-cotyledon
Summary:        Cotyledon provides a framework for defining long-running services.
%description -n python3-cotyledon

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir cotyledon-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-cotyledon usr/lib/python3*/site-packages/cotyledon* usr/lib64/python3*/site-packages/cotyledon* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/cotyledon* usr/lib64/python3*/site-packages/cotyledon* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-cotyledon -f %{oreon_filedir}/python3-cotyledon.list

%changelog

%autochangelog
