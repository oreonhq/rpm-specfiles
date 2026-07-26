%global source0_hash none

Name:		pari-seadata
Version:	20090618
Release:	31%{?dist}
Summary:	PARI/GP Computer Algebra System modular polynomials
License:	GPL-2.0-or-later
URL:		https://pari.math.u-bordeaux.fr/packages.html
Source0:	https://pari.math.u-bordeaux.fr/pub/pari/packages/seadata.tgz
Source1:	https://pari.math.u-bordeaux.fr/pub/pari/packages/seadata.tgz.asc
Source2:	https://pari.math.u-bordeaux.fr/pub/pari/packages/seadata-big.tar
Source3:	https://pari.math.u-bordeaux.fr/pub/pari/packages/seadata-big.tar.asc
# Public key 0xb5444815, owned by Bill Allombert <allomber@math.u-bordeaux.fr>
Source4:	gpgkey-4940AE28C5F8E8A35E4D8D287833ECF1B5444815.gpg
# Public key 0x4522e387, Bill Allombert <Bill.Allombert@math.u-bordeaux.fr>
Source5:	gpgkey-42028EA404A2E9D80AC453148F0E7C2B4522E387.gpg
BuildArch:	noarch

BuildRequires:	gpgverify
BuildRequires:	parallel

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
# Pari can read compressed data files, so save space
# First, decompress the compressed files so we can recompress with --best
gunzip data/seadata/*.gz
parallel %{?_smp_mflags} --no-notice gzip --best ::: data/seadata/sea*

%install
mkdir -p %{buildroot}%{_datadir}/pari/
cp -a data/seadata %{buildroot}%{_datadir}/pari/
%{_fixperms} %{buildroot}%{_datadir}/pari/

%files
%doc README
%dir %{_datadir}/pari/
%dir %{_datadir}/pari/seadata/
%{_datadir}/pari/seadata/sea0*
%{_datadir}/pari/seadata/sea2*
%{_datadir}/pari/seadata/sea3*
%{_datadir}/pari/seadata/sea4*

%files		big
%doc README.big
%{_datadir}/pari/seadata/sea5*
%{_datadir}/pari/seadata/sea6*
%{_datadir}/pari/seadata/sea7*

%changelog
%autochangelog
