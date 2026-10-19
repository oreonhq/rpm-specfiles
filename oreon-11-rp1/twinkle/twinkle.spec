%global source0_hash 148f84c7b1a517afdd789512fde93e943f12bd67fd5277771a7792da4854950e
%global commit 78313b43dd0de6f124ca4d5aad33fd2248a52dab
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global snap .git%{shortcommit}
Name:           twinkle
Version:        1.11.0
Release:        1%{?dist}
Summary:        SIP-based VoIP client
License:        GPL-2.0-or-later
URL:            https://github.com/LubosD/%{name}
%if 0%{?commit:1}
Source0:        https://github.com/LubosD/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
%else
%endif
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  bcg729-devel
BuildRequires:  bison
BuildRequires:  ccrtp-devel
BuildRequires:  cmake
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  file-devel
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gsm-devel
BuildRequires:  libatomic
BuildRequires:  libsndfile-devel
BuildRequires:  libxml2-devel
BuildRequires:  libzrtpcpp-devel
BuildRequires:  readline-devel
BuildRequires:  speex-devel
BuildRequires:  speexdsp-devel
BuildRequires:  ucommon-devel
# /oreon:deps
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
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop || :
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
