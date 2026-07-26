%global source0_hash 02fdc312b8ceeb5786b28bf905f54328f414040ff42f45c83007f24b76cc9f7a

Name:           bmon
Version:        4.0
Release:        15%{?dist}
Summary:        Bandwidth monitor and rate estimator

License:        BSD-2-Clause and MIT
URL:            https://github.com/tgraf/bmon
Source0:        https://github.com/tgraf/bmon/releases/download/v%{version}/bmon-%{version}.tar.gz

Patch1:         bmon-4.0-buffer_size.patch

BuildRequires:  gcc
BuildRequires:  libconfuse-devel
BuildRequires:  libnl3-devel
BuildRequires:  make
BuildRequires:  ncurses-devel

%description
bmon is a monitoring and debugging tool to capture networking related
statistics and prepare them visually in a human friendly way. It
features various output methods including an interactive curses user
interface and a programmable text output for scripting.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure
make %{?_smp_mflags} V=1

%install
make install DESTDIR=%{buildroot} INSTALL="install -p"

%files
%license LICENSE.BSD
%license LICENSE.MIT
%{_bindir}/bmon
%{_mandir}/man8/bmon.8*
%{_docdir}/bmon/examples/bmon.conf

%changelog
%autochangelog
