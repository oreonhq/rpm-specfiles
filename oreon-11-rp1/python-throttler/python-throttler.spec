%global source0_hash 3bdf235ed8eb70d68b900bdc35daa854fd5981c298f8de0fb848a42d61f78774

Name:           python-throttler
Version:        1.2.3
Release:        %autorelease
Summary:        Easy throttling with asyncio support

# SPDX
License:        MIT
URL:            https://github.com/uburuntu/throttler
Source:         %{url}/archive/v%{version}/throttler-%{version}.tar.gz

BuildSystem:            pyproject
BuildOption(install):   -l throttler

BuildArch:      noarch

# The “dev” extra has many unwanted dependencies for linting, etc; see
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters.
# Rather than patching them out, we just list test dependencies manually.
BuildRequires:  %{py3_dist aiohttp}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-asyncio}
# Run tests in parallel; this speeds up the build quite a bit.
BuildRequires:  %{py3_dist pytest-xdist}

%global common_description %{expand:
Zero-dependency Python package for easy throttling with asyncio support.}

%description %{common_description}

%package -n python3-throttler
Summary:        %{summary}

%description -n python3-throttler %{common_description}

%check -a
%pytest -n auto -v

%files -n python3-throttler -f %{pyproject_files}
%doc examples/

%changelog
%autochangelog
