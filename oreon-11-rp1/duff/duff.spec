%global source0_hash 15b721f7e0ea43eba3fd6afb41dbd1be63c678952bf3d80350130a0e710c542e

Name:		duff
Version:	0.5.2
Release:	32%{?dist}
Summary:	Quickly find duplicate files

License:	zlib
URL:		http://duff.sourceforge.net/
Source0:	http://sourceforge.net/projects/%{name}/files/%{name}/%{version}/%{name}-%{version}.tar.gz
Patch1:		duff-linking-to-shared-library-sha.patch
Patch2:		duff-remove-docs-of-sha.patch
BuildRequires:  gcc
BuildRequires:	sha-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires: make

%description
Duff is a command-line utility for quickly finding duplicates in a given set of
files

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
#Remove bundled sha and unnecessary files
rm -rf src/sha*
rm -rf autom4te.cache
rm -rf README.SHA
%patch -P1 -p1
%patch -P2 -p1

%build
autoreconf -fi
autoheader
CFLAGS="%{optflags} -I/usr/include/sha"
export CFLAGS
%configure \
	--disable-rpath
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} INSTALL="install -p" CP="cp -p" install
%find_lang %{name}
find %{buildroot} -name 'join-duplicates.sh' | xargs chmod 0755

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_bindir}/duff
%dir %{_datadir}/duff
%{_datadir}/duff/join-duplicates.sh
%{_docdir}/duff
%{_mandir}/man1/duff.1*

%changelog
%autochangelog
