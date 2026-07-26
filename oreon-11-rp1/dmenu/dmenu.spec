%global source0_hash 8fbace2a0847aa80fe861066b118252dcc7b4ca0a0a8f3a93af02da8fb6cd453

Name:           dmenu
Version:        5.4
Release:        %autorelease
Summary:        Generic menu for X
License:        MIT
URL:            http://tools.suckless.org/%{name}
Source0:        http://dl.suckless.org/tools/%{name}-%{version}.tar.gz
BuildRequires:  binutils
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  fontconfig-devel
BuildRequires:  libX11-devel
BuildRequires:  libXft-devel
BuildRequires:  libXinerama-devel
BuildRequires:  make
BuildRequires:  sed

%description
Dynamic menu is a generic menu for X, originally designed for dwm. It manages
huge amounts (up to 10.000 and more) of user defined menu items efficiently.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%make_build \
  X11INC=%{_includedir} \
  X11LIB=%{_libdir} \
  CFLAGS='-std=c99 -pedantic -Wall $(INCS) $(CPPFLAGS) %{build_cflags}' \
  LDFLAGS='%{build_ldflags} $(LIBS)'

%install
%make_install PREFIX=%{_prefix}

%files
%doc LICENSE README
%{_bindir}/%{name}*
%{_bindir}/stest
%{_mandir}/man*/%{name}.*
%{_mandir}/man*/stest.*

%changelog
%autochangelog
