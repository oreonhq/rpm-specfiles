%global source0_hash 36001524e936be45cd826f1cfbd4ebd839c2a7c087e4351c93ed044bdb2fef86

Name:           python-kanboard
Version:        1.1.7
Release:        6%{?dist}
Summary:        Client library for Kanboard API

License:        MIT
URL:            https://github.com/kanboard/python-api-client
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Kanboard is project management software that focuses on the Kanban
methodology.

This package provides client library for Kanboard API.
}

%description %_description

%package -n python3-kanboard
Summary:        %{summary}

%description -n python3-kanboard %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n python-api-client-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files kanboard

%check
%{python3} -m unittest

%files -n python3-kanboard -f %{pyproject_files}
%doc README.rst
%doc LICENSE

%changelog
%autochangelog
