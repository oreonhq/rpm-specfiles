%global source0_hash 366ce0ce3f9447302f5567009269c8bb3882d808f33eefac85ba367e875c8615

Name:          nmh
Version:       1.8
Release:       10%{?dist}
Summary:       A capable MIME-email-handling system with a command-line interface
# Automatically converted from old format: BSD - review is highly recommended.
License:       LicenseRef-Callaway-BSD
URL:           https://savannah.nongnu.org/projects/nmh
Source0:       https://download-mirror.savannah.gnu.org/releases/%{name}/%{name}-1.8.tar.gz
Patch0:        nmh-use-smtp-port.patch
BuildRequires: cyrus-sasl-devel
BuildRequires: gcc
BuildRequires: gdbm-devel
BuildRequires: libcurl-devel
BuildRequires: make
BuildRequires: ncurses-devel
BuildRequires: openssl-devel
BuildRequires: readline-devel
BuildRequires: w3m
Requires:      w3m
Suggests:      %{_bindir}/vi
Suggests:      %{_sbindir}/sendmail
# pick also provides /usr/bin/pick and its man page, Bug 2027139
Conflicts:     pick
# scalasca also provides /usr/bin/scan and its man page
Conflicts:     scalasca

%description
nmh is a collection of single-purpose programs that send, receive,
show, search, and otherwise manipulate emails, including MIME.
They combine well with other Unix programs, easing the development
of custom shorthand commands as shell scripts.
Optional GUI interfaces are provided by the external xmh and exmh
projects.  nmh is a descendant of the RAND MH, Mail Handler, project.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-1.8
%patch -P 0 -p1

# Avoid regenerating autotools machinery.
touch aclocal.m4 Makefile.in config.h.in configure

%build
CFLAGS="$RPM_OPT_FLAGS"
%configure
%make_build

%install
%make_install INSTALL="install -p"

%files
%{_bindir}/*
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/*
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/*
%{_mandir}/man[8751]/*
%doc %{_pkgdocdir}/*

%changelog
%autochangelog
