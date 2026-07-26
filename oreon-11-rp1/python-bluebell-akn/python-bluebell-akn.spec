%global source0_hash 9635050a311f8effeb46888e573aa4871eb54aa24d7f700bf087620c1fb4525a

Name:           python-bluebell-akn
Version:        3.1.1
Release:        %autorelease
Summary:        Transforms text to and from Akoma Ntoso

License:        LGPL-3.0-or-later
URL:            https://github.com/laws-africa/bluebell
Source:         %{pypi_source bluebell_akn}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Bluebell is a (fairly) generic Akoma Ntoso 3 parser, supporting all
hierarchical elements and multiple document types.

Bluebell supports the following Akoma Ntoso (AKN) document types:

act, bill (hierarchicalStructure)
debateReport, doc, statement (openStructure)
judgment (judgmentStructure)
Bluebell tries to walk the line between being expressive and supporting a range
of AKN documents and structures, while being simple to use and not requiring
that authors have an in-depth knowledge of AKN.

Bluebell will always produce structurally valid Akoma Ntoso, no matter what
input is given. It will never refuse to parse malformed input. If it does, it's
a bug.}

%description %_description

%package -n     python3-bluebell-akn
Summary:        %{summary}

%description -n python3-bluebell-akn %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n bluebell_akn-%{version}

%generate_buildrequires
%pyproject_buildrequires 

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l bluebell

%check
%pyproject_check_import
%{py3_test_envvars} %{python3} -m unittest

%files -n python3-bluebell-akn -f %{pyproject_files}
%{_bindir}/bluebell
%doc README.md

%changelog
%autochangelog
