%global source0_hash 717f9179a0dbed357012ddad50a5ad3d5e4d9a0b8712680d4e687f5e6e6ed9b3

%bcond tests 1

Name:           python-lazy-loader
Version:        0.5
Release:        %autorelease
Summary:        Populate library namespace without incurring immediate import costs

License:        BSD-3-Clause
URL:            https://github.com/scientific-python/lazy-loader
Source:         %{pypi_source lazy_loader}

BuildSystem:            pyproject
BuildOption(install):   -l lazy_loader

BuildArch:      noarch

%if %{with tests}
# The “test” extra includes unwanted linters, etc.; we manually BR pytest
# rather than patching out all the others from pyproject.toml.
BuildRequires:  %{py3_dist pytest}
# These are required for some of the tests, but are not captured in the
# metadata, so we must BR them manually as well:
BuildRequires:  %{py3_dist numpy}
BuildRequires:  %{py3_dist scipy}
%endif

%global common_description %{expand:
lazy-loader makes it easy to load subpackages and functions on demand.

Motivation:

• Allow subpackages to be made visible to users without incurring import costs.
• Allow external libraries to be imported only when used, improving import
  times.}

%description %{common_description}

%package -n python3-lazy-loader
Summary:        %{summary}

%description -n python3-lazy-loader %{common_description}

%check -a
%if %{with tests}
%pytest
%endif

%files -n python3-lazy-loader -f %{pyproject_files}
%doc CHANGELOG.md
%doc README.md

%changelog
%autochangelog
