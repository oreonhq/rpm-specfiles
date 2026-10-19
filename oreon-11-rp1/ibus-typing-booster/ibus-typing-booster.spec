%global source0_hash 8469fbc41817c566e0a8746a154f4697fea9595a9d089ff881c8397d5b1858c7
Name:       ibus-typing-booster
Version:    2.31.1
Release:        1%{?dist}
Summary:        A completion input method
License:    GPL-3.0-or-later AND Apache-2.0
URL:        https://mike-fabian.github.io/ibus-typing-booster/
Source0:        https://github.com/mike-fabian/ibus-typing-booster/releases/download/%{version}/ibus-typing-booster-%{version}.tar.gz
Requires:   ibus >= 1.5.3
Requires:   m17n-lib
%{?__python3:Requires: %{__python3}}
Requires:   python3-dbus
Requires:   python3-distro
Requires:   python3-enchant
Requires:   python3-pyxdg
%if 0%{?fedora} || (0%{?oreon} >= 11)
Requires:     python3-rapidfuzz
%endif
%if 0%{?fedora} >= 24 || 0%{?rhel} > 7 || (0%{?oreon} >= 11)
Recommends: google-noto-emoji-color-fonts
Recommends: google-noto-emoji-fonts
Recommends: gdouros-symbola-fonts
Recommends: python3-langtable
Recommends: python3-pyaudio
Recommends: python3-regex
Recommends: python3-pyatspi
Recommends: wl-clipboard
Recommends: python3-httpx
%endif
%if 0%{?fedora} >= 26 || 0%{?rhel} > 7 || (0%{?oreon} >= 11)
Requires: cldr-emoji-annotation
Requires: unicode-ucd
%endif
%if 0%{?fedora} >= 24 || 0%{?rhel} > 7 || (0%{?oreon} >= 11)
%else
%endif
%if 0%{?fedora} || (0%{?oreon} >= 11)
%endif
%if 0%{?fedora} >= 35 || (0%{?oreon} >= 11)
%endif
%if 0%{?fedora} && 0%{?fedora} >= 34 || (0%{?oreon} >= 11)
%endif
BuildArch:  noarch
ExcludeArch: ppc64 s390x
# oreon:deps
BuildRequires:  appstream
BuildRequires:  dbus-x11
BuildRequires:  dconf
BuildRequires:  desktop-file-utils
BuildRequires:  enchant2
BuildRequires:  gcc
BuildRequires:  glib2
BuildRequires:  glibc-gconv-extra
BuildRequires:  glibc-langpack-am
BuildRequires:  glibc-langpack-ar
BuildRequires:  glibc-langpack-cs
BuildRequires:  glibc-langpack-de
BuildRequires:  glibc-langpack-en
BuildRequires:  glibc-langpack-km
BuildRequires:  glibc-langpack-pt
BuildRequires:  gtk3
BuildRequires:  hunspell-cs
BuildRequires:  hunspell-de
BuildRequires:  hunspell-en
BuildRequires:  hunspell-es
BuildRequires:  hunspell-fr
BuildRequires:  hunspell-it
BuildRequires:  hunspell-ko
BuildRequires:  ibus
BuildRequires:  ibus-devel
BuildRequires:  libappstream-glib
BuildRequires:  m17n-db-devel
BuildRequires:  m17n-db-extras
BuildRequires:  m17n-lib
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-enchant
BuildRequires:  python3-gobject
BuildRequires:  python3-gobject-base
BuildRequires:  python3-libvoikko
BuildRequires:  python3-pyxdg
BuildRequires:  python3-rapidfuzz
BuildRequires:  python3-regex
BuildRequires:  voikko-fi
# /oreon:deps
%description
Ibus-typing-booster is a context sensitive completion
input method to speedup typing.

%package tests
Summary:        Tests for the %{name} package
Requires:       %{name} = %{version}-%{release}
%description tests
The %{name}-tests package contains tests that can be used to verify
the functionality of the installed %{name} package.

%package -n emoji-picker
Summary: An emoji selection tool
Requires: ibus-typing-booster = %{version}-%{release}
%description -n emoji-picker
A simple application to find and insert emoji and other
Unicode symbols.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

