%global source0_hash 2c28ed7acea27ae3d541036f2e2ca5ed7e0121badf477e3cfa5ec8d282337e23

Summary: pilot desktop software
Name: jpilot
Version: 1.8.2
Release: 35%{?dist}
License: GPL-2.0-only
URL: https://www.jpilot.org/
Source0: https://www.jpilot.org/tarballs/jpilot-%{version}.tar.gz
Source1: jpilot.desktop

Patch0: jpilot-0.99.7-conf.patch
Patch1: jpilot-1.8.2-gcc10.patch
Patch2: jpilot-configure-c99.patch
Patch3: jpilot-callback-types.patch

BuildRequires: gcc
BuildRequires: gettext, pilot-link-devel, perl-XML-Parser, libgcrypt-devel
BuildRequires: intltool
BuildRequires: gtk2-devel >= 2.0.3
BuildRequires: pilot-link >= 0.12.5
BuildRequires: make
BuildRequires: ImageMagick
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

Requires: hicolor-icon-theme
# for XMP icons support
Requires: gdk-pixbuf2-modules-extra

ExcludeArch: s390, s390x

%description
J-Pilot is a desktop organizer application for the palm pilot that runs under
Linux.  It is similar in functionality to the one that 3com distributes for a
well known rampant legacy operating system.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .confp
%patch -P1 -p1 -b .gcc10
%patch -P2 -p1
%patch -P3 -p1
iconv -f windows-1252 -t utf-8 AUTHORS >AUTHORS.aux
mv AUTHORS.aux AUTHORS

%build
%configure --disable-rpath --with-pilot-prefix=%{_prefix}

cd po
make clean
make update-po
cd ..

make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT libdir=%{_libdir}/jpilot/plugins install

mkdir -p $RPM_BUILD_ROOT%{_datadir}/jpilot/ \
         $RPM_BUILD_ROOT%{_datadir}/applications

ls -la jpilotrc*
install -m644 jpilotrc.* $RPM_BUILD_ROOT%{_datadir}/jpilot/
install -p empty/*.pdb $RPM_BUILD_ROOT%{_datadir}/jpilot/
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}

# install icon
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
convert icons/jpilot-icon3.xpm $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/jpilot.png

mkdir $RPM_BUILD_ROOT%{_metainfodir}
cat <<EOF > $RPM_BUILD_ROOT%{_metainfodir}/%{name}.appdata.xml
<?xml version="1.0" encoding="UTF-8"?>
<component type="desktop-application">
    <id>org.jpilot.JPilot</id>
    <name>J-Pilot</name>
    <summary>pilot desktop software</summary>
    <metadata_license>FSFAP</metadata_license>
    <project_license>GPL-2.0-only</project_license>
    <description>
        <p>
            J-Pilot is a desktop organizer application for the palm pilot that runs under
            Linux.  It is similar in functionality to the one that 3com distributes for a
            well known rampant legacy operating system.
        </p>
    </description>
    <launchable type="desktop-id">%{name}.desktop</launchable>
    <provides>
        <binary>jpilot</binary>
    </provides>
    <content_rating type="oars-1.1"/>
    <developer_name>Judd Montgomery</developer_name>
    <releases>
        <release version="%{version}" date="%(date +%F -r %{SOURCE0})" />
    </releases>
    <screenshots>
        <screenshot type="default">
            <caption>Datebook Screen</caption>
            <image>https://www.jpilot.org/screenshots/jpilot-datebook.png</image>
        </screenshot>
        <screenshot>
            <caption>Address Screen</caption>
            <image>https://www.jpilot.org/screenshots/jpilot-address.png</image>
        </screenshot>
        <screenshot>
            <caption>Todo Screen</caption>
            <image>https://www.jpilot.org/screenshots/jpilot-todo.png</image>
        </screenshot>
        <screenshot>
            <caption>Memo Screen</caption>
            <image>https://www.jpilot.org/screenshots/jpilot-memo.png</image>
        </screenshot>
    </screenshots>
    <url type="homepage">%{url}</url>
</component>
EOF
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/%{name}.appdata.xml

%find_lang %name

%files -f %{name}.lang
%doc %{_docdir}/jpilot
%{_bindir}/*
%{_datadir}/jpilot
%{_datadir}/icons/hicolor/*/*/jpilot.*
%{_libdir}/%{name}
%{_mandir}/man1/*.*
%{_datadir}/applications/*
%{_metainfodir}/%{name}.appdata.xml

%changelog
%autochangelog
