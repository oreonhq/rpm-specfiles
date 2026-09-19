%global source0_hash 849ba852c7f37b6772365cb0c42a94cde0fe75efba91363e96a0e7ef797ba565

Name:           calcurse
Version:        4.8.2
Release:        3%{?dist}
Summary:        Text-based personal organizer

License:        BSD-2-Clause
URL:            https://calcurse.org
Source0:        https://calcurse.org/files/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gettext-devel ncurses-devel autoconf automake asciidoc
BuildRequires:  make
Requires:       python3-httplib2

%description
Calcurse is a text-based calendar and scheduling application. It helps 
keep track of events, appointments, and everyday tasks.

A configurable notification system reminds the user of upcoming 
deadlines, and the curses based interface can be customized to suit user 
needs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
install -p -m 0644 doc/calcurse.1 $RPM_BUILD_ROOT%{_mandir}/man1/
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/%{name}
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS doc/*.txt
%{_bindir}/calcurse*
%{_mandir}/man1/calcurse.1.gz

%changelog
%autochangelog
