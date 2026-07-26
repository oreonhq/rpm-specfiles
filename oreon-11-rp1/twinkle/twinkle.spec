%global source0_hash 148f84c7b1a517afdd789512fde93e943f12bd67fd5277771a7792da4854950e

%global commit 78313b43dd0de6f124ca4d5aad33fd2248a52dab
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global snap .git%{shortcommit}

Name:           twinkle
Version:        1.10.3
Release:        10%{?snap}%{?dist}
Summary:        SIP-based VoIP client

# Incorrect FSF addresses: https://github.com/LubosD/twinkle/issues/71
License:        GPL-2.0-or-later
URL:            https://github.com/LubosD/%{name}
%if 0%{?commit:1}
Source0:        https://github.com/LubosD/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
%else
Source0:        https://github.com/LubosD/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
%endif

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  alsa-lib-devel
BuildRequires:  bcg729-devel
BuildRequires:  bison
BuildRequires:  ccrtp-devel
BuildRequires:  flex
# The Fedora package is incompatible with the version required by twinkle
# BuildRequires:  ilbc-devel
BuildRequires:  libatomic
BuildRequires:  libsndfile-devel
BuildRequires:  libxml2-devel
BuildRequires:  libzrtpcpp-devel
BuildRequires:  file-devel
BuildRequires:  gsm-devel
BuildRequires:  readline-devel
BuildRequires:  speex-devel
BuildRequires:  speexdsp-devel
BuildRequires:  ucommon-devel

Requires:       hicolor-icon-theme

%description
Twinkle is a SIP-based VoIP client.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if 0%{?commit:1}
%autosetup -p1 -n %{name}-%{commit}
%else
%autosetup -p1
%endif

%build
%cmake -DWITH_ZRTP=On \
    -DWITH_SPEEX=On \
    -DWITH_ILBC=Off \
    -DWITH_DIAMONDCARD=Off \
    -DWITH_GSM=On \
    -DWITH_G729=On
%cmake_build

%install
%cmake_install
%find_lang %{name} --with-qt

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop || :

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS
%{_bindir}/%{name}
%{_bindir}/%{name}-console
%{_bindir}/%{name}-uri-handler
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/twinkle.svg
%{_datadir}/pixmaps/%{name}.png
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/providers.csv
%{_datadir}/%{name}/ringback.wav
%{_datadir}/%{name}/ringtone.wav
%{_datadir}/%{name}/twinkle16.png
%{_datadir}/%{name}/twinkle32.png
%{_datadir}/%{name}/twinkle48.png
%doc %{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
