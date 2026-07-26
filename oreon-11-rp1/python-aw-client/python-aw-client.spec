%global source0_hash 3ad46b33b5ea201d73dd07779876af6d7a44cffabf9a4020a991fda4911f41ca

%bcond check 0
%global srcname aw-client

Name:           python-%{srcname}
Version:        0.5.14
Release:        %autorelease
Summary:        Client library for ActivityWatch in Python

License:        MPL-2.0
URL:            https://github.com/ActivityWatch/aw-client
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%global _description %{expand:
Client library for ActivityWatch in Python.}

%description %{_description}

%package -n python3-%{srcname}
Summary:    %{summary}

%description -n python3-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files aw_client

%check
# skip test_client.py due to a http connection error
# skip test_failqueue.py due to missing aw_server dependency
%pytest --ignore=tests/test_client.py \
        --ignore=tests/test_failqueue.py

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%license LICENSE.txt
%{_bindir}/aw-client

%changelog
%autochangelog
