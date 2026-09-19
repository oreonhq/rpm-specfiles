%global source0_hash 174bb632c4ed812a57225a73ecab5293fcbab0368c454d113bf3c039722695bb

Summary: 	CVS Utilities
Name: 		cvsutils
Version: 	0.2.6
Release: 	25%{?dist}
License: 	GPL-3.0-or-later
URL: 		http://www.red-bean.com/cvsutils
Source: 	http://www.red-bean.com/cvsutils/releases/cvsutils-%{version}.tar.gz

BuildRequires:	perl-generators
BuildRequires:	make

Requires: 	cvs
BuildArch:	noarch

%description
CVS Utilities is a collection of tools to facilitate working with
Concurrent Versions System (CVS).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure
%{make_build}

%install
%{make_install}

for f in ${RPM_BUILD_ROOT}%{_bindir}/*; do
  echo ".so man1/cvsutils.1" > \
          ${RPM_BUILD_ROOT}%{_mandir}/man1/$(basename $f).1 
done

%files
%doc NEWS README AUTHORS
%license COPYING
%{_bindir}/*
%{_mandir}/man1/*

%changelog
%autochangelog
