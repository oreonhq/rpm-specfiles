%global source0_hash 9dcf02e65f2971b80047b377468e72a268e15c0af3cf1238e6ff14f7f91143b8

Name:           python-outcome
Version:        1.3.0.post0
Release:        %autorelease
Summary:        Capture the outcome of Python function calls
License:        MIT OR Apache-2.0
URL:            https://github.com/python-trio/outcome
Source:         %{pypi_source outcome}
BuildArch:      noarch

%global _description %{expand:
Outcome provides a function for capturing the outcome of a Python function
call, so that it can be passed around.}

%description %_description

%package -n python3-outcome
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-outcome %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n outcome-%{version}
sed -i '/^pytest-cov\b/d' test-requirements.txt

%generate_buildrequires
%pyproject_buildrequires test-requirements.txt

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l outcome

%check
%pytest

%files -n python3-outcome -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
