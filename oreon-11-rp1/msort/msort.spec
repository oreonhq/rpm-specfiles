%global source0_hash 596793367839a2886863f3564086a74a8249651c968ad6bb74aace531e3b7120

Summary:       Sort files in sophisticated ways
Name:          msort
Version:       8.53
Release:       60%{?dist}
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:       GPL-3.0-only
URL:           http://billposer.org/Software/msort.html
Source0:       http://billposer.org/Software/Downloads/msort-%{version}.tar.bz2
Patch0:        msort-8.53-dso.patch
Patch1:        msort-8.53-format.patch
Patch2:        msort-8.53-mlimits.patch
Patch3:        msort-configure-c99.patch
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc
BuildRequires: gmp-devel
BuildRequires: libicu-devel
BuildRequires: libuninum-devel >= 2.5
BuildRequires: make
BuildRequires: tre-devel >= 0.8.0
Requires:      iwidgets
%description
Msort is a program for sorting files in sophisticated ways. Records
need not be single lines. Key fields may be selected by position, tag,
or character range. For each key, distinct exclusions, multigraphs,
substitutions. and a sort order may be defined. Comparisons may be
lexicographic, numeric, by string length, date, or time. Optional keys
are supported. Msort uses the Unicode character set and provides full
Unicode case-folding. The basic program has a somewhat complex command
line interface, but may be driven by an optional GUI.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
aclocal
automake --add-missing --copy
autoconf
export LDFLAGS="%{__global_ldflags} -fPIC"
export CFLAGS="%{optflags}"
%configure --disable-utf8proc
make %{?_smp_mflags} CFLAGS="%{optflags} -fPIC" LDFLAGS="%{__global_ldflags} -fPIC"

%install
make DESTDIR=%{buildroot} install
install -p -m 0644 -D msort.1 %{buildroot}%{_mandir}/man1/msort.1

%check
touch hybrid-ips.txt
./msort -ql -t SRC= -c h -t DST= -c h hybrid-ips.txt
rm hybrid-ips.txt

%files
%license COPYING
%doc AUTHORS ChangeLog Doc/* NEWS README TODO
%{_bindir}/msg
%{_bindir}/msort
%{_mandir}/man1/msort.1*

%changelog
%autochangelog
