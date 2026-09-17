%global source0_hash 98a80a58a15ea664dfa62e1e5ae51c737f9555ef114e483f3b3c2674d9c51495

Name:           nudoku
Version:        6.0.0
Release:        %autorelease
Summary:        Ncurses based Sudoku game
License:        GPL-3.0-only
Url:            https://github.com/jubalh/%{name}
Source0:        https://github.com/jubalh/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cairo-devel
BuildRequires:  gettext-devel
BuildRequires:  ncurses-devel

%description
nudoku is a ncurses based Sudoku game.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
autoreconf -i
export CFLAGS="%{build_cflags} -I%{_datadir}/gettext"
%configure --enable-cairo
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
%find_lang %{name}

%files -f %{name}.lang
%license LICENSE
%doc README.md
%{_bindir}/nudoku
%{_mandir}/man6/nudoku.6.*

%changelog
%autochangelog
