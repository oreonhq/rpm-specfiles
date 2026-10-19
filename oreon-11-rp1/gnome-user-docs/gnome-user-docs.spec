%global source0_hash bf3ebd7fa1da70617884b07392de8d605305cfef71c2e883749cb08ff0d6a7d1
%global tarball_version %(echo %{version} | tr '~' '.')
%global major_version %(echo %{tarball_version} | cut -d "." -f 1)
Name:           gnome-user-docs
Version:        51.0
Release:        1%{?dist}
Summary:        GNOME User Documentation
License:        CC-BY-SA-3.0
URL:            https://help.gnome.org/
Source0:        https://download.gnome.org/sources/%{name}/51/%{name}-%{version}.tar.xz
BuildArch:      noarch
# oreon:deps
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  yelp-tools
# /oreon:deps
%description
This package contains end-user documentation for the GNOME desktop
environment.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
# check for human errors
if [ `echo "%{version}" | grep -cE "\.alpha|\.beta|\.rc"` = "1" ]; then echo "Error: Use tilde in Version field in front of alpha/beta/rc; checked '%{version}'" 1>&2; exit 1; fi

%autosetup -p1 -n %{name}-%{tarball_version}

%build

%configure
%make_build
%install
%make_install
%find_lang %{name} --all-name --with-gnome
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 50.0-1
- Prepare for Oreon 11 (RP1)
