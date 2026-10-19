%global source0_hash b0c11ca8131b8b227b8d5108e6ed39772222bd5aab030ed430e8f99057c4c409
Name:           python-responses
Version:        0.26.3
Release:        1%{?dist}
Summary:        A utility library for mocking out the _requests_ Python library.
License:        Apache-2.0
URL:            https://github.com/getsentry/responses
Source0:        https://files.pythonhosted.org/packages/source/r/responses/responses-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 60
Requires:       python3-responses = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-responses
Summary:        A utility library for mocking out the _requests_ Python library.
%description -n python3-responses

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir responses-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-responses usr/lib/python3*/site-packages/responses* usr/lib64/python3*/site-packages/responses* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/responses* usr/lib64/python3*/site-packages/responses* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-responses -f %{oreon_filedir}/python3-responses.list

%changelog

%autochangelog
