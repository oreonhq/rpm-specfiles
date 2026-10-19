%global source0_hash c889ec9ca460a81ec485316ecf93fe9814330914b3391bfe6f4286e1c4302949
Name:           python-py-tes
Version:        1.1.4
Release:        1%{?dist}
Summary:        Python SDK for the GA4GH Task Execution API
License:        MIT
URL:            https://github.com/ohsu-comp-bio/py-tes
Source0:        https://github.com/ohsu-comp-bio/py-tes/archive/%{version}/py-tes-%{version}.tar.gz
BuildArch:      noarch
%global common_description %{expand:
This is a library for interacting with servers implementing the GA4GH Task
Execution Schema (https://github.com/ga4gh/task-execution-schemas).}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-py-tes = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-py-tes
Summary:        Python SDK for the GA4GH Task Execution API
%py_provides python3-tes
%description -n python3-py-tes %{common_description}

%prep
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-py-tes usr/lib/python3*/site-packages/py_tes* usr/lib64/python3*/site-packages/py_tes* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/py_tes* usr/lib64/python3*/site-packages/py_tes* usr/bin/*

%check

ignore="${ignore-} --ignore=tests/integration"
%pytest ${ignore-} -v
%files
%files -n python3-py-tes -f %{oreon_filedir}/python3-py-tes.list

%changelog

%autochangelog
