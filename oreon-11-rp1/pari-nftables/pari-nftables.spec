%global source1_hash ae7969f3bd2f05375289c2f3aec068f062ae64e9b7e3308f0e8e63722f466f04
%global source0_hash 8dd3393ce6b3cfcf599f094f7b22bdffe17c3ba25deb912513d54676bd7cfe92
Name:           pari-nftables
Version:        20080929
Release:        12%{?dist}
Summary:        PARI/GP Computer Algebra System number field tables
License:        GPL-2.0-or-later
URL:            https://pari.math.u-bordeaux.fr/packages.html
Source0:        https://pari.math.u-bordeaux.fr/pub/pari/packages/nftables.tgz
Source1:        https://pari.math.u-bordeaux.fr/pub/pari/packages/nftables.tgz.asc
Source2:        gpgkey-dd6754092ef692988cfcdcbad49a9c20edef8d6a.gpg
ExcludeArch:    %{ix86}
BuildArch:      noarch
# oreon:deps
BuildRequires:  gpgverify
BuildRequires:  parallel
# /oreon:deps
%description
This package contains the optional PARI package nftables, which provides the
historical megrez number fields tables (errors fixed, 1/10th the size, easier
to use).  These tables can be queried by readvec.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Verify the source file
%{gpgverify} --data=%{SOURCE0} --signature=%{SOURCE1} --keyring=%{SOURCE2}

%autosetup -c

# We'll ship the README as %%doc
mv nftables/README .

%build

parallel %{?_smp_mflags} --no-notice gzip --best ::: nftables/*.gp
%install
mkdir -p %{buildroot}%{_datadir}/pari
cp -a nftables %{buildroot}%{_datadir}/pari
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
