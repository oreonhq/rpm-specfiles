%global source0_hash 42b7c2cee268f71d7e1c1ad4f69bcda0ecd65578a96722187c6b76378d26ba0a
Name:           mate-common
Summary:        mate common build files
Version:        1.28.0
Release:        1%{?dist}
License:        GPL-3.0-or-later
URL:            http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.28/mate-common-%{version}.tar.xz
BuildArch:      noarch
Requires:       automake
Requires:       autoconf
Requires:       autoconf-archive 
Requires:       gettext
Requires:       intltool
Requires:       libtool
Requires:       glib2-devel
Requires:       gtk-doc
Requires:       itstool
Requires:       yelp-tools
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make
# /oreon:deps
%description
binaries for building all MATE desktop sub components

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure
make %{?_smp_mflags} V=1
%install
%{make_install}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
