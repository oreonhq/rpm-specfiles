%global source0_hash 3bb868bb2c5e5e9ba69ca70d45736738cb1e8d6879f2c74207dfa8869ddf00b9

%global majorver 1.0
%global appdata_name org.xubuntu.XfpanelSwitch

Name:		xfpanel-switch
Version:	1.0.7
Release:	19%{?dist}
Summary:	A simple application to manage Xfce panel layouts

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:	GPL-3.0-only
URL:		https://launchpad.net/%{name}
Source0:	https://launchpad.net/%{name}/%{majorver}/%{version}/+download/%{name}-%{version}.tar.bz2

%if 0%{?fedora}
BuildRequires:	python3-devel
%endif

BuildRequires:	make
BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	libappstream-glib
BuildRequires:	desktop-file-utils
BuildArch:	noarch
Requires:	xfce4-panel

%description
A simple application to manage Xfce panel layouts

With the modular Xfce Panel, a multitude of panel layouts can be created. 
This tool makes it possible to backup, restore, import, and export these 
panel layouts.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
#cannot use configure macro here
./configure --prefix=/usr
%make_build

%install
%make_install

rm -f %{buildroot}%{_docdir}/%{name}/COPYING

%find_lang %{name}

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{appdata_name}.appdata.xml

%files -f %{name}.lang
%license COPYING
%doc NEWS AUTHORS README INSTALL
%{_datadir}/%{name}/*
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/*.appdata.xml

%changelog
%autochangelog
