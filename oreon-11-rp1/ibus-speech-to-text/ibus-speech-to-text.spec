%global source0_hash 0c82326805bd2fdf1fbb2dec81639a283297d6d67b97d30d7587f42a8b5497ef

%global debug_package %{nil}
Name:   ibus-speech-to-text
Version:  0.7.0
Release:  2%{?dist}
Summary:  A speech to text IBus Input Method using VOSK
ExcludeArch: %{ix86}
License:  GPL-3.0-or-later
URL:     https://github.com/Manish7093/IBus-Speech-To-Text
Source0: https://github.com/Manish7093/IBus-Speech-To-Text/archive/refs/tags/%{version}.tar.gz
BuildRequires:  meson
BuildRequires:  python3-devel
BuildRequires:  ibus-devel >= 1.5.3
BuildRequires:  libadwaita-devel
BuildRequires:  gstreamer1-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  python3-pywhispercpp

Requires:    ibus >= 1.5.3
Requires:    python3-dbus
Requires:    python3-babel
Requires:    gstreamer1
Requires:    gobject-introspection
Requires:    gst-vosk >= 0.3.0
Requires:    gtk4
Requires:    dconf
Requires:    python3-pywhispercpp

%description
A speech to text IBus Input Method using VOSK and WhisperCpp
which can be used to dictate text to any application

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n IBus-Speech-To-Text-%{version}

%build
%meson
%meson_build

%install
%meson_install
desktop-file-validate %{buildroot}/%{_datadir}/applications/ibus-setup-stt.desktop
%py_byte_compile %{python3} %{buildroot}%{_datadir}/%{name}
%find_lang ibus-stt

%files -f ibus-stt.lang
%license COPYING
%doc AUTHORS README.md
%{_libexecdir}/ibus-engine-stt
%{_libexecdir}/ibus-setup-stt
%{_datadir}/ibus-stt
%{_datadir}/ibus/component/stt.xml
%{_datadir}/applications/ibus-setup-stt.desktop
%{_datadir}/glib-2.0/schemas/org.freedesktop.ibus.engine.stt.gschema.xml

%changelog
%autochangelog
