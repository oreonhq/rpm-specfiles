%global source0_hash e9868a2e7de7f2d8b076e77956a70aba425ed58a28bf28988f8d017d8233e091

%global desc These provide several pieces of "middleware" (or filters) that can be nested\
to build web applications.  Each piece of middleware uses the WSGI (PEP 333)\
interface, and should be compatible with other middleware based on those\
interfaces.
%global sum Tools for using a Web Server Gateway Interface stack

Name:           python-paste
Version:        3.10.1
Release:        13%{?dist}
BuildArch:      noarch

# Most of the code is MIT
# paste/exceptions/collector.py is ZPLv2.0
# paste/evalexception/media/MochiKit.packed.js AFL (2.1) or MIT
# paste/lint.py MIT or Apache v2
# PySourceColor.py, Python
# Automatically converted from old format: MIT and ZPLv2.0 and Python and (AFL or MIT) and (MIT or ASL 2.0) - review is highly recommended.
License:        LicenseRef-Callaway-MIT AND ZPL-2.0 AND LicenseRef-Callaway-Python AND (LicenseRef-Callaway-AFL OR LicenseRef-Callaway-MIT) AND (LicenseRef-Callaway-MIT OR Apache-2.0)
Summary:        %sum
URL:            https://github.com/pasteorg/paste
#Source0:        %%{pypi_source}
Source0:        https://github.com/pasteorg/paste/archive/%{version}/Paste-%{version}.tar.gz
Patch1:         paste-import-urlparse.patch

BuildRequires:  python3-devel
BuildRequires:  python3-pyOpenSSL
BuildRequires:  python3-pytest
BuildRequires:  python3-six >= 1.4.0
# required for tests
BuildRequires:  python3-openid
BuildRequires:  python3-paste-deploy

%description
%desc

%package -n python3-paste
Summary:        Tools for using a Web Server Gateway Interface stack

Requires: python3-pyOpenSSL
Requires: python3-setuptools
Requires: python3-six

%description -n python3-paste
%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n paste-%{version} -p1

# Paste-2.0.3 seems to have a few .py.orig files that don't appear in upstream scm. Let's drop them.
find . -name "*.orig" -delete

# Strip #! lines that make these seem like scripts
%{__sed} -i -e '/^#!.*/,1 d' paste/util/scgiserver.py paste/debug/doctest_webapp.py

# clean docs directory
pushd docs
rm StyleGuide.txt
popd

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files paste

%check
# exclude broken modules from import tests
%pyproject_check_import -e 'paste.debug.*' -e paste.flup_session -e paste.transaction -e paste.util.scgiserver
export PYTHONPATH=$(pwd)
# We don't have access to the wider internet in the buildsystem
# Also disable urlparser and cgiapp tests, which fails with new setuptools
py.test -k \
  "not test_paste_website and not test_proxy_to_website and not test_modified and not urlparser and not cgiapp"

%files -n python3-paste -f %{pyproject_files}
%doc docs/*
%{python3_sitelib}/Paste-%{version}-py%{python3_version}-nspkg.pth

%changelog
%autochangelog
