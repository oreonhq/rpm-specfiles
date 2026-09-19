%global source0_hash 399e2422bfd0e012081a214b496dbe152e5c2c8581f8b9e85017d5b07269b589

%global srcname colcon-alias

Name:           python-%{srcname}
Version:        0.1.1
Release:        7%{?dist}
Summary:        Extension for colcon to create and modify command aliases

License:        Apache-2.0
URL:            https://github.com/colcon/%{srcname}
Source0:        https://github.com/colcon/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

# Not submitted upstream - compatibility with pytest 2.9.X
Patch0:         %{name}-0.1.1-pytest-compat.patch

BuildArch:      noarch

%description
An extension for colcon-core to create and modify command aliases.

Aliases condense any number of colcon command invocations made up of a verb
followed by all associated arguments down to another 'alias' verb. When
invoking the alias verb, additional arguments can be appended to the original
invocations.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-colcon-core >= 0.17.0
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-filelock
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-PyYAML
BuildRequires:  python%{python3_pkgversion}-setuptools >= 30.3.0
Conflicts:      python%{python3_pkgversion}-colcon-mixin < 0.2.2
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-colcon-core >= 0.17.0
Requires:       python%{python3_pkgversion}-filelock
Requires:       python%{python3_pkgversion}-PyYAML
%endif

%description -n python%{python3_pkgversion}-%{srcname}
An extension for colcon-core to create and modify command aliases.

Aliases condense any number of colcon command invocations made up of a verb
followed by all associated arguments down to another 'alias' verb. When
invoking the alias verb, additional arguments can be appended to the original
invocations.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
%pytest -m 'not linter' test

%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/colcon_alias/
%{python3_sitelib}/colcon_alias-%{version}-py%{python3_version}.egg-info/

%changelog
%autochangelog
