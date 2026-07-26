%global source0_hash 9a0e1e05816fc91029d0c272ecaafc2fb3bc1a3746cf87604843333a1563d178

%global aud_plugin_api %(grep '[ ]*#define[ ]*_AUD_PLUGIN_VERSION[ ]\\+' %{_includedir}/libaudcore/plugin.h 2>/dev/null | sed 's!.*_AUD_PLUGIN_VERSION[ ]*\\([0-9]\\+\\).*!\\1!')
%if 0%{aud_plugin_api} > 0
%global aud_plugin_dep Requires: audacious(plugin-api)%{?_isa} = %{aud_plugin_api}
%endif
%{?aud_plugin_dep}

%global plugindir %(%___build_pre; pkg-config audacious --variable=plugin_dir 2>/dev/null)

Summary: TFMX & Future Composer input plugin for Audacious
Name: audacious-plugin-fc
Version: 0.9.4
Release: 4%{?dist}
Provides: audacious-plugins-fc = %{version}-%{release}
URL: https://github.com/mschwendt/audacious-plugins-fc
License: GPL-2.0-or-later
Source0: https://github.com/mschwendt/audacious-plugins-fc/releases/download/%{version}/audacious-plugins-fc-%{version}.tar.bz2

Patch0: audacious-plugins-fc-0.9.4-uri.patch

BuildRequires: pkgconfig(audacious) >= 3.8
BuildRequires: libtfmxaudiodecoder-devel
BuildRequires: pkgconfig
BuildRequires: libtool automake
BuildRequires: gcc-c++ make

# for /usr/bin/appstream-util
BuildRequires: libappstream-glib

%description
This is an input plugin for Audacious which can play back TFMX
and Future Composer music files from AMIGA. Song-length detection
and seek are implemented, too.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Enforce availability of the audacious(plugin-api) dependency.
%{!?aud_plugin_dep:echo 'No audacious(plugin-api) dependency!' && exit -1}

# just a guard
pkg-config --print-variables audacious | grep ^plugin_dir

%autosetup -p1 -n audacious-plugins-fc-%{version}

%build
%configure --disable-static
%make_build

%install
%make_install
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/*.xml

%files
%license COPYING
%doc README.md
%{plugindir}/Input/fcdecoder.so
#exclude %%{plugindir}/Input/fcdecoder.la
%{_datadir}/appdata/*.xml

%changelog
%autochangelog
