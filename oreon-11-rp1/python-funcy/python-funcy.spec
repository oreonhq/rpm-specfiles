%global source0_hash feaebecc5292eed08a9c73c20417a4bb9ab2578a0782ecfca39af7c79e88d4c6

%global srcname funcy

Name:           python-%{srcname}
Version:        1.17
Release:        14%{?dist}
Summary:        Fancy and practical functional tools

License:        BSD-3-Clause
URL:            https://github.com/Suor/funcy
Source:		https://github.com/Suor/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:	python3-devel

%global _description \
A collection of fancy functional tools focused on practicality.

%description %{_description}

%package     -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
# we're skipping the tests because python-whatever is retired

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst CHANGELOG

%changelog
%autochangelog
