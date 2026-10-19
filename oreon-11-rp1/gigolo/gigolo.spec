%global source0_hash 29951a16ca48c5350fa862417a253bc45c2762106027c216bb7a56eabdd7f0f6
%global minorversion 0.6
Name:           gigolo
Version:        0.6.0
Release:        1%{?dist}
Summary:        GIO/GVFS management application
License:        GPL-2.0-only
URL:            http://goodies.xfce.org/projects/applications/gigolo/
Source0:        http://archive.xfce.org/src/apps/%{name}/%{minorversion}/%{name}-%{version}.tar.bz2
Requires:       gvfs-fuse
Obsoletes: sion < 0.1.0-3
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gtk3-devel
BuildRequires:  make
# /oreon:deps
%description
A frontend to easily manage connections to remote filesystems using GIO/GVFS. 
It allows you to quickly connect/mount a remote filesystem and manage
bookmarks of such. 

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure
%make_build
%install
%make_install
%find_lang %{name}
rm -rf %{buildroot}/%{_datadir}/doc/gigolo
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
