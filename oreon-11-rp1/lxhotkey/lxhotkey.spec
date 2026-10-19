%global source0_hash f32686d298d86ae1e97c9e3d27ba1f01b6a0f17dbbbbd67dfbf82e7c0080c592
Name:			lxhotkey
Version:		0.1.2
Release:        4%{?dist}
Summary:        Hotkeys management utility
License:		GPL-2.0-or-later
URL:			https://wiki.lxde.org/en/LXHotkey
Source0:        https://github.com/lxde/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libfm)
# /oreon:deps
%description
LXHotkey is an utility which let you to have an interface 
to manage hotkeys (also known as shortcuts), 
i.e. key combinations which, when pressed, do something 
with your desktop.

%package		devel
Summary:		Development files for %{name}
Requires:		%{name}%{?_isa} = %{version}-%{release}
%description 	devel
The %{name}-devel package contains header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

# Add ACLOCAL_PATH for gettext 0.25 (ref: bug 2366708)
export ACLOCAL_PATH=%{_datadir}/gettext/m4/
bash autogen.sh

%build

%configure \
	--with-gtk=2 \
	--disable-silent-rules \
	%{nil}
%make_build
%install
%make_install
desktop-file-install \
	--delete-original \
	--remove-key=NotShowIn \
	--add-only-show-in=LXDE \
	--set-icon=preferences-desktop-keyboard \
	%{buildroot}%{_datadir}/applications/%{name}-gtk.desktop
%find_lang %{name}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n lxhotkey-devel -f %{oreon_filedir}/lxhotkey-devel.list

%changelog

%autochangelog
