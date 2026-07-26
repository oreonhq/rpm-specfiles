%global source0_hash fe2d158e1fb7458ac5a3aaf9ff418d8ffdbb38edd45e6d5889d58525373a6d21

%global srcname zuul-sphinx

Name:           python-%{srcname}
Version:        0.4.1
Release:        24%{?dist}
Summary:        Sphinx extension for Zuul jobs

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://zuul-ci.org
Source0:        https://opendev.org/zuul/zuul-sphinx/archive/%{version}.tar.gz

BuildArch:      noarch

%description
A Sphinx extension for documenting Zuul jobs.

%package -n     python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr
Requires:       python3-pbr
Requires:       python3-sphinx
Requires:       python3-PyYAML
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
A Sphinx extension for documenting Zuul jobs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{srcname}
# Remove bundled eggs
rm -rf *requirements.txt %{srcname}.egg-info

%build
export PBR_VERSION=%{version}
%py3_build

%install
export PBR_VERSION=%{version}
%py3_install

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/zuul_sphinx-%{version}-py3*.egg-info/
%{python3_sitelib}/zuul_sphinx/

%changelog
%autochangelog
