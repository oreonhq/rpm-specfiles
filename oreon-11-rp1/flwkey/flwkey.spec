%global source0_hash e36e86788d7543261cd8f809b4e127d62df5578a39660353c0c0e6d1a4f7c09d
Name:           flwkey
Version:        1.2.4
Release:        1%{?dist}
Summary:        Modem program for the K1EL Winkeyer series
License:        GPL-3.0-or-later AND LicenseRef-Callaway-MIT
URL:            http://www.w1hkj.org/
Source0:        http://www.w1hkj.org/files/flwkey/%{name}-%{version}.tar.gz
Source99:       flwkey.appdata.xml
Requires:       xdg-utils
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  fltk-devel
BuildRequires:  flxmlrpc-devel
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  make
# /oreon:deps
%description
Flwkey is a Winkeyer (or clone) control program for Amateur Radio use.  It
may be used concurrently with fldigi, fllog and flrig.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

rm -rf src/xmlrpcpp

%build

export LIBS="-lfltk"
%configure
%make_build
%install
%make_install
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
