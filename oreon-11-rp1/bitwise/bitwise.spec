%global source0_hash 806271fa5bf31de0600315e8720004a8f529954480e991ca84a9868dc1cae97e

Name:           bitwise
Version:        0.50
Release:        %autorelease
Summary:        Terminal based bit manipulator in ncurses

# The entire source code is GPL-3.0-or-later except for
# the shunting-yard code and its test which are BSD 2-Clause
License:        GPL-3.0-or-later AND BSD-2-Clause
URL:            https://github.com/mellowcandle/bitwise
Source0:        %{url}/releases/download/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(cunit)

%description
Bitwise is multi base interactive calculator supporting dynamic base conversion
and bit manipulation. It's a handy tool for low level hackers, kernel
developers and device drivers developers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-v%{version}

%build
%configure
%make_build

%install
%make_install

%check
%make_build check

%files
%license COPYING
%doc README ChangeLog NEWS
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
