%global source0_hash 562af28316ee335ee38c1172c2d5ecccb79f55c368fb9f2c6f40fc0f416bb01b

Name:		pari-galpol
Version:	20180625
Release:	19%{?dist}
Summary:	PARI/GP Computer Algebra System Galois polynomials
License:	GPL-2.0-or-later
URL:		http://pari.math.u-bordeaux.fr/packages.html
VCS:		git:https://pari.math.u-bordeaux.fr/git/galpol.git
Source0:	http://pari.math.u-bordeaux.fr/pub/pari/packages/galpol.tgz
Source1:	http://pari.math.u-bordeaux.fr/pub/pari/packages/galpol.tgz.asc
# Public key 0x4522e387, Bill Allombert <Bill.Allombert@math.u-bordeaux.fr>
Source2:	gpgkey-42028EA404A2E9D80AC453148F0E7C2B4522E387.gpg
BuildArch:	noarch

BuildRequires:	gpgverify

%description
This package contains the optional PARI package galpol, which contains a
database of polynomials defining Galois extensions of the rationals
representing all abstract groups of order up to 143 for all signatures (3657
groups, 7194 polynomials).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Verify the source file
%{gpgverify} --keyring=%{SOURCE2} --signature=%{SOURCE1} --data=%{SOURCE0}

%autosetup -c
mv data/galpol/README .

%build

%install
mkdir -p %{buildroot}%{_datadir}/pari/
cp -a data/galpol %{buildroot}%{_datadir}/pari/
%{_fixperms} %{buildroot}%{_datadir}/pari/

%files
%doc README
%{_datadir}/pari/

%changelog
%autochangelog
