%global source0_hash a985492da81aa1588dfc056d9a7c6ca83f66254c0b90f25afc682a70713d4d4b

%global pypi_name pysol-cards

Name:           python-%{pypi_name}
Version:        0.24.0
Release:        6%{?dist}
Summary:        Deal PySol FC Cards
License:        MIT
URL:            https://fc-solve.shlomifish.org/
Source0:        %{pypi_source pysol_cards}
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel

%description
The pysol-cards python module allows the python developer to generate the
initial deals of some PySol FC games.

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}

%description -n python%{python3_pkgversion}-%{pypi_name}
The pysol-cards python module allows the python developer to generate the
initial deals of some PySol FC games.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n pysol_cards-%{version}
sed -i '/^#! \/usr\/bin\/env python\(3\)\?$/d' pysol_cards/*.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
# Must do the default python version install last because
# the scripts in /usr/bin are overwritten with every setup.py install.
%pyproject_install
%pyproject_save_files -l pysol_cards

%check
%pyproject_check_import

%files -n python%{python3_pkgversion}-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
