%global source0_hash 042614dcc04afc68f1cfa2a32f353dc31b06f0674ebab3bfa8e67472709fe657
%define		majorver	5.1
%define		date		20070304
%define		debug_package	%{nil}
Name:		mecab-jumandic
Version:	%{majorver}.%{date}
Release:        35%{?dist}
Summary:        JUMAN dictorionary for MeCab
License:	BSD-3-Clause
URL:		http://mecab.sourceforge.net/
Source0:        http://downloads.sourceforge.net/mecab/%{name}-%{majorver}-%{date}.tar.gz
Requires:	mecab
# oreon:deps
BuildRequires:  make
BuildRequires:  mecab-devel
# /oreon:deps
%description
MeCab JUMAN is a dictionary for MeCab using CRF estimation
based on Kyoto corpus.
This dictionary is for UTF-8 use.

%package 	EUCJP
Summary:	JUMAN dictionary for Mecab with encoded by EUC-JP
Requires:	mecab
%description EUCJP

MeCab JUMAN is a dictionary for MeCab using CRF estimation
based on Kyoto corpus.
This dictionary is for EUC-JP use.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{majorver}-%{date}

%build

%configure \
	--with-mecab-config=%{_bindir}/mecab-config \
	--with-charset=utf8
%{__make} %{?_smp_mflags}
%{__mkdir} UTF-8
%{__cp} -p \
	*.bin *.dic *.def dicrc \
	UTF-8/
%{__make} clean
%configure \
	--with-mecab-config=%{_bindir}/mecab-config
%{__make} %{?_smp_mflags}
%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT
%{__mv} $RPM_BUILD_ROOT%{_libdir}/mecab/dic/jumandic \
	$RPM_BUILD_ROOT%{_libdir}/mecab/dic/jumandic-EUCJP
%{__mv} -f UTF-8/* .
%{__make} install DESTDIR=$RPM_BUILD_ROOT
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

if test -f %{_sysconfdir}/mecabrc ; then
	%{__sed} -i -e 's|^dicdir.*|dicdir = %{_libdir}/mecab/dic/jumandic|' \
		%{_sysconfdir}/mecabrc || :
fi
%post EUCJP

if test -f %{_sysconfdir}/mecabrc ; then
	%{__sed} -i -e 's|^dicdir.*|dicdir = %{_libdir}/mecab/dic/jumandic-EUCJP|' \
		%{_sysconfdir}/mecabrc || :
fi
%files -f %{oreon_filedir}/main.list
%files -n mecab-jumandic-EUCJP -f %{oreon_filedir}/mecab-jumandic-EUCJP.list

%changelog

%autochangelog
