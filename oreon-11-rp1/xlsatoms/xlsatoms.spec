%global source0_hash f4bfa15f56c066d326a5d5b292646708f25b9247506840b9047cd2687dcc71b7

Summary:    X11 atom list utility
Name:       xlsatoms
Version:    1.1.4
Release:    8%{?dist}
License:    MIT
URL:        http://www.x.org

Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz

BuildRequires:  make
BuildRequires:  gettext-devel
BuildRequires:  libtool

BuildRequires:  pkgconfig(x11)

Obsoletes: xorg-x11-utils < 7.5-39

%description
xlsatoms prints the atom database from an X server.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure
%make_build

%install
%make_install

%files
%{_bindir}/xlsatoms
%{_mandir}/man1/xlsatoms.1*

%changelog
%autochangelog
