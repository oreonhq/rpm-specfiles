%global source0_hash 54b690809f0c56ab3085a18e15a0c3804d4a0d127f38aef0b5cf5f859d0f6639

Name:		diceware
Version:	1.0.1
Release:	6%{?dist}
Summary:	Create passphrases which one can remember

# Code is GPL-3.0-or-later but then there are the wordlists:
License:	GPL-3.0-or-later and MIT and CC-BY-3.0 and CC0-1.0 and CC-BY-4.0
URL:		https://pypi.python.org/pypi/diceware
Source0:	https://files.pythonhosted.org/packages/source/d/%{name}/%{name}-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	python3-devel
BuildRequires:	python3-pytest
BuildRequires:	%{_bindir}/rst2man

%description
A simple command line tool which can create simple passphrases
which human can remember.

%package doc
Summary:    Documentation for Diceware
BuildArch:  noarch
BuildRequires:	python3-sphinx
BuildRequires:	python3-sphinx_rtd_theme
%description doc
Diceware is a simple command line tool which can create simple
passphrases which human can remember.

This package provides documentation for Diceware.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l diceware
mkdir -p %{buildroot}%{_mandir}/man1
rst2man docs/manpage.rst %{buildroot}%{_mandir}/man1/diceware.1

pushd docs
PYTHONPATH=%{buildroot}%{python3_sitelib} sphinx-build-3 -b html -d _build/doctrees . _build/html
popd

# Remove unneeded build artifacts.
rm -rf docs/_build/.buildinfo
rm -rf docs/_build/html/.buildinfo
rm -rf docs/_build/.doctrees

%check
%pytest

%files doc
%doc docs/_build/html

%files -f %{pyproject_files}
%doc README.rst COPYRIGHT
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/diceware.1*

%changelog
%autochangelog
