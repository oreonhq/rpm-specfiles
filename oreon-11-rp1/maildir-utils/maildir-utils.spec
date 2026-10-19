%global source0_hash edea1a4e6be390a2bf5260e0156813f9b473c2d91da934b219dbb38229b0930a
Name:           maildir-utils
Version:        1.14.3
Release:        1%{?dist}
Summary:        A command-line mail organization utility
License:        GPL-3.0-or-later
URL:            http://www.djcbsoftware.nl/code/mu/index.html
Source0:        https://github.com/djcb/mu/releases/download/v%{version}/mu-%{version}.tar.xz
Patch0:         1.14.3-mu4e-docs-directory.patch
Patch1:         1.14.3-mu-docs-directory.patch
Patch2:         1.14.3-mu-guile-scripts-directory.patch
Patch3:         1.14.3-mu-scm-directory.patch
Requires:       emacs-filesystem >= 26.3
Requires:       xapian-core
# oreon:deps
BuildRequires:  dh-autoreconf
BuildRequires:  emacs
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  guile30-devel
BuildRequires:  libtool
BuildRequires:  libuuid-devel
BuildRequires:  make
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmime-3.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  readline-devel
BuildRequires:  texinfo
BuildRequires:  xapian-core
BuildRequires:  xapian-core-devel
BuildRequires:  xapian-core-libs
# /oreon:deps
%description
Maildir-utils (mu) is a command-line utility for organizing and
searching email.

%package guile
Summary:        Guile bindings for mu (maildir-utils)
BuildRequires:  guile30-devel
Requires:       guile30
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-guile-devel < 1.8.10-1
%description guile
This package contains the Guile bindings for mu
(maildir-utils).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir mu-%{version}
%oreon_prep
%build

%meson \
    -Dguile=enabled \
    -Dcld2=disabled \
    -Dreadline=enabled
%meson_build
%install
%meson_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n maildir-utils-guile -f %{oreon_filedir}/maildir-utils-guile.list

%changelog

%autochangelog
