%global source0_hash 224e89d364eb3b73f1cf756d05494a98421a93cbf54349a2c85fc607eb755ed7

%global branch 3.22

%global rel_ver 3.22.26

Name:          mate-themes
Version:       %{rel_ver}
Release:       %autorelease
Summary:       MATE Desktop themes
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later
URL:           http://mate-desktop.org
BuildArch:     noarch
Source0:       http://pub.mate-desktop.org/releases/themes/%{branch}/%{name}-%{version}.tar.xz

BuildRequires: make
BuildRequires: mate-common
BuildRequires: gtk2-devel
BuildRequires: gdk-pixbuf2-devel

Requires:      mate-icon-theme
Requires:      gtk2-engines
Requires:      gtk-murrine-engine

%description
MATE Desktop themes

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

#NOCONFIGURE=1 ./autogen.sh

%build
%configure

make %{?_smp_mflags} V=1

%install
%{make_install}

find %{buildroot} -name '*.la' -exec rm -rf {} ';'
find %{buildroot} -name '*.a' -exec rm -rf {} ';'

%files
%doc AUTHORS COPYING README ChangeLog
%{_datadir}/themes/BlackMATE/
%{_datadir}/themes/BlackMATE-border/
%{_datadir}/themes/BlueMenta/
%{_datadir}/themes/BlueMenta-border/
%{_datadir}/themes/Blue-Submarine/
%{_datadir}/themes/Blue-Submarine-border/
%{_datadir}/themes/ContrastHigh/
%{_datadir}/themes/GreenLaguna/
%{_datadir}/themes/GreenLaguna-border/
%{_datadir}/themes/Green-Submarine/
%{_datadir}/themes/Green-Submarine-border/
%{_datadir}/themes/HighContrast/metacity-1/metacity-theme-1.xml
%{_datadir}/themes/HighContrastInverse/
%{_datadir}/themes/Menta/
%{_datadir}/themes/Menta-border/
%{_datadir}/themes/TraditionalOk/
%{_datadir}/themes/TraditionalGreen/
%{_datadir}/themes/Shiny/
%{_datadir}/themes/YaruGreen/
%{_datadir}/themes/YaruOk/
%{_datadir}/icons/ContrastHigh/
%{_datadir}/icons/mate/cursors/
%{_datadir}/icons/mate-black/

%changelog
%autochangelog
