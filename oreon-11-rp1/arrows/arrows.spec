%global source0_hash a8d18e1798d23c26e4d0330db745356d01cc4a3231b669643e08e426eb842d3f

Name:           arrows
Version:        0.6
Release:        42%{?dist}
Summary:        Neat little maze game
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://noreason.ca/?file=software
Source0:        http://noreason.ca/data/arrows-%{version}.tar.gz
Source1:        arrows.desktop
Source2:        arrows.png
Patch0:         arrows-level-5.patch 
BuildRequires:  gcc
BuildRequires:  gtk2-devel desktop-file-utils
BuildRequires: make
Requires:       hicolor-icon-theme

%description
It's a maze game of sorts. Guide the spinning blue thing through
the maze of arrows, creating and destroying arrows as necessary
to collect the green things.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
make clean

%build
make %{?_smp_mflags} CCOPTS="$RPM_OPT_FLAGS"

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 755 %{name} $RPM_BUILD_ROOT%{_bindir}
install -m 644 arrfl.? $RPM_BUILD_ROOT%{_datadir}/%{name}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/24x24/apps
install -p -m 644 %{SOURCE2}\
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/24x24/apps

%files
%doc LICENSE README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/24x24/apps/%{name}.png

%changelog
%autochangelog
