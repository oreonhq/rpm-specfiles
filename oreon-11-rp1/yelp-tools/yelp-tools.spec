%global source0_hash none

%global tarball_version %(echo %{version} | tr '~' '.')

%bcond url_handler 0%{?rhel}

Name:          yelp-tools
Version:       42.1
Release:       %autorelease
Summary:       Create, manage, and publish documentation for Yelp

License:       GPL-2.0-or-later
URL:           https://wiki.gnome.org/Apps/Yelp/Tools
Source0:        https://download.gnome.org/sources/%{name}/42/%{name}-%{tarball_version}.tar.xz
BuildArch:     noarch

# https://gitlab.gnome.org/GNOME/yelp-tools/-/merge_requests/12
Patch:         url-handler.patch

BuildRequires: meson
BuildRequires: pkgconfig(yelp-xsl)
BuildRequires: python3-lxml
BuildRequires: itstool
BuildRequires: libxslt

Requires: /usr/bin/itstool
Requires: /usr/bin/xmllint
Requires: /usr/bin/xsltproc
Requires: mallard-rng
Requires: python3-lxml
Requires: yelp-xsl

%description
yelp-tools is a collection of scripts and build utilities to help create,
manage, and publish documentation for Yelp and the web. Most of the heavy
lifting is done by packages like yelp-xsl and itstool. This package just
wraps things up in a developer-friendly way.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -n %{name}-%{tarball_version}

%build
%meson \
%if %{with url_handler}
  -Durl_handler=enabled \
%endif
  %{nil}
%meson_build

%install
%meson_install

%files
%doc AUTHORS README.md NEWS
%license COPYING COPYING.GPL
%{_bindir}/yelp-build
%if %{with url_handler}
%{_bindir}/yelp-build-url-handler
%endif
%{_bindir}/yelp-check
%{_bindir}/yelp-new
%if %{with url_handler}
%{_datadir}/applications/yelp-build-url-handler.desktop
%endif
%{_datadir}/yelp-tools
%{_datadir}/aclocal/yelp.m4

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 42.1-1
- Prepare for Oreon 11 (RP1)
