%global source0_hash a985492da81aa1588dfc056d9a7c6ca83f66254c0b90f25afc682a70713d4d4b
%global pypi_name pysol-cards
Name:           python-%{pypi_name}
Version:        0.24.0
Release:        6%{?dist}
Summary:        Deal PySol FC Cards
License:        MIT
URL:            https://fc-solve.shlomifish.org/
Source0:        https://files.pythonhosted.org/packages/source/p/pysol_cards/pysol_cards-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pysol-cards = %{version}-%{release}
# /oreon:deps
%description
The pysol-cards python module allows the python developer to generate the
initial deals of some PySol FC games.

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        Deal PySol FC Cards
%description -n python%{python3_pkgversion}-%{pypi_name}
The pysol-cards python module allows the python developer to generate the
initial deals of some PySol FC games.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n pysol_cards-%{version}
sed -i '/^#! \/usr\/bin\/env python\(3\)\?$/d' pysol_cards/*.py

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/pysol_cards* usr/lib64/python3*/site-packages/pysol_cards* usr/bin/*

%check

%pyproject_check_import
%files
%files -n python3-pysol-cards -f %{oreon_filedir}/python3-pysol-cards.list

%changelog

%autochangelog
