%global source0_hash e753d6a92d17105ad0d374f0349579b7e7bb070d4bebf5ec28ea105cb0c5b507
Name:           xbanish
Version:        1.8
Release:        1%{?dist}
Summary:        Banish the mouse cursor when typing, show it again when the mouse moves
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/jcs/xbanish
Source0:        https://github.com/jcs/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libX11-devel
BuildRequires:  libXfixes-devel
BuildRequires:  libXi-devel
BuildRequires:  libXt-devel
BuildRequires:  make
# /oreon:deps
%description
xbanish hides the mouse cursor when you start typing, and shows it again when
the mouse cursor moves or a mouse button is pressed. This is similar to xterm's
pointerMode setting, but xbanish works globally in the X11 session.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%set_build_flags
%make_build
%install
export PREFIX='%{_prefix}'
export MANDIR='%{_mandir}/man1'
export INSTALL_PROGRAM='install -p'
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
