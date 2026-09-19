%global source0_hash 4aea02f38cf92fa4aa44732d4ed98648df839e6537d6f0417c3fe18e1a34f880

%{!?tcl_version: %global tcl_version %(echo 'puts $tcl_version' | tclsh)}
%{!?tcl_sitelib: %global tcl_sitelib %{_datadir}/tcl%{tcl_version}}

Name:           bwidget
Version:        1.10.1
Release:        4%{?dist}
Summary:        Extended widget set for Tk

License:        TCL
URL:            http://tcllib.sourceforge.net/
Source0:        http://downloads.sourceforge.net/tcllib/bwidget-%{version}.tar.gz

BuildArch:      noarch
Requires:       tcl(abi) = 9.0 tk
BuildRequires:  tcl

%description
An extended widget set for Tcl/Tk.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%{__sed} -i 's/\r//' LICENSE.txt

%build
# Nothing to build!

%install
# Don't bother with the included configure script and Makefile.  They
# are missing a lot of pieces and won't work at all.  Installation is
# pretty simple, so we can just do it here manually.
mkdir -p %{buildroot}/%{tcl_sitelib}/%{name}%{version}/
mkdir %{buildroot}/%{tcl_sitelib}/%{name}%{version}/lang
mkdir %{buildroot}/%{tcl_sitelib}/%{name}%{version}/images

install -m 0644 -pD *.tcl %{buildroot}/%{tcl_sitelib}/%{name}%{version}/
install -m 0644 -pD lang/*.rc %{buildroot}/%{tcl_sitelib}/%{name}%{version}/lang/
install -m 0644 -pD images/*.gif images/*.xbm %{buildroot}/%{tcl_sitelib}/%{name}%{version}/images/

%files
%{tcl_sitelib}/%{name}%{version}
%doc README.txt LICENSE.txt
%doc BWman/*.html

%changelog
%autochangelog
