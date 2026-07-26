%global source0_hash 847b16378047a0d786e7a9059cb2ef6e25d5af1cd3c618a5615fb85c5aac6f51

%global commit e8082035dafe0241739d7f7d16f7ecfd2ce06172
%global shortcommit %{sub %{commit} 1 7}
%global commitdate 20251124

Name:           wl-clipboard
Version:        2.2.1%{?commitdate:^git%{commitdate}.%{shortcommit}}
Release:        2%{?dist}
Summary:        Command-line copy/paste utilities for Wayland

License:        GPL-3.0-or-later
URL:            https://github.com/bugaevc/wl-clipboard
%if %{defined commitdate}
Source:         %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
%else
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
%endif

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel >= 1.39

Recommends:     xdg-utils
Recommends:     mailcap

%description
Command-line Wayland clipboard utilities, `wl-copy` and `wl-paste`,
that let you easily copy data between the clipboard and Unix pipes,
sockets, files and so on.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -C

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license COPYING
%doc README.md
%{_bindir}/wl-copy
%{_bindir}/wl-paste
%{_mandir}/man1/wl-clipboard.1.*
%{_mandir}/man1/wl-copy.1.*
%{_mandir}/man1/wl-paste.1.*
%{_datadir}/bash-completion/completions/wl-*
%{_datadir}/fish/vendor_completions.d/wl-*
%{_datadir}/zsh/site-functions/_wl-*

%changelog
%autochangelog
