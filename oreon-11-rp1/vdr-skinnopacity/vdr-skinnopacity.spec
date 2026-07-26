%global source0_hash 3af0d3c12a31cf8ad5e933d8b10eb052fb889b7893fc023d92a4da720877aa72

%global pname   SkinNopacity
%global sname   skinnopacity

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

Name:           vdr-skinnopacity
Version:        1.1.19
Release:        11%{?dist}
Summary:        A highly customizable native true color skin for the Video Disc Recorder
License:        GPL-2.0-or-later
URL:            https://gitlab.com/kamel5/SkinNopacity
Source0:        https://gitlab.com/kamel5/%{pname}/-/archive/%{version}/%{pname}-%{version}.tar.bz2
# informed upstream to put copyright and licensing details in source files
# http://projects.vdr-developer.org/issues/1679
# Configuration files for plugin parameters. These are Fedora specific and not in upstream.
Source1:        %{name}.conf

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  freetype-devel
BuildRequires:  pkgconfig(GraphicsMagick++)
BuildRequires:  vdr-devel >= %{vdr_version}
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}
Requires:       %{name}-data = %{version}-%{release}

%description 
The VDR plugin "nOpacity" is a highly customizable native true color skin
for the Video Disc Recorder.

%package data
Summary:       Icons files for %{name}
BuildArch:     noarch
Requires:      %{name} = %{version}-%{release}

%description data
This package contains icons files.
 
%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pname}-%{version}
iconv -f iso-8859-1 -t utf-8 README > README.utf8 ; mv README.utf8 README

%build
%make_build CFLAGS="%{optflags} -fPIC" CXXFLAGS="%{optflags} -fPIC" IMAGELIB=graphicsmagick

%install
# make install would install the themes under /etc, let's not use that
make install-lib install-i18n install-icons DESTDIR=%{buildroot}
# install the themes to the custom location used in Fedora
install -dm 755 %{buildroot}%{vdr_vardir}/themes
install -dm 755 %{buildroot}%{_sysconfdir}/vdr/plugins/%{sname}/themeconfigs/
install -pm 644 themes/*.theme %{buildroot}%{vdr_vardir}/themes/
install -pm 644 conf/theme-* %{buildroot}%{_sysconfdir}/vdr/plugins/%{sname}/themeconfigs/

# skinnopacity.conf
install -Dpm 644 %{SOURCE1} \
    %{buildroot}%{_sysconfdir}/sysconfig/vdr-plugins.d/skinnopacity.conf

%find_lang %{name}

%files -f %{name}.lang
%doc COPYING HISTORY* README*
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/skinnopacity.conf
%config(noreplace) %{_sysconfdir}/vdr/plugins/%{sname}/themeconfigs/theme-*.conf
%{vdr_plugindir}/libvdr-*.so.%{vdr_apiversion}
%{vdr_vardir}/themes/nOpacity-*.theme

%files data
%{vdr_resdir}/plugins/skinnopacity/icons/

%changelog
%autochangelog
