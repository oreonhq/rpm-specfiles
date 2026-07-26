%global source0_hash 9bcf96b4b6d222b09c05c1e8388faafb37e50923117b679085fc4d297c4b4b81

Name:           python-roundrobin
Version:        0.0.4
Release:        14%{?dist}
Summary:        Rather small collection of round robin utilites

License:        MIT
URL:            https://github.com/linnik/roundrobin
Source:         %{url}/archive/%{version}/roundrobin-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
# required for tests
BuildRequires:  python3-pytest

%global _description %{expand:
This is rather small collection of round robin utilites}

%description %_description

%package -n python3-roundrobin
Summary:        %{summary}

%description -n python3-roundrobin %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n roundrobin-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files roundrobin

%check
%pytest test.py

%files -n python3-roundrobin -f %{pyproject_files}
%doc README.*
%license LICENSE

%changelog
%autochangelog
