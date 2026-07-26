%global source0_hash 836a778de4fec4dcd1dcd89ed8abff8a221f58308462e1c4aa2a3cf30148f0b9

Name:           python-stack-data
Version:        0.6.3
Release:        %autorelease
Summary:        Extract data from python stack frames and tracebacks for informative displays

# SPDX
License:        MIT
URL:            http://github.com/alexmojaki/stack_data
Source0:        %{pypi_source stack_data}
# don't run type checks, see
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
Patch:          no-typeguard.patch

# Support pygments 2.19+
Patch:          https://github.com/alexmojaki/stack_data/pull/58.patch
# Patches for Alpine; not submitted to the upstream project
# https://gitlab.alpinelinux.org/alpine/aports/-/merge_requests/83491
Patch:          fix-pygments2.patch
Patch:          fix-pygments3.patch

BuildArch:      noarch
BuildRequires:  python3-devel
# Extra test dependency
# Tests use Cython and try to compile some extensions
BuildRequires:  gcc

%global _description %{expand:
This is a library that extracts data from stack frames and tracebacks,
particularly to display more useful tracebacks than the default.}

%description %_description

%package -n     python3-stack-data
Summary:        %{summary}

%description -n python3-stack-data %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n stack_data-%{version}

%generate_buildrequires
%pyproject_buildrequires -r -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files stack_data

%check
# A hack for until https://github.com/alexmojaki/stack_data/issues/59 is fixed
export FIX_STACK_DATA_TESTS=1
%tox

%files -n python3-stack-data -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
