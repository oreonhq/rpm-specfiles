Name:           herbstluftwm
Version:        0.9.5
Release:        1%{?dist}
Summary:        A manual tiling window manager
License:        BSD-2-Clause
URL:            https://herbstluftwm.org
Source0:        https://herbstluftwm.org/tarballs/%{name}-%{version}.tar.gz
Patch0:         0.9.5-cstdint-gcc15.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  asciidoc

%description
herbstluftwm is a manual tiling window manager for X11 using Xlib and Glib.
Tags can be added and removed at runtime, and each tag has its own layout.
It is configured at runtime via ipc calls from herbstclient.

%package        zsh
Summary:        Herbstluftwm zsh completion support
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       zsh

%description    zsh
zsh completion for %{name}.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

for f in "%{buildroot}%{_pkgdocdir}/examples/*.sh"
do
    sed -i -e "s|#!/usr/bin/env bash|#!/usr/bin/bash|" $f
done

for f in "%{buildroot}%{_sysconfdir}/xdg/%{name}/*"
do
    sed -i -e "s|#!/usr/bin/env bash|#!/usr/bin/bash|" $f
done

rm %{buildroot}%{_pkgdocdir}/LICENSE
rm -r %{buildroot}%{_pkgdocdir}/html

%files
%license LICENSE
%doc AUTHORS MIGRATION NEWS
%doc doc/*.{html,txt}
%{_sysconfdir}/xdg/%{name}
%{_bindir}/*
%{_datadir}/bash-completion/completions/herbstclient
%{_datadir}/fish/vendor_completions.d/herbstclient.fish
%{_datadir}/xsessions/%{name}.desktop
%{_mandir}/man1/*
%{_mandir}/man7/*
%{_pkgdocdir}/examples/
%{_pkgdocdir}/hlwm-doc.json

%files zsh
%{_datadir}/zsh/site-functions/_herbstclient

%changelog
* Thu Oct 22 2026 Oreon <oreonproject.org> - 0.9.5-1
- import
