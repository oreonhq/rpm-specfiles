%global source0_hash 9e72ef3776ffa2861080c7ffc08e6992fdb29c746cb0bed055f6f707edaa47a2

Name:		cocot
Version:	20080315
Release:	31%{?dist}
License:	BSD
URL:		http://vmi.jp/software/cygwin/cocot.html
Source0:	http://vmi.jp/software/cygwin/%{name}-%{version}.tar.bz2
Patch0:		cocot-c99.patch

Summary:	COde COnverter on Tty

BuildRequires:  gcc
BuildRequires: make
%description
Cocot is a kanji code conversion program, running as a filter between
a terminal (tty) and a process running on it.  Cocot can be used with
ssh or telnet.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
iconv -f EUC-JP -t UTF-8 --output README.ja.UTF-8 README.ja
mv README.ja.UTF-8 README.ja

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%files
%doc AUTHORS COPYING NEWS README README.ja
%{_bindir}/cocot

%changelog
%autochangelog
