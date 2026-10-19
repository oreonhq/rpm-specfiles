%global source0_hash ada280f045010baaef2204470c688f4aa515accfba9bfbcef2e554facb631609
Name:       libloc
Version:    0.9.19
Release:        1%{?dist}
Summary:        Library to determine a location of an IP address in the Internet
License:    LGPL-2.1-or-later
SourceLicense:  LGPL-2.1-or-later AND CC-BY-SA-4.0 AND (GPL-1.0-or-later OR Artistic-1.0-Perl) AND GPL-2.0-or-later AND GPL-2.0-or-later WITH Autoconf-exception-macro AND FSFAP AND FSFULLR
URL:        https://location.ipfire.org/
Source0:        https://source.ipfire.org/releases/%{name}/%{name}-%{version}.tar.gz
Patch0:     libloc-0.9.18-address-Fix-endianess-problem-when-fetching-octets-i.patch
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  docbook-style-xsl
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  gnulib-devel
BuildRequires:  grep
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  libxslt
BuildRequires:  lua-rpm-macros
BuildRequires:  make
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  pkgconf-m4
BuildRequires:  pkgconf-pkg-config
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(python)
BuildRequires:  python3-devel
BuildRequires:  sed
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
This is a lightweight library which can be used to query the IPFire Location
database.

%package devel
Summary:        Developmental files for libloc C library
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains header files and other files helpful when developing
applications using libloc library.

%package -n lua-%{name}
Summary:        Lua interface to libloc library
License:        LGPL-2.1-or-later
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description -n lua-%{name}
This is Lua binding to libloc, a library to determine an IP address location
in the Internet.

%package -n perl-%{name}
Summary:        Perl interface to libloc library
License:        LGPL-2.1-or-later AND (GPL-1.0-or-later OR Artistic-1.0-Perl)
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description -n perl-%{name}
Location is a Perl interface to libloc, a library to determine an IP address
location in the Internet.

%package -n python3-%{name}
Summary:        Python interface to libloc library
License:        LGPL-2.1-or-later AND CC-BY-SA-4.0
Requires:       %{name}%{?_isa} = %{version}-%{release}
%py_provides python3-location
%description -n python3-%{name}
This is Python binding to libloc, a library to determine an IP address location
in the Internet.

%package tools
Summary:        Tools for downloading and querying IPFire Location database
BuildArch:      noarch
Requires:       python3-%{name} = %{version}-%{release}
Recommends:     %{name}-tools-bash-completion = %{version}-%{release}
%description tools
"location" program retrieves information from the location database. This data
can be used to determine a location of an IP address in the Internet and for
building firewall rules to block access from certain autonomous systems or
countries. There is also an integration with systemd which helps updating the
location database periodically.

%package tools-bash-completion
Summary:        Bash completion support for IPFire location tools
BuildArch:      noarch
Requires:       bash-completion
Requires:       %{name}-tools = %{version}-%{release}
%description tools-bash-completion
This package implements Bash completion scripts for IPFire location tools.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# Unbundle m4 macros
rm m4/ax_prog_perl_modules.m4 m4/ld-version-script.m4

%build

autoreconf -fi -I%{_datadir}/gnulib/m4
%global default_database_file %{_sharedstatedir}/location/database.db
%{configure} \
    --disable-analyzer \
    --enable-bash-completion \
    --with-database-path=%{default_database_file} \
    --enable-debug \
    --enable-largefile \
    --enable-ld-version-script \
    --enable-lua \
    --enable-man_pages \
    --enable-nls \
    --enable-perl \
    --enable-shared \
    --disable-silent-rules \
    --disable-static \
    --with-systemd \
    --with-systemdsystemunitdir=%{_unitdir}
%{make_build}
%install
%{make_install}
find %{buildroot} -name '*.la' -delete
%{_fixperms} %{buildroot}/*
install -d -m 0755 %{buildroot}/%{python3_sitelib}/%{name}-%{version}.dist-info
cat <<'EOF' >%{buildroot}/%{python3_sitelib}/%{name}-%{version}.dist-info/WHEEL
Wheel-Version: 1.0
Generator: handmade
Root-Is-Purelib: false
Tag: py3-none-any
EOF
chmod 0644 %{buildroot}/%{python3_sitelib}/%{name}-%{version}.dist-info/WHEEL
cat <<'EOF' >%{buildroot}/%{python3_sitelib}/%{name}-%{version}.dist-info/METADATA
Metadata-Version: 2.1
Name: %{name}
Version: %{version}
Home-page: %{url}
Requires-Dist: psycopg
EOF
chmod 0644 %{buildroot}/%{python3_sitelib}/%{name}-%{version}.dist-info/METADATA
%find_lang %{name}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/*/lib*.so.* usr/*/lib*.so.*

%check

unset LOC_LOG
make check %{?_smp_mflags} || (cat ./test-suite.log; exit 1)
%post tools

%systemd_post location-update.service
%preun tools

%systemd_preun location-update.service
%postun tools

%systemd_postun_with_restart location-update.service
%files -f %{oreon_filedir}/main.list
%files -n libloc-devel -f %{oreon_filedir}/libloc-devel.list
%files -n lua-libloc -f %{oreon_filedir}/lua-libloc.list
%files -n perl-libloc -f %{oreon_filedir}/perl-libloc.list
%files -n python3-libloc -f %{oreon_filedir}/python3-libloc.list
%files -n libloc-tools -f %{oreon_filedir}/libloc-tools.list
%files -n libloc-tools-bash-completion -f %{oreon_filedir}/libloc-tools-bash-completion.list

%changelog

%autochangelog
