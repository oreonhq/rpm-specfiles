Name:		nkf
Epoch:		1
Version:	2.1.4
Release:	38%{?dist}
License:	Zlib
URL:		http://nkf.osdn.jp/
Source0:	http://iij.dl.osdn.jp/nkf/64158/%{name}-%{version}.tar.gz
## snippet from the source code
Source3:	nkf.copyright
Source4:	nkf.1j
Patch0:		%{name}-fix-man.patch
BuildRequires: make
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	gcc

Summary:	A Kanji code conversion filter

%description
Nkf is a Kanji code converter for terminals, hosts, and networks. Nkf
converts input Kanji code to 7-bit JIS, MS-kanji (shifted-JIS) or
EUC.

%package -n perl-NKF
Summary:	Perl extension for Network Kanji Filter

%description -n perl-NKF
This is a Perl Extension version of nkf (Network Kanji Filter).
It converts the last argument and return converted result.
Conversion details are specified by flags before the last argument.

%prep
%autosetup -p1
cp -p %{SOURCE4} .

%build
%set_build_flags
%make_build CFLAGS="$CFLAGS" LDFLAGS="$LDFLAGS"
cp -p %{SOURCE3} .
pushd NKF.mod
perl Makefile.PL PREFIX=%{_prefix} INSTALLDIRS=vendor
%make_build CLFAGS="$CFLAGS" LDFLAGS="$LDFLAGS"
popd

%install
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/{man1,ja/man1}

./nkf -e nkf.1j > nkf.1jeuc
iconv -f euc-jp -t utf-8 nkf.1jeuc > nkf.1utf8
touch -r nkf.1j nkf.1utf8
install -m 755 -p nkf $RPM_BUILD_ROOT%{_bindir}
install -m 644 -p nkf.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 -p nkf.1utf8 $RPM_BUILD_ROOT%{_mandir}/ja/man1/nkf.1
pushd NKF.mod
%make_install
rm -f	$RPM_BUILD_ROOT%{perl_vendorarch}/perllocal.pod		\
	$RPM_BUILD_ROOT%{perl_archlib}/perllocal.pod		\
	$RPM_BUILD_ROOT%{perl_vendorarch}/auto/NKF/NKF.bs	\
	$RPM_BUILD_ROOT%{perl_vendorarch}/auto/NKF/.packlist
popd
chmod 0755 $RPM_BUILD_ROOT%{perl_vendorarch}/auto/NKF/NKF.so


%check
make test

%files
%doc nkf.doc
%license nkf.copyright
%{_bindir}/nkf
%{_mandir}/man1/nkf.1*
%{_mandir}/ja/man1/nkf.1*

%files -n perl-NKF
%doc nkf.doc
%license nkf.copyright
%{perl_vendorarch}/NKF.pm
%{perl_vendorarch}/auto/*
%{_mandir}/man3/NKF.3pm.gz

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.1.4-38
- Prepare for Oreon 11 (RP1)
