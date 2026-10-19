%global source0_hash e0a29b2f5e178362f71950c45ec49b43ccc75cacf44356948377e71cdfee119b
Summary:        X11 utility to view and edit application resources
Name:          editres
Version:       1.1.1
Release:        1%{?dist}
License:       MIT
URL:           https://www.x.org
Source0:        https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz
Patch01:       editres-1.0.6-format-security.patch
Obsoletes:     xorg-x11-resutils < 7.7-9
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libxkbfile-devel
BuildRequires:  make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xt)
# /oreon:deps
%description
editres is a tool that allows users and application developers to view
the full widget hierarchy of any Xt Toolkit application that speaks the
Editres protocol  In addition, editres will help the user construct
resource specifications, allow the user to apply the resource to
the application and view the results dynamically.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --disable-silent-rules --disable-xprint
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
