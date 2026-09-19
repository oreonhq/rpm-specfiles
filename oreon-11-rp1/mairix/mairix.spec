%global source0_hash 7b6a9f5642d7b883d5e63cd4f3c29b0c92a244fec84eea0d807c5191683ad124

%global gitver 1cc06f4a73ba4b940008c1ffc398d2ac708cd6d6
%global gitrel %(c=%{gitver}; echo ${c:0:6})
%global gitdate 20220920
Name:           mairix
Version:        0.24
Release:        23.%{gitdate}git%{gitrel}%{?dist}
Summary:        A program for indexing and searching email messages

License:        GPL-2.0-only
URL:            http://www.rc0.org.uk/mairix
#Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source0:        https://github.com/rc0/mairix/archive/%{gitver}/mairix-%{gitver}.tar.gz
Patch0:         mairix-build.patch

BuildRequires:  gcc make bison flex bzip2-devel xz-devel zlib-devel

%description
mairix is a program for indexing and searching email messages
stored in Maildir, MH or mbox folders.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{!?gitver:%{version}}%{?gitver}
%patch -P0 -p1 -b .build

for i in NEWS; do
  iconv -f iso8859-1 -t utf8 -o ${i}{_,} && touch -r ${i}{,_} && mv -f ${i}{_,}
done

%build
%configure
%make_build

%install
%make_install
rm -rf $RPM_BUILD_ROOT%{_datadir}/zsh

%check
# it doesn't pass currently
#chmod 755 test/scripts/*
#make check

%files
%license COPYING
%doc ACKNOWLEDGEMENTS NEWS README dotmairixrc.eg
%{_bindir}/mairix
%{_mandir}/man1/mairix.1*
%{_mandir}/man5/mairixrc.5*

%changelog
%autochangelog
