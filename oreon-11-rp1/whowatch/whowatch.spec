%global source0_hash 9bdf0338850fd66036cb4db1f7a61b35f502158c315981f7176d8f834a0b5a02

Summary: Display information about users currently logged on 
Name: whowatch
Version: 1.8.6
Release: 22%{?dist}
License: GPL-2.0-only
URL: http://wizard.ae.krakow.pl/~mike/

Source0: https://github.com/mtsuszycki/whowatch/archive/whowatch-%{version}.tar.gz
Patch0: whowatch-configure-c99.patch

# Submitted upstream: https://github.com/mtsuszycki/whowatch/pull/13
Patch1: whowatch-gcc15-fixes.patch

BuildRequires: make
BuildRequires: gcc
BuildRequires: ncurses-devel

%description
Whowatch is an interactive who-like program that displays information about the
users currently logged on to the machine, in real time. Besides standard
information (login name, tty, host, user's process), the type of the connection
(ie. telnet or ssh) is shown. You can toggle display between users' command or
idle time. You can watch processes tree, navigate in it and send INT and KILL
signals.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
# Avoid regenerating configure script because whowatch-configure-c99.patch
# updates it directly.
touch aclocal.m4 Makefile.in src/config.h.in
%configure
%{__make} %{?_smp_mflags}

%install
%{__install} -d -m0755 %{buildroot}%{_mandir}/man1/ \
			%{buildroot}%{_bindir}
%makeinstall

%files
%doc AUTHORS ChangeLog PLUGINS.readme README TODO
%doc %{_mandir}/man1/whowatch.1*
%license COPYING
%{_bindir}/whowatch

%changelog
%autochangelog
