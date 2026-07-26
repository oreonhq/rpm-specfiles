%global source0_hash 451ba344490b764d9d2ffd7df2e00ad1e8fd34fc3ffdb36d3829564e6bdd05c9

Name:           ptrash
Version:        1.1
Release:        23%{?dist}
Summary:        Move file(s) to $XDG_DATA_HOME/Trash directory

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://pjp.dgplug.org/tools/
Source0:        http://pjp.dgplug.org/tools/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc
%description
Ptrash moves the named file(s) to the Trash directory. Trash is located
under $XDG_DATA_HOME directory as defined by the Trash specification.[*]
It is a simple console based utility, I wrote after deleting some files,
which I couldn't retrieve back. Ptrash can also restore file(s) back to there
original location.

[*] https://standards.freedesktop.org/trash-spec/trashspec-latest.html

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
rm -f $RPM_BUILD_ROOT/%{_infodir}/dir

%files
%doc README COPYING
%_bindir/ptrash
%_infodir/*
%_mandir/man1/*

%changelog
%autochangelog
