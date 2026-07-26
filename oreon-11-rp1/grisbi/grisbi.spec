%global source0_hash bd3adbabfc4b4dfc05eff62d2b36458a24b0f00d07cf35a29f6af2f203c77a3f

Name:		grisbi
Version:	2.0.5
Release:	9%{?dist}
Summary:	Personal finances manager

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://www.grisbi.org
Source0:	http://downloads.sourceforge.net/project/grisbi/grisbi%20stable/2.0.x/%{version}/%{name}-%{version}.tar.bz2
Source1:	%{name}.appdata.xml

BuildRequires:  gcc
BuildRequires:	gtk3-devel
BuildRequires:	libxml2-devel
BuildRequires:	glib2-devel
BuildRequires:	libgsf-devel
BuildRequires:	gettext-devel
BuildRequires:	desktop-file-utils
BuildRequires:	libofx-devel >= 0.9.0
BuildRequires:	openssl-devel
BuildRequires:	intltool
BuildRequires:	ImageMagick
BuildRequires:	libappstream-glib
BuildRequires: make

Requires:	xdg-utils

%description
Grisbi is a very functional personal financial management program
with a lot of features: checking, cash and liabilities accounts,
several accounts with automatic contra entries, several currencies,
including euro, arbitrary currency for every operation, money
interchange fees, switch to euro account per account, description
of the transactions with third parties, categories, sub-categories,
financial year, notes, breakdown, transfers between accounts, even
for accounts of different currencies, bank reconciliation, scheduled
transactions, automatic recall of last transaction for every third
party, nice and easy user interface, user manual, QIF import/export.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
# FIXME: package should not install help files into _pkgdocdir
%configure --disable-silent-rules --docdir=%{_pkgdocdir}
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
install -D -p -m 644 %{SOURCE1} %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml

desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}.desktop

for f in AUTHORS COPYING NEWS README ABOUT-NLS; do
    cp -p $f %{buildroot}%{_pkgdocdir}/$f
done

%find_lang %{name}

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml

%files -f %{name}.lang
%doc %{_pkgdocdir}/
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/mime-info/%{name}.*
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/pixmaps/*
%{_datadir}/icons/hicolor/*/apps/grisbi.*
%{_datadir}/icons/hicolor/*/mimetypes/application-x-grisbi.*
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1.*
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/glib-2.0/schemas/org.gtk.grisbi.gschema.xml

%changelog
%autochangelog
