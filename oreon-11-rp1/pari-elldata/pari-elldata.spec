%global source0_hash none

Name:		pari-elldata
Version:	20210301
Release:	13%{?dist}
Summary:	PARI/GP Computer Algebra System elliptic curves
License:	GPL-2.0-or-later
URL:		https://pari.math.u-bordeaux.fr/packages.html
Source0:	https://pari.math.u-bordeaux.fr/pub/pari/packages/elldata.tgz
Source1:	https://pari.math.u-bordeaux.fr/pub/pari/packages/elldata.tgz.asc
# Public key 0x4522e387, Bill Allombert <Bill.Allombert@math.u-bordeaux.fr>
Source2:	gpgkey-42028EA404A2E9D80AC453148F0E7C2B4522E387.gpg

BuildArch:	noarch

BuildRequires:	gpgverify
BuildRequires:	parallel

%description
This package contains the optional PARI package elldata, which provides the
Elliptic Curve Database of J. E. Cremona Elliptic, which can be queried by
ellsearch and ellidentify.

%prep
# Verify the source file
%{gpgverify} --data=%{SOURCE0} --signature=%{SOURCE1} --keyring=%{SOURCE2}

%autosetup -c

# We'll ship the README as %%doc
mv data/elldata/README .

%build
# Pari can read compressed data files, so save space
parallel %{?_smp_mflags} --no-notice gzip --best ::: data/elldata/ell*

%install
mkdir -p %{buildroot}%{_datadir}/pari/
cp -a data/elldata %{buildroot}%{_datadir}/pari/
%{_fixperms} -c %{buildroot}%{_datadir}/pari/

%files
%doc README
%{_datadir}/pari/

%changelog
%autochangelog
