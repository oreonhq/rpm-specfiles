%global source0_hash d028cf9308006589fedbb204e932a389ecbda6388ee604847a1c438af7e10484

Name:           grhino
Version:        0.16.1
Release:        24%{?dist}
Summary:        Reversi game for GNOME, supporting the Go/Game Text Protocol

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://rhino.sourceforge.net/
Source0:        http://downloads.sourceforge.net/rhino/grhino-%{version}.tar.gz
# from https://packages.debian.org/sid/grhino
Patch0:         %{name}-0.16.1-fix-format-security.patch

BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libgnomeui-devel
BuildRequires:  scrollkeeper
BuildRequires: make
#Requires:       
Requires(post):         scrollkeeper
Requires(postun):       scrollkeeper

%description
GRhino, or Rhino its former name, is a Reversi game on Linux and other UNIX-like
systems as long as GNOME 2 libraries are installed. It is currently under
development and a new version is available occasionally.

What distinguish GRhino from most other Reversi games is that GRhino will be
targeted for experienced Reversi players. Strong AI is the main focus with some
additional good, useful features (like an endgame solver) is planned. The
ultimate target strength of the AI is that it should be able to beat the best
human player at the highest difficulty level. Beating Logistello (the strongest
program available) is not in the plan :)

GRhino supports the Go/Game Text Protocol (GTP), allowing it to be used as an
engine for a GTP-compliant controller like Quarry.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1

%build
%configure
%make_build

%install
%make_install

# desktop file
desktop-file-install \
        --dir $RPM_BUILD_ROOT%{_datadir}/applications \
        --remove-key=Version\
        desktop/%{name}.desktop

# Icon
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps

%find_lang %{name}

%post
scrollkeeper-update -q -o %{_datadir}/omf/%{name} || :

%postun
scrollkeeper-update -q || :

%files -f %{name}.lang
%license COPYING
%doc ChangeLog NEWS README TODO
%{_bindir}/grhino
%{_bindir}/gtp-rhino
%{_datadir}/applications/*.desktop
%{_datadir}/gnome/help/grhino/
%{_datadir}/pixmaps/grhino.png
%{_datadir}/grhino-%{version}/
%{_datadir}/omf/grhino/

%changelog
%autochangelog
