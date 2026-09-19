%global source0_hash none

Name:           ooo2txt
Version:        0.0.6
Release:        36%{?dist}
Summary:        Convert OpenOffice documents to simple text
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://ooo2txt.fr.st/
Source0:        http://oootools.free.fr/ooo2txt/download/source/ooo2txt.006.pl
Source1:        http://oootools.free.fr/ooo2txt/download/source/update.txt
Source2:        http://oootools.free.fr/ooo2txt/download/source/readme.txt
Source3:        http://oootools.free.fr/ooo2txt/download/licence/LGPL.txt
Source4:        %{name}.pod
Patch0:         ooo2txt-0.0.6-fixes.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  %{_bindir}/pod2man
BuildRequires:  perl-generators
BuildRequires:  sed

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

%files
%doc update.txt readme.txt LGPL.txt
%{_bindir}/ooo2txt
%{_mandir}/man1/ooo2txt.1*

%changelog
%autochangelog
