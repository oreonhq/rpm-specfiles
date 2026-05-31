%global source0_hash fa26203291bfc97b53976c9e0c5152a3340a6aa42bd1497a2771a997b6f6ee32

%global modname rpmfluff

Name:          python-%{modname}
Version:       0.6.7
Release:       1%{?dist}
Summary:       Lightweight way of building RPMs, and sabotaging them

License:       GPL-2.0-or-later
URL:           https://pagure.io/rpmfluff
Source0:        https://pagure.io/releases/%{modname}/%{modname}-%{version}.tar.xz

BuildArch:     noarch

%global _description \
rpmfluff provides a python library for building RPM packages, and\
sabotaging them so they are broken in controlled ways.\
\
It is intended for use when validating package analysis tools such as RPM lint.\
It can also be used to construct test cases for package management software\
such as RPM, YUM, and DNF.

%description %{_description}

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-rpm
Requires:       rpm-build
Requires:       createrepo_c

%description -n python3-%{modname} %{_description}

Python 3 version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{modname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%check
python3 -m unittest %{modname}.test

%files -n python3-%{modname}
%license LICENSE
%doc README.md
%{python3_sitelib}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.6.7-1
- Prepare for Oreon 11 (RP1)
