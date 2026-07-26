%global source0_hash ddff80acdebfffc9cb7de2e20761936ea06fcc7cf362678d4b66bd7bbce9e8e2

%global srcname SimpleTAL
%global pkgname simpletal

Name:		python3-%{pkgname}
Version:	5.2
Release:	36%{?dist}
Summary:	An XML based template processor for TAL, TALES and METAL specifications
# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
URL:		http://www.owlfish.com/software/simpleTAL/
Source0:	http://www.owlfish.com/software/simpleTAL/downloads/%{srcname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python3-devel

%description
SimpleTAL is a stand alone Python implementation of the TAL, TALES and
METAL specifications used in Zope to power HTML and XML templates.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pkgname}

# remove x-bits from example files
find examples -name '*.py' -exec chmod -x {} \;

%check
%{__python3} runtests.py || :

%files -f %{pyproject_files}
%doc Changes.txt README.txt
%doc documentation/html
%doc examples

%changelog
%autochangelog
