%global source0_hash 24b7e613de3ee79aafddeb130240d859cfa7fe179a4fcb86f5b16d146a76e85f

%global		mainver	2.5.2
%global 		tarver		%(echo %mainver | sed -e 's|\\.||g')
%global 		snap_digit		20220518
%global		snap_german	18Mai2022

Name:		gabedit
Summary:	GUI for computational chemistry
Version:	%{mainver}
Release:	0.13%{?snap_digit:_snap%{snap_digit}}%{?dist}
URL:		http://gabedit.sourceforge.net/home.html
License:	MIT

Source0:	https://sites.google.com/site/allouchear/Home/gabedit/download/GabeditSrc%{tarver}%{?snap_german:_%{snap_german}}.tar.gz
#Source0:	https://downloads.sourceforge.net/%{name}/GabeditSrc%{tarver}.tar.gz
# fix csh shebang
Patch2:	%{name}-csh.patch
# fix bug #774594 and other crashes
Patch4:	%{name}-strlen.patch
# Fix compilation error with -Werror=implicit-function-declaration
Patch5:	%{name}-2.5.1-function-prototype-typo.patch
# Fix -Werror=array-bounds
Patch6:	%{name}-2.5.1-array-bounds.patch
# Remove apparent memory leak detected by -Wunused-variable
Patch7:	%{name}-2.5.1-apparent-leak.patch
# C23: avoid bool keyword usage
Patch8:	%{name}-2.5.1-c23-bool-keyword.patch
# C23: support strict function prototype
Patch9:	%{name}-2.5.1-c23-function-proto.patch
# show_homepage: use xdg-open
Patch10:	%{name}-2.5.1-show_homepage-use-xdg-open.patch

BuildRequires: 	gcc
BuildRequires:	make
BuildRequires:	desktop-file-utils

BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtkglext-1.0)
BuildRequires:	gl2ps-devel

Requires:			hicolor-icon-theme

%description
Gabedit is a Graphical User Interface to Gamess-US, Gaussian, Molcas,
Molpro and MPQC computational chemistry packages. Gabedit includes
graphical facilities for generating keywords and options, molecule
specifications and their input sections for even the most advanced
calculation types. Gabedit includes an advanced Molecule Builder. You
can use it to rapidly sketch in molecules and examine them in three
dimensions. You can build molecules by atom, ring, group, amino acid and
nucleoside. You can also read geometry from a file. Most major molecular
file formats are supported.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n GabeditSrc%{tarver}%{?snap_german:_%{snap_german}}
%patch -P2 -p1
%patch -P4 -p1 -b .strlen
%patch -P5 -p1 -b .implicit
%patch -P6 -p1 -b .bounds
%patch -P7 -p1 -b .leak
%patch -P8 -p1 -b .bool
%patch -P9 -p1 -b .c23
%patch -P10 -p1 -b .xdg

# package_notes needs buildsubdir to be defined
%if "x%{?buildsubdir}" == "x"
%global buildsubdir GabeditSrc%{tarver}%{?snap_german:_%{snap_german}}
%endif

# remove Win32-specific files
rm -rf \
	utils/InnosSetupScriptWin32 \
	utils/Others/gabedit64.bat \
	%{nil}

echo "external_gtkglarea=1" >> CONFIG
echo "external_gl2ps=1" >> CONFIG

sed -i.link CONFIG \
	-e 's@/usr/lib@%{_libdir}@g' \
	%{nil}

pushd utils/Others
	sed -i.dos -e 's@\r@@g' isotopNIST.txt
	touch -r isotopNIST.txt{.dos,}
	rm isotopNIST.txt.dos
popd

sed -i.cflags CONFIG \
	-e '\@COMMONCFLAGS@s|-Wall -O2 |%{build_cflags} -Werror=implicit-function-declaration -Werror=array-bounds |' \
	-e '\@COMMONCFLAGS@s|-Wno-unused-variable||' \
	-e 's|-fno-common||' \
	%{nil}

echo -e "LDFLAGS\t= %{build_cflags} %{build_ldflags}" >> CONFIG

# Kill huge useless warnings
grep -rl G_CONST_RETURN . | xargs sed -i  -e 's|G_CONST_RETURN|const|g'

%build
# Revoke %%set_build_flags
unset CFLAGS
unset LDFLAGS
make %{?_smp_mflags} -k

%install
install -d %{buildroot}/%{_bindir}
install -cp -m755 %{name} %{buildroot}/%{_bindir}

install -d %{buildroot}%{_datadir}/applications
desktop-file-install \
	--dir=%{buildroot}%{_datadir}/applications \
	utils/Others/gabedit.desktop

for size in 16 24 32 48 ; do
	install -d %{buildroot}/%{_datadir}/icons/hicolor/${size}x${size}/apps
	install -cp -m644 icons/Gabedit${size}.png \
		%{buildroot}/%{_datadir}/icons/hicolor/${size}x${size}/apps/%{name}.png
done

%files
%license	License
%doc	ChangeLog
%doc	utils
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*.png

%changelog
%autochangelog
