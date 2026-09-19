%global source0_hash c531f18d28ec173e8adaa899a1cfb9cc01c5f26e57845e6524d1991cd9b17194

%define _hardened_build 1

Summary: ne, the nice editor
Name: ne
Version: 3.3.4
Release: 3%{?dist}
License: GPL-3.0-or-later
Source0: https://ne.di.unimi.it/ne-%{version}.tar.gz
URL: https://ne.di.unimi.it/
Requires: ncurses
BuildRequires: gcc
BuildRequires: ncurses-devel
BuildRequires: make
BuildRequires: bash
BuildRequires: perl
BuildRequires: texinfo
BuildRequires: sed

%description 
ne is a free (GPL'd) text editor based on the POSIX standard that runs (we
hope) on almost every UN*X machine. ne is easy to use for the beginner, but
powerful and fully configurable for the wizard, and most sparing in its
resource usage.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
cd src
%make_build NE_GLOBAL_DIR=%{_datadir}/ne LIBS=-lncurses OPTS="%{optflags} -fno-strict-aliasing -Wno-parentheses"

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/ne/syntax
mkdir -p $RPM_BUILD_ROOT%{_datadir}/ne/macros
mkdir -p $RPM_BUILD_ROOT%{_infodir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -p -m 755 ./src/ne $RPM_BUILD_ROOT%{_bindir}/ne
install -p -m 644 ./extensions $RPM_BUILD_ROOT%{_datadir}/ne/extensions
install -p -m 644 ./syntax/*.jsf $RPM_BUILD_ROOT%{_datadir}/ne/syntax
install -p -m 644 ./macros/* $RPM_BUILD_ROOT%{_datadir}/ne/macros
install -p -m 644 ./doc/ne.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -p -m 644 ./doc/ne.info* $RPM_BUILD_ROOT%{_infodir}
rm INSTALL.md
mv doc/html .

%files
%{_bindir}/ne
%{_datadir}/ne/
%{_mandir}/man1/ne.1*
%doc %{_infodir}/ne.info*
%doc ./README.md
%doc ./NEWS
%doc ./CHANGES

%package doc
Summary: Documentation for ne, the nice editor
BuildArch: noarch

%description doc
Documentation for ne, the nice editor.

%files doc
%license ./COPYING
%doc html
%doc ./doc/ne.texinfo
%doc ./doc/ne.pdf
%doc ./doc/ne.txt
%doc ./doc/default.*

%changelog
%autochangelog
