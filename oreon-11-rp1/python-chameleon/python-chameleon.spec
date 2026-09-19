%global source0_hash f228d32d13562f7d976c0bcd7db56c138662676865a7d78b7d274064076f6cb4

%global srcname Chameleon

Name:           python-chameleon
Version:        4.6.0
Release:        8%{?dist}
Summary:        XML-based template compiler

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/malthe/chameleon
Source0:        https://github.com/malthe/chameleon/archive/%{version}/chameleon-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-lxml

%generate_buildrequires
%pyproject_buildrequires -t

%global _description\
Chameleon is an XML attribute language template compiler. It comes with\
implementations for the Zope Page Templates (ZPT) and Genshi templating\
languages.\
\
The engine compiles templates into Python byte-code. This results in\
performance which is on average 10-15 times better than implementations which\
use run-time interpretation.

%description %_description

%package -n python3-chameleon
Summary: %summary

Requires:   python3-setuptools
Requires:   python3-lxml

%description -n python3-chameleon %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n chameleon-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files chameleon

%check
%pyproject_check_import -e 'chameleon.tests*'
%tox

%files -n python3-chameleon -f %{pyproject_files}
%doc README.rst
%exclude %{python3_sitelib}/chameleon/tests

%changelog
%autochangelog
