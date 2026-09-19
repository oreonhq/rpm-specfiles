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
Source0:        https://gitlab.com/vedvyas/doxytag2zealdb/-/archive/v%{version}/%{shortname}-v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel >= 3.6
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(docopt) >= 0.6.2
BuildRequires:  python3dist(lxml) >= 3.6.0
BuildRequires:  python3dist(beautifulsoup4) >= 4.4.1

%description    %{descrip}

%package -n %{shortname}
Summary:  %{summary}
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

# Fixup the script's executable features
chmod +x %{buildroot}%{python3_sitelib}/%{shortname}/doxytag2zealdb.py
%py3_shebang_fix %{buildroot}%{python3_sitelib}/%{shortname}/doxytag2zealdb.py

%files -n %{shortname}
%license COPYING
%doc CONTRIBUTORS
%doc README.md
%{_bindir}/doxytag2zealdb

%files -n python3-%{shortname}
%license COPYING
%doc CONTRIBUTORS
%doc README.md
%{python3_sitelib}/%{shortname}
%{python3_sitelib}/%{shortname}-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
