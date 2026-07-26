%global source0_hash d152489345ae9a714c8465ea0441a5d1e58610078f5341d086bb2b8eba670062

%global sname   skinelchihd
%global commit0 56fc1731410f32d6f13507b8548c9d955af35759
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gitdate 20241008

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

Name:           vdr-skinelchihd
Version:        1.2.10
# Release:        0.8.%%{gitdate}git%%{shortcommit0}%%{?dist}
Release:        1%{?dist}
Summary:        A Elchi based skin with True Color support for the Video Disc Recorder
License:        GPL-2.0-or-later
URL:            https://github.com/FireFlyVDR/vdr-plugin-skinelchihd
Source0:        %url/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Source0:        %%url/archive/%%{commit0}/%%{name}-%%{shortcommit0}.tar.gz
# Configuration files for plugin parameters. These are Fedora specific and not in upstream.
Source1:        %{name}.conf
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  gettext
%if 0%{?fedora} >= 38
BuildRequires:  pkgconfig(GraphicsMagick++)
%else
BuildRequires:  ImageMagick-c++-devel
%endif
BuildRequires:  vdr-devel >= %{vdr_version}
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}

%description
This plugin for Klaus Schmidinger's Video Disc Recorder VDR adds the "Elchi HD"
skin. It is based on the Elchi skin with major re-factoring to make use of newer
VDR features like True Color support.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n vdr-plugin-%{sname}-%%{version}
#%%autosetup -n vdr-plugin-%%{sname}-%%{commit0}

%build
%{set_build_flags}
%if 0%{?fedora} >= 38
%make_build IMAGELIB=graphicsmagick
%else
%make_build IMAGELIB=imagemagick
%endif

%install
# make install would install the themes under /etc, let's not use that
make install-lib install-i18n DESTDIR=%{buildroot}
# install the themes to the custom location used in Fedora
install -dm 755 %{buildroot}%{vdr_vardir}/themes
install -pm 644 themes/*.theme %{buildroot}%{vdr_vardir}/themes/

# skinelchihd.conf
install -Dpm 644 %{SOURCE1} \
    %{buildroot}%{_sysconfdir}/sysconfig/vdr-plugins.d/skinelchihd.conf

%find_lang %{name}

%files -f %{name}.lang
%doc HISTORY* README*
%license COPYING
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/skinelchihd.conf
%{vdr_plugindir}/libvdr-*.so.%{vdr_apiversion}
%{vdr_vardir}/themes/ElchiHD-*.theme

%changelog
%autochangelog
