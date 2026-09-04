%global source0_hash 481ace9720a8f752d26b9ba047a95885bcce0b863b30e561efb1deaf5144dad5

Name:           doclifter
Version:        2.20
Release:        12%{?dist}
Summary:        Translates documents written in troff macros to DocBook

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://www.catb.org/~esr/%{name}/

Source0:        https://gitlab.com/esr/%{name}/-/archive/%{version}/%{name}-%{version}.tar.gz
# The template for man page translations can be created with this command:
# po4a-updatepo -v -M utf-8 -f man --option groff_code=verbatim -m manlifter.1 -p manlifter.pot
Source1:        https://mariobl.fedorapeople.org/Translations/%{name}/manlifter.1.de.po

# fix shebang in doclifter
Patch0:         %{name}.patch

Requires:       plotutils
Requires:       python3

BuildArch:      noarch
BuildRequires:  plotutils
BuildRequires:  po4a
BuildRequires:  python3
BuildRequires:  xmlto
BuildRequires:  make

%description
The doclifter program translates documents written in troff macros to DocBook.

Lifting documents from presentation level to semantic level is hard, and
a really good job requires human polishing.  This tool aims to do everything
that can be mechanized, and to preserve any troff-level information that might
have structural implications in XML comments.

This tool does the hard parts.  TBL tables are translated into DocBook
table markup, PIC into SVG, and EQN into MathML (relying on pic2svg
and GNU eqn for the last two).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%patch -P0

%build
%make_build doclifter.1 manlifter.1

%install

install -p -D -m 0755 doclifter %{buildroot}%{_bindir}/doclifter
install -p -D -m 0755 manlifter %{buildroot}%{_bindir}/manlifter
install -p -D -m 0644 doclifter.1 %{buildroot}%{_mandir}/man1/doclifter.1
install -p -D -m 0644 manlifter.1 %{buildroot}%{_mandir}/man1/manlifter.1

# Generate and install localized man page
# TODO: check whether the translation is up to date
mkdir -p man/de
po4a-translate -M utf-8 -f man \
               --option groff_code=verbatim \
               -p %SOURCE1 -m manlifter.1 \
               -l man/de/manlifter.1

install -p -D -m 0644 man/de/manlifter.1 \
        %{buildroot}%{_mandir}/de/man1/manlifter.1

%check
%__make check

%files
%doc README TODO
%license COPYING
%{_bindir}/manlifter
%{_bindir}/doclifter
%{_mandir}/man1/doclifter.1.*
%{_mandir}/man1/manlifter.1.*
%{_mandir}/de/man1/manlifter.1.*

%changelog
%autochangelog
