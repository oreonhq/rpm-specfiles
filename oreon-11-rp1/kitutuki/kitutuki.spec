%global source0_hash 024e3aba658f44c381097cc52b2383b7d62f661a656f86ce22ad7630df1199ed

Name:		kitutuki
Version:	0.9.6
Release:	39%{?dist}
Summary:	Shell script language
Summary(ja):	シェルスクリプティング言語 

# SPDX confirmed
License:	GPL-1.0-or-later
URL:		http://ab25cq.web.fc2.com/
Source0:	http://ab25cq.web.fc2.com/%{name}-%{version}.tgz
## Not sent to the upstream, must do later
##
# Misc fixes for Makefile
Patch0:		kitutuki-0.9.5-makefile-misc-fix.patch
# Patch for kitutuki_help
Patch1:		kitutuki-0.9.1-kitutuki_help.patch
# Patch for configure, need autoconf
Patch2:		kitutuki-0.9.3-configure-migemo.patch
# Patch to compile with gcc10 -fno-common
Patch3:		kitutuki-0.9.6-gcc10-fno-common.patch

BuildRequires:  gcc
BuildRequires:	cmigemo-devel
BuildRequires:	ncurses-devel
BuildRequires:	oniguruma-devel
BuildRequires:	readline-devel

# Patch2
BuildRequires:	autoconf
BuildRequires:	make

%description
Kitutuki is a shell script language.

%description	-l ja
Kitutukiはシェルスクリプト言語です

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
%{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

# Makefile
%patch -P0 -p1 -b .mk
sed -i.strip -e '/install/s| -s | |' Makefile.in
sed -i.stamp -e 's|\([ \t][ \t]*install \)|\1 -p |' Makefile.in

# Other patches
%patch -P1 -p1 -b .help
%patch -P3 -p1 -b .gcc10

# configure
%patch -P2 -p1 -b .cf
autoconf
sed -i.cflags -e '/CFLAGS=/s|-fPIC|-fPIC %{optflags}|' configure

# Miscs
iconv -f EUC-JP -t UTF-8 README.ja.txt > README.ja.txt.utf8
touch -r README.ja.txt{,.utf8}
mv -f README.ja.txt{.utf8,}

%build
%configure \
	--sysconfdir=%{_libdir}/%{name} \
	--includedir=%{_includedir}/%{name} \
	--with-migemo \
	--with-system-migemodir=%{_datadir}/cmigemo \
	%{nil}

make %{?_smp_mflags} \
	docdir=%{_defaultdocdir}/%{name}/

%install
rm -rf %{buildroot}
# make install DESTDIR=%%{buildroot}
# Above does not work...
rm -rf ./Trash
%makeinstall \
	sysconfdir=%{buildroot}%{_libdir}/%{name}/ \
	includedir=%{buildroot}%{_includedir}/%{name}/ \
	docdir=$(pwd)/Trash/ \
	%{nil}

# Move kitutuki.ksh to %%{_sysconfdir}/%{name}
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
mv %{buildroot}%{_libdir}/%{name}/kitutuki.ksh \
	%{buildroot}%{_sysconfdir}/%{name}
ln -sf ../../../%{_sysconfdir}/%{name}/kitutuki.ksh \
	%{buildroot}%{_libdir}/%{name}/

%ldconfig_scriptlets

%files
%doc	AUTHORS
%license	GPL
%lang(ja)	%doc	README.ja.txt
%doc	usage.en.txt
%lang(ja)	%doc	usage.ja.txt

%dir %{_sysconfdir}/%{name}
# In case that kitutuki.ksh changes much as this is quite a
# new package, rather mark this as no-noreplace
%config	%{_sysconfdir}/%{name}/kitutuki.ksh
%{_bindir}/%{name}
%{_libdir}/libkitutuki.so.1{,.*}
%{_libdir}/%{name}/

%files	devel
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}/

%changelog
%autochangelog
