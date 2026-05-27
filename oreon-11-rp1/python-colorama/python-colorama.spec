%global source0_hash 2d0543c3970840160b32656ab83d43b7f3533208c2c5f3ee5b839940d00af0bd

%global pypi_name colorama

Name:           python-%{pypi_name}
Version:        0.4.6
Release:        %autorelease
Summary:        Cross-platform colored terminal text

License:        BSD-3-Clause
URL:            https://github.com/tartley/colorama
Source0:        https://github.com/tartley/colorama/archive/0.4.6/colorama-0.4.6.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
# for check
BuildRequires:  python3dist(pytest)


%description
Makes ANSI escape character sequences, for producing colored
terminal text and cursor positioning, work under MS Windows.

ANSI escape character sequences have long been used to produce colored terminal
text and cursor positioning on Unix and Macs. Colorama makes this work on
Windows, too.
It also provides some shortcuts to help generate ANSI sequences, and works fine
in conjunction with any other ANSI sequence generation library, such as
Termcolor.

%package -n python3-%{pypi_name}
Summary:        Cross-platform colored terminal text

%description -n python3-%{pypi_name}
Makes ANSI escape character sequences, for producing colored
terminal text and cursor positioning, work under MS Windows.

ANSI escape character sequences have long been used to produce colored terminal
text and cursor positioning on Unix and Macs. Colorama makes this work on
Windows, too.
It also provides some shortcuts to help generate ANSI sequences, and works fine
in conjunction with any other ANSI sequence generation library, such as
Termcolor.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files colorama

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc CHANGELOG.rst README.rst
%license LICENSE.txt

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.4.6-1
- Prepare for Oreon 11 (RP1)
