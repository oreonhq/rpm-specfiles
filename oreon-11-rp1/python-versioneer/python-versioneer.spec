%global source0_hash 5ab283b9857211d61b53318b7c792cf68e798e765ee17c27ade9f6c924235731

%global _description %{expand:
Versioneer is a tool to automatically update version strings by asking your
version-control system about the current tree.}

Name:           python-versioneer
Version:        0.29
Release:        1%{?dist}
Summary:        Easy VCS-based management of project version strings
License:        Unlicense
URL:            https://github.com/warner/python-versioneer
Source0:        https://files.pythonhosted.org/packages/32/d7/854e45d2b03e1a8ee2aa6429dd396d002ce71e5d88b77551b2fb249cb382/versioneer-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description %_description

%package -n     python3-versioneer
Summary:        %{summary}

%description -n python3-versioneer %_description

%pyproject_extras_subpkg -n python3-versioneer toml

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n versioneer-%{version}

%generate_buildrequires
%pyproject_buildrequires -x toml

%build
%pyproject_wheel

%install
%pyproject_install
sed -r -i '1{/^#!/d}' %{buildroot}%{python3_sitelib}/versioneer.py
%pyproject_save_files -l versioneer

%check
%{python3} setup.py make_versioneer
%{python3} -m unittest discover test

%files -n python3-versioneer -f %{pyproject_files}
%doc README.md details.md
%{_bindir}/versioneer

%changelog
%autochangelog
