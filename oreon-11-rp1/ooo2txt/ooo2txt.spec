%global source3_hash 54b46124ef3457e6dacc856fffe1d7bafc56c58d9840dc6c3058c001993a7b95
%global source2_hash cdde1e7ce8285c4f6ab872691c2c1464a86215747360deff00b82523ca2c82c7
%global source1_hash c7a77b39ab04fc8cfbe759d29e8d70d871603c6ee6c2880804123fa998a7d8b2
%global source0_hash a60e66babe88a7d664188bea4f0ccac37b28d356b0b0cdbd9b2a9fea73410fc0
Name:           ooo2txt
Version:        0.0.6
Release:        1%{?dist}
Summary:        Convert OpenOffice documents to simple text
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://ooo2txt.fr.st/
Source0:        http://oootools.free.fr/ooo2txt/download/source/ooo2txt.006.pl
Source1:        http://oootools.free.fr/ooo2txt/download/source/update.txt
Source2:        http://oootools.free.fr/ooo2txt/download/source/readme.txt
Source3:        http://oootools.free.fr/ooo2txt/download/licence/LGPL.txt
Source4:        %{name}.pod
Patch0:         ooo2txt-0.0.6-fixes.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  //bin/pod2man
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  sed
# /oreon:deps
%description
ooo2txt converts OpenOffice documents to simple text.

%prep

%setup -q -T -c
cp -p %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} .
sed -e 's/\r//' ooo2txt.006.pl > ooo2txt.006.pl.eol
touch -r ooo2txt.006.pl ooo2txt.006.pl.eol
mv ooo2txt.006.pl.eol ooo2txt.006.pl
%patch -P0 -p1 -b .fixes
touch -r ooo2txt.006.pl.fixes ooo2txt.006.pl

%build

pod2man ooo2txt.pod > ooo2txt.1
touch -r ooo2txt.pod ooo2txt.1
%install
install -d -m755 $RPM_BUILD_ROOT%{_bindir} $RPM_BUILD_ROOT%{_mandir}/man1
install -p -m755 ooo2txt.006.pl $RPM_BUILD_ROOT%{_bindir}/ooo2txt
install -p -m644 ooo2txt.1 $RPM_BUILD_ROOT%{_mandir}/man1/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
