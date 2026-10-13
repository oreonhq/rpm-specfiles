%global source0_hash fe4fc3dc798dbf1f0ef5865e2b1b4f7cc0352b6a511b25ab7594906c64a73629

Name:           python-debian
Version:        1.1.1
Release:        %autorelease
Summary:        Modules for Debian-related data formats
# debfile.py, arfile.py, debtags.py are release under GPL v3 or above
# everything else is GPLv2+
License:        GPL-2.0-or-later AND GPL-3.0-or-later
Source0:        %{pypi_source python_debian}
URL:            https://salsa.debian.org/python-debian-team/python-debian
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
#tests
BuildRequires:  dpkg
BuildRequires:  python3-chardet
BuildRequires:  python3-pytest
%if ! 0%{?rhel}
BuildRequires:  python3-apt
%endif

%global _description\
This package provides Python modules that abstract many formats of Debian\
related files. Currently handled are:\
* Debtags information (debian.debtags module)\
* debian/changelog (debian.changelog module)\
* Packages files, pdiffs (debian.debian_support module)\
* Control files of single or multiple RFC822-style paragraphs, e.g.\
  debian/control, .changes, .dsc, Packages, Sources, Release, etc.\
  (debian.deb822 module)\
* Raw .deb and .ar files, with (read-only) access to contained\
  files and meta-information

%description %_description

%package -n python3-debian
Summary:        Modules for Debian-related data formats
BuildRequires:  python3-devel
Requires:       python3-chardet
Requires:       xz
Requires:       python3-six
Suggests:       gnupg
%if ! 0%{?rhel}
Recommends:     python3-apt
%endif

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

%autosetup -p1 -n python_debian-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files debian

%check
%pyproject_check_import

%files -n python3-debian -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
