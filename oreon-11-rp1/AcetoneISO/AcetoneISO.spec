%global source0_hash 82a1e0d13a6b48f7a1f9878a528ea4320792b8c77463e8d80c42e67eafe8cd9d

Name:		AcetoneISO
Version:	6.7
Release:	44%{?dist}
Summary:	CD/DVD Image Manipulator
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://www.acetoneteam.org/
#Source0:	http://www.acetoneteam.org/Archivia/%{name}-%{version}.tar.gz
# Upstream source includes poweriso binary, closed source, no redistribution permission.
Source0:	%{name}-%{version}-clean.tar.gz
Patch0:		AcetoneISO-6.7-welcome-to-2017.patch
BuildRequires:  gcc
BuildRequires: 	kdewebdev-devel, desktop-file-utils
Requires:	p7zip, xbiso, k3b, kde-runtime, arts, cdrdao, nrg2iso
# There is no konqueror for ppc/ppc64. - 2017-06-15
# Or s390x. - 2017-09-05
ExcludeArch:	ppc %{power64} s390x
# Overkill, but I'm being thorough
Requires:	util-linux, coreutils, kdewebdev
Requires:       kdialog, konsole, kdesu, konqueror

%description
AcetoneISO: The CD/DVD image manipulator for Linux, it can do the following:
- Mount and Unmount ISO, MDF, NRG (if iso-9660 standard)
- Convert / Extract / Browse to ISO : *.bin *.mdf *.nrg *.img *.daa *.cdi 
  *.xbx *.b5i *.bwi *.pdi
- Play a DVD Movie ISO with most used media players
- Generate an ISO from a Folder or CD/DVD
- Generate MD5 file of an image
- Encrypt an image
- Split image into X megabyte chunks
- Highly compress an image
- Rip a PSX cd to *.bin to make it work with epsxe/psx emulators
- Service-Menu support for Konqueror
- Restore a lost CUE file of *.bin *.img

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .fixup

%build
cd src/
chmod -x *.c
mkdir ../binaries
# xbiso is in its own package
# so is nrg2iso.
for i in b5i2iso.c cdi2iso.c mdf2iso.c pdi2iso.c; do
  SHORTNAME=`echo $i | sed 's/.c//'`
  gcc $RPM_OPT_FLAGS $i -o ../binaries/$SHORTNAME
done

%install
rm -rf $RPM_BUILD_ROOT 
mkdir $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -p binaries/* $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/apps/%{name}/scripts/
sed -i 's|/opt/acetoneiso/|/usr/|g' %{name}-%{version}/AcetoneISO.kmdr
chmod -x %{name}-%{version}/AcetoneISO.kmdr
install -p %{name}-%{version}/AcetoneISO.kmdr $RPM_BUILD_ROOT%{_datadir}/apps/%{name}/scripts
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -p %{name}-%{version}/*.png $RPM_BUILD_ROOT%{_datadir}/pixmaps
mkdir -p $RPM_BUILD_ROOT%{_sbindir}
sed -i 's|/opt/acetoneiso/.|%{_sbindir}|g' %{name}-%{version}/acetoneiso-*mount.desktop
chmod -x %{name}-%{version}/acetoneiso-*mount.desktop
install -p %{name}-%{version}/*.sh $RPM_BUILD_ROOT%{_sbindir}

sed -i 's|/opt/acetoneiso/|%{_datadir}/apps/%{name}/scripts/|g' %{name}-%{version}/acetoneiso
install -p %{name}-%{version}/acetoneiso $RPM_BUILD_ROOT%{_bindir}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/apps/konqueror/servicemenus/
install -p %{name}-%{version}/acetoneiso-*mount.desktop $RPM_BUILD_ROOT%{_datadir}/apps/konqueror/servicemenus/

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
mv %{name}-%{version}/AcetoneISO %{name}-%{version}/AcetoneISO.desktop
sed -i 's|/opt/acetoneiso/|%{_datadir}/apps/%{name}/scripts/|g' %{name}-%{version}/AcetoneISO.desktop
sed -i "s|'/usr/share/apps/AcetoneISO/scripts/AcetoneISO.kmdr'|/usr/share/apps/AcetoneISO/scripts/AcetoneISO.kmdr|g" %{name}-%{version}/AcetoneISO.desktop
desktop-file-install --vendor ""			\
	--dir $RPM_BUILD_ROOT%{_datadir}/applications	\
	--add-category System				\
	%{name}-%{version}/AcetoneISO.desktop

%files
%doc GPL README changelog
%{_bindir}/acetoneiso
%{_bindir}/b5i2iso
%{_bindir}/cdi2iso
%{_bindir}/mdf2iso
%{_bindir}/pdi2iso
%{_sbindir}/playiso-unmount.sh
%{_sbindir}/turbo.sh
%{_datadir}/applications/*.desktop
%{_datadir}/apps/%{name}/
%{_datadir}/apps/konqueror/servicemenus/acetoneiso-*.desktop
%{_datadir}/pixmaps/*.png

%changelog
%autochangelog
