%global source0_hash f7483f44fb9cc70f066ab43e891e2eb757a46028947dd1bfbc70cb2afadac0e5

Name:       ibus-handwrite
Version:    3.0.0
Release:    29%{?dist}
Summary:    IBus handwrite project
License:    GPL-2.0-or-later
URL:        http://code.google.com/p/ibus-handwrite/
Source0:    https://github.com/microcai/ibus-handwrite/releases/download/3.0/%{name}-%{version}.tar.bz2
Patch0:     fixes-blink-issue.patch
Patch1:     ibus-handwrite-fixes-compile.patch

BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  gettext ibus-devel gtk3-devel
BuildRequires:  zinnia-devel
BuildRequires: make

Requires:   ibus

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

%autosetup -p1

%build
autoconf
%configure --disable-static --enable-zinnia --with-zinnia-tomoe=%{_datadir}/zinnia/model/tomoe/
make %{?_smp_mflags}

%install
make DESTDIR=${RPM_BUILD_ROOT} install

# Register as AppStream components to be visible in the software center
#
# NOTE: It would be *awesome* if these files were maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
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

%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_datadir}/ibus-handwrite
%{_libexecdir}/ibus-engine-handwrite

%files ja
%{_datadir}/appdata/handwrite-jp.appdata.xml
%{_datadir}/ibus/component/handwrite-jp.xml

%files zh_CN
%{_datadir}/appdata/handwrite-zh.appdata.xml
%{_datadir}/ibus/component/handwrite-zh.xml

%changelog
%autochangelog
