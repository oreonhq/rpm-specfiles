%global source0_hash 8218d82f034269ec11eeca96464fb4202027286175b93cf3f1847b650377efd9
%global commit 287e4bee6fd430ffb52604049de80a27a77ff6b4
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:		libs3
Version:	4.1
Release:        1%{?dist}
Summary:        C Library and Tools for Amazon S3 Access
License:	LGPL-3.0-or-later OR GPL-2.0-or-later
URL:		https://github.com/bji/libs3
Source0:        https://github.com/bji/%{name}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
Patch0:		libs3-openssl3.patch
Patch1:		libs3-long-opts.patch
# oreon:deps
BuildRequires:  curl-devel
BuildRequires:  gcc
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  openssl-devel
# /oreon:deps
%description
This package includes the libs3 shared object library, needed to run
applications compiled against libs3, and additionally contains the s3
utility for accessing Amazon S3.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{commit}
%patch -P0 -p1
%patch -P1 -p1

%build

sed -e 's!^CFLAGS +=!& %{build_cflags}!' \
    -e 's!^LDFLAGS =!& %{build_ldflags}!' \
    -e 's!$(INSTALL) -Dps!$(INSTALL) -Dp!' \
    -i GNUmakefile
%make_build exported
%install
%make_install DESTDIR=%{buildroot}%{_prefix} LIBDIR=%{buildroot}%{_libdir}
rm %{buildroot}%{_libdir}/libs3.a
chmod 755 %{buildroot}%{_libdir}/libs3.so.4.1
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%make_build test
%files -f %{oreon_filedir}/main.list
%files -n libs3-devel -f %{oreon_filedir}/libs3-devel.list

%changelog

%autochangelog
