%global source0_hash 51ab9c4e5fdd37e03c90df6756f30c0b61a34f066cb625f8924feedc4b3ec3fe

Summary: A tool for printing multiple pages of text on each printed page
Name: mpage
Version: 2.5.7
Release: 24%{?dist}
License: GPL-2.0-or-later
Url: http://www.mesa.nl/pub/mpage/
Source: ftp://ftp.mesa.nl/pub/mpage/mpage-%{version}.tgz
Patch0: mpage25-config.patch
Patch1:  mpage-2.5.7-fixdecl.patch
BuildRequires: make
BuildRequires: gcc

%description
The mpage utility takes plain text files or PostScript(TM) documents
as input, reduces the size of the text, and prints the files on a
PostScript printer with several pages on each sheet of paper. Mpage is
very useful for viewing large printouts without using up lots of
paper. Mpage supports many different layout options for the printed
pages.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .config
%patch -P 1 -p1 -b .fixdecl

%build
make BINDIR=%{_bindir} LIBDIR=%{_datadir} MANDIR=%{_mandir}/man1

iconv -f iso-8859-2 -t utf-8 CHANGES > CHANGES.tmp && \
touch -r CHANGES CHANGES.tmp && mv CHANGES.tmp CHANGES

%install
mkdir -p $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/mpage,%{_mandir}/man1}

make PREFIX=$RPM_BUILD_ROOT/%{_prefix} BINDIR=$RPM_BUILD_ROOT/%{_bindir} \
	LIBDIR=$RPM_BUILD_ROOT/%{_datadir} \
	MANDIR=$RPM_BUILD_ROOT/%{_mandir}/man1 \
	install

%files
%license COPYING
%doc CHANGES Copyright README NEWS TODO FAQ
%{_bindir}/mpage
%{_mandir}/man1/mpage.*
%{_datadir}/mpage

%changelog
%autochangelog
