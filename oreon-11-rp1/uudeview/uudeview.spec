%global source0_hash 69e5ccf7a49858e019cfd85831f4a37bd5e9d568322ff38a2fbbe000376df6ef

%global _hardened_build 1
%global snapshot 1
%global OWNER hannob
%global PROJECT uudeview
%global commit 7ef9e26532b39bdcedd319c07b6b77fc70e270dd
%global commitdate 20241111
#global gittag 0.5.20
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           uudeview
Version:        0.5.20%{?snapshot:^%{commitdate}git%{shortcommit}}
Release:        5%{?dist}

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
%if 0%{?snapshot}
Source0:        https://github.com/%{OWNER}/%{PROJECT}/archive/%{commit}/%{name}-%{commit}.tar.gz
BuildRequires:  autoconf
%else
Source0:        http://www.fpx.de/fp/Software/UUDeview/download/uudeview-%{version}.tar.gz
%endif
Source1:        xdeview.desktop
Patch0:         uudeview-threads.patch
URL:            http://www.fpx.de/fp/Software/UUDeview/
Summary:        Applications for uuencoding, uudecoding, ...
BuildRequires:  make
BuildRequires:  inews
BuildRequires:  texlive-collection-latexextra
BuildRequires:  transfig, desktop-file-utils
BuildRequires:  tk-devel
BuildRequires:  gcc
Requires:       %{_sbindir}/sendmail

%description
Handles uuencoding, xxencoding, yEnc, and base-64 encoding (MIME). Can do
automatic splitting of large encodes, automatic posting.  A must for
anyone serious encoding/decoding.

%package        -n uulib-devel
Summary:        Binary news message decoding library
Provides:       uulib = %{version}-%{release}
Provides:       uulib-static = %{version}-%{release}
Obsoletes:      uulib < 0.5.20-11
Obsoletes:      uulib-static < 0.5.20-16

%description    -n uulib-devel
uulib is a library of functions for decoding uuencoded, xxencoded,
Base64-encoded, and BinHex-encoded data. It is also capable of
encoding data in any of these formats except BinHex.

This package contains header files and static libraries for uulib.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if 0%{?snapshot}
%autosetup -p1 -n %{name}-%{commit}
autoreconf -i
%else
%autosetup -p1
%endif
%{__sed} -i -e "s,for ff_subdir in lib,for ff_subdir in %{_lib},g" configure

%build
%configure --enable-sendmail=%{_sbindir}/sendmail
make %{?_smp_mflags}
cd doc
make
pdflatex library.ltx

%install
sed -i -e "s,xdeview.1,xdeview.1 uuwish.1,g" Makefile
make install BINDIR=$RPM_BUILD_ROOT/%{_bindir} MANDIR=$RPM_BUILD_ROOT/%{_mandir}
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  --mode 644 \
  --add-category X-Fedora \
  %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT/%{_includedir}
install -p -m 0644 uulib/uudeview.h $RPM_BUILD_ROOT/%{_includedir}/
mkdir -p $RPM_BUILD_ROOT/%{_libdir}
install -p -m 0644 uulib/libuu.a $RPM_BUILD_ROOT/%{_libdir}/

%files
%doc COPYING HISTORY IAFA-PACKAGE README uudeview.lsm
%{_mandir}/man1/*.1*
%{_bindir}/uudeview
%{_bindir}/uuenview
%{_bindir}/uuwish
%{_bindir}/xdeview
%{_datadir}/applications/*.desktop

%files -n uulib-devel
%doc COPYING HISTORY doc/library.pdf
%{_includedir}/*.h
%{_libdir}/*.a

%changelog
%autochangelog
