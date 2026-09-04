%global source0_hash 46ee5ac6a9552864ba2d447f87964dd3bd759ed8a7990bd28b1c404cdbdfe7ab

%global debug_package %{nil}

Summary:       An additive synthesizer using JACK
Name:          Add64
Version:       3.9.3
Release:       20%{?dist}
URL:           http://sourceforge.net/projects/add64
Source0:       http://downloads.sourceforge.net/project/add64/%{name}-%{version}.tar.bz2
Source1:       %{name}.desktop
# icon taken from screenshot
Source2:       add64.png
Source3:       Makefile
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:       GPL-3.0-only

BuildRequires: jack-audio-connection-kit-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: desktop-file-utils
BuildRequires: make

%description
Add64 is an additive synthesizer using Qt and the JACK audio connection kit

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}

%build
%{_qt5_libdir}/qt5/bin/qmake -makefile
make %{?_smp_mflags}

%install
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_datadir}/applications
install -d -m 755 %{buildroot}%{_datadir}/pixmaps

install -m 755 -p %{name} %{buildroot}%{_bindir}
install -m 644 -p %{SOURCE2} %{buildroot}%{_datadir}/pixmaps
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications    \
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
BugReportURL: https://sourceforge.net/p/add64/discussion/general/thread/6ff4fec1/
SentUpstream: 2014-09-17
-->
<application>
  <id type="desktop">Add64.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Additive software sound synthesizer</summary>
  <description>
    <p>
      Add64 is an additive modular software synthesizer for generating sounds.
      Unlike other software synthesizers -- that use a skeuomorphic interface of
      knobs, sliders and buttons, Add64 displays a spectral graph and allows the
      user to modify the oscillators and related parameters.
    </p>
  </description>
  <url type="homepage">http://www.amsynth.com/add64.html</url>
  <screenshots>
    <screenshot type="default">http://www.amsynth.com/images/Add64-Harmonics.png</screenshot>
  </screenshots>
  <!-- FIXME: change this to an upstream email address for spec updates
  <updatecontact>someone_who_cares@upstream_project.org</updatecontact>
   -->
</application>
EOF

%files 
%doc LICENSE 
%{_bindir}/%{name}
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/add64.png

%changelog
%autochangelog
