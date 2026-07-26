%global source0_hash 39751a2d28d40c88538cc03aa72a113dcae59fc49e8e7727f30219a6cc9ef997

%global srcname Mathics_Scanner

Name:           python-mathics-scanner
Version:        1.3.0
Release:        %autorelease
Summary:        Character Tables and Tokenizer for Mathics and the Wolfram Language

License:        GPL-3.0-only
URL:            https://mathics.org
Source:         %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
This package provides character tables and a tokenizer for Mathics and the
Wolfram Language.}

%description %_description

%package -n     python3-mathics-scanner
Summary:        %{summary}
Recommends:     python3dist(mathics_scanner[full]) = %{version}-%{release}

%description -n python3-mathics-scanner %_description

%pyproject_extras_subpkg -n python3-mathics-scanner full

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -x full

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files mathics_scanner

%check
%pytest

%files -n python3-mathics-scanner -f %{pyproject_files}
%license COPYING.txt
%doc README.rst CHANGES.rst AUTHORS.txt ChangeLog
%{_bindir}/mathics-generate-json-table

%changelog
%autochangelog
