%global source0_hash 7cb0c7c18f46870875189e9a9e3e0e0b44b29cdc2e6405e40bdb9f0fb64291ab
%global pname   screenshot
%global vdr_version 2.6.9
Name:           vdr-%{pname}
Version:        0.0.16
Release:        50%{?dist}
Summary:        VDR plugin: Takes screenshots
License:        GPL-1.0-or-later
URL:            https://github.com/jowi24/vdr-screenshot
Source0:        %{name}-%{version}.tar.gz
Patch0:         %{pname}.fullhd.patch
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  vdr-devel
# /oreon:deps
%description
With this plugin you can take still images of your screen. After installing
the plugin, a new mainmenu entry "Screenshot" will show up. Each time you
select this item, a file /var/cache/vdr/screenshot/title-yyyymmdd-hhmmss.jpg
will be created, where title is the current transmission or the recording
currently replayed.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}
chmod -c -x screenshot.c
# For older VDR versions <=1.7.34
cp Makefile.pre.1.7.34 Makefile

iconv -f iso-8859-1 -t utf-8 HISTORY > HISTORY.utf8 ; mv HISTORY.utf8 HISTORY

%build

%make_build AUTOCONFIG= LIBDIR=. LOCALEDIR=./locale \
    VDRDIR=%{_libdir}/vdr all
%install
install -dm 755 $RPM_BUILD_ROOT%{vdr_plugindir}
install -dm 755 $RPM_BUILD_ROOT%{vdr_cachedir}/screenshot
install -pm 755 libvdr-*.so.%{vdr_apiversion} $RPM_BUILD_ROOT%{vdr_plugindir}
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/locale
cp -pR locale/* $RPM_BUILD_ROOT%{_datadir}/locale
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
