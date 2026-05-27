%global source0_hash 61300f603798ecf1d7786570789f0ff3f5a1acf075a6fb9f756837d166e37d14
%global source1_hash 05220b4b4f1c6c56d3b4acf6998d79768dccd22c379639a6cf3589fbbd54ba1d

Summary: A text file browser similar to more, but better
Name: less
Version: 692
Release: 3%{?dist}
# less dual license GPL-3.0-only OR BSD-2-Clause
# lesspipe GPL-2.0-or-later
License: (GPL-3.0-only OR BSD-2-Clause) AND GPL-2.0-or-later
Source0: https://www.greenwoodsoftware.com/less/%{name}-%{version}.tar.gz
%global lesspipe_version 2.22
Source1: https://github.com/wofr06/lesspipe/archive/refs/tags/v%{lesspipe_version}.tar.gz#/lesspipe-%{lesspipe_version}.tar.gz
Source2: less.sh
Source3: less.csh
Patch4: less-394-time.patch
Patch5: less-475-fsync.patch
Patch6: less-436-manpage-add-old-bot-option.patch
Patch8: less-458-lessecho-usage.patch
Patch9: less-458-less-filters-man.patch
Patch10: less-458-lesskey-usage.patch
Patch11: less-458-old-bot-in-help.patch
Patch13: less-436-help.patch
URL: https://www.greenwoodsoftware.com/less/
BuildRequires: ncurses-devel
BuildRequires: autoconf automake libtool
BuildRequires: make
# for lesspipe make test
BuildRequires: perl-Archive-Tar
# for less-color's Perl dependencies
BuildRequires: perl-generators
# for lesspipe
Recommends: (less-color = %{version}-%{release} if perl-interpreter)
Recommends: unzip
Recommends: html2text
Recommends: 7zip

%description
The less utility is a text file browser that resembles more, but has
more capabilities.  Less allows you to move backwards in the file as
well as forwards.  Since less doesn't have to read the entire input file
before it starts, less starts up more quickly than text editors (for
example, vi).

You should install less because it is a basic utility for viewing text
files, and you'll use it frequently.

%package color
# perl files GPL-1.0-or-later, the rest GPL-2.0-or-later
License: GPL-2.0-or-later AND GPL-1.0-or-later
Summary: Colorizers for less
Requires: %{name} = %{version}-%{release}
Conflicts: less < 685-5

%description color
Syntax highlighting modes for the less pager.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%(test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; })
%setup -q -a 1
%patch -P 4 -p1 -b .time
%patch -P 5 -p2 -b .fsync
%patch -P 6 -p1 -b .manpage-add-old-bot-option
%patch -P 8 -p1 -b .lessecho-usage
%patch -P 9 -p1 -b .less-filters-man
%patch -P 10 -p1 -b .lesskey-usage
%patch -P 11 -p1 -b .old-bot
%patch -P 13 -p1 -b .help

# get consistent result localy and on builders
sed -i -e 's|"#!/usr/bin/env $selected_shell"|"#!$shellcmd"|' -e '/ZSH_/d' lesspipe-%{lesspipe_version}/configure

%build
rm -f ./configure
autoreconf -fiv
%configure
%make_build CFLAGS="%{optflags} -D_GNU_SOURCE -D_LARGEFILE_SOURCE -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64"

pushd lesspipe-%{lesspipe_version}
./configure --prefix=%{_prefix} --shell=%{_bindir}/sh --bash-completion-dir=%{_datadir}/bash-completion/completions/
# do not run make, it does nothing atm, but it reruns configure with wrong argumens
popd

%install
%make_install
mkdir -p $RPM_BUILD_ROOT/etc/profile.d
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT/etc/profile.d
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT/etc/profile.d

pushd lesspipe-%{lesspipe_version}
%make_install
rm -rf $RPM_BUILD_ROOT/usr/share/bash-completion/
popd

%check
pushd lesspipe-%{lesspipe_version}
# we dont have all required components to pass full test, but it is still
# useful to run for debug purposes
make test ||:
popd

%files
%doc README NEWS INSTALL
%license LICENSE COPYING
/etc/profile.d/*
%{_bindir}/less
%{_bindir}/lesscomplete
%{_bindir}/lessecho
%{_bindir}/lesskey
%{_bindir}/lesspipe.sh
%{_mandir}/man1/*

%files color
%{_bindir}/archive_color
%{_bindir}/code2color
%{_bindir}/vimcolor

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 692-3
- Prepare for Oreon 11 (RP1)
