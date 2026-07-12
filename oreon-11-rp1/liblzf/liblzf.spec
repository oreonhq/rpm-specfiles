%global source0_hash 9c5de01f7b9ccae40c3f619d26a7abec9986c06c36d260c179cedd04b89fb46a

Name:           liblzf
Version:        3.6
Release:        34%{?dist}
Summary:        Small data compression library

# Automatically converted from old format: BSD or GPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-BSD OR GPL-2.0-or-later
URL:            http://oldhome.schmorp.de/marc/liblzf.html
Source0:        http://dist.schmorp.de/liblzf/liblzf-%{version}.tar.gz
# Adds autoconf and in particular support for building shared libraries.
# 7th Feb 2011 - Mail sent upstream to author. Awaiting conclusion. 
Patch0:         liblzf-%{version}-autoconf-20140314.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires: make

%description
LibLZF is a very small data compression library. It consists 
of only two .c and two .h files and is very easy to 
incorporate into your own programs.  The compression algorithm 
is very, very fast, yet still written in portable C.

%package        devel
Provides:       liblzf-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%if 0%{?el4}%{?el5}
Requires:       pkgconfig
%endif


%description    devel
The liblzf-devel package contains libraries and header files for
developing applications that use liblzf.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
%patch -P0 -p1

%build
sh ./bootstrap.sh
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
# Binary does different things depending
# on the name it is called by.
pushd %{buildroot}%{_bindir}
ln -s lzf unlzf
#Leave lzcat  out since it conflicts with xz-lzma-compat.
#If ever needed would need an alternative setting up,
#if someone ever asks I'll do it.
#ln -s lzf lzcat
popd
rm -f %{buildroot}%{_libdir}/liblzf.la

%ldconfig_scriptlets

%files
%{_bindir}/lzf
%{_bindir}/unlzf
%{_libdir}/liblzf.so.*
# The cs directory contains a .net implementation of lzf.
# Will happily add a .net sub package if given a patch.
%doc README Changes LICENSE cs

%files devel
%{_includedir}/lzf.h
%{_includedir}/lzfP.h
%{_libdir}/liblzf.so
%{_libdir}/pkgconfig/liblzf.pc

%changelog
%autochangelog
