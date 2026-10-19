%global source0_hash 1946b830b6e627d315755b94aa69b93de82952d1fbb25010b6f363fc02a07f0c
%define soversion 0
Name:           sso-mib
Version:        0.10.2
Release:        1%{?dist}
Summary:        Tools and library for Single-Sign-On with CA for Entra via Himmelblau
License:        LGPL-2.1-only AND GPL-2.0-only AND MIT
URL:            https://github.com/siemens/sso-mib
Source0:        https://github.com/siemens/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libjwt)
BuildRequires:  pkgconfig(uuid)
# /oreon:deps
%description
Applications can link with this library to get Entra Conditional Access tokens
for authentication and Single-Sign-On from the Himmelblau stack.

%package libs
Summary:        Shared library for SSO with Entra via Himmelblau
License:        LGPL-2.1-only
%description libs
Applications can link with this library to get Entra Conditional Access tokens
for authentication and Single-Sign-On from the Himmelblau stack.

This package contains the shared library.

%package devel
Summary:        Development files for %{name}-libs
License:        LGPL-2.1-only
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(gio-2.0)
Requires:       pkgconfig(glib-2.0)
Requires:       pkgconfig(uuid)
%description devel
Applications can link with this library to get Entra Conditional Access tokens
for authentication and Single-Sign-On from the Himmelblau stack.

This package contains the development files for the shared library.

%package tool
Summary:        Command line tool for SSO with Entra via Himmelblau
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
License:        GPL-2.0-only
%description tool
This package contains the command line tool to get Entra Conditional Access tokens
for authentication and Single-Sign-On from the Himmelblau stack.

%package gch-smtp-o365
Summary:        Git credential helper for SMTP on O365 via Himmelblau
License:        MIT
Enhances:       git-core
%description -n sso-mib-gch-smtp-o365
This package contains a git send-email credential helper to authenticate SMTP
on O365.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%conf
%meson

%build

%meson_build
%install
%meson_install
install -Dpm0644 debian/sso-mib-tool.bash-completion \
    %{buildroot}%{_datadir}/bash-completion/completions/sso-mib-tool
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n sso-mib-libs -f %{oreon_filedir}/sso-mib-libs.list
%files -n sso-mib-devel -f %{oreon_filedir}/sso-mib-devel.list
%files -n sso-mib-tool -f %{oreon_filedir}/sso-mib-tool.list
%files -n sso-mib-gch-smtp-o365 -f %{oreon_filedir}/sso-mib-gch-smtp-o365.list

%changelog

%autochangelog
