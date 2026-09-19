%global source0_hash 102a0ffbf952124f1be222fd6989da4ec7cce04e49f613009e5f54ad37618825

Summary:       Curses-like terminal wrapper, with colored strings
Name:          python-curtsies
Version:       0.4.3
Release:       6%{?dist}
License:       MIT
URL:           https://github.com/bpython/curtsies
Source0:       https://files.pythonhosted.org/packages/source/c/curtsies/curtsies-%{version}.tar.gz
BuildArch:     noarch
BuildRequires: python3-blessed
BuildRequires: python3-blessings
BuildRequires: python3-cwcwidth
BuildRequires: python3-devel
BuildRequires: python3-pyte
BuildRequires: python3-pytest
BuildRequires: python3-setuptools
%global _description\
Curtsies is curses-like terminal wrapper, can be to annotate portions\
of strings with terminal colors and formatting.\
\
Most terminals will display text in color if you use ANSI escape codes\
- curtsies makes rendering such text to the terminal easy. Curtsies\
assumes use of an VT-100 compatible terminal: unlike curses, it has no\
compatibility layer for other types of terminals.
%description %_description

%package     -n python3-curtsies
Summary:        %summary
Requires:       python3-blessings >= 1.5
Requires:       python3-cwcwidth
%description -n python3-curtsies %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n curtsies-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l curtsies

%check
%pytest

%files -n python3-curtsies -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
