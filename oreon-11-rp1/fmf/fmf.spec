%global source0_hash 131b557786b912f99d49d8dcc84196e3c2f39c5ce5ffe8b78e48150afd380dc3
Name:          fmf
Version:       1.7.0
Release:        1%{?dist}
Summary:        Flexible Metadata Format
License:       GPL-2.0-or-later
BuildArch:     noarch
URL:           https://github.com/teemtee/fmf
Source0:        https://files.pythonhosted.org/packages/source/f/fmf/fmf-%{version}.tar.gz
Requires:      git-core
Obsoletes:     python3-fmf < %{version}-%{release}
%py_provides   python3-fmf
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-fmf = %{version}-%{release}
# /oreon:deps
%package -n       python3-fmf+tests
Summary:        Metapackage for python3-fmf tests extras
Requires:       python3-fmf = %{version}-%{release}
Provides:       python3dist(fmf[tests]) = %{version}-%{release}

%description -n python3-fmf+tests
Metapackage for python3-fmf tests extras.

%package -n       python3-fmf+docs
Summary:        Metapackage for python3-fmf docs extras
Requires:       python3-fmf = %{version}-%{release}
Provides:       python3dist(fmf[docs]) = %{version}-%{release}

%description -n python3-fmf+docs
Metapackage for python3-fmf docs extras.

%description
The fmf Python module and command line tool implement a flexible
format for defining metadata in plain text files which can be
stored close to the source code. Thanks to hierarchical structure
with support for inheritance and elasticity it provides an
efficient way to organize data into well-sized text documents.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir fmf-%{version}
%oreon_prep
%build

%pyproject_wheel
cp docs/header.txt man.rst
tail -n+7 README.rst >> man.rst
rst2man man.rst > fmf.1
%install
%pyproject_install
mkdir -p %{buildroot}%{_mandir}/man1
install -pm 644 fmf.1* %{buildroot}%{_mandir}/man1
%oreon_autofiles main

%check

%pyproject_check_import
%files

%changelog

%autochangelog
