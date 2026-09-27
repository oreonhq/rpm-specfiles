%global source0_hash 410489f33b2673fd77452134f557da41ee6e3e46854cab82f2b4c2e3bb35eb82

%global giturl  https://github.com/Quansight-Labs/accessible-pygments

Name:           python-accessible-pygments
Version:        0.0.5
Release:        %autorelease
Summary:        Accessible pygments themes

License:        BSD-3-Clause
URL:            https://quansight-labs.github.io/accessible-pygments/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/accessible-pygments-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
%global orbs_pyproject_requires_options -x tests
%global orbs_pyproject_files_options -l a11y_pygments

%description
This package includes a collection of accessible themes for pygments based on
different sources.

%package     -n python3-accessible-pygments
Summary:        %{summary}

%py_provides python3-a11y-pygments

%description -n python3-accessible-pygments
This package includes a collection of accessible themes for pygments based on
different sources.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n accessible-pygments-%{version}

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_buildrequires %{?orbs_pyproject_requires_options}

%build
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{?orbs_pyproject_files_options}

%check
%pytest -v

%files -n python3-accessible-pygments -f %{pyproject_files}
%doc CHANGELOG.md README.md

%changelog
%autochangelog
