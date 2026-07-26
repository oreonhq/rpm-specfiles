%global source0_hash f566845b691f755b5a7390cd2ab511b92f8a0deb35f3b98708d153a16373884e

Name:           python-snakemake-executor-plugin-cluster-generic
Version:        1.0.9
Release:        %autorelease
Summary:        Generic cluster executor for Snakemake

# SPDX
License:        MIT
URL:            https://github.com/snakemake/snakemake-executor-plugin-cluster-generic
# We use the GitHub archive instead of the PyPI sdist to get CHANGELOG.md and
# the tests.
Source:         %{url}/archive/v%{version}/snakemake-executor-plugin-cluster-generic-%{version}.tar.gz

BuildSystem:            pyproject
BuildOption(install):   -L snakemake_executor_plugin_cluster_generic

BuildArch:      noarch

# See: [tool.poetry.dev-dependencies] in pyproject.toml
BuildRequires:  %{py3_dist pytest}
BuildRequires:  snakemake >= 8

%global common_description %{expand:
A generic Snakemake executor plugin for submission of jobs to cluster systems
that provide a submission command that accepts the path to a job script (like
PBS, LSF, SGE, ...).}

%description %{common_description}

%package -n python3-snakemake-executor-plugin-cluster-generic
Summary:        %{summary}

%description -n python3-snakemake-executor-plugin-cluster-generic %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n snakemake-executor-plugin-cluster-generic-%{version}

%check -a
%if %{without bootstrap}
%pytest -v tests/tests.py
%endif

%files -n python3-snakemake-executor-plugin-cluster-generic -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.md
%doc README.md

%changelog
%autochangelog
