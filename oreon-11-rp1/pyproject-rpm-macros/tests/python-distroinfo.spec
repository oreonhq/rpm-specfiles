%global source0_hash d3f62a8bc39bf819036f22e07fa82b1a6f5647b2d0b96dadb521a84193cca027

Name:             python-distroinfo
Version:          0.3.2
Release:          0%{?dist}
Summary:          Parsing and querying distribution metadata stored in text/YAML files
License:          Apache-2.0
URL:              https://github.com/softwarefactory-project/distroinfo
Source0:        https://files.pythonhosted.org/packages/source/d/distroinfo/distroinfo-0.3.2.tar.gz
BuildArch:        noarch

BuildRequires:    pyproject-rpm-macros
BuildRequires:    python3-devel
BuildRequires:    python3-pytest
BuildRequires:    git-core

%description
This package uses setuptools and pbr.
It has setup_requires and tests that %%pyproject_buildrequires correctly
handles that including runtime requirements.
Run %%pyproject_check_import with top-level modules filtering.


%package -n python3-distroinfo
Summary:          %{summary}

%description -n python3-distroinfo
...


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -n distroinfo-%{version}
# we don't need pytest-runner
sed -Ei "s/(, )?'pytest-runner'//" setup.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l distroinfo


%check
%pytest
%pyproject_check_import -t


%files -n python3-distroinfo -f %{pyproject_files}
%doc README.rst AUTHORS
