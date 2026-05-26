# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 494abfce781418259b1e9d8888c73af4de4b6f3be36cc75d9baa8baa0f2a7a39
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name:           mm-common
Version:        1.0.7
Release:        %autorelease
Summary:        Common build files of the C++ bindings

BuildArch:      noarch
License:        GPL-2.0-or-later
URL:            https://gtkmm.org
Source0:        https://download.gnome.org/sources/%{name}/1.0/%{name}-%{version}.tar.xz

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
%oreon_verify_sources
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
