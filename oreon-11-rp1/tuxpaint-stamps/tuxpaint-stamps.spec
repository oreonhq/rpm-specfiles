%global source0_hash none

Name:           tuxpaint-stamps
Version:        2020.05.29
Release:        15%{?dist}
Summary:        Extra stamp files for tuxpaint
License:        GPL-1.0-or-later AND GFDL-1.1-or-later AND CC-BY-SA-2.0 AND CC-BY-SA-2.5 AND CC-BY-SA-3.0 AND LicenseRef-Fedora-Public-Domain
URL:            http://www.tuxpaint.org/
Source0:        https://downloads.sourceforge.net/tuxpaint/%{name}/2020-05-29/%{name}-%{version}.tar.gz
Patch0:         python3.patch
Patch1:         indent.patch

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  gettext
BuildRequires:  python3-devel
Requires:       tuxpaint

%description
This package is a collection of 'rubber stamps' for Tux Paint's "Stamp" tool.

%prep
%setup -q
# note need to update this if version is something other than a date
sed -i "s/VER_DATE=\`date +\"%%Y.%%m.%%d\"\`/VER_DATE=\`date +%{version}\`/" Makefile
%patch -P 0 -p0
%patch -P 1 -p0
%py3_shebang_fix .

%build
(cd po && sh ./createpo.sh)
(cd po && ./createtxt.sh)

%install
install -d $RPM_BUILD_ROOT%{_datadir}/tuxpaint/stamps
make install-all PREFIX=$RPM_BUILD_ROOT%{_prefix}
# Register as an add-on to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.metainfo.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!--
Copyright 2016 Colin B. Macdonald

Copying and distribution of this file, with or without modification,
are permitted in any medium without royalty provided the copyright
notice and this notice are preserved.  This file is offered as-is,
without any warranty.
-->
<!--
BugReportURL: https://sourceforge.net/p/tuxpaint/feature-requests/172/
SentUpstream: 2016-06-02
-->
<component type="addon">
  <id>tuxpaint-stamps</id>
  <extends>tuxpaint.desktop</extends>
  <name>Tuxpaint Stamps</name>
  <summary>"Rubber stamp" images of animals, plants, vehicles, and many more</summary>
  <url type="homepage">http://tuxpaint.org/</url>
  <metadata_license>FSFAP</metadata_license>
</component>
EOF

pushd po
for file in *.po ; do
    loc=`echo $file | sed -e 's/tuxpaint-stamps-\(.*\).po/\1/'`
    mkdir -p $RPM_BUILD_ROOT%{_datadir}/locale/$loc/LC_MESSAGES
    msgfmt -o $RPM_BUILD_ROOT%{_datadir}/locale/$loc/LC_MESSAGES/tuxpaint-stamps.mo $file
done
popd

# License is bad on this file, Creative Commons Sampling Plus 1.0 is non-free.
rm -rf $RPM_BUILD_ROOT%{_datadir}/tuxpaint/stamps/vehicles/emergency/firetruck.ogg

%find_lang %{name}

%files -f %{name}.lang
%doc docs/*.txt
%lang(el) %doc docs/el
%lang(es) %doc docs/es
%lang(fr) %doc docs/fr
%lang(hu) %doc docs/hu
%defattr(0644,root,root,0755)
%{_datadir}/tuxpaint/stamps/*
%{_datadir}/appdata/%{name}.metainfo.xml

%changelog
%autochangelog
