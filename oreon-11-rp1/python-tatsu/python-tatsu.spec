%global source0_hash 953634c319e62ac49aac2d01138856c09e1e0a9d0f369c541ab6f213659b6a9a

%global srcname TatSu
%global forgeurl https://github.com/neogeny/TatSu

Name:           python-tatsu
Version:        5.13.1
Release:        %autorelease
Summary:        Python parser generator from grammars in a variation of EBNF

License:        BSD-3-Clause-Attribution
URL:            https://tatsu.readthedocs.io
# PyPI tarball doesn't include tests
Source:         %{forgeurl}/archive/v%{version}/%{srcname}-%{version}.tar.gz
# Add missing license text for markdown_parser.leg
Patch:          %{forgeurl}/pull/367.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  sed

%global _description %{expand:
TatSu is a tool that takes grammars in a variation of EBNF as input, and
outputs memoizing (Packrat) PEG parsers in Python.}

%description %_description

%package -n     python3-tatsu
Summary:        %{summary}

%description -n python3-tatsu %_description

%pyproject_extras_subpkg -n python3-tatsu colorization,parproc

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

# Drop unneeded shebangs
sed -r -i '1{/^#!/d}' tatsu/bootstrap.py tatsu/g2e/__init__.py

%generate_buildrequires
%pyproject_buildrequires -x colorization,parproc

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l tatsu

%check
%pytest -v

%files -n python3-tatsu -f %{pyproject_files}
%doc README.rst
%{_bindir}/g2e
%{_bindir}/tatsu

%changelog
%autochangelog
