%global source0_hash 2d2068fb55115807d3ac77a4ca68fa48803e84ebb0ee2340f858107a36522638

Name:           python-texttable
Version:        1.7.0
Release:        %autorelease
Summary:        Python module to create simple ASCII tables
License:        MIT
URL:            https://github.com/foutaise/texttable
Source:         %{pypi_source texttable}
BuildArch:      noarch

%global common_description %{expand:
Texttable is a module to generate a formatted text table, using ASCII
characters.}

%description %{common_description}

%package -n python3-texttable
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%description -n python3-texttable %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n texttable-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l texttable

%check
%pytest --verbose tests.py

%files -n python3-texttable -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
