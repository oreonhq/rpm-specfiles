%global source0_hash 8b412432c6055b0b7d14c310000ae93352ed6754f70fa8f7c34141f91c4e3219
Name:           python-exceptiongroup
Version:        1.3.1
Release:        1%{?dist}
Summary:        Backport of PEP 654 _exception groups_
License:        MIT
URL:            https://github.com/agronholm/exceptiongroup
Source0:        https://files.pythonhosted.org/packages/source/e/exceptiongroup/exceptiongroup-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-exceptiongroup = %{version}-%{release}
# /oreon:deps
%package -n       python3-exceptiongroup+test
Summary:        Metapackage for python3-exceptiongroup test extras
Requires:       python3-exceptiongroup = %{version}-%{release}
Requires:       python3dist(pytest) >= 6
Provides:       python3dist(exceptiongroup[test]) = %{version}-%{release}

%description -n python3-exceptiongroup+test
Metapackage for python3-exceptiongroup test extras.

%description

%package -n     python3-exceptiongroup
Summary:        Backport of PEP 654 _exception groups_
# oreon:reqs
Requires:       python3dist(typing-extensions) >= 4.6.0
# /oreon:reqs
%description -n python3-exceptiongroup

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir exceptiongroup-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-exceptiongroup usr/lib/python3*/site-packages/exceptiongroup* usr/lib64/python3*/site-packages/exceptiongroup* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/exceptiongroup* usr/lib64/python3*/site-packages/exceptiongroup* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-exceptiongroup -f %{oreon_filedir}/python3-exceptiongroup.list

%changelog

%autochangelog
