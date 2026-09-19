%global source0_hash b20394bed4689525f537bf8193c235324477b1963beb6d583690132c411b1b85

%global srcname kaptan

Name:           python-%{srcname}
Version:        0.6.0
Release:        7%{?dist}
Summary:        Configuration parser

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/emre/kaptan
Source:         %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

%description
%{summary}.

%package -n python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(pytest)
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}
sed -i -e 's/PyYAML>=3.13,<6/PyYAML/' requirements/base.txt

%build
%py3_build

%install
%py3_install

%check
%pytest -v tests

# A man page has been requested upstream here:
# https://github.com/emre/kaptan/issues/44
%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/
%{_bindir}/%{srcname}

%changelog
%autochangelog
