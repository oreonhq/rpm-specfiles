%global source0_hash f839cf536e6638a6e0ca1cfd54ac761bf3bb2b5a7ecf9349557e53acc5244d36
Name:           python-requests-futures
Version:        1.1.0
Release:        1%{?dist}
Summary:        Asynchronous Python HTTP for Humans.
License:        Apache-2.0
URL:            https://github.com/ross/requests-futures
Source0:        https://files.pythonhosted.org/packages/source/r/requests_futures/requests_futures-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
Requires:       python3-requests-futures = %{version}-%{release}
# /oreon:deps
%package -n       python3-requests-futures+test
Summary:        Metapackage for python3-requests-futures test extras
Requires:       python3-requests-futures = %{version}-%{release}
Requires:       python3dist(pytest) >= 6.2.5
Requires:       python3dist(pytest-cov) >= 3.0.0
Requires:       python3dist(pytest-httpbin) >= 2.0.0
Provides:       python3dist(requests-futures[test]) = %{version}-%{release}

%description -n python3-requests-futures+test
Metapackage for python3-requests-futures test extras.

%package -n       python3-requests-futures+dev
Summary:        Metapackage for python3-requests-futures dev extras
Requires:       python3-requests-futures = %{version}-%{release}
Requires:       python3dist(pytest) >= 6.2.5
Requires:       python3dist(pytest-cov) >= 3.0.0
Requires:       python3dist(pytest-httpbin) >= 2.0.0
Requires:       python3dist(black) >= 26.0.0
Requires:       python3dist(black) < 27.0.0
Requires:       python3dist(build) >= 0.7.0
Requires:       python3dist(isort) >= 5.11.4
Requires:       python3dist(pyflakes) >= 2.2.0
Requires:       python3dist(readme-renderer[rst]) >= 26.0
Requires:       python3dist(twine) >= 3.4.2
Provides:       python3dist(requests-futures[dev]) = %{version}-%{release}

%description -n python3-requests-futures+dev
Metapackage for python3-requests-futures dev extras.

%package -n       python3-requests-futures+docs
Summary:        Metapackage for python3-requests-futures docs extras
Requires:       python3-requests-futures = %{version}-%{release}
Requires:       python3dist(sphinx) >= 8.1.0
Requires:       python3dist(sphinx-copybutton) >= 0.5.2
Provides:       python3dist(requests-futures[docs]) = %{version}-%{release}

%description -n python3-requests-futures+docs
Metapackage for python3-requests-futures docs extras.

%description

%package -n     python3-requests-futures
Summary:        Asynchronous Python HTTP for Humans.
# oreon:reqs
Requires:       python3dist(requests) >= 1.2.0
# /oreon:reqs
%description -n python3-requests-futures

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir requests_futures-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-requests-futures usr/lib/python3*/site-packages/requests_futures* usr/lib64/python3*/site-packages/requests_futures* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/requests_futures* usr/lib64/python3*/site-packages/requests_futures* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-requests-futures -f %{oreon_filedir}/python3-requests-futures.list

%changelog

%autochangelog
