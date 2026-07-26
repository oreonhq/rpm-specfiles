%global source0_hash cc5638e2ca63183c9efb2b60d88c9ed1c1e338d41df45492dad078db4400aeb1

%global srcname easyargs
%global _description %{expand:
A project designed to make command line argument parsing easy.  There are many
ways to create a command line parser in python: argparse, docopt, click.  These
are all great options, but require quite a lot of configuration and sometimes
you just need a function to be called.  Enter easyargs.  Define the function
that you want to be called, decorate it and let easyargs work out the command
line.}

%bcond_without  tests

Name:           python-%{srcname}
Version:        0.9.4
Release:        33%{?dist}
Summary:        Making argument parsing easy
License:        MIT
URL:            https://github.com/stedmeister/easyargs
Source:         %pypi_source
# https://github.com/stedmeister/easyargs/pull/17
Patch:          0001-Multiline-docstrings-now-have-a-space-between-them-i.patch
# https://github.com/stedmeister/easyargs/pull/18
Patch:          0002-Use-standard-library-mock-when-available.patch
# https://github.com/stedmeister/easyargs/pull/19
Patch:          0003-Add-support-for-Python-3.6-through-3.11.patch

BuildArch:      noarch
BuildRequires:  python3-devel

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n %{srcname}-%{version}
find -name \*.py | xargs sed -i -e '1 {/^#!/d}'

%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-x test}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%if %{with tests}
%pytest
%else
%pyproject_check_import
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
