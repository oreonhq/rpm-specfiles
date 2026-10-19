%global source0_hash 7c7b9c6510de633af7ab46e9f85bb8ed916b021d012482e5ca01651be55b79f6
%undefine _annotated_build
Name:		9wm
Summary:        Emulation of the Plan 9 window manager 8 1/2
Version:	1.4.2
Release:        8%{?dist}
License:	MIT
Source0:        https://github.com/9wm/9wm/archive/%{version}.tar.gz
Source1:	9wm.desktop
URL:		https://woozle.org/neale/src/9wm/
Requires:	xterm
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  make
# /oreon:deps
%description
9wm is an X window manager which attempts to emulate the Plan 9 window
manager 8-1/2 as far as possible within the constraints imposed by X.
It provides a simple yet comfortable user interface, without garish
decorations or title-bars. Or icons.  And it's click-to-type.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n 9wm-%{version}

%build

CFLAGS="$RPM_OPT_FLAGS" %make_build
%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man1
make DESTDIR=%{buildroot} BIN=%{buildroot}%{_bindir} MANDIR=%{buildroot}%{_mandir}/man1 install install.man
desktop-file-install					\
--dir=${RPM_BUILD_ROOT}%{_datadir}/xsessions/		\
%{SOURCE1}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
