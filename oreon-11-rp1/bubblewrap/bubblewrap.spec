%global source0_hash 4734237473c0e5d695e4e9034a34e43b2dbf5164655bd13fa59ae376b2b7a765
Name:    bubblewrap
Version: 0.13.0
Release:        1%{?dist}
Summary:        Core execution tool for unprivileged containers
License: LGPL-2.0-or-later
URL:     https://github.com/containers/bubblewrap/
Source0:        https://github.com/containers/bubblewrap/releases/download/v%{version}/bubblewrap-%{version}.tar.xz
# oreon:deps
BuildRequires:  /usr/bin/xsltproc
BuildRequires:  docbook-style-xsl
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libselinux)
# /oreon:deps
%description
Bubblewrap (/usr/bin/bwrap) is a core execution engine for unprivileged
containers that works as a setuid binary on kernels without
user namespaces.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson -Dman=enabled -Dselinux=enabled
%meson_build
%install
%meson_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
