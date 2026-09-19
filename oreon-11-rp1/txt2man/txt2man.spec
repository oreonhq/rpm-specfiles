%global source0_hash 4d9b1bfa2b7a5265b4e5cb3aebc1078323b029aa961b6836d8f96aba6a9e434d

Name:           txt2man
Version:        1.7.1
Release:        11%{?dist}
Summary:        Convert flat ASCII text to man page format

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/mvertes/txt2man
Source0:        https://github.com/mvertes/%{name}/archive/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  gawk

Requires:       gawk

%description
txt2man is a shell script using gnu awk, that should run on any
Unix-like system. The syntax of the ASCII text is very straightforward
and looks very much like the output of the man(1) program.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# No idea why but github archive is prepending the name twice
%setup -q -n %{name}-%{name}-%{version}

%build
%{make_build}

%install
#manual install
install -p -m 0755 -D bookman $RPM_BUILD_ROOT%{_bindir}/bookman
install -p -m 0755 -D src2man $RPM_BUILD_ROOT%{_bindir}/src2man
install -p -m 0755 -D txt2man $RPM_BUILD_ROOT%{_bindir}/txt2man

install -p -m 0644 -D bookman.1 $RPM_BUILD_ROOT%{_mandir}/man1/bookman.1
install -p -m 0644 -D src2man.1 $RPM_BUILD_ROOT%{_mandir}/man1/src2man.1
install -p -m 0644 -D txt2man.1 $RPM_BUILD_ROOT%{_mandir}/man1/txt2man.1

%files
%doc COPYING Changelog README
%{_bindir}/*
%{_mandir}/man?/*

%changelog
%autochangelog
