%global source0_hash b6d8d9c76585db8ef5fa00d4931902fa4b8cbe8166f528f44fc403961a3f3759

%global _hardened_build 1

Name:           tmux
Version:        3.6a
Release:        1%{?dist}
Summary:        A terminal multiplexer

License:        ISC AND BSD-2-Clause AND BSD-3-Clause AND SSH-short AND LicenseRef-Fedora-Public-Domain
URL:            https://tmux.github.io/
Source0:        https://github.com/tmux/tmux/releases/download/3.6a/tmux-3.6a.tar.gz
Source2:        tmux@.service
Source3:        README.polkit
BuildRequires:  byacc
BuildRequires:  gcc
BuildRequires:  systemd-devel
BuildRequires:  libutempter-devel
BuildRequires:  make
BuildRequires:  pkgconfig(libevent_core) >= 2
BuildRequires:  pkgconfig(tinfo)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(ncursesw)
%if "%0{?commit}" != "0"
BuildRequires:  automake
%endif

%description
tmux is a "terminal multiplexer."  It enables a number of terminals (or
windows) to be accessed and controlled from a single terminal.  tmux is
intended to be a simple, modern, BSD-licensed alternative to programs such
as GNU Screen.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup

%build
%configure --enable-sixel --enable-systemd --enable-utempter
%make_build


%install
%make_install

# Install the systemd file
install -Dpm 644 %{SOURCE2} %{buildroot}%{_unitdir}/tmux@.service

# Install the polkit example file
install -Dpm 644 %{SOURCE3} %{buildroot}%{_docdir}/tmux/README.polkit

%post
if [ "$1" = 1 ]; then
  if [ ! -f %{_sysconfdir}/shells ] ; then
    touch %{_sysconfdir}/shells
  fi
  for binpath in %{_bindir} /bin; do
    if ! grep -q "^${binpath}/tmux$" %{_sysconfdir}/shells; then
       (cat %{_sysconfdir}/shells; echo "$binpath/tmux") > %{_sysconfdir}/shells.new
       mv %{_sysconfdir}/shells{.new,}
    fi
  done
fi

%postun
if [ "$1" = 0 ] && [ -f %{_sysconfdir}/shells ] ; then
  sed -e '\!^%{_bindir}/tmux$!d' -e '\!^/bin/tmux$!d' < %{_sysconfdir}/shells > %{_sysconfdir}/shells.new
  mv %{_sysconfdir}/shells{.new,}
fi

%files
%license COPYING
%doc CHANGES README* example_tmux.conf README.polkit
%{_bindir}/tmux
%{_mandir}/man1/tmux.1.*
%{_unitdir}/tmux@.service

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.6a-1
- Prepare for Oreon 11 (RP1)
