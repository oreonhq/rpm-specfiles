%global source0_hash c3d0d2f47602b21949ffb8669a7ef0a8ca5fa13ed5c1ee1d2d81edf05616187f

%bcond_without tests

%global srcname urwid

Name:          python-%{srcname}
Version:       3.0.4
Release:       %autorelease
Summary:       Console user interface library

# examples/twisted_serve_ssh.py is MIT
License:       LGPL-2.1-or-later AND MIT
URL:           http://excess.org/urwid/
Source0:        https://files.pythonhosted.org/packages/source/u/urwid/urwid-3.0.4.tar.gz

BuildArch:     noarch

%global _description\
Urwid is a Python library for making text console applications.  It has\
many features including fluid interface resizing, support for UTF-8 and\
CJK encodings, standard and custom text layout modes, simple markup for\
setting text attributes, and a powerful, dynamic list box that handles a\
mix of widget types.  It is flexible, modular, and leaves the developer in\
control.

%description %_description

%package -n python3-%{srcname}
Summary: %summary
%{?python_provide:%python_provide python3-urwid}
BuildRequires: python3-devel
BuildRequires: python3-pytest

%description -n python3-%{srcname} %_description

%generate_buildrequires
%pyproject_buildrequires

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{srcname}-%{version}
sed -i -e 's/--cov=urwid//' pyproject.toml
find urwid -type f -name "*.py" -exec sed -i -e '/^#!\//, 1d' {} \;
find urwid -type f -name "*.py" -exec chmod 644 {} \;

%build
%pyproject_wheel
find examples -type f -exec chmod 0644 \{\} \;

%check
%if %{with tests}
%pytest tests/
%endif

%install
%pyproject_install
%pyproject_save_files %{srcname}

%files -n python3-%{srcname} -f %{pyproject_files}
%license COPYING
%doc README.rst examples docs

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.0.4-1
- Prepare for Oreon 11 (RP1)
