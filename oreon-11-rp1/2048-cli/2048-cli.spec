%global source0_hash acee3d596f05b881d4076803c6ed91a76f0e77aec3c9adb0e80504710a8f9dab
Name:           2048-cli
Version:        0.9.1
Release:        26%{?dist}
Summary:        The game 2048 for your Linux terminal
License:        MIT
URL:            https://github.com/Tiehuis/%{name}
Source0:        https://github.com/Tiehuis/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0000:      %{name}-%{version}-include-string-h.patch
Patch0001:      %{name}-%{version}-fix-Wformat.patch
# oreon:deps
BuildRequires:  SDL2_ttf-devel
BuildRequires:  gcc
BuildRequires:  liberation-mono-fonts
BuildRequires:  make
BuildRequires:  ncurses-devel
# /oreon:deps
%description
A cli version of the game 2048 for your Linux terminal.

%package nocurses
Summary:        The game 2048 for your Linux terminal (non-ncurses)
%description nocurses
A non-ncurses cli version of the game 2048 for your Linux terminal.

%package sdl
Summary:        The game 2048 for your Linux terminal (SDL)
BuildRequires:  SDL2_ttf-devel
BuildRequires:  liberation-mono-fonts
Requires:       liberation-mono-fonts
%description sdl
A SDL version of the game 2048 for your Linux terminal.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

export TTF_FONT_PATH="%{_datadir}/fonts/liberation/LiberationMono-Regular.ttf"
%make_build terminal
mv 2048 2048nc
%make_build sdl
mv 2048 2048sdl
%make_build curses
%install
mkdir -p %{buildroot}{%{_bindir},%{_mandir}/man1,%{_pkgdocdir}}
install -pm 0755 2048 2048nc 2048sdl %{buildroot}%{_bindir}
install -pm 0644 man/2048.1 %{buildroot}%{_mandir}/man1/2048.1
install -pm 0644 man/2048.1 %{buildroot}%{_mandir}/man1/2048nc.1
install -pm 0644 man/2048.1 %{buildroot}%{_mandir}/man1/2048sdl.1
%oreon_autofiles 2048-cli-nocurses usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles 2048-cli-sdl usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n 2048-cli-nocurses -f %{oreon_filedir}/2048-cli-nocurses.list
%files -n 2048-cli-sdl -f %{oreon_filedir}/2048-cli-sdl.list

%changelog

%autochangelog
