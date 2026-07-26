%global source0_hash 8f2015c05e2ad82f12ae4cf12b363d34f527a4bbc8c369667f239e4542e1e510

Name:           dvtm
Version:        0.15
Release:        24%{?dist}
Summary:        Tiling window management for the console
License:        MIT and ISC
URL:            http://www.brain-dump.org/projects/%{name}/
Source0:        http://www.brain-dump.org/projects/%{name}/%{name}-%{version}.tar.gz
Patch0:         %{name}-0.14-build.patch
Patch1:         %{name}-0.15-terminfo-provided-by-ncurses.patch
BuildRequires:  binutils
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  sed
Requires:       ncurses-term

%description
dvtm brings the concept of tiling window management, popularized by
X11-window managers like dwm to the console. As a console window
manager it tries to make it easy to work with multiple console based
programs like vim, mutt, cmus or irssi.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .build
%patch -P1 -p1 -b .terminfo

%build
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-status
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
