%global source0_hash 5ab283b9857211d61b53318b7c792cf68e798e765ee17c27ade9f6c924235731
Name:           python-versioneer
Version:        0.29
Release:        1%{?dist}
Summary:        Easy VCS-based management of project version strings
License:        Unlicense
URL:            https://github.com/warner/python-versioneer
Source0:        https://files.pythonhosted.org/packages/32/d7/854e45d2b03e1a8ee2aa6429dd396d002ce71e5d88b77551b2fb249cb382/versioneer-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-versioneer = %{version}-%{release}
# /oreon:deps
%package -n       python3-versioneer+toml
Summary:        Metapackage for python3-versioneer toml extras
Requires:       python3-versioneer = %{version}-%{release}
Provides:       python3dist(versioneer[toml]) = %{version}-%{release}

%description -n python3-versioneer+toml
Metapackage for python3-versioneer toml extras.

%description

%package -n     python3-versioneer
Summary:        Easy VCS-based management of project version strings
%description -n python3-versioneer

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir versioneer-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
sed -r -i '1{/^#!/d}' %{buildroot}%{python3_sitelib}/versioneer.py
%oreon_autofiles python3-versioneer usr/lib/python3*/site-packages/versioneer* usr/lib64/python3*/site-packages/versioneer* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/versioneer* usr/lib64/python3*/site-packages/versioneer* usr/bin/*

%check

%{python3} setup.py make_versioneer
%{python3} -m unittest discover test
%files
%files -n python3-versioneer -f %{oreon_filedir}/python3-versioneer.list

%changelog

%autochangelog
