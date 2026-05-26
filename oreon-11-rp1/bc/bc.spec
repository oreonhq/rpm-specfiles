Summary: GNU's bc (a numeric processing language) and dc (a calculator)
Name: bc
Version: 1.08.2
Release: 4%{?dist}
License: GPL-3.0-or-later
URL: https://www.gnu.org/software/bc/
Source0: https://ftp.gnu.org/gnu/bc/bc-%{version}.tar.gz
Source1: https://ftp.gnu.org/gnu/bc/bc-%{version}.tar.gz.sig
Source2: kevin_pizzini.asc
Patch1: bc-1.06-dc_ibase.patch
Patch2: bc-1.06.95-doc.patch
Patch3: bc-1.07.1-readline-echo-empty.diff
# oreon url source checksums begin
%global source0_sha256 ae470fec429775653e042015edc928d07c8c3b2fc59765172a330d3d87785f86
%global source0_file bc-1.08.2.tar.gz
# oreon url source checksums end
BuildRequires: bison
BuildRequires: ed
BuildRequires: flex
BuildRequires: gcc
BuildRequires: make
BuildRequires: readline-devel
BuildRequires: texinfo
# for gpg verification
BuildRequires: gnupg2

%description
The bc package includes bc and dc. Bc is an arbitrary precision
numeric processing arithmetic language. Dc is an interactive
arbitrary precision stack based calculator, which can be used as a
text mode calculator.

Install the bc package if you need its number handling capabilities or
if you would like to use its text mode calculator.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/bc-1.08.2.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "ae470fec429775653e042015edc928d07c8c3b2fc59765172a330d3d87785f86" || { echo "oreon: Source0 SHA256 mismatch for bc-1.08.2.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%configure --with-readline
%make_build

%install
%make_install
rm -f %{buildroot}/%{_infodir}/dir

%files
%license COPYING COPYING.LIB
%doc FAQ AUTHORS NEWS README Examples/
%{_bindir}/dc
%{_bindir}/bc
%{_mandir}/man1/bc.1*
%{_mandir}/man1/dc.1*
%{_infodir}/bc.info*
%{_infodir}/dc.info*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.08.2-4
- Prepare for Oreon 11 (RP1)
