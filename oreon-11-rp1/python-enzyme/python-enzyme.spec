%global source0_hash b5744e59d9d83e40909ee2407e6e30d065b36c3123ab7d9e36839db5e9bdf703

%global srcname enzyme

Name:           python-%{srcname}
Version:        0.5.2
Release:        9%{?dist}
Summary:        Python module to parse video metadata
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/Diaoul/enzyme
Source:         %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# Tests disabled
#BuildRequires:  PyYAML
#BuildRequires:  python3-PyYAML
#BuildRequires:  python2-requests
#BuildRequires:  python3-requests

%global _description %{expand:
Enzyme is a Python module to parse video metadata.}

%description %_description

%package -n python3-%{srcname}
Summary:        %summary
%{?python_provide:%python_provide python3-%{srcname}}
Suggests:       %{name}-doc

%description -n python3-%{srcname} %_description

%package doc
Summary:        %summary

%description doc %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
# Tests disabled because they try to download files
#%%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE

%files doc
%doc README.md docs/index.rst docs/api
%license LICENSE

%changelog
%autochangelog
