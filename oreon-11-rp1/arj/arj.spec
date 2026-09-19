%global source0_hash 589e4c9bccc8669e7b6d8d6fcd64e01f6a2c21fe10aad56a83304ecc3b96a7db

Summary:        Archiver for .arj files
Name:           arj
Version:        3.10.22
Release:        46%{?dist}
License:        GPL-2.0-or-later
URL:            https://arj.sourceforge.net/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# unarj.* from Debian
Source1:        unarj.sh
Source2:        unarj.1
Patch0:         arj-3.10.22-arches_align.patch
Patch1:         arj-3.10.22-no_remove_static_const.patch
Patch2:         arj-3.10.22-64_bit_clean.patch
Patch3:         arj-3.10.22-parallel_build.patch
Patch4:         arj-3.10.22-use_safe_strcpy.patch
Patch5:         arj-3.10.22-doc_refer_robert_k_jung.patch
Patch6:         arj-3.10.22-security_format.patch
Patch7:         arj-3.10.22-missing-protos.patch
Patch8:         arj-3.10.22-custom-printf.patch
# Filed into upstream bugtracker as https://sourceforge.net/tracker/?func=detail&aid=2853421&group_id=49820&atid=457566
Patch9:         arj-3.10.22-quotes.patch
Patch10:        arj-3.10.22-security-afl.patch
Patch11:        arj-3.10.22-security-traversal-dir.patch
Patch12:        arj-3.10.22-security-traversal-symlink.patch
BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  make
Provides:       unarj = %{version}-%{release}
Obsoletes:      unarj < 3

%description
This package is an open source version of the arj archiver. It has
been created with the intent to preserve maximum compatibility and
retain the feature set of original ARJ archiver as provided by ARJ
Software, Inc.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1
%patch -P8 -p1
%patch -P9 -p1
%patch -P10 -p1
%patch -P11 -p1
%patch -P12 -p1

pushd gnu
  autoconf
popd

%build
pushd gnu
  %configure
popd

# Disable binary strippings
%make_build ADD_LDFLAGS=""

%install
%make_install

install -D -p -m 644 resource/rearj.cfg.example $RPM_BUILD_ROOT%{_sysconfdir}/rearj.cfg
install -p -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/unarj
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/man1/unarj.1

# remove the register remainders of arj's sharewares time
rm -f $RPM_BUILD_ROOT%{_bindir}/arj-register
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/arj-register.1*

%files
%license doc/COPYING
%doc ChangeLog* doc/rev_hist.txt
%config(noreplace) %{_sysconfdir}/rearj.cfg
%{_bindir}/*arj*
%{_libdir}/arj/
%{_mandir}/man1/*arj*.1*

%changelog
%autochangelog
