%global source0_hash 3c30640374cf0c824e869d2ed22cdb4e9afa9251ac0db988c38e3a788ddf72df

%global rctag rc5

Name:		guitone
Version:	1.0
Release:	0.39%{?rctag:.%rctag}%{?dist}
Summary:	A frontend for Monotone
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
URL:		http://guitone.thomaskeller.biz/
Source:		%{url}releases/%{version}%{?rctag:%rctag}/%{name}-%{version}%{?rctag:%rctag}.tgz
Patch0:		guitone-1.0rc5-cpp11.patch
Patch1:		guitone-1.0rc5-format-security.patch
# License is GPLv3+.  This forces us to build against qt >= 4.3.4.
BuildRequires:	qt4-devel >= 4.3.4
BuildRequires:	gcc-c++
BuildRequires:	make
BuildRequires:	desktop-file-utils
Requires:	monotone >= 0.99.1

%description 
Guitone is a Qt-based, cross-platform graphical user interface for the
distributed version control system monotone. It aims towards a full
implementation of the monotone automation interface and is especially
targeted at beginners. 

Functionality provided by guitone:

* Browse a loaded workspace, filter by file states
* Display attributes of selected files
* Open files in the system's default viewer on double-click
* Show file differences for single and multiple files
* List keys from the loaded database and generate new keys
* Checkout, export and commit revisions
* Query recent revisions from a loaded database

and much more.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}%{?rctag:%rctag}
%patch -P0 -p1
%patch -P1 -p1

cat >%{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=Guitone
Comment=Frontend for Monotone
Exec=guitone
Icon=guitone
Terminal=false
Type=Application
Categories=Application;Development;
EOF

%build
%{qmake_qt4} LRELEASE=lrelease-qt4 -config release guitone.pro
make %{?_smp_mflags}

%install
install -m 755 -D -p bin/guitone %{buildroot}%{_bindir}/guitone
install -m 644 -D -p res/icons/guitone.png %{buildroot}%{_datadir}/pixmaps/guitone.png

desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  --vendor="" \
  %{name}.desktop

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<!--
EmailAddress: me@thomaskeller.biz
SentUpstream: 2014-09-18
-->
<application>
  <id type="desktop">guitone.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Graphical viewer for Monotone repositories</summary>
  <description>
    <p>
     Guitone is a tool to visually navigate Monotone repositories.
     Guitone aims to be a full implementation of the monotone automation
     interface, and provides features such as:
    </p>
    <ul>
      <li>Browsing a loaded workspace, with filtering by file states</li>
      <li>Display of the attributes of files</li>
      <li>Opening of files with the system's default editor or browser</li>
      <li>Showing differences between files</li>
    </ul>
  </description>
  <url type="homepage">https://guitone.thomaskeller.biz/</url>
  <screenshots>
    <screenshot type="default">https://guitone.thomaskeller.biz/web/screens/1.0rc2/changeset_browser.png</screenshot>
  </screenshots>
  <!-- FIXME: change this to an upstream email address for spec updates
  <updatecontact>someone_who_cares@upstream_project.org</updatecontact>
   -->
</application>
EOF

# the tests subdir currently contains only a stub of a testsuite, and
# upstream told us not to use it yet, so no 'check' section.

%files
%doc NEWS README README.driver
%license COPYING
%{_bindir}/guitone
%{_datadir}/pixmaps/guitone.png
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/guitone.desktop

%changelog
%autochangelog
