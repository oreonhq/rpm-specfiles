%global source0_hash 9f97e4c808f656ce22739eec43a7c1741f645b7decef37d4fb048edb33e8caad

Name:           odfpy
Version:        1.4.1
Release:        18%{?dist}
Summary:        Python library for manipulating OpenDocument files

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/eea/odfpy
Source0:        https://github.com/eea/%{name}/archive/release-%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         odfpy-allow-py38-testing.patch

BuildArch:      noarch

%description
Odfpy aims to be a complete API for OpenDocument in Python. Unlike
other more convenient APIs, this one is essentially an abstraction
layer just above the XML format. The main focus has been to prevent
the programmer from creating invalid documents. It has checks that
raise an exception if the programmer adds an invalid element, adds an
attribute unknown to the grammar, forgets to add a required attribute
or adds text to an element that doesn't allow it.

These checks and the API itself were generated from the RelaxNG
schema, and then hand-edited. Therefore the API is complete and can
handle all ODF constructions, but could be improved in its
understanding of data types.

%package -n python3-%{name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-defusedxml

%{?python_provide:%python_provide python3-%{name}}

Provides:       odfpy = %{version}-%{release}
Obsoletes:      odfpy < %{version}-%{release}

%description -n python3-%{name}
Odfpy aims to be a complete API for OpenDocument in Python. Unlike
other more convenient APIs, this one is essentially an abstraction
layer just above the XML format. The main focus has been to prevent
the programmer from creating invalid documents. It has checks that
raise an exception if the programmer adds an invalid element, adds an
attribute unknown to the grammar, forgets to add a required attribute
or adds text to an element that doesn't allow it.

These checks and the API itself were generated from the RelaxNG
schema, and then hand-edited. Therefore the API is complete and can
handle all ODF constructions, but could be improved in its
understanding of data types.

This package provides Python 3 build of %{name}.

%package doc
Summary:        %{summary}

%description doc
Odfpy aims to be a complete API for OpenDocument in Python. Unlike
other more convenient APIs, this one is essentially an abstraction
layer just above the XML format. The main focus has been to prevent
the programmer from creating invalid documents. It has checks that
raise an exception if the programmer adds an invalid element, adds an
attribute unknown to the grammar, forgets to add a required attribute
or adds text to an element that doesn't allow it.

These checks and the API itself were generated from the RelaxNG
schema, and then hand-edited. Therefore the API is complete and can
handle all ODF constructions, but could be improved in its
understanding of data types.

This package provides documentation of %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-release-%{version}
# Change shebang in all relevant files
find -type f -exec sed -i '1s=^#!/usr/bin/\(python\|env python\)[23]\?=#!%{__python3}=' {} +

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{_builddir}/%{name}-release-%{version} pytest

%files -n python3-%{name}
%license GPL-LICENSE-2.txt APACHE-LICENSE-2.0.txt
%{_bindir}/*
%{_mandir}/man1/*
%{python3_sitelib}/*egg-info
%{python3_sitelib}/odf

%files doc
%license GPL-LICENSE-2.txt APACHE-LICENSE-2.0.txt
%doc doc examples contrib

%changelog
%autochangelog
