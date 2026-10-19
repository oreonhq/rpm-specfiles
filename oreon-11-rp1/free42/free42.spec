%global source0_hash 61baf9230a980485c659c2c133676b2ae37634306d6b6f7d5ffde1bf3bc63de5
%global app_id  com.thomasokken.free42
Name:           free42
Epoch:          1
Version:        3.3.12
Release:        1%{?dist}
License:        GPL-2.0-only AND BSD-3-Clause
Summary:        42S Calculator Simulator
URL:            https://www.thomasokken.com/free42/
Source0:        https://www.thomasokken.com/free42/upstream/free42-nologo-%{version}.tgz
Patch0:         free42-makefile.patch
Patch1:         free42-intel-lib-arches.patch
Provides:       bundled(IntelRDFPMathLib) = 2.1
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gtk3-devel
BuildRequires:  libappstream-glib
BuildRequires:  make
# /oreon:deps
%description
Free42 is a complete re-implementation of the 42S calculator and the
82240 printer.  It was written from scratch, without using any HP code.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir free42-nologo-%{version}
%oreon_prep
%build

cd gtk
export CFLAGS_OPT="%{optflags}"
make BCD_MATH=1 AUDIO_ALSA=1
cat <<EOF >%{app_id}.desktop
[Desktop Entry]
Name=Free42
GenericName=Free42 calculator simulator
Exec=free42dec
Icon=free42
Terminal=false
Type=Application
Categories=Utility;Calculator;
StartupWMClass=%{name}dec
EOF
cat <<EOF >%{app_id}.appdata.xml
<?xml version="1.0" encoding="UTF-8"?>
<component type="desktop-application">
    <id>%{app_id}</id>
    <name>Free42</name>
    <summary>42S Calculator Simulator</summary>
    <metadata_license>FSFAP</metadata_license>
    <project_license>GPL-2.0</project_license>
    <description>
        <p>
            Free42 is a complete re-implementation of the 42S calculator and the
            82240 printer.  It was written from scratch, without using any HP code.
        </p>
    </description>
    <launchable type="desktop-id">free42.desktop</launchable>
    <provides>
        <binary>free42dec</binary>
    </provides>
    <content_rating type="oars-1.1"/>
    <developer_name>Thomas Okken</developer_name>
    <releases>
        <release version="%{version}" date="%(date +%F -r %{SOURCE0})" />
    </releases>
    <url type="homepage">https://www.thomasokken.com/free42/</url>
</component>
EOF
%install
install -D -p -m 755 gtk/free42dec %{buildroot}%{_bindir}/free42dec
install -D -p -m 644 gtk/icon-48x48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
install -D -p -m 644 gtk/icon-128x128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
install -D -p -m 644 gtk/%{app_id}.desktop %{buildroot}%{_datadir}/applications/%{app_id}.desktop
install -D -p -m 644 gtk/%{app_id}.appdata.xml %{buildroot}%{_metainfodir}/%{app_id}.appdata.xml
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{app_id}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{app_id}.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
