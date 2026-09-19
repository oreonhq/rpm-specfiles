%global source0_hash 54c8d0982f979750825a81b2453ade33d4d573eadcc4582d48d7265c6c20cb0a

Name:           tunneler
Version:        1.1.1
Release:        40%{?dist}
Summary:        Clone of legendary Tunneler game

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://users.jyu.fi/~tvkalvas/code/tunneler/
Source0:        http://users.jyu.fi/~tvkalvas/code/tunneler/%{name}-%{version}.tar.gz
Source1:        tunneler.svg
Source2:        tunneler.desktop
Patch0:         tunneler-1.1.1-lm.patch
Patch1:         tunneler-1.1.1-inline.patch
Patch2:         tunneler-1.1.1-fix-fortify-source.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  desktop-file-utils
BuildRequires:  SDL-devel
BuildRequires:  autoconf automake

%description
A clone of legendary game made by Geoffrey Silverton in 1991. In the game
two players using the same keyboard and the same screen each control an
underground tank. Goal is to find and destroy the opponent's tank. Since
only small part of the map is displayed on the split screen, you might
actually have some searching to do.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
autoreconf -i
%configure
%make_build

%install
%make_install
install -d %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
install -m 644 -p %{SOURCE1} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
desktop-file-install %{SOURCE2} \
%if (0%{?fedora} && 0%{?fedora} < 19) || (0%{?rhel} && 0%{?rheld} < 7)
        --vendor=fedora \
%endif
        --dir=${RPM_BUILD_ROOT}%{_datadir}/applications

%files
%{_bindir}/tunneler
%{_datadir}/icons/hicolor/scalable/apps/tunneler.svg
%{_datadir}/applications/*.desktop
%doc INSTALL README
%license COPYING

%changelog
%autochangelog
