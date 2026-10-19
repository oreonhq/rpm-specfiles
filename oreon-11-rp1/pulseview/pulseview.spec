%global source0_hash f042f77a3e1b35bf30666330e36ec38fab8d248c3693c37b7e35d401c3bfabcb
Name:           pulseview
Version:        0.4.2
Release:        1%{?dist}
Summary:        Signal acquisition and analysis GUI for sigrok
License:        GPL-3.0-or-later
URL:            http://www.sigrok.org
Source0:        http://www.sigrok.org/download/source/%{name}/%{name}-%{version}.tar.gz
Patch0:         pulseview-qt.patch
Patch1:         0001-Fix-broken-build-due-to-C-template-behind-C-linkage.patch
Patch2:         pulseview-cpp14.patch
Requires:       hicolor-icon-theme
Requires:       qt5-qtsvg
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(libsigrokcxx)
BuildRequires:  pkgconfig(libsigrokdecode)
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
# /oreon:deps
%description
PulseView is an application for enabling data acquisition and analysis with
test and measurement devices such as logic analyzers, oscilloscopes,
mixed-signal devices, digital multimeters and sensors, etc. It uses sigrok
libraries under the hood.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake -DCMAKE_BUILD_TYPE=Release -DDISABLE_WERROR=True
%cmake_build
%install
%cmake_install
mv %{buildroot}/%{_datadir}/metainfo %{buildroot}/%{_datadir}/appdata
desktop-file-validate \
	%{buildroot}/%{_datadir}/applications/org.sigrok.PulseView.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
