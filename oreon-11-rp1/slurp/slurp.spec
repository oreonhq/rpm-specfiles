%global source0_hash eeb282b2adc8db5614b852596340b69da6f3954cf6cfbdc4392da509c934208a

Name:		slurp
Version:	1.5.0
Release:	6%{?dist}
Summary:	Select a region in Sway

License:	MIT
URL:		https://github.com/emersion/slurp
Source0:	%{url}/releases/download/v%{version}/slurp-%{version}.tar.gz
Source1:	%{url}/releases/download/v%{version}/slurp-%{version}.tar.gz.sig
Source2:	https://emersion.fr/.well-known/openpgpkey/hu/dj3498u4hyyarh35rkjfnghbjxug6b19

BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(wayland-cursor)
BuildRequires:	pkgconfig(wayland-protocols) >= 1.32
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	scdoc
BuildRequires:	meson
BuildRequires:	gcc
BuildRequires:	gnupg2

%description
Slurp is a command-line tool that allows the user to visually select a region
and prints it to the standard output.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%{_bindir}/slurp
%{_mandir}/man1/slurp.1*

%changelog
%autochangelog
