%global source0_hash d8a5222828c3adab70adf69a5583f1d32eb5ece04304f7f8392b6a353aa2228c
Summary:        X Display Manager Control Protocol library
Name: libXdmcp
Version: 1.1.5
Release:        5%{?dist}
License: MIT-open-group
URL: http://www.x.org
Source0:        https://www.x.org/pub/individual/lib/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  xmlto
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  xorg-x11-util-macros
# /oreon:deps
%description
X Display Manager Control Protocol library.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}
%description devel
libXdmcp development package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -v --install --force
%configure --disable-static
make V=1 %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -rf $RPM_BUILD_ROOT%{_docdir}
%ldconfig_post
%ldconfig_postun
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libXdmcp-devel -f %{oreon_filedir}/libXdmcp-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.5-5
- Prepare for Oreon 11 (RP1)
