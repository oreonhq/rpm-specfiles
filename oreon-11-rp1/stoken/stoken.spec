%global source0_hash 102e2d112b275efcdc20ef438670e4f24f08870b9072a81fda316efcc38aef9c
Name:           stoken
Version:        0.93
Release:        1%{?dist}
Summary:        Token code generator compatible with RSA SecurID 128-bit (AES) token
License:        LGPL-2.1-or-later
URL:            https://github.com/stoken-dev/stoken
Source0:        https://github.com/%{name}-dev/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(hogweed)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(nettle)
# /oreon:deps
%description
Software Token for Linux/UNIX. It's a token code generator compatible with RSA
SecurID 128-bit (AES) tokens. It is a hobbyist project, not affiliated with or
endorsed by RSA Security.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{_isa} = %{version}-%{release}
%description devel
Software Token for Linux/UNIX. It's a token code generator compatible with RSA
SecurID 128-bit (AES) tokens. It is a hobbyist project, not affiliated with or
endorsed by RSA Security.

This package provides the development files for %{name}.

%package libs
Summary:        Libraries for %{name}
%description libs
Software Token for Linux/UNIX. It's a token code generator compatible with RSA
SecurID 128-bit (AES) tokens. It is a hobbyist project, not affiliated with or
endorsed by RSA Security.

This package contains %{name} libraries.

%package cli
Summary:        Command line tool for %{name}
%description cli
Software Token for Linux/UNIX. It's a token code generator compatible with RSA
SecurID 128-bit (AES) tokens. It is a hobbyist project, not affiliated with or
endorsed by RSA Security.

This package contains the command line tool for %{name}.

%package gui
Summary:        Graphical interface program for %{name}
%description gui
Software Token for Linux/UNIX. It's a token code generator compatible with RSA
SecurID 128-bit (AES) tokens. It is a hobbyist project, not affiliated with or
endorsed by RSA Security.

This package contains the graphical interface program for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -v -f --install
%configure --with-gtk --disable-static
%make_build
%install
%make_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-gui.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-gui-small.desktop
make check
find %{buildroot} -type f -name "*.la" -delete
rm -fr %{buildroot}%{_docdir}/%{name}
%files -f %{oreon_filedir}/main.list
%files -n stoken-devel -f %{oreon_filedir}/stoken-devel.list
%files -n stoken-libs -f %{oreon_filedir}/stoken-libs.list
%files -n stoken-cli -f %{oreon_filedir}/stoken-cli.list
%files -n stoken-gui -f %{oreon_filedir}/stoken-gui.list

%changelog

%autochangelog
