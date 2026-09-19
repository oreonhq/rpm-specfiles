%global source0_hash 131b557786b912f99d49d8dcc84196e3c2f39c5ce5ffe8b78e48150afd380dc3

Name:          fmf
Version:       1.7.0
Release:       6%{?dist}

Summary:       Flexible Metadata Format
License:       GPL-2.0-or-later
BuildArch:     noarch

URL:           https://github.com/teemtee/fmf
Source:        %{pypi_source fmf}

# Main fmf package requires the Python module
BuildRequires: python3-devel
BuildRequires: python3dist(docutils)
BuildRequires: git-core
Requires:      git-core

Obsoletes:     python3-fmf < %{version}-%{release}
%py_provides   python3-fmf

%description
The fmf Python module and command line tool implement a flexible
format for defining metadata in plain text files which can be
stored close to the source code. Thanks to hierarchical structure
with support for inheritance and elasticity it provides an
efficient way to organize data into well-sized text documents.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n fmf-%{version}

%generate_buildrequires
%pyproject_buildrequires -x tests %{?epel:-w}

%build
%pyproject_wheel
cp docs/header.txt man.rst
tail -n+7 README.rst >> man.rst
rst2man man.rst > fmf.1

%install
%pyproject_install
%pyproject_save_files fmf

mkdir -p %{buildroot}%{_mandir}/man1
install -pm 644 fmf.1* %{buildroot}%{_mandir}/man1

%check
%pyproject_check_import

%files -f %{pyproject_files}
%{_mandir}/man1/*
%{_bindir}/%{name}
%doc README.rst examples

%changelog
%autochangelog
