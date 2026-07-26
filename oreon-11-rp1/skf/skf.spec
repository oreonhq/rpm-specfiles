%global source0_hash 947477575e80ead5ad50e665a3ae7ac22e591a76cb48a54b529f8813789ec00d

%if 0%{?fedora} < 19
%global	rubyabi	1.9.1
%endif

#%%define usescm 1
%undefine	usescm

%global	repoid		78199

%global	mainver	2.10.16
%global	prever	2.10.10
#%%define	betaver	-rc1
%undefine	betaver
%define	betarel	%(echo %betaver | sed -e 's|-|_|' | sed -e 's|^_||')

%global	baserelease	19

%undefine        _changelog_trimtime

Name:		skf
Version:	%{mainver}
Release:	%{?betaver:0.}%{baserelease}%{?betaver:.%betarel}%{?dist}
Summary:	Utility binary files in Simple Kanji Filter

License:	LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT AND LicenseRef-Callaway-UCD
URL:		http://osdn.jp/projects/skf
Source0:	https://ftp.iij.ad.jp/pub/osdn.jp/skf/%{repoid}/skf_%{mainver}%{?betaver}.tar.xz
Source1:	skf-basic-test.sh
Source2:	create-skf-tarball-from-scm.sh
# https://osdn.net/projects/skf/ticket/39882
Source11:	https://ymu.dl.osdn.jp/ticket/g/s/sk/skf/39882/5733/pythontest
# rubyext: remove unneeded ptr -> VALUE conversion
# ref: https://bugzilla.redhat.com/show_bug.cgi?id=2256789
Patch0:	skf-2.10.16-rubyext-ptr-conversion.patch
# rubyext: type check for argument (ref: bug 2256789)
Patch1:	skf-2.10.16-rubyext-ptr-typecheck.patch
# Support C23 strict prototype
Patch2:	skf-2.10.16-c23-function-proto.patch

# common BR
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	gettext
# For iconv for Japanese locale
BuildRequires:	glibc-all-langpacks
# BR for extenstions
BuildRequires:	swig
BuildRequires:	ruby-devel
BuildRequires:	rubygems-devel
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl(ExtUtils::Embed)
BuildRequires:	python3-devel
%if 0%{?usescm} >= 1
BuildRequires:	autoconf
%endif
# Patch0 needs autoconf anyway
BuildRequires:	autoconf

Requires:	%{name}-common = %{version}-%{release}
Obsoletes:	python2-skf < %{prever}.99
Obsoletes:	skf-python < %{prever}.99

%package	common
Summary:	Common files for Simple Kanji Filter - i18n kanji converter

%package	ruby
Summary:	Ruby extension module for %{name}
Requires:	%{name}-common = %{version}-%{release}
%if 0%{?fedora} >= 19
Requires:	ruby(release)
%else
Requires:	ruby(abi) = %{rubyabi}
%endif
Provides:	ruby(skf) = %{version}-%{release}

%package	-n python3-skf
Summary:	Python3 extension module for %{name}
Requires:	%{name}-common = %{version}-%{release}

%package	perl
Summary:	Perl extension module for %{name}
Requires:	%{name}-common = %{version}-%{release}

%description
This package contains utility binary files in skf.

%description	common
skf is an i18n-capable kanji filter. skf is designed for
reading documents in various languages and codes using kanji
or unicode capable display devices. Like other kanji filters,
skf provides basic Japanese kanji code conversion features, 
include to/from JIS, EUC, Shift-JIS, UCS2, KEIS83 and UTF-7/8,
but also support various international codesets include Korian
and Chinese standard codesets.

Unlike nkf, skf does not provide additional fancy features
like broken jis recovery, but it has support for ISO-8859's,
European domestic sets, JIS X-0212/X-0213 code conversion, 
IBM gaiji support and can add other code supports easily.

This package contains files commonly used by other skf related
packages.

%description	ruby
This package contains Ruby extension module for skf.

%description	-n python3-skf
This package contains Python3 extension module for skf.

%description	perl
This package contains Perl extension module for skf.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -T -a 0
ln -sf %{name}-* main

cp -p %SOURCE1 .

pushd main

%patch -P0 -p1 -b .rubyptr
%patch -P1 -p1 -b .rubycheck
%patch -P2 -p2 -b .c23

%if 0%{?usescm} >= 1
autoconf

mkdir -p doc || :
touch doc/empty

find . -type d -name CVS | sort -r | xargs rm -rf
%endif

## Fixing build error
# Fix pythonext build error on F-14+
sed -i -e '/python_version=.*substr/s|)-2|)-3|' configure

# Fix for ruby 3
sed -i.ruby3 skf_convert.h \
	-e 's@^#if defined.SKF_RUBY3.*$@#if 0@'
sed -i configure.ac configure \
	-e '\@^[ \t][ \t]*ruby_19_preferred="yes"@i ruby_21_preferred="yes";@' \
	-e '\@^RUBY=.*false@d' \
	%{nil}

# Support ruby4
sed -i.ruby4 \
	skf_convert.i config.h.in \
	-e 's@|| defined(SKF_RUBY3)@|| defined(SKF_RUBY3) || defined(SKF_RUBY4)@' \
	%{nil}

## configure option, etc
# change optflags, don't strip
# believe upstream
#sed -i.flags -e 's|-Wno-format-security||' configure

