%global source0_hash d2158edddb923ea23ac309086598fe99b84bd9f0fc7cc1a73cb0383dbfb3c88a

Name:          par
Version:       1.53.0
Release:       18%{?dist}
Summary:       Paragraph reformatter, vaguely like fmt, but more elaborate
License:       LicenseRef-Par
URL:           http://www.nicemice.net/par/
Source0:       http://www.nicemice.net/par/Par-1.53.0.tar.gz
BuildRequires: gcc
BuildRequires: make

%description
par is a filter which copies its input to its output, changing all
white characters (except newlines) to spaces, and reformatting each
paragraph.  Paragraphs are separated by protected, blank, and bodiless
lines (see the man page Terminology section for definitions), and
optionally delimited by indentation (see the d option in the Options
section).  Each output paragraph is generated from the corresponding
input paragraph as follows:

  1) An optional prefix and/or suffix is removed from each input line.
  2) The remainder is divided into words (separated by spaces).
  3) The words are joined into lines to make an eye-pleasing paragraph.
  4) The prefixes and suffixes are reattached.

If there are suffixes, spaces are inserted before them so that they
all end in the same column.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Par-1.53.0

%build
%make_build -f protoMakefile CC="gcc -c $RPM_OPT_FLAGS"

%install
install -d %{buildroot}/%{_bindir}
install -d %{buildroot}/%{_mandir}/man1
install par %{buildroot}/%{_bindir}
install -m 644 par.1 %{buildroot}/%{_mandir}/man1

%files
%{_bindir}/par
%{_mandir}/man1/par.1*
%doc par.doc releasenotes

%changelog
%autochangelog
