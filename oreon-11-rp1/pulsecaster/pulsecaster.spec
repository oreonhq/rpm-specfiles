%global source0_hash d52a425c78fc468659a92954332c57b3707fe149d34f37031d367c5a73eed92b

Name:           pulsecaster
Version:        0.9
Release:        24%{?dist}
Summary:        A PulseAudio-based podcast recorder

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://fedorahosted.org/pulsecaster
Source0:        http://fedorahosted.org/released/%{name}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel, python3-setuptools
BuildRequires:  desktop-file-utils, gettext

Requires:       python3-pulsectl
Requires:       python3-gobject
Requires:       gstreamer1 >= 1.0
Requires:       python3-dbus >= 0.83

%description
PulseCaster is a simple PulseAudio-based tool for making podcast
interviews. It is designed for ease of use and simplicity. The user
makes a call with a preferred PulseAudio-compatible Voice-over-IP
(VoIP) softphone application such as Ekiga or Twinkle, and then starts
PulseCaster to record the conversation to a multimedia file. The
resulting file can be published as a podcast or distributed in other
ways.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%{__python3} setup.py build
for F in po/*.po ; do
    L=`echo $F | %{__sed} 's@po/\([^\.]*\).po@\1@'`
    msgfmt -o po/$L.mo $F
done

%install
rm -rf $RPM_BUILD_ROOT
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
desktop-file-install \
    --dir=${RPM_BUILD_ROOT}%{_datadir}/applications \
    %{name}.desktop
for D in ${RPM_BUILD_ROOT}%{_datadir}/locale/* ; do
    mv ${D}/LC_MESSAGES/*.mo ${D}/LC_MESSAGES/%{name}.mo
done
%find_lang %{name}

 
%files -f %{name}.lang
%doc AUTHORS README.md COPYING TODO
%{python3_sitelib}/*
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/GConf/gsettings/*
%{_datadir}/appdata/*
%{_datadir}/glib-2.0/schemas/*

%changelog
%autochangelog
