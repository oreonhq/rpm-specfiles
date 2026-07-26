%global source0_hash f042f77a3e1b35bf30666330e36ec38fab8d248c3693c37b7e35d401c3bfabcb

Name:           pulseview
Version:        0.4.2
Release:        25%{?dist}
Summary:        Signal acquisition and analysis GUI for sigrok
# Combined GPLv3+ (libsigrok and libsigrokdecode) and GPLv2+ (pulseview)
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://www.sigrok.org
Source0:        %{url}/download/source/%{name}/%{name}-%{version}.tar.gz
# https://sigrok.org/gitweb/?p=pulseview.git;a=commitdiff;h=ae726b70a7ada9a4be5808e00f0c951318479684
Patch0:         pulseview-qt.patch
# Upstream commit ed643f0b4ac587204a5243451cda181ee1405d62
Patch1:         0001-Fix-broken-build-due-to-C-template-behind-C-linkage.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=2429719
# move to C++14 needed by Boost 1.90
Patch2:         pulseview-cpp14.patch
BuildRequires:  pkgconfig(libsigrokcxx) >= 0.5.2
BuildRequires:  pkgconfig(libsigrokdecode) >= 0.5.2
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       hicolor-icon-theme
# https://bugzilla.redhat.com/show_bug.cgi?id=1819609
# needed for plugins that handle displaying SVG graphics
Requires:       qt5-qtsvg

%description
PulseView is an application for enabling data acquisition and analysis with
test and measurement devices such as logic analyzers, oscilloscopes,
mixed-signal devices, digital multimeters and sensors, etc. It uses sigrok
libraries under the hood.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
# TODO: Please submit an issue to upstream (rhbz#2381376)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake -DCMAKE_BUILD_TYPE=Release -DDISABLE_WERROR=True
%cmake_build

%install
%cmake_install

# Why you install appdata in bad location, you sigrok upstream?
mv %{buildroot}/%{_datadir}/metainfo %{buildroot}/%{_datadir}/appdata

desktop-file-validate \
	%{buildroot}/%{_datadir}/applications/org.sigrok.PulseView.desktop

appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml

%files
%doc README
%license COPYING
%{_mandir}/man1/%{name}.1*
%{_bindir}/%{name}
%{_datadir}/applications/org.sigrok.PulseView.desktop
%{_datadir}/icons/hicolor/48x48/apps/pulseview.png
%{_datadir}/icons/hicolor/scalable/apps/pulseview.svg
%{_datadir}/appdata/org.sigrok.PulseView.appdata.xml

%changelog
%autochangelog