## directory change
# change the directory where tables are to be installed
sed -i.table -e "s|^lskfdir=.*$|lskfdir='%{_libdir}/%{name}'|" configure

## documents
# EUC-JP related
sed -i.eucjp -e '/JOMANDIR/d' Makefile.in
popd # from main

# Okay, duplicate main directory
for ext in \
	python3 \
	ruby perl
do
	mkdir -p $ext
	cp -pr main/* $ext
done

# change optflags
# add -fno-strict-aliasing
%global	optflags_old	%optflags
%global	optflags	%optflags_old -fno-strict-aliasing

%build
# Parallel make all unsafe

OPTS=""
OPTS="$OPTS --enable-debug"
OPTS="$OPTS --disable-strip"

OPTS="$OPTS --with-ruby_sitearch_dir=%{ruby_vendorarchdir}"
PYTHON3OPTS="$OPTS --enable-python3 --with-python_sitearch_dir=%{python3_sitearch}"

# Workaround for ruby 3
export RUBY=ruby

# A. main
pushd main
%configure $OPTS
make -j1
popd

# B. extensions
for ext in \
	ruby perl \
	%{nil}
do
	pushd $ext

    if [ $ext == ruby ] ; then
        export CFLAGS="%optflags $(pkg-config --cflags ruby)"
    fi

	%configure $OPTS
	unset CFLAGS
	make -j1 ${ext}ext

	# Check if tables generated in each extension are
	# the same as in main
	shopt -s nullglob
	pushd table
	for f in *stb
	do
		cmp --quiet $f ../../main/table/$f || exit 1
	done
	popd
	shopt -u nullglob

	popd
done

# python3
pushd python3
export PYTHON=python3
%configure $OPTS $PYTHON3OPTS
unset CFLAGS
# The following is pythonext, not python3ext
make -j1 pythonext
unset PYTHON
popd

# tweak find-debuginfo.sh
%global	debuginfo_subdir	%{name}-%{version}-%{release}.%{?_arch}
%global	__debug_install_post_old	%__debug_install_post
%global	__debug_install_post		\
	\
	%__debug_install_post_old \
	pushd %{buildroot}%{_prefix}/src/debug/%{debuginfo_subdir} \
	for ext in \\\
		python3 \\\
		ruby python perl \
	do \
		test -d $ext || continue \
		cd $ext \
		for file in * \
		do \
			if test -f ../main/$file \
			then \
				status=$(cmp --quiet $file ../main/$file && echo $? || echo $?) \
				if test $status = 0 ; then \
					ln -sf ../main/$file $file \
				fi \
			fi \
		done \
		cd .. \
	done \
	for ext in \\\
		ruby perl \
	do \
		cd $ext \
		for file in *_table_defs.h \
		do \
			status=$(cmp --quiet $file ../python/$file && echo $? || echo $?) \
			if test $status = 0 ; then \
				ln -sf ../python/$file $file \
			fi \
		done \
		cd .. \
	done \
	popd \
	%{nil}

%install
rm -rf %{buildroot}

OPTS=""
OPTS="${OPTS} DESTDIR=%{buildroot}"
OPTS="${OPTS} INSTALL='install -p'"
OPTS="${OPTS} INSTALL_DATA='install -p -m 0644'"

OPTS="$OPTS JMANDIR=%{_mandir}/ja/man1"

# A. main
eval make -C main ${OPTS} install locale_install

# Kill documents, will install with %%doc
rm -rf %{buildroot}%{_defaultdocdir}

# B. extentions
for ext in ruby \
	%{nil}
do
	eval make -C $ext ${OPTS} ${ext}ext_install
done
## python3
( eval make -C python3 ${OPTS} pythonext_install )

## perl
pushd perl
mkdir -p %{buildroot}%{perl_vendorarch}/auto/skf
install -cpm 0644 skf.pm %{buildroot}%{perl_vendorarch}
install -cpm 0755 skf.so %{buildroot}%{perl_vendorarch}/auto/skf/skf.so
popd

## Cleanup

%find_lang %{name}

%check
# Setting environ
export PATH=%{buildroot}%{_bindir}:$PATH

export PERL5LIB=%{buildroot}%{perl_vendorarch}
export python3PATH=%{buildroot}%{python3_sitearch}
export RUBYLIB=%{buildroot}%{ruby_vendorarchdir}

export CHECK_PYTHON2=no

# SOURCE1
sh %{SOURCE1}
(
  export PYTHONPATH=${python3PATH}
  python3 %{SOURCE11}
)

%files
%defattr(-,root,root,-)
%{_bindir}/skf

%{_mandir}/man1/skf.1*
%lang(ja)	%{_mandir}/ja/man1/skf.1*

%files	common	-f %{name}.lang
%defattr(-,root,root,-)
%lang(ja)	%doc	main/debian/changelog
%doc	main/README.txt
%license	main/copyright
%if 0%{?usescm} < 1
%lang(ja)	%doc	main/doc/
%endif

%{_libdir}/%{name}/

%files	ruby
%defattr(-,root,root,-)
%{ruby_vendorarchdir}/skf.so

%files	-n python3-skf
%defattr(-,root,root,-)
%{python3_sitearch}/_skf.so
%{python3_sitearch}/skf.py*
%{python3_sitearch}/__pycache__/skf.*

%files	perl
%defattr(-,root,root,-)
%{perl_vendorarch}/skf.pm
%{perl_vendorarch}/auto/skf/

%changelog
%autochangelog
