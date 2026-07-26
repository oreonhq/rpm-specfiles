%global source0_hash 29b76ba495feba399ccd4314fb5dc8cba5e7f26d918bcfe1f22f4cdb7dab4bd2

# https://github.com/MarkusEh/vdr-plugin-live/commit/ca482f157cdae62c412103e9f7cdceea38b974dc
%global commit0 ca482f157cdae62c412103e9f7cdceea38b974dc
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gitdate 20260202

# Set vdr_version based on Fedora version
# Default
%global vdr_version 2.6.9

%if 0%{?fedora} == 42
%global vdr_version 2.7.4
%elif 0%{?fedora} == 43
%global vdr_version 2.7.7
%elif 0%{?fedora} >= 44
%global vdr_version 2.8.1
%endif

Name:           vdr-live
Version:        3.5.4
Release:        0.6.%{gitdate}git%{shortcommit0}%{?dist}
# Release:        2%%{?dist}
Summary:        An interactive web interface with HTML5 live stream support for VDR

# The entire source code is GPL-2.0-or-later except live/js/mootools/ which is LicenseRef-Callaway-MIT
License:        GPL-2.0-or-later AND LicenseRef-Callaway-MIT
URL:            https://github.com/MarkusEh/vdr-plugin-live
Source0:        https://github.com/MarkusEh/vdr-plugin-live/archive/%{commit0}/%{name}-%{version}-%{shortcommit0}.tar.gz
# Source0:        https://github.com/MarkusEh/vdr-plugin-live/archive/v%%{version}.tar.gz#/%%{name}-%%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  vdr-devel >= %{vdr_version}
BuildRequires:  pcre2-devel
BuildRequires:  tntnet-devel
BuildRequires:  cxxtools-devel
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}
Requires:       %{name}-data = %{version}-%{release}

%description
New version with HTML5 live stream support.
Live, the "Live Interactive VDR Environment", is a plugin providing the
possibility to interactively control the VDR and some of it's plugins by
a web interface.

Unlike external utility programs that communicate with VDR and it's plugins
by SVDRP, Live has direct access to VDR's data structures and is thus very
fast.

%package data
Summary:       Images, themes and JavaScript for %{name}
BuildArch:     noarch
Requires:      %{name} = %{version}-%{release}

%description data
This package contains images, themes and JavaScript.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n vdr-plugin-live-%{commit0}
#%%autosetup -p1 -n vdr-plugin-live-%%{version}

# delete unused directories and files
find -name .git -type d -or -name gitignore -type d | xargs rm -rfv

# remove bundled tntnet libraries
rm -rf httpd

iconv -f iso-8859-1 -t utf-8 README > README.utf8 ; mv README.utf8 README

%build
%make_build CFLAGS="%{optflags} -fPIC" CXXFLAGS="%{optflags} -fPIC"

%install
%make_install

# live.conf
install -Dpm 644 %{SOURCE1} \
    %{buildroot}%{_sysconfdir}/sysconfig/vdr-plugins.d/live.conf

%find_lang %{name}

%files -f %{name}.lang
%doc CONTRIBUTORS README
%license COPYING
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/live.conf
%config(noreplace) %{_sysconfdir}/vdr/plugins/live/ffmpeg.conf
%{vdr_plugindir}/libvdr-*.so.%{vdr_apiversion}

%files data
%{vdr_resdir}/plugins/live/

%changelog
%autochangelog
