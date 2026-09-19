%global source0_hash 12a505b98863f6c5cf1f749f9080be3b42b3eac5a35b59630e67bea7241364ca

Name:           cppi
Version:        1.18
Release:        28%{?dist}
Summary:        C preprocessor directive indenter

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://savannah.gnu.org/projects/cppi/
Source0:        http://ftp.gnu.org/gnu/cppi/cppi-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires: make
%description
cppi indents the C preprocessor directives to reflect their nesting and ensures
that there is exactly one space character between each #if, #elif, #define
directive and the following token.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure --disable-silent-rules
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%find_lang cppi

%check
make check

%files -f cppi.lang
%doc AUTHORS ChangeLog COPYING NEWS THANKS TODO
%{_bindir}/cppi
%{_mandir}/man1/cppi.1*

%changelog
%autochangelog
