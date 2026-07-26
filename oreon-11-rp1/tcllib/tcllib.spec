%global source0_hash 642c2c679c9017ab6fded03324e4ce9b5f4292473b62520e82aacebb63c0ce20

%{!?tcl_version: %global tcl_version %(echo 'puts $tcl_version' | tclsh)}
%{!?tcl_sitelib: %global tcl_sitelib %{_datadir}/tcl%{tcl_version}}

Summary:    The standard Tcl library
Name:       tcllib
Version:    2.0
Release:    4%{?dist}
License:    TCL
Source:     https://core.tcl-lang.org/tcllib/uv/%{name}-%{version}.tar.xz
URL:        https://core.tcl-lang.org/tcllib/doc/trunk/embedded/index.md
BuildArch:  noarch

Requires:   tcl(abi) = 9.0

BuildRequires: tcl >= 8.6

%description
Tcllib, the Tcl Standard Library is a collection of Tcl packages
that provide utility functions useful to a large collection of Tcl
programmers.

%package -n tcl8-tcllib
Summary: The standard tcllib library in the tcl8.6 dir
Requires: tcl(abi) = 8.6

%description -n tcl8-tcllib
Tcllib, the Tcl Standard Library is a collection of Tcl packages
that provide utility functions useful to a large collection of Tcl
programmers. This is a compatibility copy for TCL 8.6.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
chmod -x modules/doctools/mpformats/fr.msg
# Convert a couple of files to UTF-8
for file in modules/struct/pool.html ; do
    iconv --from=ISO-8859-1 --to=UTF-8 ${file} > ${file}.new
    mv -f ${file}.new ${file}
done

%build
# Nothing to build!

%install
echo 'not available' > modules/calendar/calendar.n
%{_bindir}/tclsh installer.tcl -no-gui -no-wait -no-html -no-examples \
    -pkg-path %{buildroot}/%{tcl_sitelib}/%name-%version \
    -app-path %{buildroot}%{_bindir} \
    -nroff-path %{buildroot}%_mandir/mann
# install HTML documentation into specific modules sub-directories:
pushd modules
cp ftp/docs/*.html ftp/
for module in comm exif ftp mime stooop struct textutil; do
    mkdir -p ../$module && cp $module/*.html ../$module/;
done
popd

# do a tcl8 round
%{_bindir}/tclsh installer.tcl -no-gui -no-wait -no-html -no-examples \
    -pkg-path %{buildroot}/%{_datadir}/tcl8.6/%{name}-%{version} \
    -app-path %{buildroot}%{_bindir} \
    -nroff-path %{buildroot}%_mandir/mann

# Clean up rpmlint warnings
find %{buildroot}/%{_datadir} -name \*.tcl -exec chmod 0644 {} \;

%files
%doc support/releases/PACKAGES README.md support/releases/history/README-2.0.txt ChangeLog
%doc exif/ ftp/ mime/ stooop/ struct/ textutil/
%license license.terms
%{tcl_sitelib}/%{name}-%{version}
%{_mandir}/mann/*
%{_bindir}/dtplite
%{_bindir}/mkdoc
%{_bindir}/nns*
%{_bindir}/page
%{_bindir}/pt
%{_bindir}/tcldocstrip

%files -n tcl8-tcllib
%license license.terms
%{_datadir}/tcl8.6/%{name}-%{version}
# binaries and manpages are not here anymore, this is just for compat.

%changelog
%autochangelog
