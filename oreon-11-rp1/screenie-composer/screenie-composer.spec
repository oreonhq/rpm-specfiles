%global source0_hash 309a65912fd8360697ba35a7df245a805c19de0c790a79b1820bdb54b4bcbac5

%global snapshot 49c2630

Name:           screenie-composer
Version:        1.0.0
Release:        0.35.20110805git%{snapshot}%{?dist}
Summary:        Fancy screenshot composer

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/ariya/screenie
# Tarballs are only available via github. The current snapshot can be downloaded at
# https://github.com/ariya/screenie/tarball/49c2630c393b003a473263001a18e27144744178
Source0:        ariya-screenie-%{snapshot}.tar.gz
Source1:        %{name}.desktop

# Link program libraries statically as they are not intended to
# be used by third-party developers. Their names are way too generic as well.
Patch0:         %{name}-%{version}-static.patch
# Fix segfault occured due to call of uninitialized class variables.
Patch1:         %{name}-%{version}-mime.patch
# remove rpath definition
Patch2:         %{name}-%{version}-rpath.patch
# undefine g++ macros major/minor expanded to gnu_dev_major/minor
Patch3:         %{name}-%{version}-gnu.patch

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  qt4-devel

%description
Screenie is an easy to use screenshot composer tool that lets you create fancy
and stylish screenshots from a given set of images. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n ariya-screenie-%{snapshot}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

find -type f -exec chmod 644 {} \;

%build
%{qmake_qt4}
make %{?_smp_mflags}

%install
install -D bin/release/Screenie %{buildroot}%{_bindir}/%{name}
install -D -p -m 644 src/Resources/img/application-icon.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  %{SOURCE1}

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
<!-- Copyright 2014 Ryan Lerch <rlerch@redhat.com> -->
<!--
BugReportURL: https://code.google.com/p/screenie/issues/detail?id=9
SentUpstream: 2014-07-08
-->
<application>
  <id type="desktop">screenie-composer.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Create stylish screenshots</summary>
  <description>
    <p>
      Screenie is a simple to use screenshot composition tool, with the abilty
      to add perspective and reflections to screenshots.
      To use screenie, the user simply imports a screenshot, then tweaks a few
      variables that control the angle of the perspective effect, the amount of
      reflection, and the background colour.
    </p>
  </description>
  <url type="homepage">https://code.google.com/p/screenie/</url>
  <screenshots>
    <screenshot type="default">http://lh6.ggpht.com/ariya.hidayat/SEW_gDTc7ZI/AAAAAAAAAdI/2jmyFxAuRYo/s400/2545790007_43dfcd4326_o.png</screenshot>
  </screenshots>
  <!-- FIXME: change this to an upstream email address for spec updates
  <updatecontact>someone_who_cares@upstream_project.org</updatecontact>
   -->
</application>
EOF

%files
%doc LICENSE.GPL2 README.txt
%{_bindir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
%autochangelog
