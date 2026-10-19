%global source0_hash f9b10df2679f8a2b1993436c6e32164b08c8543c9a653a66a8bcbdb8f6eac915
%define		__default_patch_fuzz	2
%define		with_system_ca_cert_file	1
%define		with_external_onig		1
%define		system_ca_cert_file		%{_sysconfdir}/pki/tls/cert.pem
%define		help_url			file://%{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}}/doc/index.html
%define		main_ver	0.6.0.1
%define		codate		20100817
%define		cotime_JST	0000
%define		strtag		cvs%{codate}T%{cotime_JST}
%define		repoid		36733
%define		baserelease	22
%define		pre_release	1
%if %{pre_release}
%define		rel		0.%{baserelease}.%{strtag}%{?dist}
%else
%define		rel		%{baserelease}%{?dist}
%endif
Summary:        A GTK+ 2ch.net BBS Browser
Name:		ochusha
Version:	%{main_ver}
Release:        1%{?dist}
URL:		http://ochusha.sourceforge.jp/
%if %{pre_release}
Source0:        %{name}-%{version}-%{strtag}.tar.bz%{__default_patch_fuzz}
%else
%endif
Source10:	ochusha-prefs-gtkrc
Source11:	ochusha.sh
Patch0:		ochusha-D20100214-gtk-deprecated.patch
Patch1:		ochusha-D20100817-format-string.patch
Patch2:		ochusha-D20100817-cpp20-equality-overload.patch
License:	LicenseRef-Callaway-BSD
Requires:	mona-fonts-VLGothic
Requires:	xdg-utils
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gtk2-devel
BuildRequires:  libSM-devel
BuildRequires:  libXt-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  oniguruma-devel
BuildRequires:  openssl-devel
BuildRequires:  sqlite-devel
# /oreon:deps
%description
The ochusha is BBS, especially 2ch.net, browser with GUI.
It uses the GTK+ toolkit for all of its interface needs.
The ochusha offers a sort of features such as multi-level
popup view of `response's, embeded and popup view of
images that helps users to interact with BBSs.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if %{pre_release}
%setup -q -n %{name}-%{main_ver}-%{strtag}
%else
%setup -q
%endif
#%%patch0 -p0 -b .gtk
%patch -P1 -p1 -b .format
%patch -P2 -p1 -b .cpp20

# Icon path fix
%{__sed} -i -e 's|Icon.*$|Icon=ochusha48|' ochusha/ochusha.desktop.in

# set xdg-open as a default browser
%{__sed} -i -e 's|firefox|xdg-open|' ochusha/ui_constants.h

# Umm...
%{__sed} -i.depre -e 's|GTK_EXTRA_CFLAGS=.*|GTK_EXTRA_CFLAGS=""|' configure.ac
%{__sed} -i.depre \
	-e 's|-D[^ ][^ ]*DEPRECATED||g' \
	libochushagtk_lgpl/Makefile.am

# Support autoconf 2.7x
%if %{pre_release}
%{__sed} -i.autoconf \
	-e 's@2.6\[0-9\]@2.[67][0-9]@' \
	autogen.sh
%endif

%if %{pre_release}
sh autogen.sh
%endif

%build

export LDFLAGS="-Wl,--rpath,%{_libdir}/%{name}"
%configure \
%if %{with_external_onig}
	--with-external-oniguruma \
%endif
%if %{with_system_ca_cert_file}
	--with-ca-cert-file=%{system_ca_cert_file} \
%endif
	--with-help-url=%{help_url} \
	--bindir=%{_libexecdir} \
	--libdir=%{_libdir}/%{name}
%{__make} %{?_smp_flags} -k
%install
%{__rm} -rf %{buildroot}
%{__rm} -rf DOCs/
%{__make} \
	DESTDIR=%{buildroot} \
	INSTALL="%{__install} -p" \
	install
%find_lang %{name}
%find_lang %{name}-properties
%{__cat} %{name}.lang %{name}-properties.lang > all.lang
%{__mkdir} DOCs/
%if ! %{with_external_onig}
%{__mkdir_p} DOCs/oniguruma
%{__cp} -p DOCs/oniguruma/COPYING DOCs/oniguruma/
%endif
%{__mkdir_p} DOCs/libochushagtk_lgpl
%{__cp} -p libochushagtk_lgpl/COPYING DOCs/libochushagtk_lgpl/
%{__rm} -f %{buildroot}/%{_libdir}/%{name}/*.{a,la,so}
%if %{with_system_ca_cert_file}
%{__rm} -f %{buildroot}/%{_datadir}/%{name}/ca-bundle.crt
%endif
pushd %{buildroot}/%{_datadir}/%{name}
rm -f *.{gif,html} \
	ochusha-* \
	ochusha.png \
	[a-np-z]*.png
popd
%{__mkdir_p} %{buildroot}%{_bindir}
%{__install} -cpm 0755 %{SOURCE11} \
	%{buildroot}%{_bindir}/%{name}
%{__install} -cpm 0644 %{SOURCE10} \
	%{buildroot}%{_datadir}/%{name}/ochusha-prefs-gtkrc
%{__mkdir_p} %{buildroot}%{_datadir}/applications
desktop-file-install \
	--delete-original \
	--remove-category Application \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/ochusha/%{name}.desktop
%{__mkdir_p} %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/
%{__ln_s} -f ../../../../ochusha/ochusha48.png \
	%{buildroot}%{_datadir}/icons/hicolor/48x48/apps/
change_encoding(){
CODE=$1
shift
for f in $*
do
	%{__mv} ${f} ${f}.tmp
	iconv -f $CODE -t UTF-8 ${f}.tmp > ${f} && 
		( touch -r ${f}.tmp $f ; %{__rm} -f ${f}.tmp ) || \
		%{__mv} ${f}.tmp ${f}
done
}
change_encoding \
	EUCJP \
	BUGS ChangeLog NEWS README TODO \
	ochusha/ochusha-gtkrc.gray
%{__mkdir_p} DOCs/ochusha
%{__cp} -a doc/ DOCs/
%{__rm} -rf DOCs/doc/Makefile* DOCs/doc/*.in DOCs/doc/CVS/
%{__cp} -p ochusha/ochusha-* DOCs/ochusha/
%{__rm} -f DOCs/ochusha/ochusha-*.h
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
