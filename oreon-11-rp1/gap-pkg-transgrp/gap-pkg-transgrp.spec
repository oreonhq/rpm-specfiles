%global source0_hash 6f2ec142a004f9d5e3b28bfa03246472fee93ceb12837206960bcb560eb72376
%global gap_pkgname transgrp
Name:           gap-pkg-%{gap_pkgname}
Version:        3.6.5
Release:        1%{?dist}
Summary:        Transitive groups library
License:        GPL-2.0-only OR GPL-3.0-only
URL:            https://www.gap-system.org/Packages/transgrp.html
VCS:            git:https://github.com/hulpke/transgrp.git
Source0:        https://www.math.colostate.edu/~hulpke/%{gap_pkgname}/%{gap_pkgname}%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): data htm lib tst
BuildOption(check): --bare -c 'LoadPackage("GAPDoc");LoadPackage("smallgrp");' tst/testall.g
Requires:       gap-core
Requires:       %{name}-data = %{version}-%{release}
# oreon:deps
BuildRequires:  GAPDoc-latex
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-smallgrp
BuildRequires:  tth
# /oreon:deps
%description
A library of transitive groups.  This package contains the code for
accessing the library.  The actual data is in the data subpackage.

%package data
Summary:        Data files for groups of degree other than 32 and 48
License:        Artistic-2.0
Requires:       %{name} = %{version}-%{release}
Obsoletes:      %{name}-data32 < 3.6.5-11
%description data
This package contains a library of transitive groups.  Groups of degree 15-30
are due to Alexander Hulpke.  Groups of degree 32 are due to John Cannon and
Derek Holt.  Groups of degree 34-48 are due to Derek Holt and Gordon Royle.
Not all degrees greater than 30 are yet available.

Groups of degree 32 are not included in Fedora due to the large size of the
file (about 266 MB).  Download it separately from
https://www.math.colostate.edu/~hulpke/transgrp/trans32.tgz if you need it.

Groups of degree 48 are not included in Fedora due to the large size of the
file (about 30 GB).  Download it separately from
https://zenodo.org/record/5935751 if you need it.

%package doc
License:        (GPL-2.0-only OR GPL-3.0-only) AND OFL-1.1-RFN AND Knuth-CTAN AND AGPL-3.0-only
Summary:        Transitive groups library documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

%autosetup -n %{gap_upname}

%conf
# There is no ext manual anymore
sed -i '/UseReferences.*ext/d' doc/manual.tex

%build

mkdir ../../doc
ln -s %{gap_libdir}/doc/ref ../../doc
cd doc
ln -s %{gap_libdir}/etc/convert.pl .
ln -s %{gap_libdir}/doc/gapmacro.tex .
ln -s %{gap_libdir}/doc/manualindex .
./make_doc
cd -
rm -fr ../../doc doc/{convert.pl,gapmacro.tex,manualindex}
%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-transgrp-data -f %{oreon_filedir}/gap-pkg-transgrp-data.list
%files -n gap-pkg-transgrp-doc -f %{oreon_filedir}/gap-pkg-transgrp-doc.list

%changelog

%autochangelog