export PYTHON=%{__python3}
%configure --disable-static --enable-installed-tests
%make_build
%install 
export PYTHON=%{__python3}
%make_install NO_INDEX=true  pkgconfigdir=%{_datadir}/pkgconfig
%py_byte_compile %{python3} /usr/share/ibus-typing-booster/engine
%py_byte_compile %{python3} /usr/share/ibus-typing-booster/setup
%if 0%{?fedora} >= 26 || 0%{?rhel} > 7 || (0%{?oreon} >= 11)
    rm $RPM_BUILD_ROOT/%{_datadir}/%{name}/data/annotations/*.xml
    rm $RPM_BUILD_ROOT/%{_datadir}/%{name}/data/annotationsDerived/*.xml
    rm $RPM_BUILD_ROOT/%{_datadir}/%{name}/data/UnicodeData.txt
    rm $RPM_BUILD_ROOT/%{_datadir}/%{name}/data/Blocks.txt
    rm $RPM_BUILD_ROOT/%{_datadir}/%{name}/data/DerivedAge.txt
    gzip -n --force --best $RPM_BUILD_ROOT/%{_datadir}/%{name}/data/*.txt
    gzip -n --force --best $RPM_BUILD_ROOT/%{_datadir}/%{name}/data/*.json
%else
    gzip -n --force --best $RPM_BUILD_ROOT/%{_datadir}/%{name}/data/*.{txt,json}
    gzip -n --force --best $RPM_BUILD_ROOT/%{_datadir}/%{name}/data/annotations/*.xml
    gzip -n --force --best $RPM_BUILD_ROOT/%{_datadir}/%{name}/data/annotationsDerived/*.xml
%endif
%find_lang %{name}
%oreon_autofiles emoji-picker usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export LC_ALL=C.UTF-8
appstreamcli validate --pedantic --no-net %{buildroot}/%{_datadir}/metainfo/*.metainfo.xml
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*.metainfo.xml
desktop-file-validate \
    $RPM_BUILD_ROOT%{_datadir}/applications/ibus-setup-typing-booster.desktop
desktop-file-validate \
    $RPM_BUILD_ROOT%{_datadir}/applications/emoji-picker.desktop
for i in */*.py
do
    echo python3 -m py_compile $i
    python3 -m py_compile $i
done
pushd engine
    if [ -e /usr/share/m17n/si-wijesekara.mim ] ; then
        python3 m17n_translit.py -v
    else
        echo "/usr/share/m17n/si-wijesekara.mim does not exist, m17n-db probably < 1.8.6, skipping doctest of m17n_translit.py"
    fi
    python3 itb_emoji.py -v
    python3 itb_util_core.py -v
    python3 itb_util_gui.py -v
popd
mkdir -p /tmp/glib-2.0/schemas/
cp org.freedesktop.ibus.engine.typing-booster.gschema.xml \
   /tmp/glib-2.0/schemas/org.freedesktop.ibus.engine.typing-booster.gschema.xml
glib-compile-schemas /tmp/glib-2.0/schemas #&>/dev/null || :
export XDG_DATA_DIRS=/tmp:%{_datadir} # /usr/share is needed to make enchant2 work!
eval $(dbus-launch --sh-syntax)
dconf dump /
dconf write /org/freedesktop/ibus/engine/typing-booster/offtherecord false
dconf write /org/freedesktop/ibus/engine/typing-booster/usedigitsasselectkeys true
dconf write /org/freedesktop/ibus/engine/typing-booster/addspaceoncommit true
dconf write /org/freedesktop/ibus/engine/typing-booster/tabenable false
dconf write /org/freedesktop/ibus/engine/typing-booster/inputmethod "'NoIME'"
dconf write /org/freedesktop/ibus/engine/typing-booster/rememberlastusedpreeditime true
dconf write /org/freedesktop/ibus/engine/typing-booster/mincharcomplete 1
dconf write /org/freedesktop/ibus/engine/typing-booster/dictionary "'en_US'"
dconf write /org/freedesktop/ibus/engine/typing-booster/emojipredictions true
dconf write /org/freedesktop/ibus/engine/typing-booster/autocommitcharacters "''"
dconf write /org/freedesktop/ibus/engine/typing-booster/pagesize 6
dconf write /org/freedesktop/ibus/engine/typing-booster/shownumberofcandidates true
dconf write /org/freedesktop/ibus/engine/typing-booster/showstatusinfoinaux true
dconf write /org/freedesktop/ibus/engine/typing-booster/inlinecompletion false
dconf write /org/freedesktop/ibus/engine/typing-booster/keybindings "{'next_input_method': <['Control+Down', 'Control+KP_Down']>, 'previous_input_method': <['Control+Up', 'Control+KP_Up']>, 'lookup_related': <['Mod5+F12']>, 'enable_lookup': <['Tab', 'ISO_Left_Tab', 'KP_Divide']>, 'select_next_candidate': <['Tab', 'ISO_Left_Tab', 'Down', 'KP_Down']>, 'lookup_table_page_down': <['Page_Down', 'KP_Page_Down', 'KP_Next']>, 'toggle_emoji_prediction': <['Mod5+F6']>, 'lookup_table_page_up': <['Page_Up', 'KP_Page_Up', 'KP_Prior']>, 'toggle_off_the_record': <['Mod5+F9']>, 'cancel': <['Escape']>, 'setup': <['Mod5+F10']>, 'select_previous_candidate': <['Shift+Tab', 'Shift+ISO_Left_Tab', 'Up', 'KP_Up']>}"
dconf dump /
make check && rc=0 || rc=1
cat tests/*.log
if [ $rc != 0 ] ; then
    exit $rc
fi
%files -f %{oreon_filedir}/main.list
%files -n ibus-typing-booster-tests -f %{oreon_filedir}/ibus-typing-booster-tests.list
%files -n emoji-picker -f %{oreon_filedir}/emoji-picker.list

%changelog

%autochangelog
