%global source0_hash none

%global tarball_version %(echo %{version} | tr '~' '.')
%global major_version %(echo %{tarball_version} | cut -d "." -f 1)

Name:           gnome-user-docs
Version:        50.0
Release:        %autorelease
Summary:        GNOME User Documentation

License:        CC-BY-SA-3.0
URL:            https://help.gnome.org/
Source0:        https://download.gnome.org/sources/%{name}/50/%{name}-%{tarball_version}.tar.xz
BuildArch:      noarch

BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  yelp-tools

%description
This package contains end-user documentation for the GNOME desktop
environment.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
# check for human errors
if [ `echo "%{version}" | grep -cE "\.alpha|\.beta|\.rc"` = "1" ]; then echo "Error: Use tilde in Version field in front of alpha/beta/rc; checked '%{version}'" 1>&2; exit 1; fi

%autosetup -p1 -n %{name}-%{tarball_version}

%build
%configure
%make_build

%install
%make_install

%find_lang %{name} --all-name --with-gnome

%files -f %{name}.lang
%license COPYING
%doc NEWS README.md

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 50.0-1
- Prepare for Oreon 11 (RP1)
