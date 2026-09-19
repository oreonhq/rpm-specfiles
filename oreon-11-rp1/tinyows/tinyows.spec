%global source0_hash 93d9379b1405736dd1fb36e0b2cd3fc58867a10f4d47351b6cd4013e4e1755fc

%global project_owner MapServer
%global project_name tinyows

Name:      tinyows
Version:   1.2.2
Release:   %autorelease
Summary:   PostGIS WFS-T and FE implementation server

License:   MIT
URL:       https://mapserver.org/tinyows/

Source0:   https://github.com/%{project_owner}/%{project_name}/archive/v%{version}/%{project_name}-%{version}.tar.gz

Source1:   no_date_footer.html

Requires:  httpd 

BuildRequires: autoconf
BuildRequires: ctags
BuildRequires: doxygen
BuildRequires: gcc
BuildRequires: indent
BuildRequires: flex
BuildRequires: libfl-static
BuildRequires: libxml2-devel
BuildRequires: postgis
BuildRequires: postgis-client
BuildRequires: postgresql-devel

%ifarch %valgrind_arches
BuildRequires: valgrind-devel
%endif

%description
TinyOWS server implements latest Open Geospatial Consortium Transactional Web
Feature Service (WFS-T) standard versions, as well as related standards such as
Filter Encoding (FE).

%package doc
Summary: Documentation files for TinyOWS Server
BuildArch: noarch

%description doc
TinyOWS server implements latest Open Geospatial Consortium Transactional Web
Feature Service (WFS-T) standard versions, as well as related standards such as
Filter Encoding (FE).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}

# clean SVN
find . -type d -name .svn -exec rm -rf '{}' +

# copy no_date_footer.html in
cp %{SOURCE1} .

%build
autoconf
%configure

# fix datadir lookup path
sed -i -e 's|/usr/tinyows/|%{_datadir}/%{name}/|' src/ows_define.h
# fix DSO lookup
sed -i -e 's|-lpq|-lpq -lm|' Makefile

# respect fedora ldflags
sed -i -e 's|-lfl $(POSTGIS_LIB)|-lfl $(LDFLAGS) $(POSTGIS_LIB)|' Makefile

%make_build

# disable timestamp inside docs
sed -i -e 's|HTML_FOOTER|HTML_FOOTER=no_date_footer.html\n\#|g' doc/Doxyfile
make doxygen

%install
install -d %{buildroot}%{_bindir}
install -p -m 0755 tinyows %{buildroot}%{_bindir}/
install -d %{buildroot}%{_datadir}/%{name}
cp -pR schema %{buildroot}%{_datadir}/%{name}/
install -d %{buildroot}%{_sysconfdir}/%{name}
install -p -m 0644 ms4w/apps/tinyows-svn/config.xml %{buildroot}%{_sysconfdir}/%{name}

ln -s --relative %{buildroot}%{_sysconfdir}/%{name}/config.xml %{buildroot}%{_datadir}/%{name}/

mkdir -p %{buildroot}%{_pkgdocdir}
cp -a doc/doxygen %{buildroot}%{_pkgdocdir}/
hardlink --ignore-time --reflink=never %{buildroot}%{_pkgdocdir}/

# NOTE(neil): 2024-08-25 tests require a postgres database running; unable to run in check
# https://github.com/MapServer/tinyows/blob/f1dc7bc86fc4d69faddd79ed2804d98c11802ba8/.github/workflows/linux.sh#L19-L22
%dnl %check

%files
%license LICENSE.md schema/LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}
%dir %{_sysconfdir}/%{name}
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/%{name}/config.xml

%files doc
%doc README.md VERSION.md
%doc %{_pkgdocdir}/doxygen

%changelog
%autochangelog
