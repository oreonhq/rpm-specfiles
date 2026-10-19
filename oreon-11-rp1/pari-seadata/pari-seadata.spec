%global source3_hash 16dc253d43138ed684822a5c3f0a5d6876d70334601df2f06ac7cf0726596c8a
%global source2_hash 7c4db2624808a5bbd2ba00f8b644a439f0508532efd680a247610fdd5822a5f2
%global source1_hash 14428827a7ebbd7702b7273320c7e6669baa34b8dd753bb0c7d457bab1afdf58
%global source0_hash c9282a525ea3f92c1f9c6c69e37ac5a87b48fb9ccd943cfd7c881a3851195833
Name:		pari-seadata
Version:	20090618
Release:        31%{?dist}
Summary:        PARI/GP Computer Algebra System modular polynomials
License:	GPL-2.0-or-later
URL:		https://pari.math.u-bordeaux.fr/packages.html
Source0:        https://pari.math.u-bordeaux.fr/pub/pari/packages/seadata.tgz
Source1:	https://pari.math.u-bordeaux.fr/pub/pari/packages/seadata.tgz.asc
Source2:	https://pari.math.u-bordeaux.fr/pub/pari/packages/seadata-big.tar
Source3:	https://pari.math.u-bordeaux.fr/pub/pari/packages/seadata-big.tar.asc
Source4:	gpgkey-4940AE28C5F8E8A35E4D8D287833ECF1B5444815.gpg
Source5:	gpgkey-42028EA404A2E9D80AC453148F0E7C2B4522E387.gpg
BuildArch:	noarch
# oreon:deps
BuildRequires:  gpgverify
BuildRequires:  parallel
# /oreon:deps
%description
This package contains the optional PARI package seadata, which provides the
modular polynomials for prime level up to 500 needed by the GP functions ellap
and ellsea.  This is suitable for finite fields of cardinality q up to 750
bits.

These polynomials were extracted from the ECHIDNA databases available at
<http://echidna.maths.usyd.edu.au/kohel/dbs/> and computed by David R. Kohel
at the University of Sydney.

%package	big
Summary:	PARI/GP Computer Algebra System big modular polynomials
Requires:	%{name} = %{version}-%{release}
%description	big
This package contains extra modular polynomials of prime level between 500 and
800.  This is suitable for finite fields of cardinality q up to 1100 bits.

%prep

# Verify the source files
%{gpgverify} --data=%{SOURCE0} --signature=%{SOURCE1} --keyring=%{SOURCE4}
%{gpgverify} --data=%{SOURCE2} --signature=%{SOURCE3} --keyring=%{SOURCE5}

%autosetup -c -a 2
mv data/seadata/README* .

%build

gunzip data/seadata/*.gz
parallel %{?_smp_mflags} --no-notice gzip --best ::: data/seadata/sea*
%install
mkdir -p %{buildroot}%{_datadir}/pari/
cp -a data/seadata %{buildroot}%{_datadir}/pari/
%{_fixperms} %{buildroot}%{_datadir}/pari/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n pari-seadata-big -f %{oreon_filedir}/pari-seadata-big.list

%changelog

%autochangelog
