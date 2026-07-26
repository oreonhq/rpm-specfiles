%global source0_hash 0a5912f5ef574c22e19cefb820afd2c16f73136d6afd0d5ed350c4cfbf76d6f0

%global revision 20250503
Name:           tack
Version:        1.11
Release:        3.%{revision}%{?dist}
Summary:        Terminfo action checker

License:        GPL-2.0-only
URL:            https://invisible-island.net/ncurses/tack.html
Source0:        https://invisible-mirror.net/archives/ncurses/current/tack-%{version}-%{revision}.tgz

BuildRequires: make
BuildRequires:  gcc ncurses-devel

%description
The tack program has three purposes: to help you build a new terminfo
entry describing an unknown terminal, to test the correctness of an
existing entry, and to develop the correct pad timings needed to ensure
that screen updates don't fall behind the incoming data stream.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}-%{revision}

%build
%configure --with-ncurses
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc AUTHORS CHANGES COPYING HISTORY README
%{_bindir}/tack
%{_mandir}/man1/tack.1*

%changelog
%autochangelog
