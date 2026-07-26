%global source0_hash 5abd6b666da08c852c54415219a48f74c355af5892c152d6ceea56f794aff793

%global srcname noggin-messages
%global modname noggin_messages

Name:           python-%{srcname}
Version:        1.0.3
Release:        13%{?dist}
Summary:        Fedora Messaging message schemas for Noggin

License:        MIT
URL:            https://github.com/fedora-infra/%{srcname}
Source0:        %{pypi_source}

## Downstream fixes
Patch1001:      0001-Revert-Include-additional-files-in-the-sdist.patch

BuildArch:      noarch
BuildRequires:  pyproject-rpm-macros >= 0-14

%description
This package contains the fedora-messaging message schemas for Noggin.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        Fedora Messaging message schemas for Noggin
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
This package contains the fedora-messaging message schemas for Noggin.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{modname}

%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc docs/index.rst

%changelog
%autochangelog
