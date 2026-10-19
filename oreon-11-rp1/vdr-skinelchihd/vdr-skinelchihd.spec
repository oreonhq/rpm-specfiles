%global source0_hash d152489345ae9a714c8465ea0441a5d1e58610078f5341d086bb2b8eba670062
%global sname   skinelchihd
%global commit0 56fc1731410f32d6f13507b8548c9d955af35759
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gitdate 20241008
%global vdr_version 2.6.9
Name:           vdr-skinelchihd
Version:        1.2.10
Release:        1%{?dist}
Summary:        A Elchi based skin with True Color support for the Video Disc Recorder
License:        GPL-2.0-or-later
URL:            https://github.com/FireFlyVDR/vdr-plugin-skinelchihd
Source0:        https://github.com/FireFlyVDR/vdr-plugin-%{sname}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.conf
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}
# oreon:deps
BuildRequires:  ImageMagick-c++-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  vdr-devel
# /oreon:deps
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
%make_build IMAGELIB=imagemagick
%install
make install-lib install-i18n DESTDIR=%{buildroot}
install -dm 755 %{buildroot}%{vdr_vardir}/themes
install -pm 644 themes/*.theme %{buildroot}%{vdr_vardir}/themes/
install -Dpm 644 %{SOURCE1} \
    %{buildroot}%{_sysconfdir}/sysconfig/vdr-plugins.d/skinelchihd.conf
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
