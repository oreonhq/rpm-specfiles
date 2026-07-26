%global source0_hash 3b35ae744b4ae79cfa1b7ac0cfc03619e144b485793f8b5e084b08c35bae83ca

Name:		kcc
Version:	2.3
Release:	64%{?dist}
License:	GPL-2.0-or-later

BuildRequires:	gcc
BuildRequires: make

## missed upstream.
Source:		ftp://ftp.sra.co.jp/pub/os/linux/JE/sources/base/%{name}.tar.gz
Source1:	kcc.1
Patch0:		kcc-2.3-dontstrip.patch
Patch1:		kcc-2.3-varargs.patch
Patch2:		kcc-2.3-fix-segv.patch
Patch3:		kcc-2.3-timestamp.patch
Patch4:		kcc-2.3-c99.patch

Summary:	Kanji Code Converter
%description
kcc is a kanji code converter with an auto detection.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}
%patch -P0 -p1 -b .dontstrip
%patch -P1 -p1 -b .varargs
%patch -P2 -p1 -b .segv
%patch -P3 -p1 -b .timestamp
%patch -P4 -p1 -b .c99

%build
make "CFLAGS=-std=gnu99 $RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/ja/man1
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
make BINPATH="$RPM_BUILD_ROOT%{_bindir}" install 
make MANPATH="$RPM_BUILD_ROOT%{_mandir}" JMANDIR="ja" install.man
for i in `find $RPM_BUILD_ROOT%{_mandir}/ja -type f`; do
	iconv -f euc-jp -t utf-8 $i > $i.new && mv -f $i.new $i && chmod 444 $i
done
install -m0644 -p %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1/
gzip -9 $RPM_BUILD_ROOT%{_mandir}/man1/kcc.1

%files
%doc README
%license COPYING
%{_bindir}/kcc
%lang(ja) %{_mandir}/ja/man1/kcc.1*
%{_mandir}/man1/kcc.1*

%changelog
%autochangelog
