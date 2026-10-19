%global source0_hash 9c5de01f7b9ccae40c3f619d26a7abec9986c06c36d260c179cedd04b89fb46a
Name:           liblzf
Version:        3.6
Release:        34%{?dist}
Summary:        Small data compression library
License:        LicenseRef-Callaway-BSD OR GPL-2.0-or-later
URL:            http://oldhome.schmorp.de/marc/liblzf.html
Source0:        http://dist.schmorp.de/liblzf/liblzf-%{version}.tar.gz
Patch0:         liblzf-%{version}-autoconf-20140314.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
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
pushd %{buildroot}%{_bindir}
ln -s lzf unlzf
popd
rm -f %{buildroot}%{_libdir}/liblzf.la
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n liblzf-devel -f %{oreon_filedir}/liblzf-devel.list

%changelog

%autochangelog
