%global source0_hash f201e9da571c681a7bbfb1e4683bdb2c80a23b005099ed0453521f59cb443434
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%bcond bootstrap 0
%global gap_pkgname   ctbllib
%global gap_skip_docs 1
Name:           gap-pkg-%{gap_pkgname}
Version:        1.3.11
Release:        1%{?dist}
Summary:        GAP Character Table Library
License:        GPL-3.0-or-later
URL:            https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/
Source0:        https://www.math.rwth-aachen.de/~Thomas.Breuer/%{gap_pkgname}/%{gap_pkgname}-%{version}.tar.gz
Source1:        %{name}-testdata.tar.xz
Patch:          %{name}-makedocrel.patch
BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): data dlnames gap4 htm tst
%if %{without bootstrap}
%endif
Requires:       gap-pkg-atlasrep
Recommends:     gap-pkg-browse
Recommends:     gap-pkg-primgrp
Recommends:     gap-pkg-smallgrp
Recommends:     gap-pkg-spinsym
Recommends:     gap-pkg-tomlib
Recommends:     gap-pkg-transgrp
# oreon:deps
BuildRequires:  GAPDoc-latex
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-atlasrep-doc
BuildRequires:  gap-pkg-browse-doc
BuildRequires:  gap-pkg-cohomolo
BuildRequires:  gap-pkg-grpconst
BuildRequires:  gap-pkg-smallgrp-doc
BuildRequires:  gap-pkg-spinsym
BuildRequires:  gap-pkg-tomlib-doc
BuildRequires:  netpbm-progs
BuildRequires:  parallel
BuildRequires:  tex(epic.sty)
# /oreon:deps
%description
This package provides the Character Table Library by Thomas Breuer.

%package doc
License:        GPL-3.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND LPPL-1.3a AND AGPL-3.0-only AND LicenseRef-Rsfs
Summary:        Character Table Library documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-pkg-atlasrep-doc
Requires:       gap-pkg-browse-doc
Requires:       gap-pkg-smallgrp-doc
Requires:       gap-pkg-tomlib-doc
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version} -b1 -p1

%conf
# Remove spurious executable bit
chmod a-x doc/utils.xml

%build

parallel %{?_smp_mflags} --no-notice gzip --best ::: data/*.tbl
%install -a
cp -a doc doc2 %{buildroot}%{gap_libdir}/pkg/%{gap_upname}
gap -l '%{buildroot}%{gap_libdir};' makedocrel.g
rm -fr doc doc2
mv %{buildroot}%{gap_libdir}/pkg/%{gap_upname}/doc{,2} .
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{gap_upname}/doc{,2}
%gap_copy_docs
%gap_copy_docs -d doc2
tar -x --strip-components=1 -f %{SOURCE0} \
    -C %{buildroot}%{gap_libdir}/pkg/%{gap_upname} \
    %{gap_upname}-%{version}/makedocrel.g
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

mkdir ~/.gap
cat > ~/.gap/gap.ini << EOF
SetUserPreference( "AtlasRep", "AtlasRepDataDirectory", "%{_builddir}/atlasrep/" );
EOF
gap -l '%{buildroot}%{gap_libdir};' << EOF
ReadPackage( "ctbllib", "tst/testinst.g" );
EOF
%if %{without bootstrap}
sed -i '/BrowseCTblLibInfo();/d' gap4/ctbltocb.g tst/docxpl.tst
gap --packagedirs .. tst/testauto.g
%endif
%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-ctbllib-doc -f %{oreon_filedir}/gap-pkg-ctbllib-doc.list

%changelog

%autochangelog
