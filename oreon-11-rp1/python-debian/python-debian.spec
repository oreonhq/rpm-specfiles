%global source0_hash fe4fc3dc798dbf1f0ef5865e2b1b4f7cc0352b6a511b25ab7594906c64a73629
Name:           python-debian
Version:        1.1.1
Release:        1%{?dist}
Summary:        Modules for Debian-related data formats
License:        GPL-2.0-or-later AND GPL-3.0-or-later
Source0:        https://files.pythonhosted.org/packages/source/p/python_debian/python_debian-%{version}.tar.gz
URL:            https://salsa.debian.org/python-debian-team/python-debian
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61
BuildRequires:  python3dist(setuptools-scm[toml]) >= 6.2
Requires:       python3-debian = %{version}-%{release}
# /oreon:deps
%package -n       python3-debian+encodings
Summary:        Metapackage for python3-debian encodings extras
Requires:       python3-debian = %{version}-%{release}
Provides:       python3dist(debian[encodings]) = %{version}-%{release}

%description -n python3-debian+encodings
Metapackage for python3-debian encodings extras.

%package -n       python3-debian+test
Summary:        Metapackage for python3-debian test extras
Requires:       python3-debian = %{version}-%{release}
Provides:       python3dist(debian[test]) = %{version}-%{release}

%description -n python3-debian+test
Metapackage for python3-debian test extras.

%description

%package -n python3-debian
Summary:        Modules for Debian-related data formats
BuildRequires:  python3-devel
Requires:       python3-chardet
Requires:       xz
Requires:       python3-six
Suggests:       gnupg
%description -n python3-debian
This package provides Python modules that abstract many formats of Debian
related files. Currently handled are:
* Debtags information (debian.debtags module)
* debian/changelog (debian.changelog module)
* Packages files, pdiffs (debian.debian_support module)
* Control files of single or multiple RFC822-style paragraphs, e.g.
  debian/control, .changes, .dsc, Packages, Sources, Release, etc.
  (debian.deb822 module)
* Raw .deb and .ar files, with (read-only) access to contained
  files and meta-information

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir python_debian-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-debian usr/lib/python3*/site-packages/debian* usr/lib64/python3*/site-packages/debian* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/debian* usr/lib64/python3*/site-packages/debian* usr/bin/*

%check

%pyproject_check_import
%files
%files -n python3-debian -f %{oreon_filedir}/python3-debian.list

%changelog

%autochangelog
