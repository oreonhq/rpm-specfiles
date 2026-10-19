%global source1_hash 242a6bf0dd360db9754034ba7c888ed5d59c14ad37aa140a7bac12b8c6683c55
%global source0_hash 80692ec350271995e147dc759929cdd79d3b645e6b5efaa6b57f4d2d05e847e5
Name:		spread-sheet-widget
Version:	0.10
Release:        1%{?dist}
Summary:        A library for Gtk+ which provides a spread sheet widget
License:	GPL-3.0-or-later
URL:		https://www.gnu.org/software/ssw/
Source0:        https://alpha.gnu.org/gnu/ssw/%{name}-%{version}.tar.gz
Source1:	https://alpha.gnu.org/gnu/ssw/%{name}-%{version}.tar.gz.sig
Source2:	BAF59BDF98664CEEF14D2A5A6A233DCD47A92289.gpg
Patch1:		spread-sheet-widget-0001-No-need-to-specify-gtk3-lib-in-pc-file.patch
Patch2:		spread-sheet-widget-0002-Use-more-standard-macros-in-pc-file.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  texinfo
# /oreon:deps
%description
GNU Spread Sheet Widget is a library for Gtk+ which provides a widget for
viewing and manipulating 2 dimensional tabular data in a manner similar to many
popular spread sheet programs.

The design follows the model-view-controller paradigm and is of complexity O(1)
in both time and space. This means that it is efficient and fast even for very
large data.

Features commonly found in graphical user interfaces such as cut and paste,
drag and drop and row/column labelling are also included.

%package devel
Summary: The development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Additional header files for development with %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1
autoreconf -ivf

%build

%configure --disable-static
%make_build
%install
%make_install
find %{buildroot} -type f -name "*.la" -delete
rm -f %{buildroot}%{_infodir}/dir
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make check
%files -f %{oreon_filedir}/main.list
%files -n spread-sheet-widget-devel -f %{oreon_filedir}/spread-sheet-widget-devel.list

%changelog

%autochangelog
