%global source0_hash c4f97e496a3666c70786d136e6f2ccc5e8a3813eb08cda35cacd7eb0d16f4d56

Name:       lingot
Version:    1.1.1
Release:    16%{?dist}
Summary:    A musical instruments tuner

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:    GPL-2.0-or-later
URL:        https://www.nongnu.org/%{name}/
Source0:    https://download.savannah.gnu.org/releases/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  alsa-lib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  fftw-devel
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  json-c-devel
BuildRequires:  gcc
BuildRequires:  gtk3-devel
BuildRequires:  libappstream-glib
BuildRequires:  libglade2-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires: make

%description
LINGOT is a musical instrument tuner. It's accurate, easy to use, and highly
configurable. Originally conceived to tune electric guitars, its
configurability gives it a more general character.

%package devel
Summary:  %{summary}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the headers and shared libraries for %{name}.
NOTE: The library is currently experimental and its interface is subject to
change.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%configure
%make_build

%install
%make_install
# we install these ourselves to have total control over what files are being
# placed there. COPYING, for example needs to be placed using the license macro
rm -rf %{buildroot}/%{_defaultdocdir}/%{name}

# Delete static libraries
find %{buildroot}/%{_libdir}/ -name "liblingot.*a" -delete

%find_lang %{name}

desktop-file-validate %{buildroot}/%{_datadir}/applications/*%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*%{name}.appdata.xml

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README THANKS
%license COPYING
%{_bindir}/%{name}
%{_datadir}/metainfo/*%{name}.appdata.xml
%{_datadir}/applications/*%{name}.desktop
%{_mandir}/man1/%{name}.1*
%{_datadir}/icons/hicolor/scalable/apps/*.%{name}.svg
%{_libdir}/liblingot.so.0
%{_libdir}/liblingot.so.0.0.0

%files devel
%{_includedir}/%{name}
%{_libdir}/liblingot.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
