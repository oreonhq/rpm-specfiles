%global source0_hash 4fca58719b88daaac5f7a7d61e86e58ee5058c6475e33e25cf285b811aaa14bd

%global commit 2a54078cbe3814105ee4f565f451b1b5947fbde0

Name:       light
Version:    1.2.2
Release:    17%{?dist}
Summary:    Control backlight controllers

License:    GPL-3.0-only
URL:        https://gitlab.com/dpeukert/light
Source0:    %{URL}/-/archive/%{commit}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires: help2man
BuildRequires: automake
BuildRequires: make

%description
Light is a program to control backlight controllers under GNU/Linux,
it is the successor of lightscript, which was a bash script
with the same purpose, and tries to maintain the same functionality.

Features

- Works excellent where other software have been proven unusable
  or problematic, thanks to how it operates internally
  and the fact that it does not rely on X.
- Can automatically figure out the best controller to use,
  making full use of underlying hardware.
- Possibility to set a minimum brightness value, as some controllers
  set the screen to be pitch black at a value of 0 (or higher).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{commit}

%build
%global build_cflags %{optflags} -fcommon
./autogen.sh
%configure
%make_build

%install
%make_install

%post
# Make sure that all saved files have correct permissions
# after fixing RHBZ 1792875
if [ -e "%{_sysconfdir}/%{name}" ]; then
    chown -R :root %{_sysconfdir}/%{name}
fi

%files
%doc COPYING
%doc ChangeLog.md
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
