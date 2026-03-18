Name:       xkbcomp
Version:    1.5.0
Release:    2%{?dist}
Summary:    XKB keymap compiler

License:    MIT-open-group AND HPND-DEC
URL:        https://www.x.org

Source0:    https://www.x.org/pub/individual/app/xkbcomp-%{version}.tar.xz

BuildRequires: make gcc
BuildRequires: libxkbfile-devel
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xorg-macros) >= 1.8

Obsoletes:  xorg-x11-xkb-utils < 7.8

%description
X.Org XKB keymap compiler

%package devel
Summary:    XKB keymap compiler development package
Requires:   pkgconfig
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
X.Org XKB keymap compiler development files

%prep
%autosetup

%build
%configure --disable-silent-rules
%make_build

%install
%make_install

%files
%license COPYING
%{_bindir}/xkbcomp
%{_mandir}/man1/xkbcomp.1*

%files devel
%{_libdir}/pkgconfig/xkbcomp.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5.0-2
- Prepare for Oreon 11 (RP1)
