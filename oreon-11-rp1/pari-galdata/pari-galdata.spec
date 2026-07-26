%global source0_hash b7c1650099b24a20bdade47a85a928351c586287f0d4c73933313873e63290dd

Name:		pari-galdata
Version:	20080411
Release:	31%{?dist}
Summary:	PARI/GP Computer Algebra System Galois resolvents
License:	GPL-2.0-or-later
URL:		http://pari.math.u-bordeaux.fr/packages.html
Source0:	http://pari.math.u-bordeaux.fr/pub/pari/packages/galdata.tgz
Source1:	http://pari.math.u-bordeaux.fr/pub/pari/packages/galdata.tgz.asc
# Public key 0xb5444815, owned by Bill Allombert <allomber@math.u-bordeaux.fr>
Source2:	gpgkey-4940AE28C5F8E8A35E4D8D287833ECF1B5444815.gpg
BuildArch:	noarch

BuildRequires:	gpgverify

%description
This package contains the optional PARI package galdata, which provides the
Galois resolvents for the polgalois function, for degrees 8 through 11.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Verify the source file
%{gpgverify} --data=%{SOURCE0} --signature=%{SOURCE1} --keyring=%{SOURCE2}

%autosetup -c

%build

%install
mkdir -p %{buildroot}%{_datadir}/pari/
cp -a data/galdata %{buildroot}%{_datadir}/pari/
%{_fixperms} %{buildroot}%{_datadir}/pari/

%files
%{_datadir}/pari/

%changelog
%autochangelog
