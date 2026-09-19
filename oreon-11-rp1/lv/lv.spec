%global source0_hash e1cd2e27109fbdbc6d435f2c3a99c8a6ef2898941f5d2f7bacf0c1ad70158bcf

%global vver	451

Name:		lv
Version:	4.51
Release:	57%{?dist}
License:	GPL-2.0-or-later
URL:		http://www.ff.iij4u.or.jp/~nrt/lv/
BuildRequires:	ncurses-devel autoconf
BuildRequires:	gcc
BuildRequires: make

Source:		http://www.ff.iij4u.or.jp/~nrt/freeware/%{name}%{vver}.tar.gz
Patch1:		lv-4.49.4-nonstrip.patch
Patch2:		lv-4.51-162372.patch
Patch3:		lv-+num-option.patch
Patch4:		lv-fastio.patch
Patch5:		lv-lfs.patch
Patch6:		%{name}-aarch64.patch
Patch7:		%{name}-no-sigvec.patch
Patch8:		%{name}-inline.patch
Patch9:		lv-c99.patch
Patch10:	%{name}-ftbfs.patch

Summary:	A Powerful Multilingual File Viewer
%description
lv is a powerful file viewer like less.
lv can decode and encode multilingual streams through
many coding systems: ISO-8859, ISO-2022, EUC, SJIS, Big5,
HZ, Unicode.
It recognizes multi-bytes patterns as regular
expressions, lv also provides multilingual grep.
In addition, lv can recognize ANSI escape sequences
for text decoration.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}%{vver}

%build
cd src
autoconf
%configure --enable-fastio
%make_build

%install
cd src
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
%make_install bindir=$RPM_BUILD_ROOT%{_bindir} libdir=$RPM_BUILD_ROOT%{_libdir} mandir=$RPM_BUILD_ROOT%{_mandir}

%files
%license GPL.txt
%doc README build hello.sample hello.sample.gif index.html
%doc relnote.html
%{_bindir}/lv
%{_bindir}/lgrep
%{_mandir}/man1/lv.1.gz
%{_libdir}/lv

%changelog
%autochangelog
