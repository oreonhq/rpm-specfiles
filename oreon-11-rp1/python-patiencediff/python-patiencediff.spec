%global source0_hash d00911efd32e3bc886c222c3a650291440313ee94ac857031da6cc3be7935204

%global pypi_name patiencediff
Name:           python-patiencediff
Version:        0.2.15
Release:        8%{?dist}
Summary:        Python implementation of the patiencediff algorithm

License:        GPL-2.0-or-later
URL:            https://www.breezy-vcs.org/
Source:         %{pypi_source}

BuildRequires:  gcc
BuildRequires:  python3-devel

%global _description %{expand:
This package contains the implementation of the patiencediff algorithm, as
first described by Bram Cohen. Like Python's difflib, this module provides
both a convenience unified_diff function for the generation of unified diffs of
text files as well as a SequenceMatcher that can be used on arbitrary
lists. Patiencediff provides a good balance of performance, nice output for
humans, and implementation simplicity.}

%description %_description

%package -n     python3-patiencediff
Summary:        %{summary}

%description -n python3-patiencediff %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n patiencediff-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files patiencediff

%check
%py3_test_envvars %{python3} -m unittest patiencediff.test_patiencediff

%files -n python3-patiencediff -f %{pyproject_files}
%doc README.rst
%{_bindir}/patiencediff

%changelog
%autochangelog
