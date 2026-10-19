%global source0_hash 99708950205d5bfd2e769519fcb6423a9f545175a29c46c7c1cf7965afc4b8eb
Name:		grim
Version:	1.5.0
Release:        1%{?dist}
Summary:        Screenshot tool for Sway
License:	MIT
URL:		https://gitlab.freedesktop.org/emersion/grim
Source0:        https://gitlab.freedesktop.org/emersion/%{name}/-/releases/v%{version}/downloads/%{name}-%{version}.tar.gz
Source1:	%{url}/-/releases/v%{version}/downloads/%{name}-%{version}.tar.gz.sig
Source2:	dj3498u4hyyarh35rkjfnghbjxug6b19
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  meson
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  scdoc
# /oreon:deps
%description
Grim is a command-line tool to grab images from Sway.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build

%meson \
	-Dbash-completions=true \
	-Dfish-completions=true
%meson_build
%install
%meson_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
