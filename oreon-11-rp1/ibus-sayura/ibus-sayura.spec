%global source0_hash 288c61af202ebfc36c826812e7ba8bcc6d5a0cc4d46db05ad2c4da2df4913d6b
Name:       ibus-sayura
Version:    1.3.2
Release:        1%{?dist}
Summary:        The Sinhala engine for IBus input platform
License:    GPL-2.0-or-later
URL:        https://pagure.io/ibus-sayura
Source0:        https://github.com/pravins/ibus-sayura/archive/1.3.2.tar.gz#/ibus-sayura-%{version}.tar.gz
Patch0:     fix-for-wayland-rhbz1724759.patch
Requires:   ibus
# oreon:deps
BuildRequires:  gettext-devel
BuildRequires:  ibus-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
# /oreon:deps
%description
The Sayura engine for IBus platform. It provides Sinhala input method.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --disable-static
make %{?_smp_mflags}
%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/sayura.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<component type="inputmethod">
  <id>sayura.xml</id>
  <metadata_license>CC0-1.0</metadata_license>
  <name>Sayura</name>
  <summary>Sihali input method</summary>
  <description>
    <p>
      The Sayura input method is designed for entering Sinhala text.
    </p>
    <p>
      Input methods are typing systems allowing users to input complex languages.
      They are necessary because these contain too many characters to simply be laid
      out on a traditional keyboard.
    </p>
  </description>
  <url type="homepage">https://fedorahosted.org/ibus-sayura/</url>
  <url type="bugtracker">https://code.google.com/p/ibus/issues/list</url>
  <url type="help">https://code.google.com/p/ibus/wiki/FAQ</url>
  <languages>
    <lang percentage="100">si</lang>
  </languages>
  <update_contact><!-- upstream-contact_at_email.com --></update_contact>
</component>
EOF
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.2-35
- Prepare for Oreon 11 (RP1)
