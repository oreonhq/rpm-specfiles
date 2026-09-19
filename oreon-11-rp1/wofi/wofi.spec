%global source0_hash 6216dc14d93cdb6170f89c1ca3aaacdeaa44862fbc9be947d614be266a9c49f6

Name:		wofi
Summary:	A launcher/menu program for wlroots based wayland compositors

Version:	1.5.3
Release:	%autorelease

License:	GPL-3.0-only
URL:		https://hg.sr.ht/~scoopta/wofi
Source0:	%{URL}/archive/v%{version}.tar.gz

BuildRequires:	meson
BuildRequires:	gcc
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gio-unix-2.0)
BuildRequires:	pkgconfig(wayland-client)

%description
Wofi is a launcher/menu program for wlroots based wayland compositors such as
sway.

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Files for development with %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-v%{version}

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING.md
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/wofi.1*
%{_mandir}/man5/wofi.5*
%{_mandir}/man7/wofi-keys.7*
%{_mandir}/man7/wofi.7*

%files devel
%{_includedir}/wofi-1/*.h
%{_libdir}/pkgconfig/wofi.pc
%{_mandir}/man3/wofi-api.3*
%{_mandir}/man3/wofi-config.3*
%{_mandir}/man3/wofi-map.3*
%{_mandir}/man3/wofi-utils.3*
%{_mandir}/man3/wofi-widget-builder.3*
%{_mandir}/man3/wofi.3*

%changelog
%autochangelog
