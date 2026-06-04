%global source0_hash 3a9db79836977e53806dff2c160a258ebba2eba8d3a2fc9435aeac94c1434cde

%global modname iso639

Name:           python-%{modname}
Version:        0.1.4
Release:        33%{?dist}
Summary:        ISO639-2 support for Python

License:        MIT
URL:            https://github.com/janpipek/iso639-python
Source0:        https://github.com/janpipek/iso639-python/archive/refs/tags/v0.1.4/iso639-0.1.4.tar.gz

BuildArch:      noarch

%description
A simple (really simple) library for working with ISO639-2 language codes.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{modname}
A simple (really simple) library for working with ISO639-2 language codes.

Python 3 version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{modname}-python-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{modname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{modname}-*.egg-info/
%{python3_sitelib}/%{modname}/

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.1.4-33
- Prepare for Oreon 11 (RP1)
