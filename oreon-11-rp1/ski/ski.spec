%global source0_hash 442ea167efef4b56c354806fa67faad3d29fa54f465f370e226404d2bd6696f0

Name:           ski
Version:        1.5.0
Release:        1%{?dist}
Summary:        IA-64 user and system mode simulator

License:        GPL-2.0-only and GPL-2.0-or-later
URL:            https://github.com/trofi/ski
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
# some syscalls are missing
ExcludeArch:    aarch64

BuildRequires:  make
BuildRequires:  elfutils-libelf-devel
BuildRequires:  ncurses-devel
BuildRequires:  automake autoconf libtool
BuildRequires:  autoconf-archive
BuildRequires:  gperf
BuildRequires:  bison flex
BuildRequires:  libtool-ltdl-devel
BuildRequires:  gcc
Obsoletes: %{name}-libs < 1.4.0
Obsoletes: %{name}-devel < 1.4.0

%description
The Ski IA-64 user and system simulator originally developed by HP.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
./autogen.sh

%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc AUTHORS NEWS README TODO ChangeLog
%doc doc/ski-notes.html doc/manual/*.pdf
%{_bindir}/ski
%{_bindir}/bski
%{_bindir}/bskinc
%{_bindir}/ski-fake-xterm
%{_mandir}/man1/ski.1*
%{_mandir}/man1/bski.1*
%{_mandir}/man1/bskinc.1*

%changelog
%autochangelog
