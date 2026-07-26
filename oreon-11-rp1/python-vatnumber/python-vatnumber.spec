%global source0_hash 4e9e9cabcff6076d8deb8a347edfd5d0ab8cab1ed344fdbe5dd4a6110a2f2c7b

%global srcname vatnumber
%global sum Python module to validate VAT numbers

Name:           python-%{srcname}
Version:        1.2
Release:        39%{?dist}
Summary:        %{sum}

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://code.google.com/p/vatnumber
Source0:        http://pypi.python.org/packages/source/v/%{srcname}/%{srcname}-%{version}.tar.gz
Patch0:         %{srcname}-1.2-py3.patch

BuildArch:      noarch

BuildRequires:	python3-devel
BuildRequires:	python3-pytest
BuildRequires:	pyproject-rpm-macros

%py_provides python3-%{srcname}

%description
%{sum}.

%package -n python3-%{srcname}
Summary:        %{sum}

%description -n python3-%{srcname}
%{sum}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{srcname}-%{version}
%patch -P0 -p1

# setup command: use_2to3 is invalid
sed -i '/use_2to3/d' setup.py
# DeprecationWarning: Please use assertTrue instead.
sed -i 's/self.assert_/assert /g' vatnumber/tests.py

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files vatnumber

%check
# test_vies trying to connect ec.europa.eu
%pytest -k 'not test_vies' vatnumber/tests.py

%files -n python3-%{srcname} -f %{pyproject_files}
%license COPYRIGHT LICENSE
%doc CHANGELOG README

%changelog
%autochangelog
