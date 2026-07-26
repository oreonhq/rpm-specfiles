%global source0_hash 791241e2b1e83031543246d9b3b304430233ff964a32a2cfac47896b4eed2513

# Copyright (C) 2023 Maxwell G <maxwell@gtmx.me>
# Copyright (C) Fedora Project Authors
# SPDX-License-Identifier: MIT
# License text: https://spdx.org/licenses/MIT

%bcond tests 1

Name:           python-annotated-types
Version:        0.7.0
Release:        9%{?dist}
Summary:        Reusable constraint types to use with typing.Annotated

License:        MIT
%global forgeurl https://github.com/annotated-types/annotated-types
URL:            %{forgeurl}
%forgemeta
Source:         %{forgesource}

BuildArch:      noarch

BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  %{py3_dist pytest}
%endif

%global _description %{expand:
PEP-593 added typing.Annotated as a way of adding context-specific metadata to
existing types, and specifies that Annotated[T, x] should be treated as T by
any tool or library without special logic for x.

This package provides metadata objects which can be used to represent common
constraints such as upper and lower bounds on scalar values and collection
sizes, a Predicate marker for runtime checks, and descriptions of how we intend
these metadata to be interpreted. In some cases, we also note alternative
representations which do not require this package.}

%description %_description

%package -n python3-annotated-types
Summary:        %{summary}

%description -n python3-annotated-types %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 %{forgesetupargs}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l annotated_types

%check
%if %{with tests}
%pytest
%endif

%files -n python3-annotated-types -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
