%global source0_hash 0bf2d72d77732f06e7f04c119507c08b9618b21c4027e3997186bd7e4d0788c4
Name:			fcitx-sunpinyin
Version:		0.4.2
Release:        1%{?dist}
Summary:        Sunpinyin Wrapper for Fcitx
License:		GPL-2.0-or-later
URL:			http://fcitx-im.org/wiki/Fcitx
Source0:        http://download.fcitx-im.org/%{name}/%{name}-%{version}.tar.xz
Requires:		fcitx
Requires:		fcitx-data
Requires:		sunpinyin-data
# oreon:deps
BuildRequires:  cmake
BuildRequires:  dbus-devel
BuildRequires:  fcitx
BuildRequires:  fcitx-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  sunpinyin
BuildRequires:  sunpinyin-devel
# /oreon:deps
%description
Fcitx-sunpinyin is a Sunpinyin Wrapper for Fcitx.

SunPinyin is an SLM (Statistical Language Model) based input method
engine. To model the Chinese language, it use a backoff bigram and
trigram language model.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}

%build

%cmake
%cmake_build
%install
%cmake_install
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
