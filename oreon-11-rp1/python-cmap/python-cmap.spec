%global source0_hash 28d5c99de241648d3985ca69f65b4a43d342ddaf23ce28313f2f24e2b4c664d7

%global pypi_name cmap
%global forgeurl https://github.com/tlambert03/cmap

Name:           python-%{pypi_name}
Version:        0.3.0
Release:        %{autorelease}
Summary:        Scientific colormaps for python, without dependencies
%forgemeta
# The colormaps carry their own licenses
License:        BSD-3-Clause AND MIT AND Apache-1.1 AND CC-BY-4.0 AND BSD-1-Clause
URL:            %forgeurl
Source:         %forgesource

BuildArch:      noarch
BuildRequires:  python3-devel
# For hatch-vcs
BuildRequires:  git-core

%global _description %{expand:
Scientific colormaps for python, with no dependencies beyond numpy.

With cmap, you can use any of the colormaps from matplotlib, cmocean,
colorbrewer, crameri, seaborn, and a host of other collections in your
python code, without having to install matplotlib or any other
dependencies beyond numpy.}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1 -S git

# Make sure this is the last step in prep
git tag v%{version}

%generate_buildrequires
%pyproject_buildrequires -x test_min

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pytest -v

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md CHANGELOG.md

%changelog
%autochangelog
