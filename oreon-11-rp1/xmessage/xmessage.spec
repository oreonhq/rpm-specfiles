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

Obsoletes:      xorg-x11-utils < 7.5-39

%description
The xmessage program displays a window containing a message from the command
line, a file, or standard input. It can also present buttons and return the
label of the selected button.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc README.md
%{_bindir}/xmessage
%{_mandir}/man1/xmessage.1*

%changelog
* Tue Apr 14 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.7-1
- Add xmessage package
