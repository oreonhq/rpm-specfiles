%global source0_hash none
%global source2_hash 3f60eb5ad847bb266ec7ee373086d24864f5558803a54a74fdabb64c88da7ba1
Summary:        Fedora AppStream metadata
Name:      appstream-data
Version:   44
Release:        1%{?dist}
BuildArch: noarch
License:   CC0-1.0 AND CC-BY-1.0 AND CC-BY-SA-1.0 AND GFDL-1.1-or-later
URL:       https://github.com/hughsie/appstream-glib
Source1:        fedora-%{version}.xml.gz
Source2:        fedora-%{version}-icons.tar.gz
Source3:   gstreamer-non-free.xml
Source4:   other-repos.xml
# oreon:deps
BuildRequires:  libappstream-glib
# /oreon:deps
%description
This package provides the distribution specific AppStream metadata required
for the GNOME and KDE software centers. The appstream data is built weekly with
/usr/bin/appstream-builder, combining the data from RPM packages in official
repositories and the extra data in fedora-appstream.

%install
DESTDIR=%{buildroot} appstream-util install-origin fedora %{SOURCE1} %{SOURCE2}
DESTDIR=%{buildroot} appstream-util install \
	%{SOURCE3} %{SOURCE4}
mv %{buildroot}%{_datadir}/app-info %{buildroot}%{_datadir}/swcatalog
mv %{buildroot}%{_datadir}/swcatalog/xmls %{buildroot}%{_datadir}/swcatalog/xml
%oreon_autofiles main

%check

if ! gunzip -c %{buildroot}%{_datadir}/swcatalog/xml/fedora.xml.gz | grep -q '<pkgname>gstreamer1-plugin-openh264</pkgname>' ; then
    echo "missing gstreamer1-plugin-openh264"
    exit 1
fi
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 44-1
- Prepare for Oreon 11 (RP1)
