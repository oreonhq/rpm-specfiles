%global source0_hash 4e8a35950b7b7ce1e49f9457a8aceffbd21fb2b34aa8386847a7a158a2cab551
Name:           nudoku
Version:        8.0.1
Release:        1%{?dist}
Summary:        Ncurses based Sudoku game
License:        GPL-3.0-only
Url:            https://github.com/jubalh/%{name}
Source0:        https://github.com/jubalh/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cairo-devel
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
# /oreon:deps
%description
nudoku is a ncurses based Sudoku game.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -i
export CFLAGS="%{build_cflags} -I%{_datadir}/gettext"
%configure --enable-cairo
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
