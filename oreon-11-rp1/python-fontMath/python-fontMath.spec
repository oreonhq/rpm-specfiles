%global source0_hash 1fd9190c9d784e1305c3c49771b91d910f246a4b7c44ede219c99a07ed7aeda4

%global srcname fontMath
%global lcname fontmath

Name:           python-%{srcname}
Version:        0.9.4
Release:        7%{?dist}
Summary:        A set of objects for performing math operations on font data

License:        MIT 
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        %{pypi_source %{lcname} 0.9.4 zip}

BuildArch:      noarch
BuildRequires:  python3-devel

%description
A set of objects for performing math operations on font data.

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname}
A set of objects for performing math operations on font data.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{lcname}-%{version}
# Relax version requirement
sed -i 's/fonttools==4.43.0/fonttools>=4.43.0/g' requirements.txt

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l fontMath

%check
export LC_ALL=C.UTF-8
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}

%changelog
%autochangelog
