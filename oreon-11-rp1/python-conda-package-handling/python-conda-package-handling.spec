%global source0_hash a68d23d795704f1b687559b89c98e73d0dbebcab077592c60bffc1dc408b72e9

%?python_enable_dependency_generator
%global srcname conda-package-handling
%global pkgname conda_package_handling

Name:           python-%{srcname}
Version:        2.4.0
Release:        %autorelease
Summary:        Create and extract conda packages of various formats

License:        BSD-3-Clause
URL:            https://github.com/conda/%{srcname}
Source0:        https://github.com/conda/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
Create and extract conda packages of various formats.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-bottle
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-pytest-mock

%description -n python%{python3_pkgversion}-%{srcname}
Create and extract conda packages of various formats.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}
sed -i -e s/archive_and_deps/archive/ setup.py
# do not run coverage in pytest
sed -i -E '/--(no-)?cov/d' setup.cfg

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pkgname}

%check
%pytest -v -rs tests

%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc AUTHORS.md CHANGELOG.md README.md
%{_bindir}/cph

%changelog
%autochangelog
