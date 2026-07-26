%global source0_hash bc6e94d91e989891c9a8dd6178089aadbb9bc652f519f740fcfa74a50c2085ba

# http://fedoraproject.org/wiki/Packaging/Debuginfo#Useless_or_incomplete_debuginfo_packages_due_to_other_reasons
%global debug_package %{nil}

Name:       gbrainy
Version:    2.4.6
Epoch:      1
Release:    %autorelease
Summary:    A brain teaser game and trainer to keep your brain trained

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:    GPL-2.0-only
URL:        https://wiki.gnome.org/Apps/gbrainy
Source0:    https://gent.softcatala.org/jmas/%{name}/%{name}-%{version}.tar.gz
# To fix 460353 :
Patch0:     %{name}-fix-location.patch
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gtk-sharp3-devel
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  librsvg2-devel
BuildRequires:  mono-devel
BuildRequires:  yelp-tools
BuildRequires:  make

# Mono only available on these:
ExclusiveArch: %mono_arches

%description
gbrainy is a brain teaser game and trainer to have
fun and to keep your brain trained.

It provides the following types of games:

* Logic puzzles. Games designed to challenge your
    reasoning and thinking skills.
* Mental calculation. Games based on arithmetical
    operations designed to prove your mental calculation skills.
* Memory trainers. Games designed to challenge your short term memory.

%package devel
Summary:      Files needed for developing with gbrainy
Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description devel
This package provides the necessary development libraries and headers
for writing gbrainy applications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0

# use mcs instead of gmcs to compile, as recommended in below link
# http://www.mono-project.com/docs/about-mono/languages/csharp/
sed -i "s#gmcs#mcs#g" configure
sed -i "s#gmcs#mcs#g" configure.ac
autoconf

%build

%configure
%make_build

%install
%make_install
desktop-file-install                                \
    --delete-original                               \
    --dir $RPM_BUILD_ROOT%{_datadir}/applications   \
    $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

# To fix a rpmlint issue
chmod a-x $RPM_BUILD_ROOT%{_libdir}/%{name}/%{name}.exe.config

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS NEWS README MAINTAINERS
%license COPYING
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/help/*
%{_datadir}/icons/hicolor/*/apps/%{name}*
%{_mandir}/man6/%{name}.6.gz
%{_datadir}/pixmaps/%{name}*
%{_datadir}/metainfo/%{name}.appdata.xml

%files devel

%changelog
%autochangelog
