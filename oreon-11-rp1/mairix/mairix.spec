%global source0_hash 7b6a9f5642d7b883d5e63cd4f3c29b0c92a244fec84eea0d807c5191683ad124
%global gitver 1cc06f4a73ba4b940008c1ffc398d2ac708cd6d6
%global gitrel %(c=%{gitver}; echo ${c:0:6})
%global gitdate 20220920
Name:           mairix
Version:        0.24
Release:        1%{?dist}
Summary:        A program for indexing and searching email messages
License:        GPL-2.0-only
URL:            http://www.rc0.org.uk/mairix
Source0:        https://github.com/rc0/%{name}/archive/%{gitver}/%{name}-%{gitver}.tar.gz
Patch0:         mairix-build.patch
# oreon:deps
BuildRequires:  bison
BuildRequires:  bzip2-devel
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
# /oreon:deps
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
%oreon_autofiles main

%check

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
