%global source0_hash 0afaf531cc34a7f8c324479fa6a9d1cf33a3deceb3deb89c3749e61a2d4a7583

Name:           sawfish-pager
Version:        0.90.4
Release:        29%{?dist}
Summary:        Pager for Sawfish window manager
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://sawfish.wikia.com/
Source0:        http://download.tuxfamily.org/sawfishpager/%{name}_%{version}.tar.bz2
Patch0: sawfish-pager-deprecated.patch
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  gmp-devel
BuildRequires:  gtk2-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  sawfish-devel >= 1.8.1
Requires:       sawfish >= 1.8.1

%description
Sawfish specific configurable pager map of your desktop with a
viewport support. It can be configured to follow where you are, or
optionally show all workspaces at once.

Check README from this package documentation how to activate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}_%{version}

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%license COPYING
%doc NEWS README TODO
%{_libdir}/sawfish/sawfishpager
%{_datadir}/sawfish/lisp/sawfish/wm/ext/*

%changelog
%autochangelog
