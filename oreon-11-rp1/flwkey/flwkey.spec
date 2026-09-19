%global source0_hash e36e86788d7543261cd8f809b4e127d62df5578a39660353c0c0e6d1a4f7c09d

Name:           flwkey
Version:        1.2.4
Release:        1%{?dist}
Summary:        Modem program for the K1EL Winkeyer series

# Automatically converted from old format: GPLv3+ and MIT - review is highly recommended.
License:        GPL-3.0-or-later AND LicenseRef-Callaway-MIT
URL:            http://www.w1hkj.org/
Source0:        http://www.w1hkj.org/files/flwkey/%{name}-%{version}.tar.gz
Source99:       flwkey.appdata.xml

BuildRequires:  gcc-c++
BuildRequires:  fltk-devel >= 1.3.4
BuildRequires:  flxmlrpc-devel >= 0.1.0
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires: make

# xdg-open is used in src/flwkey.cxx
Requires:       xdg-utils

%description
Flwkey is a Winkeyer (or clone) control program for Amateur Radio use.  It
may be used concurrently with fldigi, fllog and flrig.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

rm -rf src/xmlrpcpp

%build
# Work around fltk-devel bug in RHEL 7.
# https://bugzilla.redhat.com/show_bug.cgi?id=1510482
export LIBS="-lfltk"
%configure
%make_build

%install
%make_install

%if 0%{?fedora}
#install appdata file
mkdir -p %{buildroot}%{_datadir}/metainfo
install -pm 0644 %{SOURCE99} %{buildroot}%{_datadir}/metainfo/
%endif

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
%if 0%{?fedora}
    appstream-util validate-relax --nonet \
    %{buildroot}%{_datadir}/metainfo/*.appdata.xml
%endif

%files
%doc AUTHORS ChangeLog README
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{?fedora:%{_datadir}/metainfo/%{name}.appdata.xml}
%{_datadir}/pixmaps/%{name}.xpm

%changelog
%autochangelog
