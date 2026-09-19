%global source0_hash 9fe5da7ec53510881dd35d7a5c677ba45f34cfe6a8e78d1abd20652cf82139a8

Name:           python-prettyprinter
Version:        0.18.0
Release:        %autorelease
Summary:        Syntax-highlighting, declarative and composable pretty printer
License:        MIT
URL:            https://github.com/tommikaikkonen/prettyprinter
BuildArch:      noarch
Source:         %{pypi_source prettyprinter}
# downstream-only patch
Patch:          0001-Avoid-build-requirement-on-pytest-runner.patch

%global _description %{expand:
Syntax-highlighting, declarative and composable pretty printer.  Drop in
replacement for the standard library pprint: just rename pprint to
prettyprinter in your imports.  Uses a modified Wadler-Leijen layout algorithm
for optimal formatting.  Write pretty printers for your own types with a dead
simple, declarative interface.}

%description %_description

%package -n python3-prettyprinter
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-hypothesis
BuildRequires:  python3-attrs
BuildRequires:  python3-ipython
BuildRequires:  python3-pytz

%description -n python3-prettyprinter %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n prettyprinter-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l prettyprinter

%check
# Many tests do not work with current versions of other software.
%pytest \
    --ignore tests/test_django \
    --ignore tests/test_ast.py \
    --ignore tests/test_numpy.py \
    --ignore tests/test_requests.py \
    --verbose

%files -n python3-prettyprinter -f %{pyproject_files}
%doc HISTORY.rst README.rst

%changelog
%autochangelog
