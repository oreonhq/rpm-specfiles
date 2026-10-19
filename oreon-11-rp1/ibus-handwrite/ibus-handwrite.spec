%global source0_hash f7483f44fb9cc70f066ab43e891e2eb757a46028947dd1bfbc70cb2afadac0e5
Name:       ibus-handwrite
Version:    3.0.0
Release:        1%{?dist}
Summary:        IBus handwrite project
License:    GPL-2.0-or-later
URL:        http://code.google.com/p/ibus-handwrite/
Source0:        https://github.com/microcai/ibus-handwrite/releases/download/3.0/%{name}-%{version}.tar.bz2
Patch0:     fixes-blink-issue.patch
Patch1:     ibus-handwrite-fixes-compile.patch
Requires:   ibus
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gtk3-devel
BuildRequires:  ibus-devel
BuildRequires:  make
BuildRequires:  zinnia-devel
# /oreon:deps
%description
IBus handwrite project.

%package        ja
Summary:        Japanese handwrite input method
Requires:       %{name} = %{version}-%{release}
Requires:       zinnia-tomoe-ja
%description    ja
The %{name}-ja package provide Japanese handwrite input method.

%package        zh_CN
Summary:        Simplified Chinese handwrite input method
Requires:       %{name} = %{version}-%{release}
Requires:       zinnia-tomoe-zh_CN
%description    zh_CN
The %{name}-zh_CN package provide Simplified Chinese handwrite input method.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoconf
%configure --disable-static --enable-zinnia --with-zinnia-tomoe=%{_datadir}/zinnia/model/tomoe/
make %{?_smp_mflags}
%install
make DESTDIR=${RPM_BUILD_ROOT} install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/handwrite-jp.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<component type="inputmethod">
  <id>handwrite-jp.xml</id>
  <metadata_license>CC0-1.0</metadata_license>
  <name>Japanese Handwriting</name>
  <summary>Japanese handwriting input method</summary>
  <description>
    <p>
      The handwriting input method is designed for entering Japanese text.
    </p>
    <p>
      Input methods are typing systems allowing users to input complex languages.
      They are necessary because these contain too many characters to simply be laid
      out on a traditional keyboard.
    </p>
  </description>
  <url type="homepage">http://code.google.com/p/ibus-handwrite/</url>
  <url type="bugtracker">https://code.google.com/p/ibus/issues/list</url>
  <url type="help">https://code.google.com/p/ibus/wiki/FAQ</url>
  <update_contact><!-- upstream-contact_at_email.com --></update_contact>
</component>
EOF
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/handwrite-zh.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<component type="inputmethod">
  <id>handwrite-zh.xml</id>
  <metadata_license>CC0-1.0</metadata_license>
  <name>Simplified Chinese Handwriting</name>
  <summary>Simplified Chinese handwriting input method</summary>
  <description>
    <p>
      The handwriting input method is designed for entering Simplified Chinese text.
    </p>
    <p>
      Input methods are typing systems allowing users to input complex languages.
      They are necessary because these contain too many characters to simply be laid
      out on a traditional keyboard.
    </p>
  </description>
  <url type="homepage">http://code.google.com/p/ibus-handwrite/</url>
  <url type="bugtracker">https://code.google.com/p/ibus/issues/list</url>
  <url type="help">https://code.google.com/p/ibus/wiki/FAQ</url>
  <update_contact><!-- upstream-contact_at_email.com --></update_contact>
</component>
EOF
%find_lang %{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ibus-handwrite-ja -f %{oreon_filedir}/ibus-handwrite-ja.list
%files -n ibus-handwrite-zh_CN -f %{oreon_filedir}/ibus-handwrite-zh_CN.list

%changelog

%autochangelog
