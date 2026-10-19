%global source0_hash dcfa2ab6103dcbd3a53f9f5d40731b4addd6a5a30f0d905ee80479a1e73df852
Name:           python-cs
Version:        5.1.0
Release:        1%{?dist}
Summary:        A simple yet powerful CloudStack API client for Python and the command-line.
License:        BSD-3-Clause
URL:            https://github.com/ngine-io/cs
Source0:        https://files.pythonhosted.org/packages/source/c/cs/cs-%{version}.tar.gz
BuildArch:      noarch
Patch:          %{forgeurl}/pull/141.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-cs = %{version}-%{release}
# /oreon:deps
%package -n       python3-cs+async
Summary:        Metapackage for python3-cs async extras
Requires:       python3-cs = %{version}-%{release}
Provides:       python3dist(cs[async]) = %{version}-%{release}

%description -n python3-cs+async
Metapackage for python3-cs async extras.

%package -n       python3-cs+highlight
Summary:        Metapackage for python3-cs highlight extras
Requires:       python3-cs = %{version}-%{release}
Provides:       python3dist(cs[highlight]) = %{version}-%{release}

%description -n python3-cs+highlight
Metapackage for python3-cs highlight extras.

%description

%package -n     python3-cs
Summary:        A simple yet powerful CloudStack API client for Python and the command-line.
%description -n python3-cs

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir cs-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-cs usr/lib/python3*/site-packages/cs* usr/lib64/python3*/site-packages/cs* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/cs* usr/lib64/python3*/site-packages/cs* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-cs -f %{oreon_filedir}/python3-cs.list

%changelog

%autochangelog
