%global source0_hash 9e2ddadc609084b5f60affb8b87e77304fed64e271e2b2b7558186cf65d81e5a
%bcond_with developer_tools
Name:           python-awscrt
Version:        0.37.0
Release:        1%{?dist}
Summary:        A common runtime for AWS Python projects
License:        Apache-2.0
URL:            https://github.com/awslabs/aws-crt-python
Source0:        https://files.pythonhosted.org/packages/source/a/awscrt/awscrt-%{version}.tar.gz
Patch0:         skip-tests-requiring-network.patch
Patch1:         skip-SHA1-in-test_crypto.patch
Patch2:         websockets.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 75.3.1
Requires:       python3-awscrt = %{version}-%{release}
# /oreon:deps
%package -n       python3-awscrt+dev
Summary:        Metapackage for python3-awscrt dev extras
Requires:       python3-awscrt = %{version}-%{release}
Requires:       python3dist(autopep8) >= 2.3.1
Requires:       python3dist(build) >= 1.2.2
Requires:       python3dist(sphinx) >= 7.2.6
Requires:       python3dist(sphinx) < 7.3
Requires:       python3dist(websockets) >= 13.1
Requires:       python3dist(h2) == 4.1.0
Provides:       python3dist(awscrt[dev]) = %{version}-%{release}

%description -n python3-awscrt+dev
Metapackage for python3-awscrt dev extras.

%description

%package -n     python3-awscrt
Summary:        A common runtime for AWS Python projects
%description -n python3-awscrt

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%if %{with developer_tools}
%endif

%prep
%global oreon_srcdir awscrt-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-awscrt usr/lib/python3*/site-packages/awscrt* usr/lib64/python3*/site-packages/awscrt* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/awscrt* usr/lib64/python3*/site-packages/awscrt* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-awscrt -f %{oreon_filedir}/python3-awscrt.list

%changelog

%autochangelog
