%global source0_hash 92fe624675e41f41f59de1208e0125dfaa8d062bbe6138bd7cd79e4dd0b6f85e

# tests depend on a git checkout of mailman server
%bcond_with tests

%global srcname mailmanclient

Name:           python-%{srcname}
Version:        3.3.3
Release:        %autorelease
Summary:        Python bindings for Mailman REST API
License:        LGPL-3.0-or-later
URL:            http://www.list.org/
Source0:        %{pypi_source %{srcname}}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%global _description %{expand:
The mailmanclient library provides official Python bindings for the GNU Mailman
3 REST API.}

%description %{_description}

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}

%description -n python%{python3_pkgversion}-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%if %{with tests}
%pyproject_buildrequires -t -x testing
%else
%pyproject_buildrequires
%endif

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%if %{with tests}
%check
%tox
%endif

%files -n  python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%license COPYING.LESSER
%doc README.rst

%changelog
%autochangelog
