%global source0_hash 0e647e525ba47523fa400a58fdec090b1cc6dcec4afbf095ee01e9e589e5a5ef

%{?python_enable_dependency_generator}
%global pkgname jinja2-time

Name:           python-jinja2-time
Version:        0.2.0
Release:        34%{?dist}
Summary:        Jinja2 Extension for Dates and Times

License:        MIT
URL:            https://github.com/hackebrot/jinja2-time
Source0:        https://github.com/hackebrot/%{pkgname}/archive/%{version}.tar.gz
# Comaptibility on newer arrow modules, from upstream MR: https://github.com/hackebrot/jinja2-time/pull/19
Patch0:         arrow-compat.patch
BuildArch:      noarch

%description
Jinja2 Extension for Dates and Times

%package     -n python3-%{pkgname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pkgname}}
BuildRequires:  python3-devel
BuildRequires:  python3-arrow
BuildRequires:  python3-jinja2
# Required for tests
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(freezegun)

%description -n python3-%{pkgname}
Jinja2 Extension for Dates and Times.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n %{pkgname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files jinja2_time

%check
%pytest tests

%files -n python3-%{pkgname} -f %{pyproject_files}
%license LICENSE
%doc *.rst

%changelog
%autochangelog
