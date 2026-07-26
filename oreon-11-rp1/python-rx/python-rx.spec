%global source0_hash a048a6e894fc9da992b186a74ff494fdb59cab5422b5bf23ebe7adcf490dcdc6

# what it's called on pypi
%global srcname Rx
# what it's imported as
%global libname rx
# name of egg info directory
%global eggname %{srcname}
# package name fragment
%global pkgname %{libname}

%global _description \
Rx is a library for composing asynchronous and event-based programs using\
observable collections and LINQ-style query operators in Python.

%bcond_with tests

Name:           python-%{pkgname}
Version:        4.1.0
Release:        %autorelease
Summary:        Reactive Extensions (Rx) for Python
License:        MIT
URL:            https://github.com/ReactiveX/RxPY
# PyPI tarball doesn't have tests
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
Patch0:         import-order.patch

BuildArch:      noarch

%description %{_description}

%package -n python3-%{pkgname}
Summary:        %{summary}
BuildRequires:  python3-coverage
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-asyncio

%description -n python3-%{pkgname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n RxPY-%{version} -p 1

# Ugh.
sed -i s/0.0.0/%{version}/g pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%if %{with tests}
%check
%pytest --verbose
%endif

%files -n python3-%{pkgname}
%license LICENSE
%doc README.rst authors.txt changes.md
%{python3_sitelib}/reactivex/
%{python3_sitelib}/reactivex-%{version}.dist-info/

%changelog
%autochangelog
