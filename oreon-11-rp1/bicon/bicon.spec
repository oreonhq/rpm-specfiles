%global source0_hash 42f88dfd073c0d903b66258774d7e14ca1887d2ae251dcffeb5ed0b4dd2d3759

Name:         bicon
License:      LGPL-2.0-or-later and Python-2.0.1
Version:      0.5
Release:      %autorelease
Summary:      Bidirectional Console
Source:       https://github.com/behdad/bicon/releases/download/%{version}/%{name}-%{version}.tar.gz
Patch0:       %{name}-HEAD.patch
URL:          https://www.arabeyes.org/Bicon

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: fribidi-devel
BuildRequires: git
BuildRequires: kbd
BuildRequires: libtool
BuildRequires: make
Requires:      kbd
Requires:      setxkbmap
Requires:      xkbcomp

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

%autosetup -S git

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

%files
%doc AUTHORS COPYING README
%{_bindir}/*
%{_libdir}/bicon/*.so.*
%dir %{_datadir}/%{name}
%{_datadir}/man/man1/*.gz

%files devel
%{_includedir}/*
%{_libdir}/bicon/*.so
%{_libdir}/pkgconfig/*.pc

%files legacyfonts
%{_datadir}/%{name}/font

%files keymaps
%{_datadir}/%{name}/keymap

%changelog
%autochangelog
