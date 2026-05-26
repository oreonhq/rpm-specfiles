# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 ae470fec429775653e042015edc928d07c8c3b2fc59765172a330d3d87785f86
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

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
%oreon_verify_sources
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
