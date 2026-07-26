%global source0_hash 173eef2bd487baf52a12d5c286d284b427388cf9e0f01a2b60d7dc347dd457e4

Name:           p0rn-comfort
Version:        0.0.4
Release:        53%{?dist}
Summary:        Support programs for browsing image-gallery sites
License:        GPL-1.0-or-later
URL:            http://www.cgarbs.de/p0rn-comfort.en.html
Source0:        http://www.cgarbs.de/stuff/p0rn-comfort-%{version}.tar.gz
Patch0:         p0rn-modules.patch
Patch1:         p0rn-static.patch
Patch2:			p0rn-paths.patch
BuildArch:      noarch
BuildRequires:      perl-generators
Requires:       lynx, wget, mmv

%description
p0rn-comfort consists of several support programs for browsing
image-gallery sites.  It includes a proxy which enables blacklisting
of thumbnail sites on-the-fly.  It also supports queueing of entire
pages for download and fetching them at a later time.  Queuing can
either be done manually (directly from your browser) or by an
automated download script which can also follow links between
different galleries.
       
%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p 1 -b .modules
%patch -P1 -p 1 -b .static
%patch -P2 -p 1 -b .paths

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{perl_vendorlib}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libexecdir}/p0rn-comfort
mkdir -p %{buildroot}%{_mandir}/man1

install -m 644 -D P0rn/DB.pm %{buildroot}%{perl_vendorlib}/P0rn/DB.pm
install -m 644 -D P0rn/Static.pm %{buildroot}%{perl_vendorlib}/P0rn/Static.pm
	

install -m 755 p0rn-bot p0rn-dbdump p0rn-dbrestore p0rn-download p0rn-grab \
	 p0rn-proxy \
	 %{buildroot}%{_bindir}

install -m 755 p0rn-dbadd p0rn-dbdel p0rn-dblist \
	%{buildroot}%{_libexecdir}/p0rn-comfort

# Create and install man-pages
#for file in p0rn-bot p0rn-dbadd p0rn-dbdel p0rn-dblist p0rn-download; do 
#	perldoc -d %{buildroot}%{_mandir}/man1/$file.1 $file
#done
#chmod 644 %{buildroot}%{_mandir}/man1/*
for file in $(cd docs; ls *.1); do
	install -m 644 docs/$file %{buildroot}%{_mandir}/man1/$file
done

%files
%doc ChangeLog COPYRIGHT README
%{_bindir}/*
%{_libexecdir}/p0rn-comfort/
%{perl_vendorlib}/*
%{_mandir}/man1/*

%changelog
%autochangelog
