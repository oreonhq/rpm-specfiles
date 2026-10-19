%global source0_hash 8fc7dc560167b2cb7193e76aca625a152dc19b0ebf49816b78539cbb90d80d02
Name: gtkspell
Version: 2.0.16
Release:        1%{?dist}
License: GPL-2.0-or-later
Summary:        On-the-fly spell checking for GtkTextView widgets
URL: http://gtkspell.sourceforge.net/
Source0:        http://gtkspell.sourceforge.net/download/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  enchant-devel
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gtk2-devel
BuildRequires:  intltool
BuildRequires:  make
# /oreon:deps
%description
GtkSpell provides word-processor-style highlighting and replacement of
misspelled words in a GtkTextView widget as you type. Right-clicking a
misspelled word pops up a menu of suggested replacements.

%package devel
Summary: Development files for GtkSpell
Requires: %{name} = %{version}-%{release}
Requires: gtk2-devel
Requires: pkgconfig
%description devel
The gtkspell-devel package provides header files for developing
applications which use GtkSpell.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

%configure --disable-gtk-doc --disable-static
%make_build
%install
rm -rf $RPM_BUILD_ROOT
%make_install
find $RPM_BUILD_ROOT -name "*.la" -exec rm {} \;
%find_lang %{name}
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n gtkspell-devel -f %{oreon_filedir}/gtkspell-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.16-34
- Prepare for Oreon 11 (RP1)
