%global source0_hash 821caa8019859c1d21b10e3d2408517f9e90d84f7171cd9b5d2f70eb568b60d2

# Quite a few tests require network. To run them locally use
# `fedpkg mockbuild --enable-network --with network`
%bcond network 0

Name:           python-pooch
Version:        1.9.0
Release:        %autorelease
Summary:        A friend to fetch your data files

%global forgeurl https://github.com/fatiando/pooch
%forgemeta

License:        BSD-3-Clause
URL:            https://www.fatiando.org/pooch
Source:         %forgesource
# Exclude `doc/` from wheel
# https://github.com/fatiando/pooch/pull/423
Patch:          https://github.com/fatiando/pooch/pull/423.patch

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Pooch manages your Python library's sample data files: 
it automatically downloads and stores them in a local directory, 
with support for versioning and corruption checks.}

%description %_description

%package -n python3-pooch
Summary:        %{summary}

%description -n python3-pooch %_description

%pyproject_extras_subpkg -n python3-pooch progress xxhash sftp

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires -x progress,xxhash,sftp,test

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pooch

%check
%pytest -v -rs %{!?with_network:-m 'not network'}

%files -n python3-pooch -f %{pyproject_files}
%doc README.md CITATION.* AUTHORS.md

%changelog
%autochangelog
