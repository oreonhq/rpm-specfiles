%global source0_hash 0af83855214bf90b4c0d149221884ab4458f3857c38972d428daebf3badd6e32
Name:		unixcw
Version:	3.6.1
Release:        7%{?dist}
Summary:        Shared library for Morse programs
License:	GPL-2.0-or-later
URL:		http://unixcw.sourceforge.net
Source0:        http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  qt4-devel
# /oreon:deps
%description
unixcw is a project providing libcw library and a set of programs using the
library: cw, cwgen, cwcp and xcwcp. The programs are intended for people who
want to learn receiving and sending Morse code. unixcw is developed and tested
on GNU/Linux system.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	pkgconfig
%description	devel
UnixCW utility libraries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}
%install
%make_install
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.a
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n unixcw-devel -f %{oreon_filedir}/unixcw-devel.list

%changelog

%autochangelog
