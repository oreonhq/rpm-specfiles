%global source0_hash a382ad57734243818e828ba161fc0357b48d8f3a7f8c29cac183492b46b58949

Name:           sxiv
Version:        26
Release:        15%{?dist}
Summary:        Simple (or small or suckless) X Image Viewer
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/muennich/%{name}/
Source0:        https://github.com/muennich/%{name}/archive/v%{version}.tar.gz
BuildRequires:  binutils
BuildRequires:  coreutils
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  giflib-devel
BuildRequires:  imlib2-devel
BuildRequires:  libexif-devel
BuildRequires:  libX11-devel
BuildRequires:  libXft-devel
BuildRequires:  make
BuildRequires:  sed
BuildRequires:  xorg-x11-proto-devel

%description
sxiv is an alternative to feh and qiv. Its only dependency besides xlib
is imlib2. The primary goal for writing sxiv is to create an image viewer,
which only has the most basic features required for fast image viewing (the
ones I want). It works nicely with tiling window managers and its code base
should be kept small and clean to make it easy for you to dig into it and
customize it for your needs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{?__global_ldflags}"
make %{?_smp_mflags}
cd icon && make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{name}.desktop
cd icon && make install DESTDIR=%{buildroot} PREFIX=%{_prefix}

%files
%license LICENSE
%doc README.md
%{_bindir}/sxiv
%{_mandir}/man1/*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*

%changelog
%autochangelog
