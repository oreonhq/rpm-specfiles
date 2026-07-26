%global source0_hash 15d600052cbe9991203d86195613f1a472157794b8477d87a93b6c1a74ae151e

%global srcname babelfish

Name: python-%{srcname}
Version: 0.6.1
Release: 9%{?dist}
Summary: Python library to work with countries and languages
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
URL: https://babelfish.readthedocs.org/
Source: https://github.com/Diaoul/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: python3dist(pytest)

%global _description %{expand:
Babelfish makes it easy to work with countries, languages, scripts, ISO codes
and IETF codes from Python. It has converters between all different data
can be extended to use custom converters and data.}

%description %_description

%package -n python3-%{srcname}
Summary: %{summary}

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -L %{srcname}

%check
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
