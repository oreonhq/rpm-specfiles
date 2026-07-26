%global source0_hash 3e03550bd1e362425649d9934c5e68f7c35fe8c4eb38a9557317592f9636eafa

%global srcname academic-file-converter

Name:           academic-admin
Version:        0.11.2
Release:        %autorelease
Summary:        Admin tool for the Academic website builder

License:        MIT
URL:            https://github.com/BuildLore/%{srcname}
Source:         https://github.com/BuildLore/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
Patch0:         academic-admin-0.11.2-dependencies.patch

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
An admin tool for the Academic website builder.}

%description %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%files -n academic-admin
%doc README.md
%license LICENSE.md
%{python3_sitelib}/academic/
%{python3_sitelib}/academic-%{version}.dist-info/
%{_bindir}/*

%changelog
%autochangelog
