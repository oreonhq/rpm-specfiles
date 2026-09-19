%global source0_hash 042614dcc04afc68f1cfa2a32f353dc31b06f0674ebab3bfa8e67472709fe657

%define		majorver	5.1
%define		date		20070304

# The data in MeCab dic are compiled by arch-dependent binaries
# and the created data are arch-dependent.
# However, this package does not contain any executable binaries
# so debuginfo rpm is not created.
%define		debug_package	%{nil}

Name:		mecab-jumandic
Version:	%{majorver}.%{date}
Release:	35%{?dist}
Summary:	JUMAN dictorionary for MeCab

# SPDX confirmed
License:	BSD-3-Clause
URL:		http://mecab.sourceforge.net/
Source0:	http://downloads.sourceforge.net/mecab/%{name}-%{majorver}-%{date}.tar.gz

BuildRequires: make
BuildRequires:	mecab-devel
Requires:	mecab

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
%{__mv} $RPM_BUILD_ROOT%{_libdir}/mecab/dic/jumandic \
	$RPM_BUILD_ROOT%{_libdir}/mecab/dic/jumandic-EUCJP

# Next install UTF-8
%{__mv} -f UTF-8/* .
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%post
# Note: post should be okay. mecab-dic expects that
# mecab is installed in advance.
if test -f %{_sysconfdir}/mecabrc ; then
	%{__sed} -i -e 's|^dicdir.*|dicdir = %{_libdir}/mecab/dic/jumandic|' \
		%{_sysconfdir}/mecabrc || :
fi

%post EUCJP
# Note: post should be okay. mecab-dic expects that
# mecab is installed in advance.
if test -f %{_sysconfdir}/mecabrc ; then
	%{__sed} -i -e 's|^dicdir.*|dicdir = %{_libdir}/mecab/dic/jumandic-EUCJP|' \
		%{_sysconfdir}/mecabrc || :
fi

%files
%doc AUTHORS
%license COPYING
%{_libdir}/mecab/dic/jumandic/

%files EUCJP
%doc AUTHORS
%license COPYING
%{_libdir}/mecab/dic/jumandic-EUCJP/

%changelog
%autochangelog
