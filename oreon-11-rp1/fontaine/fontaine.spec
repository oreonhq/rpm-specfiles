%global source0_hash 583856ba40c0c12dd1bc75226d0f59f77abf5e12d1d803efd97439fab4a14c1b

%global revision 70

Name:             fontaine
Version:          0
Release:          40.svn%{revision}%{?dist}
Summary:          Font file meta information utility
License:          GPL-2.0-or-later
URL:              http://unifont.org/fontaine/

Source0:          https://sourceforge.net/code-snapshots/svn/f/fo/fontaine/code/fontaine-code-r%{revision}-trunk.zip

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:    cmake gettext
BuildRequires:    freetype-devel

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

%files -f %{name}.lang
%doc documentation/html
%license documentation/GPL-2.0-LICENSE
%{_bindir}/%{name}

%changelog
%autochangelog
