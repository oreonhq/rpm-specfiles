%global source0_hash 42f88dfd073c0d903b66258774d7e14ca1887d2ae251dcffeb5ed0b4dd2d3759
Name:         bicon
License:      LGPL-2.0-or-later and Python-2.0.1
Version:      0.5
Release:        1%{?dist}
Summary:        Bidirectional Console
Source0:        https://github.com/behdad/bicon/releases/download/%{version}/%{name}-%{version}.tar.gz
Patch0:       %{name}-HEAD.patch
URL:          https://www.arabeyes.org/Bicon
Requires:      kbd
Requires:      setxkbmap
Requires:      xkbcomp
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fribidi-devel
BuildRequires:  git
BuildRequires:  kbd
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
BiCon is the bidirectional console as presented by Arabeyes.

%package devel
Summary:        Development Libraries for BiCon
Requires:       %{name} = %{version}-%{release}
%description devel
The bicon-devel package contains the libraries and header files
that are needed for writing applications with BiCon.

%package legacyfonts
Summary:        Font Files for BiCon
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description legacyfonts
The bicon-fonts package contains the font files for BiCon.

%package keymaps
Summary:        Keymap Files for BiCon
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description keymaps
The bicon-keymaps package contains the keymap files for BiCon.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

libtoolize
autoreconf --verbose --force --install
%configure \
  --disable-static
make %{?_smp_mflags}
%install
make DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p" install
rm -f $RPM_BUILD_ROOT%{_libdir}/bicon/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/bicon/*.a
%oreon_autofiles bicon-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles bicon-legacyfonts usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles bicon-keymaps usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n bicon-devel -f %{oreon_filedir}/bicon-devel.list
%files -n bicon-legacyfonts -f %{oreon_filedir}/bicon-legacyfonts.list
%files -n bicon-keymaps -f %{oreon_filedir}/bicon-keymaps.list

%changelog

%autochangelog
