%global source0_hash a0cbbd6634166ea8dfc16d0744d06f3205d51b86d539d0114decfb3f8fd85b41

Name:           python-htmlmin2
Version:        0.1.13
Release:        %autorelease
Summary:        Configurable HTML Minifier with safety features

License:        BSD-3-Clause AND Python-2.0.1
URL:            https://github.com/wilhelmer/htmlmin
Source:         %{url}/archive/v%{version}/htmlmin-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

# Vendored and modified copy of Lib/html/parser.py from cpython under
# htmlmin/python3html
# License: Python-2.0.1
Provides:       bundled(cpython) = 3.6

%global _description %{expand:
This package provides a configurable HTML Minifier with safety features. This
is a fork of htmlmin.}

%description %_description

%package -n     python3-htmlmin2
Summary:        %{summary}

%description -n python3-htmlmin2 %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n htmlmin-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l htmlmin

%check
%pytest -v

%files -n python3-htmlmin2 -f %{pyproject_files}
%doc README.rst CHANGELOG
%{_bindir}/htmlmin

%changelog
%autochangelog
