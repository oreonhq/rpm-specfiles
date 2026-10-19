%global source0_hash 572fd8eed70786b1fbff6e7fec62eab7bd731beea074022d1b5a480ecf2df586
%{!?tcl_version: %define tcl_version %(echo 'puts $tcl_version' | tclsh)}
%{!?tcl_sitelib: %define tcl_sitelib %{_datadir}/tcl%{tcl_version}}
Name:           iwidgets
Version:        4.1.1
Release:        1%{?dist}
Summary:        A set of useful widgets based on itcl and itk
License:        MIT
URL:            http://incrtcl.sourceforge.net/
Source0:        http://downloads.sourceforge.net/sourceforge/incrtcl/iwidgets-%{version}.tar.gz
Patch0:         iwidgets-calls.patch
Patch1:         iwidgets4.0.1-wish85.diff
BuildArch:      noarch
Requires:       tcl(abi) = 8.6 itk
# oreon:deps
BuildRequires:  itcl-devel
BuildRequires:  tcl
# /oreon:deps
%description
A set of useful widgets based on itcl and itk.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .calls
%patch -P1 -p1 -b .wish85

%build

sed -e "s#@itcl_VERSION@#4.0#" -e "s#@PACKAGE_VERSION@#%{version}#" < iwidgets.tcl.in > iwidgets.tcl
sed -e "s#@PACKAGE_VERSION@#%{version}#" < pkgIndex.tcl.in > pkgIndex.tcl
%install
mkdir -p %{buildroot}/%{tcl_sitelib}/%{name}%{version}
install -p -m 644 generic/*.* %{buildroot}/%{tcl_sitelib}/%{name}%{version}
install -p -m 644 generic/tclIndex %{buildroot}/%{tcl_sitelib}/%{name}%{version}
install -p -m 644 iwidgets.tcl %{buildroot}/%{tcl_sitelib}/%{name}%{version}
install -p -m 644 pkgIndex.tcl %{buildroot}/%{tcl_sitelib}/%{name}%{version}
mkdir -p %{buildroot}/%{tcl_sitelib}/%{name}%{version}/demos
for i in demos/* ; do
    if [ -f $i ] ; then
        install -p -m 644 $i %{buildroot}/%{tcl_sitelib}/%{name}%{version}/demos
    fi
done
chmod 755 %{buildroot}/%{tcl_sitelib}/%{name}%{version}/demos/catalog
chmod 755 %{buildroot}/%{tcl_sitelib}/%{name}%{version}/demos/scopedobject
mkdir -p %{buildroot}/%{tcl_sitelib}/%{name}%{version}/demos/images
install -p -m 644 demos/images/*.* %{buildroot}/%{tcl_sitelib}/%{name}%{version}/demos/images
mkdir -p %{buildroot}/%{tcl_sitelib}/%{name}%{version}/demos/html
install -p -m 644 demos/html/*.html %{buildroot}/%{tcl_sitelib}/%{name}%{version}/demos/html
mkdir -p %{buildroot}/%{_mandir}/mann
install -p -m 644 doc/*.n %{buildroot}/%{_mandir}/mann/
rm %{buildroot}/%{_mandir}/mann/panedwindow.n
rm %{buildroot}/%{_mandir}/mann/datefield.n
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
