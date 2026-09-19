%global source0_hash 81e9e67f9ee3334c896272272098366e20f5a0f988a8295877f22a7bbe9d5688

Name:           boinc-tui
Version:        2.7.2
Release:        3%{?dist}
Summary:        Fullscreen Text Mode Manager For BOINC Client

License:        GPL-3.0-or-later
URL:            https://github.com/suleman1971/boinctui

%global commit       8e48d9c9c81b320ea17b56f2050a09df4eecce6a
%global shortcommit  %(c=%{commit}; echo ${c:0:7})
%global snapshotdate 20250818
Source0:        https://github.com/suleman1971/boinctui/archive/%{commit}/boinctui-%{shortcommit}.tar.gz

BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  ncurses-devel
BuildRequires:  expat-devel
BuildRequires:  openssl-devel
BuildRequires:  gcc-c++
BuildRequires: make

%description
 boinc-tui is a fullscreen text mode control tool for BOINC client
 It can manage local and remote clients (via boinc RPC), and allows
 you to switch between  clients with a hot key.
 boinctui uses curses library and provides the following features:
  * Fullscreen curses based text user interface
  * Switch between several BOINC clients hosts via hot key
  * View task list (run, queue, suspend e.t.c state)
  * View message list
  * Suspend/Resume/Abort tasks
  * Update/Suspend/Resume/Reset/No New Task/Allow New Task for projects
  * Toggle activity state GPU and CPU tasks
  * Run benchmarks
  * Manage BOINC client on remote hosts via boinc_gui protocol

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n boinctui-%{commit}

%build
autoreconf -vif
%configure --without-gnutls
%make_build

%install
%make_install DOCDIR=%{_pkgdocdir}
mkdir -p %{buildroot}%{_mandir}/man1
install -p -m 0644 boinctui.1 %{buildroot}%{_mandir}/man1/

%files
%doc %{_pkgdocdir}/changelog
%license gpl-3.0.txt
%{_bindir}/boinctui
%{_mandir}/man1/boinctui.1.*

%changelog
%autochangelog
