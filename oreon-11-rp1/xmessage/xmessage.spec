# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 703fccb7a0b772d61d7e603c189b9739866aa97ba985c727275420f829a30356
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name:           xmessage
Version:        1.0.7
Release:        1%{?dist}
Summary:        Display a message or query in a window

License:        MIT
URL:            https://www.x.org
Source0:        https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz

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
%oreon_verify_sources
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
