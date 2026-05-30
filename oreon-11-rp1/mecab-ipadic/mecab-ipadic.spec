%global source0_hash b62f527d881c504576baed9c6ef6561554658b175ce6ae0096a60307e49e3523

# This spec file is very similar with mecab-jumandic

%define		majorver	2.7.0
%define		date		20070801

%define		mecabver	0.96

# The data in MeCab dic are compiled by arch-dependent binaries
# and the created data are arch-dependent.
# However, this package does not contain any executable binaries
# so debuginfo rpm is not created.
%define		debug_package	%{nil}

Name:		mecab-ipadic
Version:	%{majorver}.%{date}
Release:	34%{?dist}
Summary:	IPA dictionary for MeCab

# SPDX confirmed
License:	NAIST-2003
URL:		http://mecab.sourceforge.net/
Source0:        http://downloads.sourceforge.net/mecab/%{name}-%{majorver}-%{date}.tar.gz
#Source2:	http://www.icot.or.jp/ARCHIVE/terms-and-conditions-for-IFS-J.html
Source2:	http://www.jipdec.or.jp/icot/ARCHIVE/terms-and-conditions-for-IFS-J.html
Source3:	LICENSE.Fedora

BuildRequires: make
BuildRequires:	mecab-devel >= %{mecabver}
Requires:	mecab >= %{mecabver}

%description
MeCab IPA is a dictionary for MeCab using CRF estimation
based on IPA corpus.
This dictionary is for UTF-8 use.

%package 	EUCJP
Summary:	IPA dictionary for Mecab with encoded by EUC-JP
Requires:	mecab >= %{mecabver}

%description EUCJP

MeCab IPA is a dictionary for MeCab using CRF estimation
based on IPA corpus.
This dictionary is for EUC-JP use.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n %{name}-%{majorver}-%{date}

%build
# First build on UTF-8
%configure \
	--with-mecab-config=%{_bindir}/mecab-config \
	--with-charset=utf8
%{__make} %{?_smp_mflags}
# Preserve them
%{__mkdir} UTF-8
%{__cp} -p \
	*.bin *.dic *.def dicrc \
	UTF-8/

# Next build on EUC-JP
# This is the default, however Fedora uses UTF-8 so
# for Fedora this must be the option.
%{__make} clean
%configure \
	--with-mecab-config=%{_bindir}/mecab-config
%{__make} %{?_smp_mflags}


%install
# First install EUC-JP
%{__rm} -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT
%{__mv} $RPM_BUILD_ROOT%{_libdir}/mecab/dic/ipadic \
	$RPM_BUILD_ROOT%{_libdir}/mecab/dic/ipadic-EUCJP

# Next install UTF-8
%{__mv} -f UTF-8/* .
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%{__cp} -p %{SOURCE2} LICENSE.jp.html
%{__cp} -p %{SOURCE3} .

%post
# Note: post should be okay. mecab-dic expects that
# mecab is installed in advance.
if test -f %{_sysconfdir}/mecabrc ; then
	%{__sed} -i -e 's|^dicdir.*|dicdir = %{_libdir}/mecab/dic/ipadic|' \
		%{_sysconfdir}/mecabrc || :
fi

%post EUCJP
# Note: post should be okay. mecab-dic expects that
# mecab is installed in advance.
if test -f %{_sysconfdir}/mecabrc ; then
	%{__sed} -i -e 's|^dicdir.*|dicdir = %{_libdir}/mecab/dic/ipadic-EUCJP|' \
		%{_sysconfdir}/mecabrc || :
fi

%files
%license COPYING
%license LICENSE.*
%doc README
%{_libdir}/mecab/dic/ipadic/

%files EUCJP
%license COPYING
%license LICENSE.*
%doc README
%{_libdir}/mecab/dic/ipadic-EUCJP/


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - %{majorver}.%{date}-34
- Prepare for Oreon 11 (RP1)
