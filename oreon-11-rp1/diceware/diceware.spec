%global source0_hash 54b690809f0c56ab3085a18e15a0c3804d4a0d127f38aef0b5cf5f859d0f6639
Name:		diceware
Version:	1.0.1
Release:        1%{?dist}
Summary:        Create passphrases which one can remember
License:	GPL-3.0-or-later and MIT and CC-BY-3.0 and CC0-1.0 and CC-BY-4.0
URL:		https://pypi.python.org/pypi/diceware
Source0:        https://files.pythonhosted.org/packages/source/d/%{name}/%{name}-%{version}.tar.gz
BuildArch:	noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-diceware = %{version}-%{release}
# /oreon:deps
%package -n       python3-diceware+tests
Summary:        Metapackage for python3-diceware tests extras
Requires:       python3-diceware = %{version}-%{release}
Requires:       python3dist(pytest) >= 2.8.3
Provides:       python3dist(diceware[tests]) = %{version}-%{release}

%description -n python3-diceware+tests
Metapackage for python3-diceware tests extras.

%package -n       python3-diceware+docs
Summary:        Metapackage for python3-diceware docs extras
Requires:       python3-diceware = %{version}-%{release}
Provides:       python3dist(diceware[docs]) = %{version}-%{release}

%description -n python3-diceware+docs
Metapackage for python3-diceware docs extras.

%package -n       python3-diceware+dev
Summary:        Metapackage for python3-diceware dev extras
Requires:       python3-diceware = %{version}-%{release}
Provides:       python3dist(diceware[dev]) = %{version}-%{release}

%description -n python3-diceware+dev
Metapackage for python3-diceware dev extras.

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
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
mkdir -p %{buildroot}%{_mandir}/man1
rst2man docs/manpage.rst %{buildroot}%{_mandir}/man1/diceware.1
pushd docs
PYTHONPATH=%{buildroot}%{python3_sitelib} sphinx-build-3 -b html -d _build/doctrees . _build/html
popd
rm -rf docs/_build/.buildinfo
rm -rf docs/_build/html/.buildinfo
rm -rf docs/_build/.doctrees
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pytest
%files
%files -n diceware-doc -f %{oreon_filedir}/diceware-doc.list

%changelog

%autochangelog
