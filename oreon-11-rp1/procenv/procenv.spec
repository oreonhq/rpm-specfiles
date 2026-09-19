%global source0_hash fac0438bf08ed73b10ace78d85acb83cf81ade5ecf866762c2c6e92e41dbde43

# Copyright (c) 2012, 2014  Dave Love
# Copyright (c) 2015 James Hunt
# MIT licence, per Fedora policy

Name:           procenv
Version:        0.60
Release:        15%{?dist}
Summary:        Utility to show process environment

License:        GPL-3.0-or-later
URL:            https://github.com/jamesodhunt/procenv
Source0:        https://github.com/jamesodhunt/procenv/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires: make
BuildRequires:  expat, libcap-devel, libselinux-devel, check-devel, gcc
BuildRequires:  numactl-devel
# Only used for testing
BuildRequires:  perl(JSON::PP)

%description
This package contains a command-line tool that displays as much
detail about itself and its environment as possible. It can be
used as a test tool, to understand the type of environment a
process runs in, and for comparing system environments.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
# See https://github.com/jamesodhunt/procenv/issues/39
export CFLAGS="$CFLAGS -Wno-error=address -Wno-error=discarded-qualifiers"
%configure
%make_build

%install
%make_install

%check
make check

%files
%{_bindir}/procenv
%{_mandir}/man1/procenv.1*
# ChangeLog is empty
%doc README.md NEWS AUTHORS TODO
%license COPYING

%changelog
%autochangelog
