%global source1_hash a103391a26fce760e4ec13e9de70ee1501ad97fa79bba77755aa2b3673b36830
%global source0_hash dd551e64932d4ab27b3f2b2d1da871c2353672fc1a74705c52e3c0de84bd0cf6
Name:		pari-elldata
Version:	20210301
Release:        13%{?dist}
Summary:        PARI/GP Computer Algebra System elliptic curves
License:	GPL-2.0-or-later
URL:		https://pari.math.u-bordeaux.fr/packages.html
Source0:        https://pari.math.u-bordeaux.fr/pub/pari/packages/elldata.tgz
Source1:	https://pari.math.u-bordeaux.fr/pub/pari/packages/elldata.tgz.asc
Source2:	gpgkey-42028EA404A2E9D80AC453148F0E7C2B4522E387.gpg
BuildArch:	noarch
# oreon:deps
BuildRequires:  gpgverify
BuildRequires:  parallel
# /oreon:deps
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

parallel %{?_smp_mflags} --no-notice gzip --best ::: data/elldata/ell*
%install
mkdir -p %{buildroot}%{_datadir}/pari/
cp -a data/elldata %{buildroot}%{_datadir}/pari/
%{_fixperms} -c %{buildroot}%{_datadir}/pari/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
