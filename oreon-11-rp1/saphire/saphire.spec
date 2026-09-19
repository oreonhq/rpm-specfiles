%global source0_hash 5dcd0ea3828a375004be7545a76b319713c6a17dcbc34189fb044ce63279d087

%global	repoid		54458
%undefine	_docdir_fmt

Name:		saphire
Version:	3.6.5
Release:	37%{?dist}
Summary:	Yet another shell

# SPDX confirmed
License:	MIT
URL:		http://ab25cq.wiki.fc2.com/
Source0:	http://dl.sourceforge.jp/sash/%{repoid}/saphire-%{version}.tgz
Patch0:	saphire-3.6.5-gcc10-fno-common.patch
Patch1:	saphire-3.6.5-c99-port.patch
Patch2:	saphire-string_chomp-public.patch
Patch3:	saphire-3.6.5-c23.patch

BuildRequires:	make
BuildRequires:  gcc
BuildRequires:	cmigemo-devel
BuildRequires:	gc-devel
BuildRequires:	ncurses-devel
BuildRequires:	oniguruma-devel
#BuildRequires:	pcre-devel
BuildRequires:	readline-devel

%description
Yet another shell

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
# Patches
%patch -P0 -p1 -b .gcc10
%patch -P1 -p1 -b .c99
%patch -P2 -p1 -b .string_chomp
%patch -P3 -p1 -b .c23

# Don't strip binary
sed -i.strip -e 's|\$(INSTALL) -s|\$(INSTALL) |' Makefile.in
# cp -> ln for library
sed -i.ln -e '/libsaphire.so/s|cp |ln -s -f |' Makefile.in
# Add current directory to library search path
sed -i.libpath -e '/^LIBS[2]*=/s|^\(.*\)$|\1 -L.|' Makefile.in
# Don't do lib-install for all
sed -i.all -e '/^all:/s|lib-install||' Makefile.in
# Keep timestamp
sed -i.stamp \
	-e 's| -m 755| -p -m 0755|g' \
	-e 's| -m 644| -p -m 0644|g' \
	Makefile.in
# Umm...
sed -i.soname \
	-e '/[ \t]/s|\( -o libsaphire.so.2.0.0 \)| -Wl,-soname,libsaphire.so.2 \1|' \
	Makefile.in

# FIX CRLF
for file in \
	CHANGELOG.txt \
	README*.txt \
	USAGE.*.txt
do
	sed -i.dos -e 's|\r||' $file
	touch -r $file{.dos,}
	rm $file.dos
done

# Some encodings or so fixes
pushd headers/saphire
for f in *.h
do
	touch -r $f $f.stamp
	iconv -f EUC-JP -t UTF-8 $f > $f.utf8 && mv -f $f.utf8 $f || rm -f $f.utf8
	iconv -f SHIFT-JIS -t UTF-8 $f > $f.utf8 && mv -f $f.utf8 $f || rm -f $f.utf8
	sed -i -e 's|\r||' $f
	touch -r $f.stamp $f
	rm -f $f.stamp
done
popd

# Prefer less over lv
sed -i.pager \
	-e 's| lv| less|' \
	-e 's|lv |less |' \
	saphire.sa

%build
# Move maybe-arch-dependent file out of %%sysconfdir
# --docdir is needed
%configure \
	--with-migemo \
	--with-system-migemodir=%{_datadir}/cmigemo \
	--sysconfdir=%{_libdir}/ \
	--docdir=%{_defaultdocdir}/%{name}-%{version}

# configure overrides $CFLAGS
# Kill parallel make
# Umm... override docdir also here
make -j1 \
	CC="gcc %{optflags}" \
	docdir=%{_defaultdocdir}/%{name}-%{version} \
	-k

# Samples
rm -rf install_samples/
mkdir -p install_samples/samples
cp -p samples/*sa install_samples/samples

pushd install_samples/samples
chmod 0644 *.sa
sed -i \
	-e '\@^#!/usr.*@d' \
	-e '\@^#!/home.*@d' \
	*.sa
popd

%install
make install \
	DESTDIR=%{buildroot} \
	includedir=%{_includedir}/%{name} \
	docdir=%{_defaultdocdir}/%{name}-%{version}
	

%ldconfig_scriptlets

%files
%doc	AUTHORS
%license	LICENSE
%doc	README.en.txt
%doc	USAGE.en.txt
%doc	install_samples/samples
%lang(ja)	%doc	CHANGELOG.txt
%lang(ja)	%doc	README.ja.txt
#%%lang(ja)	%doc	TODO.ja.txt
%lang(ja)	%doc	USAGE.ja.txt

%{_bindir}/%{name}
%{_bindir}/saphiresh
%{_libdir}/lib%{name}.so.2*
%dir %{_libdir}/%{name}/
%{_libdir}/%{name}/%{name}.sa*
%{_libdir}/%{name}/completion.sa*
%{_libdir}/%{name}/shelp.sa*

%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/saphiresh.1*

%files	devel
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/lib%{name}.so

%changelog
%autochangelog
