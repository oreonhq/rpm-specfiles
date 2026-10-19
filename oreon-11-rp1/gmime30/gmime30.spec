%global source0_hash 84cd2a481a27970ec39b5c95f72db026722904a2ccf3fdbd57b280cf2d02b5c4
Name:           gmime30
Version:        3.2.15
Release:        4%{?dist}
Summary:        Library for creating and parsing MIME messages
License:        LGPL-2.1-or-later
URL:            https://github.com/jstedfast/gmime
Source0:        https://github.com/jstedfast/gmime/releases/download/%{version}/gmime-%{version}.tar.xz
# oreon:deps
BuildRequires:  gettext
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  make
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gpg-error)
BuildRequires:  pkgconfig(gpgme)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  vala
# /oreon:deps
%description
The GMime suite provides a core library and set of utilities which may be
used for the creation and parsing of messages using the Multipurpose
Internet Mail Extension (MIME).

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir gmime-%{version}
%oreon_prep
%build

%configure --disable-static
%make_build V=1
%install
%make_install
find $RPM_BUILD_ROOT -type f -name "*.la" -delete
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n gmime30-devel -f %{oreon_filedir}/gmime30-devel.list

%changelog

%autochangelog
