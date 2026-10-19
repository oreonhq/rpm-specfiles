%global source0_hash 5cbbfef7502c1aa785d71f2bb7247d1ba6c81896291cb6385621f866d25282c3
Name:		sigscheme
Version:	0.9.5
Release:        1%{?dist}
License:	BSD-3-Clause
URL:		https://github.com/uim/sigscheme
Source0:        https://github.com/uim/sigscheme/releases/download/%{version}/%{name}-%{version}.tar.bz2
Summary:        R5RS Scheme interpreter for embedded use
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libgcroots-devel
BuildRequires:  make
# /oreon:deps
%description
sigscheme is a R5RS Scheme interpreter that features small footprint,
low memory consumption, multibytes characters handling and more.

%package devel
Summary:	Development files for sigscheme
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig
%description devel
sigscheme is a R5RS Scheme interpreter that features small footprint,
low memory consumption, multibytes characters handling and more.

This package contains header files and development library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --disable-static --with-libgcroots=installed
make %{?_smp_mflags}
%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="/usr/bin/install -p"
rm $RPM_BUILD_ROOT%{_libdir}/*.la
rm -rf $RPM_BUILD_ROOT%{_docdir}/sigscheme
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make check
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n sigscheme-devel -f %{oreon_filedir}/sigscheme-devel.list

%changelog

%autochangelog
