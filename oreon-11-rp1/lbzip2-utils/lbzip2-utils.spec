%global source0_hash f43e9d60851df86ec17ae2deafd203f1a7691294338f66d8b2102c510246a83b

Name:           lbzip2-utils
Version:        1.0
Release:        29%{?dist}
Summary:        Utilities for working with bzip2 compressed files
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://lbzip2.org/
Source0:        http://archive.lbzip2.org/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc

Requires:       lbzip2

%description
This package provides a collection of utility programs to work with
compressed files in bz2 format.  These utilities are supplementary to
lbzip2 compression tool.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%check
make check

%files
%doc AUTHORS COPYING NEWS README
%{_bindir}/*
%{_mandir}/man1/*

%changelog
%autochangelog
