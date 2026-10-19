%global source0_hash bfe8f21dcab1ef4b115654e17212bcb03b6a10083340803f496f226b4a082cf6
%global tarball_version %(echo %{version} | tr '~' '.')
Name: gnome-devel-docs
Version: 40.3
Release:        1%{?dist}
Summary:        GNOME developer documentation
License: GFDL-1.1-or-later AND CC-BY-SA-3.0 AND CC-BY-SA-4.0 AND CC-BY-SA-3.0 WITH GNOME-examples-exception
URL: https://developer.gnome.org
Source0:        https://download.gnome.org/sources/%{name}/40/%{name}-%{version}.tar.xz
BuildArch: noarch
# oreon:deps
BuildRequires:  docbook-utils
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  make
BuildRequires:  yelp-tools
# /oreon:deps
%description
This package contains documents which are targeted for GNOME developers.
It contains, e.g., the Human Interface Guidelines, the Integration Guide
and the Platform Overview.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}-%{tarball_version}

%build

%configure
make %{?_smp_mflags}
%install
%make_install
%find_lang %{name} --all-name --with-gnome
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
