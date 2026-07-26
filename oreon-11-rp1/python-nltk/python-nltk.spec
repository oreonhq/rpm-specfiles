%global source0_hash 03e06c8c13e352133962c4395ebe0696905c9f1fbdead2d19deae37ba48eb47c

%global mod_name nltk
Name:           python-nltk
Epoch:          1
Version:        3.9.1
Release:        7%{?dist}
Summary:        Natural Language Toolkit

# The entire source code is ASL 2.0 except nltk/stem/porter.py is
# GPLv2+ with exceptions
# Automatically converted from old format: ASL 2.0 and GPLv2+ with exceptions - review is highly recommended.
License:        Apache-2.0 AND LicenseRef-Callaway-GPLv2+-with-exceptions
URL:            http://www.nltk.org/
Source0:        https://github.com/nltk/nltk/archive/%{version}.tar.gz#/%{mod_name}-%{version}.tar.gz
BuildArch:      noarch

# https://github.com/nltk/nltk/pull/3309
Patch1: fix-import-WordNetLemmatizer.patch

%global _description\
NLTK is a Python package that simplifies the construction of programs\
that process natural language; and defines standard interfaces between\
the different components of an NLP system.  It was designed primarily\
to help teach graduate and undergraduate students about computational\
linguistics; but it is also useful as a framework for implementing\
research projects.

%description %_description

%package -n python3-%{mod_name}
Summary:        Natural Language Toolkit (Python 3)
BuildRequires:  python3-devel

%description -n python3-%{mod_name}
NLTK is a Python package that simplifies the construction of programs
that process natural language; and defines standard interfaces between
the different components of an NLP system.  It was designed primarily
to help teach graduate and undergraduate students about computational
linguistics; but it is also useful as a framework for implementing
research projects.

This package provides the Python 3 build of NLTK.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{mod_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{mod_name}

%check
# skip tests since it requires nltk-data and a few utilities not available in
# Fedora
#%%{__python3} %%{mod_name}/test/runtests.py

%files -n python3-%{mod_name} -f %{pyproject_files}
%{_bindir}/%{mod_name}
%doc AUTHORS.md CONTRIBUTING.md ChangeLog README.md

%changelog
%autochangelog
