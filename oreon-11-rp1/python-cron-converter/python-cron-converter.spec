%global source0_hash b6cc11365b25bb406ee9fb97c3b3f1e9680cde5fb36759b90540e125e203e3b9
Name:           python-cron-converter
Version:        2.0.1
Release:        1%{?dist}
Summary:        Cron string parser and scheduler for Python
License:        MIT
URL:            https://github.com/Sonic0/cron-converter
Source0:        https://github.com/Sonic0/cron-converter/archive/v%{version}/cron-converter-%{version}.tar.gz
BuildArch:      noarch
%global common_description %{expand:
Cron-converter provides a Cron string parser (from string/lists to
string/lists) and iteration for the datetime object with a cron like format.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-cron-converter = %{version}-%{release}
# /oreon:deps
%package -n       python3-cron-converter+test
Summary:        Metapackage for python3-cron-converter test extras
Requires:       python3-cron-converter = %{version}-%{release}
Provides:       python3dist(cron-converter[test]) = %{version}-%{release}

%description -n python3-cron-converter+test
Metapackage for python3-cron-converter test extras.

%package -n       python3-cron-converter+mypy
Summary:        Metapackage for python3-cron-converter mypy extras
Requires:       python3-cron-converter = %{version}-%{release}
Provides:       python3dist(cron-converter[mypy]) = %{version}-%{release}

%description -n python3-cron-converter+mypy
Metapackage for python3-cron-converter mypy extras.

%description %{common_description}

%package -n python3-cron-converter
Summary:        Cron string parser and scheduler for Python
%description -n python3-cron-converter %{common_description}

%prep
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-cron-converter usr/lib/python3*/site-packages/cron_converter* usr/lib64/python3*/site-packages/cron_converter* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/cron_converter* usr/lib64/python3*/site-packages/cron_converter* usr/bin/*

%check

%{py3_test_envvars} %{python3} -m unittest discover -v tests/unit
%{py3_test_envvars} %{python3} -m unittest discover -v tests/integration
%files
%files -n python3-cron-converter -f %{oreon_filedir}/python3-cron-converter.list

%changelog

%autochangelog
