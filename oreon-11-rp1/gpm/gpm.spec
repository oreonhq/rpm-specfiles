%global source0_hash fa199e5c7745506df32ebe84d5454385cd6b82cc5036e9247763e41eb4983259
Summary:        A mouse server for the Linux console
Name: gpm
Version: 1.20.7
Release:        1%{?dist}
License: GPL-2.0-or-later AND LicenseRef-OFSFDL
URL: http://www.nico.schottelius.org/software/gpm/
Source0:        https://github.com/telmich/gpm/archive/1.20.7/gpm-1.20.7.tar.gz
Source1:        gpm.service
Patch0: https://github.com/telmich/gpm/compare/1.20.7...e82d1a653ca94aa4ed12441424da6ce780b1e530.diff
Requires(post): info
Requires(preun): info
%define LIBVER 2.1.0
Requires: linuxconsoletools
Requires: %{name}-libs = %{version}-%{release}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  gawk
BuildRequires:  libcap-ng-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl-Text-Unidecode
BuildRequires:  perl-constant
BuildRequires:  perl-interpreter
BuildRequires:  sed
BuildRequires:  systemd-rpm-macros
BuildRequires:  texinfo
# /oreon:deps
%description
Gpm provides mouse support to text-based Linux applications like the
Emacs editor and the Midnight Commander file management system. Gpm
also provides console cut-and-paste operations using the mouse and
includes a program to allow pop-up menus to appear at the click of a
mouse button.

%package libs
Summary: Dynamic library for gpm
%description libs
This package contains the libgpm.so dynamic library which contains
the gpm system calls and library functions.

%package devel
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libs = %{version}-%{release}
Summary: Development files for the gpm library
%description devel
The gpm-devel package includes header files and libraries necessary
for developing programs which use the gpm library. The gpm provides
mouse support to text-based Linux applications.

%package static
Requires: %{name} = %{version}-%{release}
Summary: Static development files for the gpm library
%description static
The gpm-static package includes static libraries of gpm. The gpm provides
mouse support to text-based Linux applications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir gpm-%{version}
%oreon_prep
%build

export CFLAGS="$CFLAGS -std=gnu17 -Wno-unused-result -Wno-sign-compare -Wno-pointer-sign"
./autogen.sh
%configure
%make_build
%install
%make_install
chmod 0755 %{buildroot}/%{_libdir}/libgpm.so.%{LIBVER}
ln -sf libgpm.so.%{LIBVER} %{buildroot}/%{_libdir}/libgpm.so
rm -f %{buildroot}%{_datadir}/emacs/site-lisp/t-mouse.el
%ifnarch s390 s390x
mkdir -p %{buildroot}%{_sysconfdir}/rc.d/init.d
mkdir -p %{buildroot}%{_unitdir}
install -m 644 conf/gpm-* %{buildroot}%{_sysconfdir}
mkdir -p %{buildroot}%{_unitdir}
install -m644 %{SOURCE1} %{buildroot}%{_unitdir}
rm -rf %{buildroot}%{_initrddir}
%else
rm -rf %{buildroot}%{_sbindir}
rm -rf %{buildroot}%{_bindir}
rm -rf %{buildroot}%{_mandir}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%post

%ifnarch s390 s390x
%systemd_post gpm.service
%endif
%preun

%ifnarch s390 s390x
%systemd_preun gpm.service
%endif
%postun

%ifnarch s390 s390x
%systemd_postun_with_restart gpm.service
%endif
%ldconfig_scriptlets libs
%files -f %{oreon_filedir}/main.list
%files -n gpm-libs -f %{oreon_filedir}/gpm-libs.list
%files -n gpm-devel -f %{oreon_filedir}/gpm-devel.list
%files -n gpm-static -f %{oreon_filedir}/gpm-static.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.20.7-1
- Import
