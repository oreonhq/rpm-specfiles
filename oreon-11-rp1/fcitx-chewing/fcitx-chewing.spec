%global source0_hash b313c7134eb173668f42535b0eb6e985eb94fdf5d2fe705940a6cbfdcbadbaf0
Name:		fcitx-chewing
Version:	0.2.3
Release:        1%{?dist}
Summary:        Chewing Wrapper for Fcitx
License:	GPL-2.0-or-later
URL:		https://fcitx-im.org/wiki/Chewing
Source0:        http://download.fcitx-im.org/fcitx-chewing/%{name}-%{version}.tar.xz
Requires:	fcitx, fcitx-data
# oreon:deps
BuildRequires:  cmake
BuildRequires:  fcitx-devel
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libchewing-devel
# /oreon:deps
%description
Fcitx-chewing is a Chewing Wrapper for Fcitx.

Chewing is a set of free intelligent Chinese 
Phonetic IME.

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
