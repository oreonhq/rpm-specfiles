%global source0_hash c0959a121ef94542e807a674142606f7e90214a2b3d1eb17300244bbb5cc2bfc

%global pypi_name jsmin

Name:           python-%{pypi_name}
Version:        3.0.1
Release:        15%{?dist}
Summary:        JavaScript minifier

License:        MIT
URL:            https://github.com/tikitu/jsmin
Source0:        %{pypi_source}

# https://github.com/tikitu/jsmin/pull/38
Patch0:		invalid_escape_sequence-dep-warn.patch

BuildArch:      noarch

BuildRequires:	python3-devel
BuildRequires:	python3-pytest
BuildRequires:	pyproject-rpm-macros
%py_provides python3-%{pypi_name}

%description
%{summary}.

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files jsmin

%check
%pytest jsmin/test.py

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst CHANGELOG.txt

%changelog
%autochangelog
