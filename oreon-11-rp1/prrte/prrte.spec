# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 285ad62b670075708b9fcfe14c54baa599733bc274d10502a82e8eebba0b7c70
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           prrte
Version:        4.1.0
Release:        %{autorelease}
Summary:        PMIx Reference RunTime Environment (PRRTE)
License:        BSD-3-Clause-Open-MPI AND BSD-2-Clause
URL:            https://github.com/openpmix/%{name}
Source0:        https://github.com/openpmix/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.bz2
Patch:         prrte-fix-cflags-before-picky.patch
Patch:         2417.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  flex
BuildRequires:  make
BuildRequires:  hwloc-devel
BuildRequires:  libevent-devel
BuildRequires:  pmix-devel >= 6.1.0
BuildRequires:  pmix-tools
BuildRequires:  perl-interpreter
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

ExcludeArch:    %{ix86}

%description
PRRTE is the PMIx Reference Run Time Environment.

The project is formally referred to in documentation by "PRRTE", and
the GitHub repository is "openpmix/%{name}".

However, we have found that most users do not like typing the two
consecutive "r"s in the name. Hence, all of the internal API symbols,
environment variables, MCA frameworks, and CLI executables all use the
abbreviated "prte" (one "r", not two) for convenience.

%package        libs
Summary:        Libraries for %{name}

%description    libs
Runtime libraries for %{name}.

%package        devel
Summary:        Development files for %{name}
License:        BSD-3-Clause-Open-MPI AND BSD-2-Clause AND MIT AND (MIT OR GPL-2.0-or-later) AND (OFL-1.1 OR MIT)
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       pmix-tools%{?_isa}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%oreon_sha256
%autosetup -p1 -n %{name}-%{version}

find src -name \*.l -print -exec touch --no-create {} \;

echo '' > src/util/qsort.h
echo 'typedef int x;' > src/util/qsort.c

./autogen.pl

%build
%configure \
    --sysconfdir=%{_sysconfdir}/prte \
    --bindir=%{_libdir}/openmpi/bin \
    --mandir=%{_libdir}/openmpi/share/man \
    --disable-static \
    --disable-silent-rules \
    --enable-shared \
    --with-sge \
    --with-pmix=%{_prefix}

%make_build

%install
%make_install

find %{buildroot} -name '*.la' -delete

rm %{buildroot}%{_docdir}/%{name}/html/.buildinfo*

%check
%make_build check

%files
%doc README.md
%{_libdir}/openmpi/bin/prte
%{_libdir}/openmpi/bin/prte_info
%{_libdir}/openmpi/bin/prte-info
%{_libdir}/openmpi/bin/prte-submit
%{_libdir}/openmpi/bin/prte-term
%{_libdir}/openmpi/bin/prted
%{_libdir}/openmpi/bin/prterun
%{_libdir}/openmpi/bin/prun
%{_libdir}/openmpi/bin/pterm
%{_libdir}/openmpi/share/man/man1/*.1*
%{_libdir}/openmpi/share/man/man5/*.5*

%files libs
%license LICENSE
%dir %{_sysconfdir}/prte
%config(noreplace) %{_sysconfdir}/prte/*
%{_datadir}/prte/
%{_libdir}/lib%{name}.so.3*

%files devel
%{_libdir}/openmpi/bin/pcc
%{_docdir}/prrte/
%{_includedir}/prte*.h
%{_includedir}/prte/
%{_libdir}/lib%{name}.so

%changelog
%autochangelog
