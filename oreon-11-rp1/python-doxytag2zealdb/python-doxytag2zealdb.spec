%global source0_hash 9f450f09676c880f2e31399d779a2aefae2f8894d18e0ab108c7e10ae550dd4d
%global shortname doxytag2zealdb
%global descrip \
doxytag2zealdb creates a SQLite3 database from a Doxygen tag file to enable\
searchable Doxygen docsets with categorized entries in tools like helm-dash,\
Zeal, and Dash.
Name:           python-%{shortname}
Version:        0.3.1
Release:        21%{?dist}
Summary:        Create a SQLite3 database from a Doxygen tag file
License:        GPL-3.0-or-later
URL:            https://gitlab.com/vedvyas/doxytag2zealdb
Source0:        https://gitlab.com/vedvyas/%{shortname}/-/archive/v%{version}/%{shortname}-v%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3dist(beautifulsoup4)
BuildRequires:  python3dist(docopt)
BuildRequires:  python3dist(lxml)
BuildRequires:  python3dist(setuptools)
# /oreon:deps
%description    %{descrip}

%package -n %{shortname}
Summary:        Create a SQLite3 database from a Doxygen tag file
Requires: python3-%{shortname} = %{version}-%{release}
%description -n %{shortname}
%{descrip}

%package -n python3-%{shortname}
Summary:    Python modules for %{shortname}
Recommends: %{shortname} = %{version}-%{release}
%description -n python3-%{shortname}
This package contains the python modules for the doxytag2zealdb program.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{shortname}-v%{version}

# Remove future since it isn't used and is deprecated/removed
# https://gitlab.com/vedvyas/doxytag2zealdb/-/issues/4
sed -i "/'future'/d" setup.py

%build

%py3_build
%install
%py3_install
chmod +x %{buildroot}%{python3_sitelib}/%{shortname}/doxytag2zealdb.py
%py3_shebang_fix %{buildroot}%{python3_sitelib}/%{shortname}/doxytag2zealdb.py
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n doxytag2zealdb -f %{oreon_filedir}/doxytag2zealdb.list
%files -n python3-doxytag2zealdb -f %{oreon_filedir}/python3-doxytag2zealdb.list

%changelog

%autochangelog
