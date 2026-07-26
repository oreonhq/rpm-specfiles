%global source0_hash 9c58ed3dff90d51f43414ce37009ad1d5b0f08ffc9fc216998a06380f01c0045

Name:           python-hatch-fancy-pypi-readme
Version:        25.1.0
Release:        6%{?dist}
Summary:        Hatch plugin for writing fancy PyPI readmes

License:        MIT
URL:            https://github.com/hynek/hatch-fancy-pypi-readme
Source0:        %{pypi_source hatch_fancy_pypi_readme}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global common_description %{expand:
This provides a Hatch metadata plugin for everyone who cares about the
first impression of their project’s PyPI landing page. It allows you to
define your PyPI project description in terms of concatenated fragments
that are based on static strings, files, and most importantly: parts of
files defined using cut-off points or regular expressions.}

%description %{common_description}

%package -n python3-hatch-fancy-pypi-readme
Summary:        %{summary}

%description -n python3-hatch-fancy-pypi-readme %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n hatch_fancy_pypi_readme-%{version} -p1

# https://github.com/hynek/hatch-fancy-pypi-readme/commit/6c06d7244183c5b71aed905c9950e3206e5f0a9e
# Drop unwanted build dependencies that upstream already dropped
sed -i 's/ \"pytest-icdiff\", \"coverage\[toml\]\", //g' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires %{?!rhel:-x tests}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files hatch_fancy_pypi_readme

%check
%pyproject_check_import
# test_end_to_end need network access
%pytest -v -k "not test_end_to_end"

%files -n python3-hatch-fancy-pypi-readme -f %{pyproject_files}
%license LICENSE.txt
%doc README.md
%{_bindir}/hatch-fancy-pypi-readme

%changelog
%autochangelog
