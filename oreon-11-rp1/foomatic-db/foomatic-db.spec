%global source0_hash none

%global dbver_rel 4.0
# When you change dbver_snap, rebuild also foomatic against this build to pick up new IEEE 1284 Device IDs.
# The postscriptdriver tags get put onto foomatic, because that's there the actual CUPS driver lives.
%global dbver_snap 20260531

Summary: Database of printers and printer drivers
Name: foomatic-db
Version: %{dbver_rel}
Release: 83.%{dbver_snap}%{?dist}
# GPL-2.0-or-later non-PPD files and some PPDs
# MIT for ppds
License: GPL-2.0-or-later AND MIT
Requires: %{name}-filesystem = %{version}-%{release}
Requires: %{name}-ppds = %{version}-%{release}

Source0:        https://github.com/OpenPrinting/foomatic-db/archive/refs/heads/master.tar.gz#/foomatic-db-%{dbver_rel}-%{dbver_snap}.tar.gz

Patch1:        foomatic-db-device-ids.patch
Patch2:        foomatic-db-invalid.patch

Url: http://www.openprinting.org
BuildArch: noarch

# Make sure we get postscriptdriver tags.
BuildRequires: python3-cups

# Build requires cups so that configure knows where to put PPDs.
BuildRequires: cups
# uses make
BuildRequires: make

# Build requires for perl
BuildRequires: perl-interpreter

# we needed sed for prep phase - removing perl from ppds
BuildRequires: sed

%description
This is the database of printers, printer drivers, and driver options
for Foomatic.

The site https://www.openprinting.org/ is based on this database.

%package filesystem
Summary: Directory layout for the foomatic package

%description filesystem
Directory layout for the foomatic package.

%package ppds
Summary: PPDs from printer manufacturers
# We ship a symlink in a directory owned by cups
BuildRequires: cups
Requires: cups
Requires: sed
Requires: %{name}-filesystem = %{version}-%{release}

%description ppds
PPDs from printer manufacturers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n foomatic-db-master

find -type d | xargs -d '\n' chmod g-s

pushd db/source

# For gutenprint printers, use gutenprint-ijs-simplified.5.2.
for i in printer/*.xml
do
  perl -pi -e 's,>gutenprint<,>gutenprint-ijs-simplified.5.2<,' $i
done

# Remove references to SpliX (Samsung/Xerox/Dell)
find printer -name '*.xml' |xargs -d '\n' grep -l "<driver>splix"|xargs -d '\n' rm -vf
rm -f driver/splix.xml

# Remove references to foo2zjs, foo2oak, foo2hp and foo2qpdl (bug #208851).
# foo2zjs-z1, foo2zjs-z2, foo2zjs-z3 (bug #967930)
# foo2lava, foo2kyo, foo2xqx (bug #438319)
# foo2slx and foo2hiperc (bug #518267)
# foo2hbpl2 (bug #970393)
# foo2hiperc-z1
for x in zjs zjs-z1 zjs-z2 zjs-z3 oak oak-z1 hp qpdl lava kyo xqx slx hiperc hiperc-z1 hbpl2
do
  find printer -name '*.xml' |xargs -d '\n' grep -l "<driver>foo2${x}"|xargs -d '\n' rm -vf
  rm -f driver/foo2${x}.xml opt/foo2${x}-*
done

# Binaries for these were previously provided by printer-filters, but aren't anymore (bug #972740)
for x in lm1100 pentaxpj pbm2l2030 pbm2l7k lex5700 lex7000 c2050 c2070 cjet
do
  find printer -name '*.xml' |xargs -d '\n' grep -l "<driver>${x}</driver>"|xargs -d '\n' rm -vf
  rm -vf driver/${x}.xml opt/${x}-*
done

# Same for all these.
for x in drv_x125 ml85p pbm2lwxl pbmtozjs bjc800j m2300w m2400w
do
  find printer -name '*.xml' |xargs -d '\n' grep -l "<driver>${x}</driver>"|xargs -d '\n' rm -vf
  rm -vf driver/${x}.xml opt/${x}-*
done

# Remove Samsung-CLP-610/620 (bug #967930), they're in foo2qpdl
find printer -name '*.xml' |grep -E 'Samsung-CLP-610|Samsung-CLP-620'|xargs -d '\n' rm -vf

# This one is part of foo2zjs
find printer -name '*.xml' |grep -E 'KONICA_MINOLTA-magicolor_2430_DL'|xargs -d '\n' rm -vf

# Remove Brother P-touch (bug #560610, comment #10)
rm -vf driver/ptouch.xml
rm -vf printer/Brother-PT-*.xml
rm -vf printer/Brother-QL-*.xml
rm -vf opt/Brother-Ptouch-*.xml

popd

# foomatic-db patches
# Don't use "-b" when patching PPD files as the backups will be packaged.

# Device IDs for:
# Brother MFC-8840D (#678065)
# HP LaserJet M1522nf MFP (#745499)
# Lexmark C453 (#770169)
# HP DeskJet 720C (bug #797099)
# Kyocera FS-1118MFP (bug #782377)
# Brother HL-2040 (bug #999040)
%patch -P 1 -p1

# These can't be generated at all (bug #866476)
%patch -P 2 -p1

# Use sed instead of perl in the PPDs (bug #512739).
find db/source/PPD -type f -name '*.ppd' -exec sed -i 's,perl -p,sed,g' {} +

%build
%configure
make PREFIX=%{_prefix}


%install
make	DESTDIR=%buildroot PREFIX=%{_prefix} \
	install

# Remove ghostscript UPP drivers that are gone in 7.07
rm -f %{buildroot}%{_datadir}/foomatic/db/source/driver/{bjc6000a1,PM760p,PM820p,s400a1,sharp,Stc670pl,Stc670p,Stc680p,Stc760p,Stc777p,Stp720p,Stp870p}.upp.xml

find %{buildroot}%{_datadir}/foomatic/db/source/ -type f | xargs -d '\n' chmod 0644

mkdir %{buildroot}%{_datadir}/foomatic/db/source/PPD/Custom

rm -f	%{buildroot}%{_datadir}/foomatic/db/source/PPD/Kyocera/*.htm \
	%{buildroot}%{_datadir}/cups/model/3-distribution

# Convert absolute symlink to relative.
rm -f %{buildroot}%{_datadir}/cups/model/foomatic-db-ppds
ln -sf ../../foomatic/db/source/PPD %{buildroot}%{_datadir}/cups/model/foomatic-db-ppds

%files filesystem
%dir %{_datadir}/foomatic/
%dir %{_datadir}/foomatic/db/
%dir %{_datadir}/foomatic/db/source/
%dir %{_datadir}/foomatic/db/source/driver/
%dir %{_datadir}/foomatic/db/source/opt/
%dir %{_datadir}/foomatic/db/source/printer/
%dir %{_datadir}/foomatic/db/source/PPD/

%files
%doc db/source/PPD/Kyocera/*.htm
%doc README
%{_datadir}/foomatic/db/oldprinterids
%{_datadir}/foomatic/db/source/printer/*
%{_datadir}/foomatic/db/source/driver/*
%{_datadir}/foomatic/db/source/opt/*
%{_datadir}/foomatic/xmlschema

%files ppds
%doc COPYING
%{_datadir}/foomatic/db/source/PPD/*
%{_datadir}/cups/model/foomatic-db-ppds

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.0-83.20230810
- Import
