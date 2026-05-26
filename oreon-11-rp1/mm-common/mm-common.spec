Name:           mm-common
Version:        1.0.7
Release:        %autorelease
Summary:        Common build files of the C++ bindings

BuildArch:      noarch
License:        GPL-2.0-or-later
URL:            https://gtkmm.org
Source0:        https://download.gnome.org/sources/%{name}/1.0/%{name}-%{version}.tar.xz
# oreon url source checksums begin
%global source0_sha256 494abfce781418259b1e9d8888c73af4de4b6f3be36cc75d9baa8baa0f2a7a39
%global source0_file mm-common-1.0.7.tar.xz
# oreon url source checksums end

BuildRequires:  meson

Requires:       doxygen
Requires:       graphviz
Requires:       libxslt
Requires:       pkgconfig

%description
The mm-common module provides the build infrastructure and utilities
shared among the GNOME C++ binding libraries.  It is a required dependency
to build glibmm and gtkmm from git.

%package docs
Summary:        Documentation for %{name}, includes example mm module skeleton
Requires:       %{name} = %{version}-%{release}

%description docs
Package contains short documentation for %{name} and example skeleton module,
which could be used as a base for new mm module.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/mm-common-1.0.7.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "494abfce781418259b1e9d8888c73af4de4b6f3be36cc75d9baa8baa0f2a7a39" || { echo "oreon: Source0 SHA256 mismatch for mm-common-1.0.7.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%doc NEWS OVERVIEW.md README.md
%{_mandir}/man1/*
%{_bindir}/*
%{_datadir}/aclocal/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/pkgconfig/*.pc

%files docs
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.7-1
- Prepare for Oreon 11 (RP1)
