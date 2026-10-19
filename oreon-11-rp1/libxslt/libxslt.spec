%global source0_hash 9acfe68419c4d06a45c550321b3212762d92f41465062ca4ea19e632ee5d216e
Name:           libxslt
Summary:        Library providing the Gnome XSLT engine
Version:        1.1.45
Release:        1%{?dist}
License:        MIT
URL:            https://gitlab.gnome.org/GNOME/libxslt
Source0:        https://download.gnome.org/sources/%{name}/1.1/%{name}-%{version}.tar.xz
Provides: xsltproc = %{version}-%{release}
Patch0:         multilib.patch
Patch1:         multilib2.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  python3-devel
# /oreon:deps
%description
This C library allows to transform XML files into other XML files
(or HTML, text, ...) using the standard XSLT stylesheet transformation
mechanism. To use it you need to have a version of libxml2 >= 2.6.27
installed. The xsltproc command is a command line interface to the XSLT engine

%package devel
Summary:        Development libraries and header files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libgpg-error-devel%{?_isa}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
chmod 644 python/tests/*

%build

autoreconf -vfi
%configure \
  --disable-static \
  --disable-silent-rules \
  --with-plugins \
  --with-python=no \
  --with-crypto=no
%make_build
%install
%make_install
find %{buildroot} -name '*.la' -print -delete
touch -m --reference=%{buildroot}%{_includedir}/libxslt/xslt.h %{buildroot}%{_bindir}/xslt-config
rm -vrf %{buildroot}%{_docdir}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%make_build tests
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n libxslt-devel -f %{oreon_filedir}/libxslt-devel.list

%changelog

%autochangelog
