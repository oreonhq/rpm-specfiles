Name:		ibus-kkc
Version:	1.5.22
Release:	29%{?dist}
Summary:	Japanese Kana Kanji input method for ibus

License:	GPL-2.0-or-later
URL:		https://github.com/ueno/ibus-kkc
Source0:	https://github.com/ueno/ibus-kkc/releases/download/v%{version}/%{name}-%{version}.tar.gz
Patch0:		ibus-kkc-content-type.patch
Patch1:         ibus-HEAD.patch

BuildRequires:	vala
BuildRequires:	intltool
BuildRequires:	libkkc-devel >= 0.3.4
BuildRequires:	ibus-devel
BuildRequires:	gtk3-devel
BuildRequires:	desktop-file-utils
BuildRequires: make
Requires:	ibus

%description
A Japanese Kana Kanji Input Method Engine for ibus.


%prep
%autosetup -p1
rm src/*vala.stamp
# don't touch XKB layout under Fedora
sed -i 's!<layout>jp</layout>!<layout>default</layout>!' src/kkc.xml.in.in


%build
%configure
make %{?_smp_mflags}


%install
%make_install INSTALL="install -p"

# Register as an AppStream component to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/kkc.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<component type="inputmethod">
  <id>kkc.xml</id>
  <metadata_license>CC0-1.0</metadata_license>
  <name>Kana Kanji</name>
  <summary>Japanese input method</summary>
  <description>
    <p>
      The Kana Kanji input method is designed for entering Japanese text.
      It uses the Kana Kanji conversion library as backend, whose algorithm is based
      on 3-gram statistical language model generated from Wikipedia data.
    </p>
    <p>
      Input methods are typing systems allowing users to input complex languages.
      They are necessary because these contain too many characters to simply be laid
      out on a traditional keyboard.
    </p>
  </description>
  <url type="homepage">https://bitbucket.org/libkkc/libkkc/</url>
  <compulsory_for_desktop>GNOME</compulsory_for_desktop>
  <project_group>GNOME</project_group>
  <developer_name>The GNOME Project</developer_name>
  <url type="bugtracker">https://code.google.com/p/ibus/issues/list</url>
  <url type="donation">http://www.gnome.org/friends/</url>
  <url type="help">https://code.google.com/p/ibus/wiki/FAQ</url>
  <update_contact><!-- upstream-contact_at_email.com --></update_contact>
</component>
EOF

desktop-file-validate %{buildroot}/%{_datadir}/applications/ibus-setup-kkc.desktop

%find_lang %{name}


%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog README
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/ibus-kkc
%{_libexecdir}/ibus-*-kkc
%{_datadir}/ibus/component/kkc.xml
%{_datadir}/applications/ibus-setup-kkc.desktop


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5.22-29
- Prepare for Oreon 11 (RP1)
