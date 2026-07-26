%global source0_hash 1d9f28465ab6094cea6915caea0fb9924fdfff75e87f0a82a36f43e18045b4d5

%global         srcname         pygtkspellcheck
%global         forgeurl        https://github.com/koehlma/pygtkspellcheck
Version:        5.0.3
%global         tag             %{version}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        Spellchecking library for GTK

# All code GPL-3.0-or-later
# LGPL-2.1-or-later files below
# pygtkspellcheck-5.0.3/utils/locales/databases/iso3166.xml
# pygtkspellcheck-5.0.3/utils/locales/databases/iso639.xml
License:        GPL-3.0-or-later AND LGPL-2.1-or-later
URL:            %{forgeurl}
Source:         %{forgeurl}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  python3-devel
# Documentation dependencies
BuildRequires:  python3-myst-parser
BuildRequires:  python3-sphinx
# Check dependency
BuildRequires:  python3-gobject-devel
BuildRequires:  gtk3-devel

BuildArch: noarch

%global _description %{expand:
Python GTK Spellcheck is a simple but quite powerful spellchecking
library for GTK written in pure Python. It's spellchecking component
is based on Enchant and it supports both GTK 3 and 4 via PyGObject.

Features

- spellchecking based on Enchant for GtkTextView
- support for word, line, and multiline ignore regular expressions
- support for both GTK 3 and 4 via PyGObject for Python 3
- configurable extra word characters such as '
- localized names of the available languages based on ISO-Codes
- support for custom ignore tags and hot swap of GtkTextBuffer
- support for Hunspell (LibreOffice) and Aspell (GNU) dictionaries
}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
# TODO: build documentation

%install
%pyproject_install
%pyproject_save_files gtkspellcheck -L

%check 
%pyproject_check_import

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%doc CHANGELOG
%license LICENSE
%doc examples

%changelog
%autochangelog
