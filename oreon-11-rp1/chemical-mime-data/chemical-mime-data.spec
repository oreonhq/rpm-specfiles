%global source0_hash none

Name:           chemical-mime-data
Version:        0.1.94
Release:        42%{?dist}
Summary:        Support for chemical/* MIME types

License:        LGPL-2.1-or-later
URL:            https://github.com/dleidert/chemical-mime
# The SF page has been removed
# Source0:        http://downloads.sourceforge.net/chemical-mime/%%{name}-%%{version}.tar.bz2
# The latest release is in the lookaside cache
Source0:        %{name}-%{version}.tar.bz2
Patch0:         chemical-mime-data-0.1.94-turbomole.patch

BuildArch:      noarch
BuildRequires:  gcc
BuildRequires:  ImageMagick
BuildRequires:  intltool
BuildRequires:  libxml2
BuildRequires:  libxslt
BuildRequires:  perl(XML::Parser)
BuildRequires:  shared-mime-info
BuildRequires: make
Requires:       pkgconfig
Requires:       shared-mime-info
Requires:       hicolor-icon-theme

%description
A collection of data files which tries to give support for various chemical
MIME types (chemical/*) on Linux/UNIX desktops. Chemical MIME's have been
proposed in 1995, though it seems they have never been registered with IANA.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
iconv -f iso8859-1 -t utf-8 ChangeLog > ChangeLog.conv && mv -f ChangeLog.conv ChangeLog
sed -i -e '/^libdir/d' chemical-mime-data.pc.in


%build
%configure --disable-update-database \
           --without-gnome-mime \
           --without-pixmaps \
           --without-kde-mime
%make_build


%install
%make_install
cp -pR $RPM_BUILD_ROOT%{_docdir}/%{name} __docs
rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}
%find_lang %{name}


%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog HACKING NEWS README THANKS TODO
%doc __docs/*
%{_datadir}/icons/hicolor/*/mimetypes/gnome-mime-chemical.png
%{_datadir}/icons/hicolor/scalable/mimetypes/gnome-mime-chemical.svgz
%{_datadir}/mime/packages/chemical-mime-data.xml
%{_datadir}/pkgconfig/chemical-mime-data.pc


%changelog
%autochangelog

