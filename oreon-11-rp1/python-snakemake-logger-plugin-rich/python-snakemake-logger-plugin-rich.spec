%global source0_hash 3727a15fef334e9d0fc71a358f9b505b5445f9a701c7a957c68af591f4e0da50
Name:           python-snakemake-logger-plugin-rich
Version:        0.5.0
Release:        1%{?dist}
Summary:        Log plugin for snakemake using Rich
License:        MIT
URL:            https://github.com/cademirch/snakemake-logger-plugin-rich
Source0:        https://github.com/cademirch/snakemake-logger-plugin-rich/archive/v%{version}/snakemake-logger-plugin-rich-%{version}.tar.gz
Patch:          %{url}/pull/27.patch
BuildArch:      noarch
%global common_description %{expand:
A logging plugin for Snakemake that utilizes rich for enhanced terminal styling
and progress bars.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-snakemake-logger-plugin-rich = %{version}-%{release}
# /oreon:deps
%package -n       python3-snakemake-logger-plugin-rich+dev
Summary:        Metapackage for python3-snakemake-logger-plugin-rich dev extras
Requires:       python3-snakemake-logger-plugin-rich = %{version}-%{release}
Requires:       python3dist(pytest) >= 8.3.5
Requires:       python3dist(snakemake) >= 9.0.1
Requires:       python3dist(ruff) >= 0.9.10
Requires:       python3dist(mypy) >= 1.0.0
Provides:       python3dist(snakemake-logger-plugin-rich[dev]) = %{version}-%{release}

%description -n python3-snakemake-logger-plugin-rich+dev
Metapackage for python3-snakemake-logger-plugin-rich dev extras.

%description %{common_description}

%package -n python3-snakemake-logger-plugin-rich
Summary:        Log plugin for snakemake using Rich
# oreon:reqs
Requires:       python3dist(pydantic) >= 2.10.6
Requires:       python3dist(rich) >= 13.9.4
Requires:       python3dist(snakemake-interface-executor-plugins) >= 9.3.2
Requires:       python3dist(snakemake-interface-logger-plugins) >= 1.0.0
# /oreon:reqs
%description -n python3-snakemake-logger-plugin-rich %{common_description}

%prep
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-snakemake-logger-plugin-rich usr/lib/python3*/site-packages/snakemake_logger_plugin_rich* usr/lib64/python3*/site-packages/snakemake_logger_plugin_rich* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/snakemake_logger_plugin_rich* usr/lib64/python3*/site-packages/snakemake_logger_plugin_rich* usr/bin/*

%check

%pytest -v
%files
%files -n python3-snakemake-logger-plugin-rich -f %{oreon_filedir}/python3-snakemake-logger-plugin-rich.list

%changelog

%autochangelog
