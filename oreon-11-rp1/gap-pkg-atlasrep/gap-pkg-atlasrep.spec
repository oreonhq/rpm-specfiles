%global source1_hash 9f82d01bb682f24406f07a701dc2cae40dcba672c6ca91e77613b9096d6b49eb
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%global source0_hash 0f9cd6cffacd23d0131f7df31b0d3b330b9af310b77dc953a17a635b655db1ec
%bcond bootstrap 0
%global gap_pkgname atlasrep
%global gap_makedoc makedocrel.g
Name:           gap-pkg-%{gap_pkgname}
Version:        2.1.12
Release:        1%{?dist}
Summary:        GAP interface to the Atlas of Group Representations
License:        GPL-3.0-or-later
URL:            https://www.math.rwth-aachen.de/~Thomas.Breuer/atlasrep/
Source0:        https://www.math.rwth-aachen.de/~Thomas.Breuer/%{gap_pkgname}//%{gap_pkgname}-%{version}.tar.gz
Source1:        %{url}/%{gap_upname}data.tar.gz
Source2:        %{name}-testdata.tar.xz
Patch:          %{name}-makedocrel.patch
BuildArch:      noarch
BuildSystem:    gap
BuildOption(build): --packagedirs ..
BuildOption(install): *.json bibl dataext datagens datapkg dataword gap tst
BuildOption(check): tst/testall.g
%if %{without bootstrap}
%endif
Requires:       coreutils
Requires:       gap-pkg-io
Requires:       gap-pkg-utils
Recommends:     gap-pkg-browse
Recommends:     gap-pkg-ctbllib
Recommends:     gap-pkg-recog
Recommends:     gap-pkg-standardff
Recommends:     gap-pkg-tomlib
# oreon:deps
BuildRequires:  GAPDoc-doc
BuildRequires:  GAPDoc-latex
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-browse-doc
BuildRequires:  gap-pkg-ctbllib-doc
BuildRequires:  gap-pkg-standardff-doc
BuildRequires:  gap-pkg-tomlib
BuildRequires:  gap-pkg-utils-doc
# /oreon:deps
%description
The aim of the AtlasRep package is to provide an interface between GAP and the
Atlas of Group Representations, a database that comprises representations of
many almost simple groups and information about their maximal subgroups.  This
database is available independent of GAP.

The AtlasRep package consists of this database and a GAP interface.  The
latter allows the user to get an overview of the database, and to access the
data in GAP format.

%package doc
License:        GPL-3.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        AtlasRep documentation
Requires:       %{name} = %{version}-%{release}
Requires:       GAPDoc-doc
Requires:       gap-pkg-browse-doc
%if %{without bootstrap}
Requires:       gap-pkg-ctbllib-doc
Requires:       gap-pkg-standardff-doc
%endif
Requires:       gap-pkg-utils-doc
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version} -p1

%conf
tar -x --strip-components=1 -f %{SOURCE1}
rm {dataext,datagens,dataword}/dummy
rm -fr dataword/{.cvsignore,CVS}

# Fix permissions
chmod a-x doc/*.xml

%build -a

tar -x --strip-components=1 -f %{SOURCE0} \
    %{gap_upname}-%{version}/makedocrel.g
sed -i "s,$PWD/doc/\.\./\.\./pkg,../..,g" doc/*.html
%check

%if %{without bootstrap}
tar -xf %{SOURCE2}
mkdir ~/.gap
cat > ~/.gap/gap.ini << EOF
SetUserPreference( "AtlasRep", "AtlasRepDataDirectory", "$PWD/" );
EOF
gap --packagedirs .. tst/testall.g
%endif
%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-atlasrep-doc -f %{oreon_filedir}/gap-pkg-atlasrep-doc.list

%changelog

%autochangelog
