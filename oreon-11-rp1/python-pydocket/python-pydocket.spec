%global source0_hash 1f6297883f9f615c65aacc622e07233137f491154251e3a8c8ec3cefb52ac7d0
Name:           python-pydocket
Version:        0.25.2
Release:        1%{?dist}
Summary:        A distributed background task system for Python functions
License:        MIT
URL:            https://docket.lol/
Source0:        https://files.pythonhosted.org/packages/source/p/pydocket/pydocket-%{version}.tar.gz
BuildArch:      noarch
Patch:          remove-pytest-unrecognized-arguments.diff
Patch:          fix-lua-unpack.diff
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pydocket = %{version}-%{release}
# /oreon:deps
%package -n       python3-pydocket+metrics
Summary:        Metapackage for python3-pydocket metrics extras
Requires:       python3-pydocket = %{version}-%{release}
Requires:       python3dist(opentelemetry-sdk) >= 1.33.0
Provides:       python3dist(pydocket[metrics]) = %{version}-%{release}

%description -n python3-pydocket+metrics
Metapackage for python3-pydocket metrics extras.

%description

%package -n     python3-pydocket
Summary:        A distributed background task system for Python functions
# oreon:reqs
Requires:       python3dist(burner-redis) >= 0.1.7
Requires:       python3dist(cloudpickle) >= 3.1.1
Requires:       python3dist(cronsim) >= 2.6
Requires:       python3dist(exceptiongroup) >= 1.2.0
Requires:       python3dist(opentelemetry-api) >= 1.33.0
Requires:       python3dist(prometheus-client) >= 0.21.1
Requires:       python3dist(py-key-value-aio[memory,redis]) >= 0.3.0
Requires:       python3dist(python-json-logger) >= 2.0.7
Requires:       python3dist(redis) >= 5
Requires:       python3dist(rich) >= 13.9.4
Requires:       python3dist(taskgroup) >= 0.2.2
Requires:       python3dist(typer) >= 0.15.1
Requires:       python3dist(typing-extensions) >= 4.12.0
Requires:       python3dist(tzdata) >= 2025.2
Requires:       python3dist(uncalled-for) >= 0.4.0
# /oreon:reqs
%description -n python3-pydocket

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pydocket-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pydocket usr/lib/python3*/site-packages/pydocket* usr/lib64/python3*/site-packages/pydocket* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pydocket* usr/lib64/python3*/site-packages/pydocket* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pydocket -f %{oreon_filedir}/python3-pydocket.list

%changelog

%autochangelog
