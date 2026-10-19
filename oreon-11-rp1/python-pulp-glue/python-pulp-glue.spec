%global source0_hash 816a49743af9fc811e2225a7100a5691469e047eb12c6a3b620f8d15f2121da7
Name:           python-pulp-glue
Version:        0.40.6
Release:        1%{?dist}
Summary:        Version agnostic glue library to talk to pulpcore_s REST API.
License:        GPL-2.0-or-later
URL:            https://github.com/pulp/pulp-cli
Source0:        https://files.pythonhosted.org/packages/source/p/pulp_glue/pulp_glue-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pulp-glue = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pulp-glue
Summary:        Version agnostic glue library to talk to pulpcore_s REST API.
# oreon:reqs
Requires:       python3dist(multidict) < 6.8
Requires:       python3dist(multidict) >= 6.0.5
Requires:       python3dist(packaging) <= 26.2
Requires:       python3dist(packaging) >= 22.0
Requires:       python3dist(pydantic) < 3
Requires:       python3dist(pydantic) >= 2.9.2
Requires:       python3dist(requests) < 2.34
Requires:       python3dist(requests) >= 2.24.0
Requires:       python3dist(requests) >= 2.25.1
Requires:       python3dist(tomli) < 2.1
Requires:       python3dist(tomli) >= 2.0.0
# /oreon:reqs
%description -n python3-pulp-glue

%prep
%global oreon_srcdir pulp_glue-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pulp-glue usr/lib/python3*/site-packages/pulp_glue* usr/lib64/python3*/site-packages/pulp_glue* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pulp_glue* usr/lib64/python3*/site-packages/pulp_glue* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pulp-glue -f %{oreon_filedir}/python3-pulp-glue.list

%changelog

%autochangelog
