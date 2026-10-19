%global source0_hash b75b420da9b0be9a3d99b1bee6ed87957b56ab54583ac1a97fbd0dc98ddddb25
%global source6_hash 1dfd8c294aff9c9011cfbc84b2099100624c1be899a764a47b7b9be0245875e0
Summary:        Shared MIME information database
Name: shared-mime-info
Version: 2.5.1
Release:        1%{?dist}
License: GPL-2.0-or-later
URL: http://freedesktop.org/Software/shared-mime-info
Source0:        https://gitlab.freedesktop.org/xdg/shared-mime-info/-/archive/%{version}/shared-mime-info-%{version}.tar.bz2
Source1: mimeapps.list
%global xdgmime_commit 04ce4cd90cb3fa77d5348662de221a6f33b21b17
Source6: https://gitlab.freedesktop.org/xdg/xdgmime/-/archive/%{xdgmime_commit}/xdgmime-%{xdgmime_commit}.tar.bz2
Patch0: 0001-Remove-sub-classing-from-OO.o-mime-types.patch
%global __requires_exclude ^/usr/bin/pkg-config$
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  git-core
BuildRequires:  glib2-devel
BuildRequires:  itstool
BuildRequires:  libxml2-devel
BuildRequires:  meson
BuildRequires:  xmlto
# /oreon:deps
%description
This is the freedesktop.org shared MIME info database.

Many programs and desktops use the MIME system to represent the types of
files. Frequently, it is necessary to work out the correct MIME type for
a file. This is generally done by examining the file's name or contents,
and looking up the correct MIME type in a database.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source6_hash}" = "none" || { f="%{SOURCE6}"; test -f "$f" || { echo "oreon: missing Source6 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source6_hash}" || { echo "oreon: Source6 hash mismatch" >&2; exit 1; }; }
%autosetup -S git_am

# xdgmime is expected under the subprojects directory
tar xjf %SOURCE6
mv xdgmime-%{xdgmime_commit}/ subprojects/xdgmime/

%build

%meson -Dupdate-mimedb=true
%meson_build
%install
%meson_install
find $RPM_BUILD_ROOT%{_datadir}/mime -type d \
| sed -e "s|^$RPM_BUILD_ROOT|%%dir |" > %{name}.files
find $RPM_BUILD_ROOT%{_datadir}/mime -type f -not -path "*/packages/*" \
| sed -e "s|^$RPM_BUILD_ROOT|%%ghost |" >> %{name}.files
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/applications
install -m 644 %SOURCE1 $RPM_BUILD_ROOT/%{_datadir}/applications/mimeapps.list
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*
%oreon_autofiles main

%check

%meson_test --suite shared-mime-info
%post

/bin/touch --no-create %{_datadir}/mime/packages &>/dev/null ||:
%transfiletriggerin -- %{_datadir}/mime
update-mime-database -n %{_datadir}/mime &> /dev/null ||:
%transfiletriggerpostun -- %{_datadir}/mime
update-mime-database -n %{_datadir}/mime &> /dev/null ||:
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
