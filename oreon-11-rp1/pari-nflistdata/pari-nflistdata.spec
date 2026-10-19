%global source1_hash fdebfacc1985026891f3f2d20f7d16428d33c7d6592ec513c504707494ee2c17
%global source0_hash 2c19a3e02afd3bba2af3071a7faa80924a75b00bb9713286c886b7fb460944bc
Name:           pari-nflistdata
Version:        20220729
Release:        10%{?dist}
Summary:        PARI/GP Computer Algebra System nflist extensions
License:        GPL-2.0-or-later
URL:            https://pari.math.u-bordeaux.fr/packages.html
Source0:        https://pari.math.u-bordeaux.fr/pub/pari/packages/nflistdata.tgz
Source1:        https://pari.math.u-bordeaux.fr/pub/pari/packages/nflistdata.tgz.asc
Source2:        gpgkey-42028EA404A2E9D80AC453148F0E7C2B4522E387.gpg
BuildArch:      noarch
# oreon:deps
BuildRequires:  gpgverify
# /oreon:deps
%description
This package is needed by nflist to list fields of small discriminant
(currently needed by the single Galois group A5) or to list most regular
extensions of Q(T) in degree larger than 7.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Verify the source file
%{gpgverify} --data=%{SOURCE0} --signature=%{SOURCE1} --keyring=%{SOURCE2}

%autosetup -n data

# We'll ship the README as %%doc
mv nflistdata/README .

%build

%install
mkdir -p %{buildroot}%{_datadir}/pari
cp -a nflistdata %{buildroot}%{_datadir}/pari
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
