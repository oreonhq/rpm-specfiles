%global source0_hash 9597b4f30ffa71fefe49613fabbd1513725ab21185ff327716cef6274999227d
Name:           homebank
Version:        5.10.3
Release:        1%{?dist}
Summary:        Free easy personal accounting for all
License:        GPL-2.0-or-later
URL:            https://gethomebank.org/
Source0:        https://gethomebank.org/public/sources/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  atk-devel
BuildRequires:  cairo-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  libofx-devel
BuildRequires:  libsoup3-devel
BuildRequires:  make
BuildRequires:  perl(XML::Parser)
# /oreon:deps
%description
HomeBank is the free software you have always wanted to manage your personal
accounts at home. The main concept is to be light, simple and very easy to use.
It brings you many features that allows you to analyze your finances in a
detailed way instantly and dynamically with powerful report tools based on
filtering and graphical charts.

%package doc
Summary: Documentation files for homebank
BuildArch: noarch
Requires: %{name} = %{version}-%{release}
%description doc
Documentation files for homebank

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# workaround for 5.10.3 difference between .tar.gz and the actual 5.10.0 dir
# this workarnoud should be remove from 5.10.3.x onwards
%autosetup -n %{name}-%{version}.0
chmod -x NEWS
chmod -x ChangeLog
chmod -x README
chmod -x AUTHORS
chmod -x COPYING
chmod -x doc/TODO
chmod -x src/*.*

%build

%configure
%make_build
%install
make install DESTDIR=%{buildroot} INSTALL='install -p'
mkdir -p %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install                                    \
        --delete-original                               \
        --dir %{buildroot}%{_datadir}/applications   \
        --mode 0644                                     \
        %{buildroot}%{_datadir}/applications/%{name}.desktop
%find_lang %{name}
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/%{name}.appdata.xml
%ldconfig_scriptlets
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n homebank-doc -f %{oreon_filedir}/homebank-doc.list

%changelog

%autochangelog
