%global source0_hash 2db1eee52e87a0cf0efeb4008460aabc020274045d194d2060ab1a562c02eec5

%global srcname TracNav

Name:           trac-tracnav-plugin
Version:        4.3
Release:        21%{?dist}
Summary:        Navigation Bar for Trac
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://svn.ipd.kit.edu/trac/javaparty/wiki/TracNav
Source0:        %{pypi_source}
BuildArch:      noarch
BuildRequires:  python3-devel
Requires:       trac >= 0.11

%description
The TracNav macro implements a fully customizable navigation bar for
the Trac wiki engine. The contents of the navigation bar is a wiki
page itself and can be edited like any other wiki page through the web
interface. The navigation bar supports hierarchical ordering of
topics. The design of TracNav mimics the design of the TracGuideToc
that was originally supplied with Trac.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n TracNav-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l tracnav

%files -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
