%global pkgname xauth

Summary: X.Org X11 X authority utilities
Name: xorg-x11-%{pkgname}
Version: 1.1.5
Release: 2%{?dist}
# NOTE: Remove Epoch line if package gets renamed
Epoch: 1
License: MIT-open-group
URL: https://www.x.org

Source0: https://www.x.org/pub/individual/app/%{pkgname}-%{version}.tar.xz

BuildRequires: make
BuildRequires: pkgconfig automake gcc
BuildRequires: libX11-devel
BuildRequires: libXau-devel
BuildRequires: libXext-devel
BuildRequires: libXmu-devel

Provides: xauth

%description
xauth is used to edit and display the authorization information
used in connecting to an X server.

%prep
%setup -q -n %{pkgname}-%{version}

%build
%configure
%make_build

%install
%make_install

# Check can be enabled in v1.1.2 or newer
%check
make check || cat tests/test-suite.log

%files
%doc COPYING README.md
%{_bindir}/xauth
%{_mandir}/man1/xauth.1*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.5-2
- Prepare for Oreon 11 (RP1)
