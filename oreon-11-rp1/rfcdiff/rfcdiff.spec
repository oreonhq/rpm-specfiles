%global source0_hash 80c886e76803b889c444cd44781f8fa34cb23943a28f18cac0ea8a1458dca265

Name:           rfcdiff
Version:        1.48
Release:        14%{?dist}
Summary:        Compares two internet draft files and outputs the difference

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://tools.ietf.org/tools/rfcdiff/
Source0:        http://tools.ietf.org/tools/rfcdiff/%{name}-%{version}.tgz

BuildArch:      noarch
BuildRequires: make
BuildRequires:  txt2man

%description
The purpose of this program is to compare two versions of an
internet-draft, and as output produce a diff in one of several
formats:
- side-by-side html diff
- paged wdiff output in a text terminal
- a text file with changebars in the left margin
- a simple unified diff output

In all cases, internet-draft headers and footers are stripped before
generating the diff, to produce a cleaner diff.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
sed -i 's|include ../Makefile.common|include Makefile.common|g' Makefile

%build
make manpage

%install
mkdir -p %{buildroot}%{_bindir} \
         %{buildroot}%{_mandir}/man1

install -pm 0755 %{name} %{buildroot}%{_bindir}/
install -pm 0644 %{name}.1.gz %{buildroot}%{_mandir}/man1/

%files
%doc changelog copyright todo
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz

%changelog
%autochangelog
