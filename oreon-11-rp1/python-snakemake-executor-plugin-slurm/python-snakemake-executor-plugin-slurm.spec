%global source0_hash cf47e23ec5090b1767f67cd11057aeb777225ec880fd4a5a387a16f076e35da4
%bcond tests 1
Name:           python-snakemake-executor-plugin-slurm
Version:        2.8.0
Release:        1%{?dist}
Summary:        A Snakemake executor plugin for submitting jobs to a SLURM cluster
License:        MIT
URL:            https://github.com/snakemake/snakemake-executor-plugin-slurm
Source0:        https://github.com/snakemake/snakemake-executor-plugin-slurm/archive/v%{version}/snakemake-executor-plugin-slurm-%{version}.tar.gz
Source1:        generate-slurm-partition-config.1
BuildArch:      noarch
%if %{with tests}
%endif
%global common_description %{expand:
%{summary}.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-snakemake-executor-plugin-slurm = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-snakemake-executor-plugin-slurm
Summary:        A Snakemake executor plugin for submitting jobs to a SLURM cluster
Requires:       slurm
# oreon:reqs
Requires:       python3dist(numpy) < 3
Requires:       python3dist(numpy) >= 2.4.5
Requires:       python3dist(pandas) < 4
Requires:       python3dist(pandas) >= 2.3.3
Requires:       python3dist(pyyaml) < 7
Requires:       python3dist(pyyaml) >= 6.0.3
Requires:       python3dist(snakemake-executor-plugin-slurm-jobstep) < 1
Requires:       python3dist(snakemake-executor-plugin-slurm-jobstep) >= 0.6.0
Requires:       python3dist(snakemake-interface-common) < 2
Requires:       python3dist(snakemake-interface-common) >= 1.23.0
Requires:       python3dist(snakemake-interface-executor-plugins) < 10
Requires:       python3dist(snakemake-interface-executor-plugins) >= 9.4.0
Requires:       python3dist(throttler) < 2
Requires:       python3dist(throttler) >= 1.2.2
# /oreon:reqs
%description -n python3-snakemake-executor-plugin-slurm %{common_description}

%install
%pyproject_install
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 '%{SOURCE1}'
%oreon_autofiles python3-snakemake-executor-plugin-slurm usr/lib/python3*/site-packages/snakemake_executor_plugin_slurm* usr/lib64/python3*/site-packages/snakemake_executor_plugin_slurm* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/snakemake_executor_plugin_slurm* usr/lib64/python3*/site-packages/snakemake_executor_plugin_slurm* usr/bin/*

%prep
%oreon_prep
%build

%pyproject_wheel
%check

%if %{with tests}
k="${k-}${k+ and }not test_group_workflow"
k="${k-}${k+ and }not test_simple_workflow"
%pytest -k "${k-}" -v tests/tests.py
%endif
%files
%files -n python3-snakemake-executor-plugin-slurm -f %{oreon_filedir}/python3-snakemake-executor-plugin-slurm.list

%changelog

%autochangelog
