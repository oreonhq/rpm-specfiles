%global source0_hash 1263c4bb481002e83a96e9253915b33241ac3e1ed6219a2793d3121f65159107

Name:           python-jaraco-path
Version:        3.7.2
Release:        %autorelease
Summary:        Miscellaneous path functions

License:        MIT
URL:            https://github.com/jaraco/jaraco.path
Source0:        %{pypi_source jaraco_path}

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
jaraco.path provides cross platform hidden file detection}

%description %_description

%package -n     python3-jaraco-path
Summary:        %{summary}

%description -n python3-jaraco-path %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n jaraco_path-%{version}

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l jaraco

%check
%pytest

%files -n python3-jaraco-path -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
