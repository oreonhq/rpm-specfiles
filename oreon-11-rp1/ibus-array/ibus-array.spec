%global source0_hash dcb543c21486a61cb54073288d1c875035628110df74c77ed3c7a32bf3788625
Name:           ibus-array
Version:        0.3.2
Release:        1%{?dist}
Summary:        The Array 30 input method for IBus input platform
Summary(zh_TW): IBus行列30輸入法
License:        GPL-2.0-or-later
URL:            https://github.com/lexical/ibus-array
Source0:        https://github.com/lexical/%{name}/archive/refs/tags/release-%{version}.tar.gz#/%{name}-release-%{version}.tar.gz
Patch0:         0001-remove-unused-python3-shebang.patch
Requires:   ibus
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  meson
BuildRequires:  pkgconf
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  pkgconfig(opencc)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  python3-devel
# /oreon:deps
%description
Array 30 input method for IBus that uses the latest keymap table
and follows the Array input method spec implementation.

%description -l zh_TW
IBus行列30輸入法，遵循行列輸入法規格書的定義，
含最新鍵碼表版本，符合一般行列輸入法用戶的慣用方式。

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-release-%{version}
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
