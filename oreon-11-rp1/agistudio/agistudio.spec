%global source0_hash b08abd4f61031b26e47c047b57641b543914b7241c8f77e57f5d8cbfe09c6258

Name: agistudio
Version: 1.3.0
Release: 36%{?dist}
Summary: AGI integrated development environment
License: GPL-2.0-or-later
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1: %{name}.desktop
Patch0: agistudio-1.3.0-format.patch
URL: http://agistudio.sourceforge.net/

BuildRequires: qt4-devel desktop-file-utils
BuildRequires: make
#Requiring nagi, needed at runtime, not picked up by rpm.
Requires: hicolor-icon-theme, nagi, gtk2

%description
AGI (Adventure Game Interpreter) is the adventure game engine used by
Sierra On-Line to create some of their early games. QT AGI Studio
is a program which allows you to view, create and edit AGI games.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%patch -P0 -p0

%build
CXXFLAGS="$RPM_OPT_FLAGS $CXXFLAGS -std=gnu++98 -fPIC"
export CXXFLAGS
cd src
%{qmake_qt4}
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/agistudio
install -m 755 src/agistudio %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/agistudio/template
mkdir -p %{buildroot}%{_datadir}/agistudio/help
install -p -m 0644 help/* %{buildroot}%{_datadir}/agistudio/help
cp -pr template/* %{buildroot}%{_datadir}/%{name}/template 

# icon
install -d %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -p -m 0644  src/app_icon.xpm %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.xpm

# desktop file
desktop-file-install  \
        --dir $RPM_BUILD_ROOT%{_datadir}/applications \
        %{SOURCE1}

%files
%doc COPYING README relnotes help/*
%{_bindir}/agistudio
%{_datadir}/agistudio/
%{_datadir}/applications/agistudio.desktop
%{_datadir}/icons/hicolor/32x32/apps/agistudio.xpm

%changelog
%autochangelog
