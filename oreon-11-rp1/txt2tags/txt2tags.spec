%global source0_hash d7083e3e9b02cb90b5439ab19ca279710f6e36008db79bde349a6e30c253a225

Name:    txt2tags
Summary: Summary: Converts text files to HTML, XHTML, LaTeX, and other formats
Version: 3.3
Release: 23%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL:     http://txt2tags.sourceforge.net/

# https://github.com/txt2tags/txt2tags/issues/207#issuecomment-544905237
Source0: https://github.com/jendrikseipp/txt2tags/archive/%{version}.tar.gz

BuildArch: noarch

BuildRequires: python3-devel
Requires:      python3

%description
Txt2tags is a document generator. It reads a text file with minimal markup as 
**bold** and //italic// and converts it to the following formats:

    * HTML
    * XHTML
    * SGML
    * LaTeX
    * Lout
    * Man page
    * Wikipedia (NEW)
    * Google Code Wiki (NEW)
    * DokuWiki (NEW)
    * MoinMoin
    * MagicPoint
    * PageMaker
    * Plain text 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%generate_buildrequires
%pyproject_buildrequires

%build
%{pyproject_wheel}

%install
%{pyproject_install}
%pyproject_save_files -l %{name}

%check
%pyproject_check_import

%files -f %{pyproject_files}
%doc CHANGELOG.md README.md
%{_bindir}/txt2tags

%changelog
%autochangelog
