# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 8fc7dc560167b2cb7193e76aca625a152dc19b0ebf49816b78539cbb90d80d02
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

### Abstract ###

Name: gtkspell
Version: 2.0.16
Release: 34%{?dist}
License: GPL-2.0-or-later
Summary: On-the-fly spell checking for GtkTextView widgets
URL: http://gtkspell.sourceforge.net/
Source: http://gtkspell.sourceforge.net/download/%{name}-%{version}.tar.gz

### Build Dependencies ###

BuildRequires: gcc
BuildRequires: make
BuildRequires: enchant-devel
BuildRequires: gtk2-devel
BuildRequires: gettext
BuildRequires: intltool

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
%oreon_verify_sources
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

%files -f %{name}.lang
%doc README AUTHORS COPYING
%{_libdir}/libgtkspell.so.0*

%files devel
%{_datadir}/gtk-doc/html/gtkspell
%{_includedir}/gtkspell-2.0
%{_libdir}/libgtkspell.so
%{_libdir}/pkgconfig/gtkspell-2.0.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.16-34
- Prepare for Oreon 11 (RP1)
