%global source0_hash d3d65fa4306f2da83115cb924c42ade3dc7bb0024f3bc9d40be9a56506af3a9a

%{!?tcl_version: %define tcl_version %(echo 'puts $tcl_version' | tclsh)}
%{!?tcl_sitelib: %define tcl_sitelib %{_datadir}/tcl%{tcl_version}}

Summary: Collection of widgets and other packages for Tk
Name: tklib
Version: 0.5
Release: 31%{?dist}
License: TCL
Source: http://downloads.sourceforge.net/tcllib/tklib-0.5.tar.gz
URL: http://tcllib.sourceforge.net/
BuildArch: noarch
Requires: tcl(abi) = 8.6 tk tcllib
BuildRequires: make
BuildRequires: tk >= 0:8.3.1 tcllib

%description
This package is intended to be a collection of Tcl packages that provide
Tk utility functions and widgets useful to a large collection of Tcl/Tk
programmers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
# Remove some execute permission bits on files that aren't executable
# to suppress some rpmlint warnings.
chmod a-x modules/plotchart/*.tcl
chmod a-x modules/swaplist/*.tcl
chmod a-x modules/widget/*.tcl
chmod a-x modules/diagrams/*.tcl
chmod a-x modules/khim/*.tcl
chmod a-x modules/khim/*.msg

iconv --from=ISO-8859-1 --to=UTF-8 modules/ctext/ctext.man > modules/ctext/ctext.man.new
mv -f modules/ctext/ctext.man.new modules/ctext/ctext.man

%build
# Override the setting for 'libdir'.  If this isn't done then the
# platform-independent script files will get installed in an arch-specific
# directory (such as /usr/lib or /usr/lib64).
%configure --libdir=%{tcl_sitelib}
# Don't bother running 'make' because there's nothing to build.

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%check
make check

%files
%doc PACKAGES README README-0.4.txt ChangeLog license.terms
%{tcl_sitelib}/tklib*
%{_mandir}/*/*

%changelog
%autochangelog
