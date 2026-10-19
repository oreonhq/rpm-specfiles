%global source0_hash 583856ba40c0c12dd1bc75226d0f59f77abf5e12d1d803efd97439fab4a14c1b
%global revision 70
Name:             fontaine
Version:          0
Release:        1%{?dist}
Summary:        Font file meta information utility
License:          GPL-2.0-or-later
URL:              http://unifont.org/fontaine/
Source0:        https://sourceforge.net/code-snapshots/svn/f/fo/%{name}/code/%{name}-code-r%{revision}-trunk.zip
# oreon:deps
BuildRequires:  cmake
BuildRequires:  freetype-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
# /oreon:deps
%description
Fontaine is a command-line utility that displays key meta information about
font files, including but not limited to font name, style, weight,
glyph count, character count, copyright, license information  and 
orthographic coverage.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n fontaine-code-r%{revision}-trunk
find -type d -name .svn | xargs -r rm -rf

%build

%cmake -DCMAKE_POLICY_DEFAULT_CMP0057=NEW -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build
%install
%cmake_install
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
