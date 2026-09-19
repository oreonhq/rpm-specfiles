%global source0_hash 9eeb51982d347aa7b33703031e2c1d8084201374665425cd62199649b29a5411

Name:           gnome-system-log
Version:        3.9.90
Release:        30%{?dist}
Epoch:          1
Summary:        A log file viewer for GNOME

# Automatically converted from old format: GPLv2+ and GFDL - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-GFDL
URL:            http://www.gnome.org
Source0:        http://download.gnome.org/sources/gnome-system-log/3.9/gnome-system-log-%{version}.tar.xz
Source1:        gnome-system-log
Source2:        org.gnome.logview.policy

BuildRequires:  gcc
BuildRequires: gtk3-devel
BuildRequires: intltool
BuildRequires: docbook-dtds
BuildRequires: desktop-file-utils
BuildRequires: itstool
BuildRequires: make

Obsoletes: gnome-utils < 1:3.3
Obsoletes: gnome-utils-devel < 1:3.3
Obsoletes: gnome-utils-libs < 1:3.3

%description
gnome-system-log lets you view various log files on your system.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/gnome-system-log.desktop

mv $RPM_BUILD_ROOT%{_bindir}/gnome-system-log $RPM_BUILD_ROOT%{_bindir}/logview
cp %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}
chmod a+x $RPM_BUILD_ROOT%{_bindir}/gnome-system-log
mkdir -p $RPM_BUILD_ROOT%{_datadir}/polkit-1/actions
cp %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/polkit-1/actions

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
BugReportURL: https://bugzilla.gnome.org/show_bug.cgi?id=730871
SentUpstream: 2014-09-18
-->
<application>
  <id type="desktop">gnome-system-log.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>View system logs</summary>
  <description>
    <p>
      System Logs is an application for viewing the system logs on your 
      computer.
      It provides a graphical viewer for the logs that one would
      typically view in a terminal, such as the boot.log or the system
      messages.
    </p>
  </description>
  <url type="homepage">https://git.gnome.org/browse/gnome-system-log/</url>
  <screenshots>
    <screenshot type="default">https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/gnome-system-log/a.png</screenshot>
  </screenshots>
</application>
EOF

%find_lang %{name} --with-gnome

# https://bugzilla.redhat.com/show_bug.cgi?id=736523
#echo "%%dir %%{_datadir}/help/C" >> aisleriot.lang
#echo "%%{_datadir}/help/C/%%{name}" >> aisleriot.lang
#for l in ca cs de el en_GB es eu fi fr it ja ko oc ru sl sv uk zh_CN; do
#  echo "%%dir %%{_datadir}/help/$l"
#  echo "%%lang($l) %%{_datadir}/help/$l/%%{name}"
#done >> %{name}.lang

%files -f %{name}.lang
%doc COPYING COPYING.docs
%{_bindir}/gnome-system-log
%{_bindir}/logview
%{_datadir}/GConf/gsettings/logview.convert
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/gnome-system-log.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-system-log.gschema.xml
%{_datadir}/icons/hicolor/*/apps/logview.png
%{_datadir}/icons/HighContrast/*/apps/logview.png
%{_datadir}/polkit-1/actions/org.gnome.logview.policy
%doc %{_mandir}/man1/gnome-system-log.1.gz

%changelog
%autochangelog
