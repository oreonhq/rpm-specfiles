%global source0_hash 39b7a5f0fefdea87885f3b6ab041e7148c600fb50017c3a283231f6dde5eca2b

Name:           t-prot
Version:        3.4
Release:        23%{?dist}
Summary:        A filter which improves the readability of email messages and Usenet posts

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://www.escape.de/~tolot/mutt/
Source0:        http://www.escape.de/~tolot/mutt/t-prot/downloads/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(Locale::gettext)
Requires:       perl(Locale::gettext)

%description
t-prot (TOFU Protection) is a filter which improves the readability of email
messages and Usenet posts by hiding some of their annoying parts. The
annoyances it handles include mailing list footers, signatures, TOFU,
sequences of blank lines, and repeated punctuation.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

# Empty build
%build

%install
install -d $RPM_BUILD_ROOT%{_bindir}
install -p -m755 t-prot $RPM_BUILD_ROOT%{_bindir}

install -d $RPM_BUILD_ROOT%{_mandir}/man1/
install -p -m 644 t-prot.1 $RPM_BUILD_ROOT%{_mandir}/man1/

%files
%doc ChangeLog TODO README contrib
%{_bindir}/t-prot
%{_mandir}/man1/t-prot.1*

%changelog
%autochangelog
