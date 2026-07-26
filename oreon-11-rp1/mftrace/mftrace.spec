%global source0_hash 626b7a9945a768c086195ba392632a68d6af5ea24ef525dcd0a4a8b199ea5f6f

Name:		mftrace
Version:	1.2.20
Release:	19%{?dist}
Summary:	Utility for converting TeX bitmap fonts to Type 1 or TrueType fonts

License:	GPL-2.0-only
URL:		http://lilypond.org/mftrace/
Source0:	http://lilypond.org/download/sources/mftrace/%{name}-%{version}.tar.gz
Patch0:		mftrace-shebang.patch
Patch1:         mftrace-1.2.20-man.patch
Patch2:         python3.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:	python3-devel autotrace
Requires:	autotrace fontforge t1utils texlive-collection-fontsrecommended

%description
mftrace is a small Python program that lets you trace a TeX bitmap
font into a PFA or PFB font (A PostScript Type1 Scalable Font) or TTF
(TrueType) font.

Scalable fonts offer many advantages over bitmaps, as they allow
documents to render correctly at many printer resolutions. Moreover,
Ghostscript can generate much better PDF, if given scalable PostScript
fonts.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%py3_shebang_fix .

sed -i -e "s|-Wall -O2|$RPM_OPT_FLAGS -std=gnu17|" GNUmakefile.in

%patch -P 0 -p0
%patch -P 1 -p0
%patch -P 2 -p0

%build
PYTHON=%{__python3} %configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc README.txt ChangeLog
%license COPYING
%{_bindir}/*
%{_mandir}/man1/%{name}*
%{_datadir}/%{name}

%changelog
%autochangelog
