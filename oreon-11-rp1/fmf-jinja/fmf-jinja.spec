%global source0_hash dd5403f12283cb7dfb6bea04a2474277d798ba6149cf38143258d1525073dd57

Name:           fmf-jinja
Version:        0.1.0
Release:        %autorelease
Summary:        Jinja template engine using FMF metadata

License:        GPL-3.0-or-later
URL:            https://github.com/LecrisUT/fmf-jinja
Source:         %{pypi_source fmf_jinja}

BuildArch:      noarch
BuildRequires:  python3-devel

%py_provides python3-fmf-jinja

%description
Jinja template engine using FMF metadata

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n fmf_jinja-%{version}
# Workaround for hatchling not preserving symlinks
# https://github.com/pypa/hatch/issues/2008
mkdir -p test/data/input
cp -r example/* test/data/input

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l fmf_jinja

%check
%pytest

%files -f %{pyproject_files}
%{_bindir}/fmf-jinja
%doc README.md

%changelog
%autochangelog
