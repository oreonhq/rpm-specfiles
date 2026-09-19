%global source0_hash 4c3a2b4abe17e42e739a8384df1a06b32fed215786dc000008a4385e74f92014

Name:		chmlib
Summary:	Library for dealing with ITSS/CHM format files
Version:	0.40
Release:	%autorelease
# ./src/lzx.[ch] licensed under GPL-2.0-or-later, rest is LGPL-2.1-or-later
License:	LGPL-2.1-or-later AND GPL-2.0-or-later
Url:		http://www.jedrea.com/chmlib/
VCS:		git:https://github.com/jedwing/CHMLib.git
Source0:	https://github.com/jedwing/CHMLib/archive/refs/heads/master.tar.gz
# backported from upstream
# backported from upstream
# Submitted upstream https://github.com/jedwing/CHMLib/pull/10
Patch3:		chm_http-port-shortopt.patch
# Submitted upstream https://github.com/jedwing/CHMLib/pull/11
Patch4:		chm_http-bind-localhost.patch
# Submitted upstream https://github.com/jedwing/CHMLib/pull/12
Patch6: chmlib-c99.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	make

%description
CHMLIB is a library for dealing with ITSS/CHM format files. Right now, it is
a very simple library, but sufficient for dealing with all of the .chm files
I've come across. Due to the fairly well-designed indexing built into this
particular file format, even a small library is able to gain reasonably good
performance indexing into ITSS archives.

%package devel
Summary:	Library for dealing with ITSS/CHM format files - development files
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Files needed for developing apps using chmlib.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n CHMLib-master
rm -f libtool
mv configure.in configure.ac
autoreconf -ivf

%build
%configure --enable-examples --disable-static
%make_build

%install
%make_install
rm -f %{buildroot}/%{_libdir}/*.la

%files
%doc README AUTHORS NEWS
%license COPYING
%{_bindir}/chm_http
%{_bindir}/enum_chmLib
%{_bindir}/enumdir_chmLib
%{_bindir}/extract_chmLib
%{_bindir}/test_chmLib
%{_libdir}/libchm.so.*

%files devel
%{_includedir}/*
%{_libdir}/libchm.so

%changelog
%autochangelog
