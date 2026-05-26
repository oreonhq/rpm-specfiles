Name:           xmessage
Version:        1.0.7
Release:        1%{?dist}
Summary:        Display a message or query in a window

License:        MIT
URL:            https://www.x.org
Source0:        https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz
# oreon url source checksums begin
%global source0_sha256 703fccb7a0b772d61d7e603c189b9739866aa97ba985c727275420f829a30356
%global source0_file xmessage-1.0.7.tar.xz
# oreon url source checksums end

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xt)

Requires:       libXaw%{?_isa}

Obsoletes:      xorg-x11-utils < 7.5-39

%description
The xmessage program displays a window containing a message from the command
line, a file, or standard input. It can also present buttons and return the
label of the selected button.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/xmessage-1.0.7.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "703fccb7a0b772d61d7e603c189b9739866aa97ba985c727275420f829a30356" || { echo "oreon: Source0 SHA256 mismatch for xmessage-1.0.7.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc README
%{_bindir}/xmessage
%{_mandir}/man1/xmessage.1*
%{_datadir}/X11/app-defaults/Xmessage
%{_datadir}/X11/app-defaults/Xmessage-color

%changelog
* Tue Apr 14 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.7-1
- Add xmessage package
