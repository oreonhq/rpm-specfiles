%global source1_hash fa8eeccd7b00a63cdadcb8d7489da12da7842e265f47226a73b1357aca8e8c9b
%global source0_hash 1852303374d7777f2a5f395fda97d78f970fa87c854ee048495a901922b7dd84
Name:		cbrpager
Version:	0.9.22
Release:        36%{?dist}
Summary:        Simple comic book pager for Linux
License:	GPL-2.0-or-later AND CC0-1.0
URL:		http://www.jcoppens.com/soft/cbrpager/index.en.php
Source0:        http://downloads.sourceforge.net/cbrpager/%{name}-%{version}.tar.gz
Source1:	http://downloads.sourceforge.net/cbrpager/%{name}-%{version}.md5
Patch0:	cbrpager-c99.patch
Requires:	gnome-icon-theme
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  pkgconfig(libgnomeui-2.0)
# /oreon:deps
%description
A no-nonsense, simple to use, small viewer for cbr and cbz
(comic book archive) files. As it is written in C, 
the executable is small and fast. It views jpg (or jpeg), 
gif and png images, and you can zoom in and out.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

for f in \
	ChangeLog \
	CONTRIBUTORS
	do
	iconv -f ISO-8859-1 -t UTF-8 $f > $f.tmp && \
		( touch -r $f $f.tmp ; %{__mv} -f $f.tmp $f )
	rm -f $f.tmp
done

cat > %{name}.desktop <<EOF
[Desktop Entry]
Name=cbrPager
Comment=A simple comic book pager for Linux
Exec=%{name} %%f
Icon=applications-graphics
Terminal=false
Type=Application
Categories=Graphics;Viewer;
EOF

%build

%configure
%make_build
%install
%{__rm} -rf $RPM_BUILD_ROOT
%make_install
desktop-file-install \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications \
	%{name}.desktop
mkdir -p $RPM_BUILD_ROOT%{_metainfodir}
cat > $RPM_BUILD_ROOT%{_metainfodir}/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ryan Lerch <rlerch@redhat.com> -->
<!--
BugReportURL: https://sourceforge.net/p/cbrpager/support-requests/4/
SentUpstream: 2014-09-17
-->
<application>
  <id type="desktop">cbrpager.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Read comics</summary>
  <description>
    <p>
      cbrPager is a simple comic book reader application with the ability to change pages and zoom.
      It features the ability to open and read cbr, cb7 and cbz comic book archives that contain
      PNG and JPEG images.
    </p>
  </description>
  <url type="homepage">http://www.jcoppens.com/soft/cbrpager/index.en.php</url>
  <screenshots>
    <screenshot type="default">http://www.jcoppens.com/soft/cbrpager/img/snap.jpeg</screenshot>
  </screenshots>
</application>
EOF
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
