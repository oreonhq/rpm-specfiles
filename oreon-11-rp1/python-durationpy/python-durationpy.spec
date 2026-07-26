%global source0_hash 0f932886b257a20c79a1fcebdcd115492b3bc07707fee8a939cf1b46e8674542

Name:           python-durationpy
Version:        0.9
Release:        %autorelease
Summary:        Module for converting between datetime.timedelta and Go's Duration strings

License:        MIT
URL:            https://github.com/icholy/durationpy
Source:         %{url}/archive/refs/tags/%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
Module for converting between datetime.timedelta and Go's Duration strings}

%description %_description

%package -n python3-durationpy
Summary:        %{summary}

%description -n python3-durationpy %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n durationpy-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l durationpy

%check
%pytest test.py

%files -n python3-durationpy -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
