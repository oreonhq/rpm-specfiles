%global source0_hash 6dd5fd5956924c85af92ebefaef1e113e38fa814355fbb0f07c26049c3014437
Name:		fcitx-hangul
Version:	0.3.1
Release:        1%{?dist}
Summary:        Hangul Engine for Fcitx
License:	GPL-2.0-or-later
URL:		https://fcitx-im.org/wiki/Hangul
Source0:        http://download.fcitx-im.org/fcitx-hangul/%{name}-%{version}.tar.xz
Requires:	fcitx
# oreon:deps
BuildRequires:  cmake
BuildRequires:  fcitx-devel
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libhangul-devel
# /oreon:deps
%description
Fcitx-hangul is a Hangul engine wrapper for Fcitx. It
Provides Korean input method from libhangul.

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
