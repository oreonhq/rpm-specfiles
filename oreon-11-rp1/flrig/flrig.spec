%global source0_hash 6a5f2b87d4fffed410a35b3a176b5d04e60ed4de3fda545079f3656e42ef42bd

# For test builds, should be set to 0 for release builds.
%global alpha 0

Name:           flrig
Version:        2.0.10
Release:        3%{?dist}
Summary:        Transceiver control program

License:        GPL-3.0-or-later AND LGPL-3.0-or-later AND GPL-3.0-only
URL:            http://www.w1hkj.com/
%if %{alpha}
Source0:        https://www.w1hkj.org/alpha/%{name}/%{name}-%{version}.tar.gz
%else
Source0:        https://www.w1hkj.org/files/%{name}/%{name}-%{version}.tar.gz
%endif
Source100:      flrig.appdata.xml
Source101:      flrig.png

Patch0:         flrig-headers.patch

BuildRequires:  gcc gcc-c++ make
BuildRequires:  fltk-devel >= 1.3.0
%if 0%{?rhel}
Provides:       bundled(xmlrpc)
%else
BuildRequires:  flxmlrpc-devel
%endif
BuildRequires:  desktop-file-utils
%if 0%{?fedora}
BuildRequires:  libappstream-glib
%endif
BuildRequires:  libudev-devel

# xdg-open is used in src/main.cxx
Requires:       xdg-utils

%description
Flrig is a transceiver control program designed to be used either stand alone or
as an adjunct to fldigi.  The supported transceivers all have some degree of
CAT.  The flrig user interface changes to accommodate the degree of CAT support
available for the transceiver in use. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%if 0%{?fedora}
export CXXFLAGS="-std=c++17 $RPM_OPT_FLAGS"
%endif
%{?rhel:export LDFLAGS="-lfltk"}
%configure
%make_build

%install
%make_install

# Install icon file manually as provided XPM icon does not work in all desktop environments.
install -D %{SOURCE101} %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/flrig.png

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%if 0%{?fedora}
mkdir -p %{buildroot}%{_datadir}/metainfo
install -pm 0644 %{SOURCE100} %{buildroot}%{_datadir}/metainfo/
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml
%endif

%files
%license COPYING
%doc AUTHORS ChangeLog README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/icons/hicolor/64x64/apps/flrig.png
%{?fedora:%{_datadir}/metainfo/*.appdata.xml}

%changelog
%autochangelog
