%global source0_hash 77ca4d7e436863f198a7754385493e2c2506168c4685d16bf86dd91948a4841c

Name:           python-pygments-ansi-color
Version:        0.3.0
Release:        %autorelease
Summary:        ANSI color-code highlighting

License:        Apache-2.0
URL:            https://github.com/chriskuehl/pygments-ansi-color
# PyPI tarball doesn't include tests
Source:         %{url}/archive/v%{version}/pygments-ansi-color-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
This package provides an ANSI color-code highlighting lexer for Pygments.}

%description %_description

%package -n     python3-pygments-ansi-color
Summary:        %{summary}

%description -n python3-pygments-ansi-color %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n pygments-ansi-color-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pygments_ansi_color

%check
%pytest -v

%files -n python3-pygments-ansi-color -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
