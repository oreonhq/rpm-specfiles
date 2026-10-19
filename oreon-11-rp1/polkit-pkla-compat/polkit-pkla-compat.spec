%global source0_hash 6db3ea16ab03d18c517c4141679b1ecf17752ab8901c2edcaa648b20c98a9707
Name:		polkit-pkla-compat
Version:	0.1
Release:        1%{?dist}
Summary:        Rules for polkit to add compatibility with pklocalauthority
License:	LGPL-2.0-or-later
URL:		https://pagure.io/polkit-pkla-compat
Source0:        https://github.com/openEuler-BaseService/polkit-pkla-compat/archive/fb72cbb49a103b8fa773063962c9dcfb888f49ff.tar.gz#/polkit-pkla-compat-%{version}.tar.xz
Requires(pre): polkit
%global _hardened_build 1
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  docbook-style-xsl
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  glib2-devel
BuildRequires:  libtool
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  polkit-devel
# /oreon:deps
%description
A polkit JavaScript rule and associated helpers that mostly provide
compatibility with the .pkla file format supported in polkit <= 0.105 for users
of later polkit releases.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n polkit-pkla-compat-fb72cbb49a103b8fa773063962c9dcfb888f49ff
autoreconf -fi

%build

%configure
%make_build
%install
%make_install
%oreon_autofiles main

%check

make check
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.1-32
- Prepare for Oreon 11 (RP1)
