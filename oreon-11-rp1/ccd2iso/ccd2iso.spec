%global source0_hash f874b8fe26112db2cdb016d54a9f69cf286387fbd0c8a55882225f78e20700fc

Name:           ccd2iso
Version:        0.3
Release:        40%{?dist}
Summary:        CloneCD image to ISO image file converter

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://ccd2iso.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/ccd2iso/ccd2iso/ccd2iso-%{version}/ccd2iso-%{version}.tar.gz
# Fix compiler warnings.
# https://sourceforge.net/tracker/?func=detail&aid=3032074&group_id=94638&atid=608543
Patch0:         %{name}-%{version}-compilerWarnings.patch
# Add a manual page from debian distro.
# Sent upstream via email 20121201
Patch1:         %{name}-%{version}-manual.patch
Patch2:         %{name}-%{version}-configure-c99.patch

#BuildRequires:  
#Requires:       

BuildRequires:  gcc
BuildRequires: make
%description
The %{name} project converts CD backup files created using the non-free CloneCD
program to a format understood by most Free Software CD writing programs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0
%patch -P1
%patch -P2 -p1
sed 's/\r//' TODO > TODO.tmp
touch -r TODO TODO.tmp
mv TODO.tmp TODO

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
rm INSTALL NEWS
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
install -d $RPM_BUILD_ROOT%{_mandir}/man1/
install -p -m644 ccd2iso.1 $RPM_BUILD_ROOT%{_mandir}/man1/ccd2iso.1
gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/ccd2iso.1

%files
%doc AUTHORS ChangeLog COPYING README TODO
%{_mandir}/man1/ccd2iso.1.gz
%{_bindir}/%{name}

%changelog
%autochangelog
