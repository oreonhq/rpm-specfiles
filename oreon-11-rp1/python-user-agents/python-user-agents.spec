%global source0_hash d36d25178db65308d1458c5fa4ab39c9b2619377010130329f3955e7626ead26

%global pkg_name user-agents

Name:           python-%{pkg_name}
Version:        2.2.0
Release:        17%{?dist}
Summary:        A library to identify devices

License:        MIT
URL:            https://github.com/selwin/python-user-agents
Source0:        %{pypi_source user-agents}
BuildArch:      noarch

BuildRequires:  python3-devel

%description
A library to identify devices (phones, tablets) and their capabilities by
parsing browser user agent strings.

%package -n python3-%{pkg_name}
Summary:        A library to identify devices

%description -n python3-%{pkg_name}
A library to identify devices (phones, tablets) and their capabilities by
parsing browser user agent strings.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pkg_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files user_agents

%check
%py3_check_import user_agents

%files -n python3-%{pkg_name}  -f %{pyproject_files}
%license LICENSE.txt
%doc README.md

%changelog
%autochangelog
