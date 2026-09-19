%global source0_hash 3bb9cf07f606260584b1df46399c0b87dd84773e7b25912b7e391e30797c5e72

%global srcname shortuuid

Name:           python-%{srcname}
Version:        1.0.13
Release:        %autorelease
Summary:        A generator library for concise, unambiguous and URL-safe UUIDs
License:        BSD-3-Clause
URL:            https://github.com/skorokithakis/shortuuid
Source0:        %{pypi_source %{srcname}}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
# Test dependencies:
BuildRequires:  python3dist(django)
BuildRequires:  python3dist(pytest)
# shortuuid.django_fields generates UUIDs for Django
Enhances:       python3dist(django)

%global _description %{expand:
shortuuid is a simple python library that generates concise, unambiguous,
URL-safe UUIDs.

Often, one needs to use non-sequential IDs in places where users will see them,
but the IDs must be as concise and easy to use as possible. shortuuid solves
this problem by generating uuids using Python's built-in uuid module and then
translating them to base57 using lowercase and uppercase letters and digits, and
removing similar-looking characters such as l, 1, I, O and 0.}

%description %{_description}

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}

%description -n python%{python3_pkgversion}-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

# this file is wrongly copied with poetry-core<2
rm -f %{buildroot}%{python3_sitelib}/COPYING

%check
%pytest -V

%files -n  python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%license COPYING
%doc README.md
%{_bindir}/shortuuid

%changelog
%autochangelog
