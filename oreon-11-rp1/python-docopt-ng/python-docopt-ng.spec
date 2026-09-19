%global source0_hash 91c6da10b5bb6f2e9e25345829fb8278c78af019f6fc40887ad49b060483b1d7

Name:           python-docopt-ng
Version:        0.9.0
Release:        %autorelease
Summary:        Humane command line arguments parser
License:        MIT
URL:            https://github.com/jazzband/docopt-ng
Source:         %{pypi_source docopt_ng}
BuildArch:      noarch

%global _description %{expand:
docopt-ng helps you create beautiful command-line interfaces.  The option
parser is generated based on the docstring that is passed to docopt function.
docopt parses the usage pattern ("Usage: ...") and option descriptions (lines
starting with dash "-") and ensures that the program invocation matches the
usage pattern; it parses options, arguments and commands based on that.  The
basic idea is that a good help message has all necessary information in it to
make a parser.}

%description %{_description}

%package -n python3-docopt-ng
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

# This software is a fork of the original docopt.  The fork switched from a
# python module (docopt.py) to a python package (docopt/__init__.py), so
# technically the rpm packages could be co-installable.  However, they are not
# co-usable, because python code can only import one or the other.  For this
# reason, we will go ahead and conflict with other rpm package.
Conflicts:      python3-docopt

%description -n python3-docopt-ng %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n docopt_ng-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files docopt

%check
%pytest

%files -n python3-docopt-ng -f %{pyproject_files}
%license LICENSE-MIT
%doc README.md

%changelog
%autochangelog
