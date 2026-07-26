%global source0_hash bf9146078c0d7359da41043bd2b713203c4fc56ef2122b3cdbb7551c3fcd8464

Name:           python-zope-i18nmessageid
Version:        7.0
Release:        6%{?dist}
Summary:        Message Identifiers for internationalization

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        ZPL-2.1
URL:            https://github.com/zopefoundation/zope.i18nmessageid
Source:         %{pypi_source zope_i18nmessageid}

BuildRequires:  python3-devel
BuildRequires:  python3-docs
BuildRequires:  gcc

%global _description %{expand:
This module provides message identifiers for internationalization.}

%description %_description

%package -n     python3-zope-i18nmessageid
Summary:        %{summary}

%description -n python3-zope-i18nmessageid %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n zope_i18nmessageid-%{version}

# Use local objects.inv for intersphinx
sed -i "s|'http://docs\.python\.org/3'|'%{_docdir}/python3-docs/html'|" docs/conf.py

# Unnecessarily wants to control the setuptools version
sed -i -e '/setuptools/s/<[0-9]\+//' pyproject.toml tox.ini

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files zope

%check
%pyproject_check_import
%ifnarch %{ix86}
# zope-testrunner fails with this on i686 - could be a bug there
# ModuleNotFoundError: No module named 'zope.i18nmessageid'
%tox
%endif

%files -n python3-zope-i18nmessageid -f %{pyproject_files}
%{python3_sitearch}/zope.i18nmessageid-%{version}-py%{python3_version}-nspkg.pth

%changelog
%autochangelog
