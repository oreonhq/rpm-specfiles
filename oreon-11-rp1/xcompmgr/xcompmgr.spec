%global source0_hash 7824f709c4f22432eaea7542ec93384e5dd48f6fcb85c12ff82d721423b0b98f

Name:          xcompmgr
Version:       1.1.10
Release:       %autorelease
Summary:       X11 composite manager

License:       MIT
URL:           https://gitlab.freedesktop.org/xorg/app/xcompmgr
Source:        https://www.x.org/archive/individual/app/%{name}-%{version}.tar.xz

BuildRequires: gcc
BuildRequires: make
BuildRequires: xorg-x11-util-macros

BuildRequires: libX11-devel
BuildRequires: libXfixes-devel
BuildRequires: libXrender-devel
BuildRequires: libXdamage-devel
BuildRequires: libXcomposite-devel
BuildRequires: libXext-devel

%description
xcompmgr is a sample compositing manager for X servers supporting the XFIXES,
DAMAGE, and COMPOSITE extensions. It enables basic eye-candy effects

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc README.md ChangeLog
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
